"""

    Models have a lot of class methods. The basic theory is this:

    - UserAsset is a base class for all user assets, e.g. individual survivors,
        settlements, users.
    - DataModel is a class object that different types of UserAsset objects
        initialize within themselves so that their data model can be treated
        like an object.

"""

# standard lib imports
from collections import OrderedDict
from copy import deepcopy
from datetime import datetime
import random

# second-party imports
from bson.objectid import ObjectId

# API imports
from app import utils

class DataModel():
    ''' Object-oriented data model object initialized with one of our UserAsset
    objects. '''

    def __init__(self, unique_foreign_key=None):
        ''' Initialize with a unique foreign key value. The self.admin_attribs
        attrib gets set ABSOLUTELY LAST so that it can be used later to ignore
        non-data-model attributes of this object. '''

        self.logger = utils.get_logger()
        self.unique_foreign_key = unique_foreign_key
        self.admin_attribs = [
            'logger', 'unique_foreign_key', 'admin_attribs'
        ]

        self.add('_id', ObjectId, required=False, immutable=True)
        self.add('created_on', datetime, required=True, immutable=True)
        self.add('created_by', ObjectId, required=False, immutable=True)
        self.add('modified_on', datetime, required=False)
        self.add('last_accessed', datetime, required=False)
        self.add('removed', datetime, required=False)



    def add(self, name=None, a_type=None, default_value=None, **kwargs):
        ''' Adds an attribute to the model. '''

        # sanity checks
        if name is None or a_type is None:
            err = 'Cannot add DataModel attribute without name and type!'
            raise AttributeError(err)
        if not isinstance(a_type, type):
            err = 'Attribute type must be a type, e.g. int, str, etc.'
            raise AttributeError(err)

        # set default, if not provided
        if default_value is None and a_type != datetime:
            default_value = a_type()

        # create the dict and set it as an attr
        attribute_dict = {
            'name': name,
            'type': a_type,
            'default': default_value,
            'required': True,
        }
        attribute_dict.update(kwargs)

        setattr(self, name, attribute_dict)


    def category(self, cat):
        ''' Returns a list of attribute keys if those attributes have the
        'category' value of 'cat'. '''

        output = []
        for key in self.attribs():
            attr = getattr(self, key)
            if attr.get('category', None) == cat:
                output.append(key)
        return output


    def new(self):
        ''' Returns a dictionary representing a new one of...whatever this
        is. Uses all attributes and sets them to their defaults. '''

        output = {}
        for key in self.attribs():
            attr = getattr(self, key)
            if attr.get('required', False):
                output[key] = attr['default']
        return output


    def apply(self, record, force_type=False):
        ''' Applies the data model to 'record', which should be a dict
        representing an instance of this data model.

        Returns a corrected version of 'record'.

        Setting 'force_type' to true forces anything we can't coerce to
        the correct type to assume its default value.
        '''

        record = deepcopy(record)

        # first part: normalize all extant attrs and add missing required attrs
        keys_to_delete = set()
        for attr in self.serialize():

            # check for missing required attributes
            if attr['required'] and attr['name'] not in record.keys():
                warn = "Adding required attr '%s' to record (default: '%s')..."
                self.logger.warning(warn, attr['name'], attr['default'])
                record[attr['name']] = attr['default']

            # for required datetime attributes, do not allow None
            if (
                attr['required'] and attr['type'] == datetime and
                record.get(attr['name'], False) is None
            ):
                record[attr['name']] = datetime.now()
                warn = "Required %s attribute '%s' cannot be None! Set to %s"
                self.logger.warning(
                    warn, attr['type'], attr['name'], record[attr['name']]
                )

            # in this loop, check the record itself, based on its attrs
            if attr['name'] in record.keys():

                # first, before we normalize or duck-type anything, add the attr
                #   to the kill list if need to
                if (
                    record[attr['name']] is None and
                    attr.get('unset_on_none', False)
                ):
                    keys_to_delete.add(attr['name'])

                # next, coerce if we need to
                if type(record[attr['name']]) != attr['type']:
                    warn = "Coercing '%s' attribute to %s type..."
                    self.logger.warning(warn % (attr['name'], attr['type']))
                    try:
                        record[attr['name']] = attr['type'](record[attr['name']])
                    except TypeError as error:
                        msg = "Could not coerce '%s' value '%s' to %s type!"
                        formatted_msg = msg % (
                            attr['name'], record[attr['name']], attr['type']
                        )
                        self.logger.error(formatted_msg)
                        if force_type:
                            record[attr['name']] = attr['default']
                        else:
                            raise utils.InvalidUsage(
                                'Unexpected attribute: %s' % formatted_msg
                            )

                # next, kill HTML and strip
                if attr['type'] == str and not attr.get('trusted_html', False):
                    orig_len = len(record[attr['name']])
                    record[attr['name']] = utils.html_stripper(
                        record[attr['name']]
                    ).strip()
                    if orig_len > len(record[attr['name']]):
                        warn = "Stripped HTML from '%s' attr..."
                        self.logger.warning(warn % (attr['name']))

                # next, check if it's in allowed options:
                if (
                    attr.get('options', None) is not None and
                    record[attr['name']] not in attr['options']
                ):
                    warn = "'%s' attr has invalid option '%s'. Random choice..."
                    self.logger.warning(
                        warn % (attr['name'], record[attr['name']])
                    )
                    record[attr['name']] = self.random_choice(attr['name'])

                # min/max it if it's an int
                if attr['type'] == int:
                    minmax = self.minmax(attr['name'], record[attr['name']])
                    if record[attr['name']] != minmax:
                        warn = "Correcting '%s' attr to min/max: %s"
                        self.logger.warning(warn % (attr['name'], minmax))
                        record[attr['name']] = minmax


        # process the kill list
        for key in keys_to_delete:
            self.logger.warning("Deleting '%s' key...", key)
            del record[key]

        # lastly, delete keys that aren't part of the model
        bogus_keys = []
        for key in record.keys():
            if key not in self.attribs():
                bogus_keys.append(key)
        for key in bogus_keys:
            warn = "Removing unknown attr '%s' from record..."
            self.logger.warning(warn % key)
            del record[key]

        return record


    def attribs(self, return_type=list):
        ''' Returns a list of keys representing the attributes. '''
        return sorted([
            key for key in self.__dict__.keys()
            if key not in self.admin_attribs
        ])


    def duck_type(self, attrib, value):
        ''' Retruns 'value' as the correct type for 'attrib'. Special handling
        for None. '''

        if value == 'None' or value is None:
            return None

        attribute = getattr(self, attrib)
        return attribute['type'](value)


    def is_valid(self, key, value, log_errors=False, return_error=False,
                raise_on_failure=False):

        ''' Checks whether or not 'attrib' can be set to 'value' without
        violating the model. '''

        failure = None

        attribute = getattr(self, key, None)

        # checks are cascading, so we do an elif, so we don't fire more than one
        if attribute is None:
            failure = "'%s' is not a part of the data model!" % key
        elif attribute.get('immutable', False):
            failure = "'%s' value cannot be changed!" % key
        elif not isinstance(value, attribute['type']):
            if not attribute.get('unset_on_none', False):
                err = "'%s' value '%s' must be %s type (not %s)!"
                failure = err % (key, value, attribute['type'], type(value))
        elif attribute.get('options', None) is not None:
            if value not in attribute['options']:
                err = "'%s' is not a valid option for '%s'. Options: %s"
                failure = err % (value, key, attribute['options'])

        #
        # process failure
        #
        if failure is not None:
            failure = 'Data model validation failure! ' + failure
            if log_errors:
                self.logger.error(failure)
            if raise_on_failure:
                raise utils.InvalidUsage(failure, 422)
            if return_error:
                return failure
            return False

        return True


    def random_choice(self, attr):
        ''' Throws an error if the attribute doesn't have an 'options' key. The
        options key, obviously must map to a value that is a list. '''

        attribute = getattr(self, attr)
        if attribute.get('options', None) is None:
            raise AttributeError("'%s' parameter does not have options!" % attr)

        return random.choice(attribute['options'])


    def serialize(self):
        ''' Serializes the model, i.e. returns a list of dicts. '''
        return [getattr(self, attr) for attr in self.attribs()]


    def minmax(self, attr, value):
        ''' Determines if 'value' is too high or too low for 'attribute' and
        returns the adjusted value. '''

        attribute = getattr(self, attr)

        if attribute.get('minimum', None) is not None:
            if value < attribute['minimum']:
                return attribute['minimum']

        if attribute.get('maximum', None) is not None:
            if value > attribute['maximum']:
                return attribute['maximum']

        return value
