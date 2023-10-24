"""

    The all-important UserAsset class method lives in this file.

    This is the base class for the assets users create and manage via the API,
    including settlements, survivors and users.

"""

# standard lib imports
from copy import deepcopy
from datetime import datetime
import importlib
import inspect
import json

# second-party imports
from bson import json_util
from bson.objectid import ObjectId
import flask
from user_agents import parse as ua_parse
import werkzeug

# local imports
from app import API, utils

from app.assets import campaigns
from ._decorators import log_event_exception_manager

class UserAsset():
    """ The base class for all user asset objects, such as survivors,
    settlements and users. All user asset controllers in the 'models' module
    use this as their base class. """


    def __repr__(self):
        """ Default __repr__ method for all user assets. Note that you should
        PROBABLY define a __repr__ for your individual assets, if for no other
        reason than to make the logs look cleaner. """

        if not hasattr(self, 'collection'):
            return '[Uninitialized UserAsset object]'

        record = getattr(self, self.collection[:-1], {})
        name = record.get('name', 'UNKNOWN')
        return "%s object '%s' [%s]" % (self.collection, name, self._id)


    def __init__(self, *args, **kwargs):
        """
        The base init() method for all UserAssets. Three things happen here:
            1. we initialize basic attributes, self.args, self.kwargs,
                seslf.logger and self.collection. We also set self.params
            2. next, we set self._id either by getting it from kwargs or from
                creating a new asset by calling self.new()
            3. once we've got self._id, we run self.load() and set self.loaded
        """

        #
        # 1. set basic UserAsset attributes
        #

        if not getattr(self, 'logger', False):
            self.logger = utils.get_logger()
        self.args = args
        self.kwargs = kwargs
        self.set_request_params()

        # try to set self.collection to not None; die if not
        if not hasattr(self, 'collection'):
            self.collection = kwargs.get('collection', None)

        if getattr(self, 'collection', None) is None:
            err_msg = (
                "User assets (settlements, survivors, users) may not be "
                "initialized without specifying a collection!"
            )
            self.logger.error(err_msg)
            raise AttributeError(err_msg)


        #   it if this object IS a Settlement, the load() call below will
        #   overwrite this:
        self.Settlement = self.kwargs.get('Settlement', None)


        #
        # 2. set self._id from kwargs or new()
        #
        self._id = self.kwargs.get('_id', None)
        if self._id is None:
            self.new()  # sets self._id

        try:
            self._id = ObjectId(self._id)   # try to force strings
        except TypeError:                   # die if we can't duck-type it
            bad_type = type(self._id).__name__
            err = 'Failed to coerce settlement ID type "%s" to OID!' % bad_type
            raise utils.InvalidUsage(err, status_code=422)

        if not isinstance(self._id, ObjectId):
            err = "The asset OID '%s' is not a valid OID!" % (self._id)
            self.logger.error(err)
            raise utils.InvalidUsage(err, status_code=422)


        # 3. now do load() and self.loaded stuff
        self.loaded = False
        try:
            self.load()
            self.loaded = True
        except Exception as e:
            err = "Could not load '%s' from '%s'!" % (self._id, self.collection)
            self.logger.error(err)
            self.logger.exception(e)
            raise


        # finally, since we're initialized, we should also be self.loaded; die
        #   bloody if we're not
        if not self.loaded:
            err = "%s UserAsset initialized but not loaded!"
            raise ValueError(err % (self))


    def new(self):
        ''' Raise a TypeError; require sub-classes to define their own new().'''
        error = (
            'Objects that inherit from UserAsset must define their own new() '
            'method for creating a new instance of themselves.'
        )
        raise TypeError(error)


    def load(self):
        """ The default/vanilla load() method for all UserAsset objects, i.e.
        settlements, survivors, users. The design here is that you call this
        from the individual asset model's load() method via super(), and then
        use the asset model's load() to add additional special stuff. """


        # do some sanity checking here around the MOST BASIC attributes required
        #   to load() a UserAsset object, regardless of collection.
        for attr in ['_id', 'collection']:
            if not hasattr(self, attr):
                raise AssetLoadError('load() requires self.%s attr!' % attr)

        if not isinstance(self.collection, str):
            err = "self.collection must be 'str' type (not %s)"
            raise AssetLoadError(err % type(self.collection))


        # use self.collection to set the mdb_doc
        mdb_doc = utils.mdb[self.collection].find_one({"_id": self._id})
        if mdb_doc is None:
            raise AssetLoadError("Asset _id '%s' not be found in '%s'!" % (
                self._id, self.collection
                )
            )

        # now use self.collection and mdb_doc to set attributes
        setattr(self, self.collection[:-1], mdb_doc)
        setattr(self, '_id', mdb_doc['_id'])
        setattr(self, 'created_by', mdb_doc.get('created_by', mdb_doc['_id']))

        self.set_last_accessed(save=True)


    def save(self, set_modified_on=False, verbose=True):
        """ Saves the user asset back to its collection in mdb, depending on
        self.collection. """

        self.set_last_accessed(save=False)

        # sanity check the object
        if self.collection not in API.config['USER_ASSET_COLLECTIONS']:
            err = "Invalid MDB collection '%s'! Record not saved..."
            raise AttributeError(err % self.collection)

        # load the record, set it
        record = self.get_record(set_modified_on=set_modified_on)
        if not record.get('_id', False):
            err = "Cannot save a record with no '_id' attribute! %s"
            raise utils.InvalidUsage(err % record)

        #  save
        utils.mdb[self.collection].save(record)

        if verbose:
            msg = "Saved %s to mdb.%s successfully!"
            self.logger.info(msg, self, self.collection)


    def serialize(self, include_api_meta=True):
        ''' Calls the user object's self.synthesize() method if it can (falls
        back to self.get_record() if it can't) and returns it as JSON. '''

        output = {}
        if include_api_meta:
            output = self.get_serialize_meta()

        output = self.get_record()
        if hasattr(self, 'synthesize'):
            output = self.synthesize()

        return json.dumps(output, default=json_util.default)


    def remove(self, delete=False):
        ''' Basic user asset removal. Probably overwrite this one in the class
        methods.

        Arming 'delete' drops the record from MDB, so exercise caution.
        '''

        if delete:
            output = utils.mdb[self.collection].delete_one(self.get_record())
            self.logger.critical('Deleted UserAsset from MDB! %s', self)
            return output.raw_result

        record = self.get_record(set_modified_on=True)
        record['removed'] = datetime.now()
        self.save()
        self.logger.warning('%s has been removed!', self)

        return self.serialize()


    def json_response(self):
        """ Calls the asset's serialize() method and creates a simple HTTP
        response. """
        return flask.Response(
            response=self.serialize(),
            status=200,
            mimetype="application/json"
        )


    def check_request_params(self, keys=[], verbose=True, raise_exception=True):
        """ Checks self.params for the presence of all keys specified in 'keys'
        list. Returns True if they're present and False if they're not.

        Set 'verbose' to True if you want to log validation failures as errors.
        """

        for k in keys:
            if k not in self.params.keys():
                if verbose:
                    err_msg = "Request is missing required parameter '%s'!" % k
                    self.logger.error(err_msg)
                if raise_exception:
                    curframe = inspect.currentframe()
                    calframe = inspect.getouterframes(curframe, 2)
                    caller_function = calframe[1][3]
                    msg = "Insufficient request parameters for this route!\
                    The %s() method requires values for the following keys:\
                    %s." % (
                        caller_function,
                        utils.list_to_pretty_string(keys)
                    )
                    self.logger.exception(msg)
                    self.logger.error("Bad request params: %s", self.params)
                    raise utils.InvalidUsage(msg, status_code=400)
                return False

        return True


    def set_request_params(self):
        """ Checks the incoming request (from Flask) for JSON and tries to add
        it to self.

        Important! The 'verbose' kwarg is deprecated in the 1.0.0 release of the
        API, as it is no longer require to see request info in non-production
        environments.

        """

        self.params = {}

        if not flask.has_request_context():
            return None

        try:
            flask.request.get_json()
        except werkzeug.exceptions.BadRequest:
            err = '[%s] %s Could not decode request JSON...'
            self.logger.info(err, flask.request.method, flask.request)
            return None

        if flask.request.get_json() is not None:
            try:
                self.params = dict(flask.request.get_json())
            except ValueError:
                warn = "%s request JSON could not be converted!"
                self.logger.warning(warn, flask.request.method)
                self.params = flask.request.get_json()
        else:
            if flask.request.method != 'GET':
                warn =  "%s type request did not contain JSON data!"
                self.logger.warning(warn, flask.request.method)
                self.logger.warn("Request URL: %s", flask.request.url)


    #
    #   universal 'get' methods for User Assets
    #

    def get_campaign(self, return_type=None):
        """ Returns the campaign handle of the settlement as a string, if
        nothing is specified for kwarg 'return_type'.

        Use 'name' to return the campaign's name (from its definition).

        'return_type' can also be dict. Specifying dict gets the
        serialized game asset. """

        # first, bomb if we're not a settlement or survivor object
        method_supported_for = ['survivors', 'settlements']
        if getattr(self, 'collection', None) not in method_supported_for:
            msg = ("Objects whose collection is '%s' may not call the "
            "get_campaign() method!" % getattr(self, 'collection', None))
            raise TypeError(msg)

        # second, get the campaign handle
        if self.collection == "survivors":
            c_handle = self.Settlement.settlement["campaign"]
        elif self.collection == "settlements":
            # 2017-11-13 - bug fix - missing campaign attrib
            if not "campaign" in self.settlement.keys():
                self.settlement["campaign"] = 'people_of_the_lantern'
                warn_msg = "%s is a legacy settlement! Adding missing\
                'campaign' attribute!" % self
                self.logger.warn(warn_msg)
                self.save()
            c_handle = self.settlement["campaign"]

        # October 2023: this needs version support!!
        if return_type is not None:
            campaign_asset = campaigns.Campaign(handle=c_handle)

            # handle return_type requests
            if return_type == 'name':
                return campaign_asset.asset["name"]
            if return_type == dict:
                return campaign_asset.asset
            if return_type == object:
                return campaign_asset

            # DEPRECATED
            if return_type == 'initialize':
                raise TypeError('Cannot initialize campaigns this way!')
#                self.campaign = campaigns.Campaign(c_dict['handle'])
#                return True

        return c_handle


    def get_current_ly(self):
        """ Convenience/legibility function to help code readbility and reduce
        typos, etc. """

        if self.collection == "survivors":
            return int(self.Settlement.settlement["lantern_year"])
        return int(self.settlement["lantern_year"])


    def get_max_ly(self):
        """ Returns the integer value of the final LY of the campaign. """

        if self.collection == "survivors":
            ly = self.Settlement.settlement['timeline'][-1]['year']
        else:
            ly = self.settlement['timeline'][-1]['year']

        return int(ly)


    def get_players(self, return_type=None):
        """ Ported from the Settlement object method.

        Returns a list of dictionaries where each dict is a short summary of
        the significant attributes of the player, as far as the settlement is
        concerned.

        This is NOT the place to get full user information and these dicts are
        intentionally sparse for exactly that reason.
        """

        player_set = set()

        # get records of all survivors matching this settlement's OID;
        #   return an empty dict if there are no survivors (no survivors == no
        #   players).
        settlement_survivor_records = utils.mdb.survivors.find(
            {'settlement': self.get_settlement_id()}
        )
        if settlement_survivor_records is None:
            return []

        # iterate thru the survivors and create the set of users
        for survivor_record in settlement_survivor_records:
            player_set.add(survivor_record.get("email", None))

        player_set = utils.mdb.users.find({"login": {"$in": list(player_set)}})

        if return_type in [int, "count"]:
            return player_set.count()
        if return_type == "email":
            return [p["login"] for p in player_set]

        # if we're still here, we need settlement info for the full return
        settlement_record = self.get_settlement_record()
        player_list = []
        for p in player_set:
            p_dict = {"login": p["login"], "_id": p["_id"]}
            if p["login"] in settlement_record.get("admins", []):
                p_dict["settlement_admin"] = True
            if p["_id"] == settlement_record.get("created_by", None):
                p_dict["settlement_founder"] = True

            player_list.append(p_dict)

        return player_list


    def get_record(self, set_modified_on=False):
        ''' Uses self.collection to return self.settlement, self.user or
        self.survivor, depending. '''
        record = getattr(self, self.collection[:-1], None)

        if set_modified_on:
            record['modified_on'] = datetime.now()

        if record is None:
            err = "Could not get record for '%s'" % (self)
            raise ValueError(err)
        return record


    def get_requester_permissions(self):
        """ Uses the flask request.User to return a str 'write', 'read' or a
        None type, if the user has no permissios for the user asset.

        'write' type access is what you get as the creator of a user asset; the
        lower 'read' level of access is for settlement assets, e.g. where a
        user might not be a settlement admin, etc.
        """

        requester = flask.request.User.user

        if requester['_id'] == getattr(self, 'created_by', None):
            return 'write'

        # carve-out for 'public' survivors
        if hasattr(self, 'survivor') and self.survivor.get('public', False):
            return 'write'

        # if we're still here, check players
        for player in self.get_players():
            if player['_id'] == requester['_id']:
                if player.get('settlement_admin', False):
                    return 'write'
                return 'read'


    def get_serialize_meta(self):
        """ Sets the 'meta' dictionary for the object when it is serialized. """

        output = deepcopy(utils.api_meta)

        if list(output['meta'].keys()) != list(utils.api_meta['meta'].keys()):
            stack = inspect.stack()
            the_class = stack[1][0].f_locals["self"].__class__
            the_method = stack[1][0].f_code.co_name
            msg = "models.UserAsset.get_serialize_meta() got modified 'meta'\
            (%s) dict during call by %s.%s()! %s" % (
                output['meta'].keys(),
                the_class,
                the_method,
                utils.api_meta['meta'].keys()
            )
            self.logger.error(" ".join(msg.split()))

        return output


    def get_settlement_record(self):
        """ Settlement and Survivor models have self.settlement_id, which this
            method uses to retrieve the raw settlement record from MDB. """
        return utils.mdb.settlements.find_one({'_id': self.get_settlement_id()})


    def get_settlement_id(self):
        ''' Returns the OID for the UserAsset's settlement. '''
        if self.collection == 'settlements':
            return self.get_record()['_id']
        if self.collection == 'survivors':
            return self.get_record()['settlement']
        raise utils.InvalidUsage('%s asset has no settlement ID!' % self)


    #
    #   universal UserAsset 'set' methods
    #

    def set_last_accessed(self, access_time=None, save=False):
        """ Set 'access_time' to a valid datetime object to set the settlement's
        'last_accessed' value or leave it set to None to set the 'last_accessed'
        time to now. """

        asset_record = getattr(self, self.collection[:-1])

        if access_time is not None:
            asset_record['last_accessed'] = access_time
        else:
            asset_record['last_accessed'] = datetime.now()

        if save:
            self.save(False)



    def list_assets(self, attrib=None, log_failures=True):
        """
        WARNING! THIS IGNORES SETTLEMENT VERSION! YHBW!!!

        Laziness method that returns a list of dictionaries where dictionary
        in the list is an asset in the object's list of those assets.

        Basically, if your object is a survivor, and you set 'attrib' to
        'abilities_and_impairments', you get back a list of dictionaries where
        dictionary is an A&I asset dictionary.

        Same goes for settlements: if you set 'attrib' to 'locations', you get
        a list where each item is a location asset dict.

        Important! This ignores unregistered/unknown/bogus items! Anything that
        cannot be looked up by its handle or name is ignored!
        """

        if attrib is None:
            msg = "The list_assets() method cannot process 'None' type values!"
            self.logger.error(msg)
            raise Exception(msg)

        output = []
        if attrib == "principles":
            A = assets.innovations.Assets()
        else:
            A = importlib.import_module('app.assets.%s' % attrib).Assets()

        asset_list = getattr(self, self.collection[:-1])[attrib]

        for a in asset_list:
            a_dict = A.get_asset(
                a,
                backoff_to_name=True,
                raise_exception_if_not_found=False
            )

            if a_dict is not None:
                output.append(a_dict)
            elif a_dict is None and log_failures:
                err = "%s Unknown '%s' asset '%s' cannot be listed!"
                self.logger.error(err, self, attrib, a)
            else:
                pass # just ignore failures and silently fail

        return output


    #
    #   semantic settlement event logging!
    #

    @log_event_exception_manager
    def log_event(self, msg=None, event_type=None, action=None,
        key=None, value=None, agent=None):

        """ This is the primary user-facing logging interface, so there' s a bit
        of a high bar for using it.

        The basic idea of creating a log entry is that we're doing a bit of the
        semantic logging (i.e. strongly typed) thing, so, depending on which
        kwargs you use when calling this method, your final outcome/message is
        going to vary somewhat.

        That said, none of the kwargs here are mandatory, because context..
        """

        #
        #   baseline attributes
        #

        # for those who still raw-dog it; force to ASCII:
        if msg is not None:
            msg = str(msg)

        # 0.) method: determine caller method
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        method = calframe[2][3]

        # 1.) event: determine event type if it's None
        if event_type is None:
            event_type = method

        # 2.) action: figure out the action; set the special action vars
        if action is None:
            action = method.split("_")[0]
        action_word, action_preposition = utils.action_keyword(action)

        # 3.) key: default the key if we don't get one
        if key is None:
            key = " ".join(method.split("_")[1:])
        if key == "settlement":
            key = ""

        # 4.) value; default the value if we don't get one
        if value is None:
            value = "UNKNOWN"
        if not isinstance(value, int):
            value = str(value)

        # set 'created_by'
        created_by = None
        created_by_email = None
        if flask.request:
            if hasattr(flask.request, 'User'):
                created_by = flask.request.User.user['_id']
                created_by_email = flask.request.User.user['login']
                if agent is None:
                    agent = "user"


        # set 'attribute_modified'
        attribute_modified = {
            'key': key,
            'value': value,
        }

        if attribute_modified['key'] is not None:
            attribute_modified['key_pretty'] = key.replace("_", " ").replace("and", "&").title()
        if attribute_modified['value'] is not None:
            attribute_modified['value_pretty'] = str(value).replace("_"," ")

        d = {
            'version': 1.3,
            'agent': agent,
            "created_on": datetime.now(),
            'created_by': created_by,
            'created_by_email': created_by_email,
            "settlement_id": getattr(self, 'settlement_id', None),
            "ly": self.get_current_ly(),
            'event_type': event_type,
            'event': msg,
            'modified': {'attribute': attribute_modified},
        }

        # survivor, if it's a survivor
        if self.collection == 'survivors':
            d['survivor_id'] = self.survivor['_id']

        # target is the settlement, unless a survivor object calls this method
        action_target = "settlement"
        if 'survivor_id' in d.keys():
            d['modified']['asset'] = {
                'type': 'survivor',
                '_id': d['survivor_id'],
                'name': self.survivor['name'],
                'sex': self.get_sex(),
            }
            action_target = "survivor"
        else:
            d['modified']['asset'] = {
                "type": "settlement",
                "name": self.settlement['name'],
                '_id': self.settlement_id
            }

        # create the 'action'
        d['action'] = {'word': action_word, 'preposition': str(action_preposition)}

        # now write the repr, which is like...the simplified sentence of the event
        if key is None and value is None:
            d['action']['repr'] = " ".join(['modified', action_target])
        elif key is not None and value is None:
            d['action']['repr'] = " ".join(['modified', action_target, key])
        else:
            if action_preposition is None:
                d['action']['repr'] = action_word
            elif action_word in ['set']:
                d['action']['repr'] = " ".join([
                    action_word,
                    action_target,
                    key,
                    action_preposition,
                    str(value)
                    ]
                )
            elif action_word in ['unset']:
                d['action']['repr'] = " ".join([action_word, action_target, key])
            elif action_target == "survivor" and action_preposition is not None:
                d['action']['repr'] = " ".join([
                    action_word,
                    "'%s'" % value,
                    action_preposition,
                    str(key)
                    ]
                )
            else:
                d['action']['repr'] = " ".join([
                    action_word,
                    "'%s'" % value,
                    action_preposition,
                    action_target,
                    str(key)
                    ]
                )

        # default a message, if incoming message is none
        if msg is None:

            # create messages for survivor updates
            if d['modified']['asset']['type'] == 'survivor':
                if d['agent'] == 'user' and action_preposition is None:
                    d['event'] = " ".join([
                        d['created_by_email'],
                        d['action']['word'],
                        "%s [%s]" % (self.survivor['name'], self.get_sex()),
                    ])
                elif d['agent'] == 'user' and action_preposition is not None:
                    survivor_name_str = "%s [%s]" % (self.survivor['name'], self.get_sex())
                    d['event'] = " ".join([
                        d['created_by_email'],
                        d['action']['word'],
                        d['modified']['attribute']['value_pretty'],
                        d['action']['preposition'],
                        survivor_name_str
                    ])

                    # prevents us from printing the survivor name twice:
                    if survivor_name_str != d['modified']['attribute']['key_pretty']:
                        d['event'] += " " + d['modified']['attribute']['key_pretty']

                else:
                    d['event'] = " ".join([
                        "%s [%s]" % (self.survivor['name'], self.get_sex()),
                        d['action']['word'],
                        d['modified']['attribute']['value_pretty'],
                        d['action']['preposition'],
                        d['modified']['attribute']['key_pretty'],
                    ])
            # create messages for settlements
            elif d['modified']['asset']['type'] == 'settlement':
                if d['agent'] == 'user' and action_preposition is None:
                    d['event'] = " ".join([
                        d['created_by_email'],
                        d['action']['word'],
                        self.settlement['name'],
                    ])
                else:
                    d['event'] = " ".join([str(d['created_by_email']), str(d['action']['repr']), ])
            else:
                d['event'] = 'Updated %s' % self

        # enforce terminal punctuation on the event "sentence"
        if d['event'][-1] not in ['.','!']:
            d['event'] = d['event'].strip()
            d['event'] += "."


        # finally, if we had a requester, now that we've settled on a message
        # text, update the requester's latest action with it
        if created_by is not None:
            if flask.request and hasattr(flask.request, 'User'):
                ua_string = str(ua_parse(flask.request.user_agent.string))
                flask.request.User.set_latest_action(d['event'], ua_string)

        # finally, insert the event (i.e. save)
        utils.mdb.settlement_events.insert(d)
        self.logger.info("%s event: %s", self, d['event'])


    #
    #   universal UserAsset request_response()
    #

    def request_response(self, action=None):
        """ The default request_response() method used by UserAsset objects.

        Individual UserAsset model request_response() methods should typically:

        1.) respond to special/magic requests for methods that aren't actually
            methods
        2.) super() this base class method to handle web methods and return the
            standard way
        """

        if getattr(self, action, None) is not None:
            method = getattr(self, action)
            if getattr(method, '_web_method', False):
                method_response = method()
                if isinstance(method_response, flask.Response):
                    return method_response
            else:
                err = "The %s endpoint is mapped to an internal method!"
                return flask.Response(response=err % action, status=400)
        else:
            err = "User action '%s' is not implemented!" % action
            return flask.Response(response = err, status=501)

        return self.json_response()
