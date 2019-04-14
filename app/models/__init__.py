"""

    Methods for working with models are kept here including everything from the
    base class/object definition to the miscellaneous helper methods for keeping
    things organized, etc.

    This file is organized thus:

        Objects:
         - AssetCollection
         - GameAsset
	Decorators (for models):
         - log_event_exception_manager

"""

# standard lib imports
from bson import json_util
from collections import OrderedDict
from copy import copy, deepcopy
import json
import os

# third party imports
import flask

# local imports
from app import utils


#
#   The AssetCollection object starts here!
#

class AssetCollection(object):
    """ The base class for game asset objects, i.e. working with the dict assets
    in the assets/ folder.

    Each model in the models/ folder should have a method that subclasses this
    base class.

    Most Asset() objects that use this as their base class will define their own
    self.assets dict, e.g. in their __init__() method. But is not mandatory:
    review the __init__ method of this class carefully before writing custom
    __init__ code in in an individual Asset() object module. """


    def __repr__(self):
        """ Complicated __repr__ for asset collections which are...complex."""

        if not hasattr(self, 'type'):
            self.logger.warn(
                "AssetCollection does not have a 'type' attribute!"
            )
            return 'AssetCollection object (no type; %s assets)' % (
                len(self.assets)
            )
        return "AssetCollection object '%s' (%s assets)" % (
            self.type,
            len(self.assets)
        )


    def __init__(self):
        """ All Assets() models must base-class this guy to get access to the
        full range of AssetCollection methods, i.e. all of the common/ubiquitous
        ones.

        Base-classing also does a little user-friendliness/auto-magic when you
        invoke it:

            - you get self.logger for free.

            - if you set 'self.root_module' to be an actual module from the
            assets folder, that module will be scraped for dictionaries: those
            dictionaries will then be used as your self.assets dict, i.e. so
            that you DO NOT have to define your self.assets in your
            models.Assets() sub class.

            - if you have assets in your model.Assets.assets dict that DO NOT
            set their own type, you can set self.type on your model.Assets when
            you initialize it (but before you base-class this module) to force
            a default 'type' attribute on all of your self.assets dict items.

            - finally, all self.assets items get a 'handle' attribute that is
            the same as their actual dictionary key value. Individual assets
            SHOULD NEVER have a 'handle' attribute.

        """

        self.logger = utils.get_logger()

        if hasattr(self, "root_module"):
            self.type = os.path.splitext(self.root_module.__name__)[-1][1:]
            self.set_assets_from_root_module()

        # preserve 'raw' types as sub types
#        for a in self.assets.keys():
#            a_dict = self.assets[a]
#            if 'type' in a_dict.keys() and not 'sub_type' in a_dict.keys():
#                self.assets[a]['sub_type'] = self.assets[a]['type']

        # type override - be careful!
        if hasattr(self, "type_override"):
            self.type = self.type_override
            for a in self.assets.keys():
                self.assets[a]["type"] = self.type_override

        # set the default 'type_pretty' value
        self.set_ui_attribs()

        for a in self.assets.keys():
            self.assets[a]["handle"] = a


    #
    #   get / set / filter methods here
    #


    def set_assets_from_root_module(self):
        """ This is the vanilla AssetCollection initialization method. You feed
        it a 'module' value (which should be something from the assets/ folder)
        and it creates a self.assets dictionary by iterating through the module.

        If you need to do custom asset initialization, that is a fine and a good
        thing to do, but do it in the actual models/whatever.py file.

        Important! Adjusting the self.assets dict before calling this method
        will overwrite any adjustments because this method starts self.assets as
        a blank dict!
        """

        # the 'type' of all assets is the name of their root module. Full stop.
        # 'sub_type' is where we want to put any kind of 'type' info that we get
        # from the asset itself.

        all_assets = {}

        for module_dict, v in self.root_module.__dict__.items():
            if isinstance(v, dict) and not module_dict.startswith('_'): # get all dicts in the module
                for dict_key in sorted(v.keys()):                               # get all keys in each dict

                    if 'sub_type' in v[dict_key].keys():
                        raise Exception("%s already has a sub type!!!!" % v[dict_key])

                    # do NOT modify the original/raw asset dictionary
                    a_dict = v[dict_key].copy()

                    # set sub_type from raw asset  'type', then set the base type
                    a_dict['sub_type'] = v[dict_key].get("type", module_dict)
                    a_dict["type"] = self.type

                    # add it back to self.assets
                    all_assets[dict_key] = a_dict

        self.assets = OrderedDict()
        for k in sorted(all_assets.keys()):
            self.assets[k] = all_assets[k]

    def set_ui_attribs(self, capitalize=True):
        """ Iterates over self.assets; adds the "type_pretty" and 'sub_type_pretty'
        to all assets in the AssetCollection.assets dict """

        for h in self.assets.keys():

            #
            #   init
            #

            a_dict = self.get_asset(handle=h)
            if a_dict.get('type', None) is None:
                raise Exception("%s asset has no 'type' attribute! %s" % (self, a_dict))

            #
            #   pretty types/sub_types
            #

            for type_attr in ['type', 'sub_type']:

                type_value = a_dict.get(type_attr, None)

                if type_value is None:
                    pretty_type = None
                else:
                    pretty_type = type_value.replace("_"," ")
                    if capitalize:
                        pretty_type = pretty_type.title()

                self.assets[h]["%s_pretty" % type_attr] = pretty_type


            #
            #   selector text
            #

            selector_text = a_dict.get('name','')
            parenthetical = []
            if a_dict.get('expansion', None) is not None:
                parenthetical.append(a_dict['expansion'].replace("_"," ").title())

            if parenthetical != []:
                selector_text += " ("
                selector_text += ", ".join(parenthetical)
                selector_text += ")"

            self.assets[h]['selector_text'] = selector_text


    #
    #   common get and lookup methods
    #

    def get_asset(self, handle=None, backoff_to_name=False,
        raise_exception_if_not_found=True):

        """ Return an asset dict based on a handle. Return None if the handle
        cannot be retrieved. """

        asset = copy(self.assets.get(handle, None))     # return a copy

        # implement backoff logic
        if asset is None and backoff_to_name:
            asset = copy(self.get_asset_from_name(handle))

        # if the asset is still None, see if we want to raise an expception
        if asset is None and raise_exception_if_not_found:
            if not backoff_to_name:
                msg = "The handle '%s' could not be found in %s!" % (
                    handle,
                    self.get_handles()
                )
                self.logger.error(msg)
            elif backoff_to_name:
                msg = "After backoff to name lookup, asset handle '%s' is not\
                in %s and could not be retrieved." % (handle, self.get_names())
                self.logger.error(msg)
            raise utils.InvalidUsage(msg)

        # finally, return the asset (or the NoneType)
        return asset


    def get_assets_by_sub_type(self, sub_type=None):
        """ Returns a list of asset handles whose 'sub_type' attribute matches
        the 'sub_type' kwarg value."""

        handles = []
        for a_dict in self.get_dicts():
            sub = a_dict.get('sub_type', None)
            if sub == sub_type:
                handles.append(a_dict['handle'])
        return handles


    def get_assets_by_type(self, asset_type=None):
        """ Returns a list of asset handles whose 'type' attribute matches
        the 'asset_type' kwarg value."""

        handles = []
        for a_dict in self.get_dicts():
            a_type = a_dict.get('type', None)
            if a_type == asset_type:
                handles.append(a_dict['handle'])
        return handles


    def get_handles(self):
        """ Dumps all asset handles, i.e. the list of self.assets keys. """

        try:
            return sorted(self.assets, key=lambda x: self.assets[x]['name'])
        except:
            return sorted(self.assets.keys())


    def get_names(self):
        """ Dumps all asset 'name' attributes, i.e. a list of name values. """

        return sorted([self.assets[k]["name"] for k in self.get_handles()])

    def get_sorted_assets(self):
        """ Returns the asset collections 'assets' dict as an OrderedDict. """

        output = OrderedDict()
        for n in self.get_names():
            asset_dict = self.get_asset_from_name(n)
            output[asset_dict['handle']] = asset_dict
        return output

    def get_sub_types(self):
        """ Dumps a list of all asset 'sub_type' attributes. """

        subtypes = set()
        for a in self.get_handles():
            a_dict = self.get_asset(a)
            subtypes.add(a_dict.get('sub_type', None))
        return sorted(subtypes)

    def get_types(self):
        """ Dumps a list of all asset 'type' attributes. """

        subtypes = set()
        for a in self.get_handles():
            a_dict = self.get_asset(a)
            subtypes.add(a_dict.get('type', None))
        return subtypes

    def get_dicts(self):
        """ Dumps a list of dicts where each dict is an asset dict. """

        output = []
        for h in sorted(self.get_handles()):
            output.append(self.get_asset(h))
        return output


    def get_keywords(self):
        """ Dumps a uniquified list of rules for all assets in the dict. """

        kw = set()
        for h in self.assets.keys():
            A = self.assets[h]
            if 'keywords' in A.keys():
                kw |= set(A['keywords'])
        return sorted(list(kw))


    def get_rules(self):
        """ Dumps a uniquified list of rules for all assets in the dict. """

        rules = set()
        for h in self.assets.keys():
            A = self.assets[h]
            if 'rules' in A.keys():
                rules |= set(A['rules'])
        return sorted(list(rules))

    def get_asset_from_name(self, name, case_sensitive=False, raise_exception_if_not_found=True):
        """ Tries to return an asset dict by looking up "name" attributes within
        the self.assets. dict. Returns None if it fails.

        By default, the mactching here is NOT case-sensitive: everything is
        forced to upper() to allow for more permissive matching/laziness. """

        if type(name) not in [str,unicode]:
            self.logger.error("get_asset_from_name() cannot proceed! '%s' is not a str or unicode object!" % name)
            if raise_exception_if_not_found:
                raise AssetInitError("The get_asset_from_name() method requires a str or unicode type name!")
            else:
                return None

        name = name.strip()

        # special backoff for this dumbass pseudo-expansion
        if name == 'White Box':
            name = 'White Box & Promo'

        if not case_sensitive:
            name = name.upper()

        name_lookup = {}
        for a in self.assets.keys():
            if "name" in self.assets[a]:
                if case_sensitive:
                    name_lookup[self.assets[a]["name"]] = a
                elif not case_sensitive:
                    asset_name_upper = self.assets[a]["name"].upper()
                    name_lookup[asset_name_upper] = a

        if name in name_lookup.keys():
            return self.get_asset(name_lookup[name])
        else:
            return None

    def filter(self, filter_attrib=None, filtered_attrib_values=[], reverse=False):
        """ Drops assets from the collection if their 'filter_attrib' value is
        in the 'attrib_values' list.

        Set 'reverse' kwarg to True to have the filter work in reverse, i.e. to
        drop all assets that DO NOT have 'filter_attrib' values in the
        'filtered_attrib_values' list.
        """

        if filter_attrib is None or filtered_attrib_values == []:
            self.logger.error("AssetCollection.filter() method does not accept None or empty list values!")
            return False

        for asset_key in self.assets.keys():
            if self.get_asset(asset_key).get(filter_attrib, None) is None:
                pass
            elif reverse:
                if self.get_asset(asset_key)[filter_attrib] not in filtered_attrib_values:
                    del self.assets[asset_key]
            else:
                if self.get_asset(asset_key)[filter_attrib] in filtered_attrib_values:
                    del self.assets[asset_key]



    #
    #   no set/get/filter methods below this point!
    #

    def request_response(self, a_name=None, a_handle=None):
        """ Processes a JSON request for a specific asset from the collection,
        initializes the asset (if it can) and then calls the asset's serialize()
        method to create an HTTP response. """

        # first, if the request is a GET, just dump everything and bail
        if flask.request and flask.request.method == "GET":
            return flask.Response(
                response=json.dumps(
                    self.assets,
                    default=json_util.default
                    ),
                status=200,
                mimetype="application/json"
            )

        # next, if the request has JSON, check for params
        if flask.request and hasattr(flask.request, 'json'):
            a_name = flask.request.json.get("name", None)
            a_handle = flask.request.json.get("handle", None)

        # if there are no lookups requested, dump everything and bail
        if a_name is None and a_handle is None:
            return flask.Response(
                response=json.dumps(
                    self.assets,
                    default=json_util.default
                ),
                status=200,
                mimetype="application/json"
            )

        # finally, do lookups and create a response based on the outcome
        if a_handle is not None:
            A = self.get_asset(a_handle)
        elif a_name is not None:
            A = self.get_asset_from_name(a_name)

        if A is None:
            return utils.http_404

        return flask.Response(
            response=json.dumps(A, default=json_util.default),
            status=200,
            mimetype="application/json"
        )



class GameAsset(object):
    """ The base class for initializing individual game asset objects. All of
    the specific models in the models/ folder will sub-class this model for
    their generally available methods, etc.

    """

    def __init__(self, handle=None, name=None):

        # initialize basic vars
        self.logger = utils.get_logger()
        self.name = name
        self.handle = handle


    def __repr__(self):
        return "%s object '%s' (assets.%s['%s'])" % (self.type.title(), self.name, self.type, self.handle)


    def initialize(self):
        """ Call this method to initialize the object. """

        if self.handle is not None:
            self.initialize_from_handle()
        elif self.name is not None:
            self.initialize_from_name()
        elif self.handle is None and self.name is None:
            raise AssetInitError("Asset objects must be initialized with 'handle' or 'name' kwargs.")
        else:
            raise AssetInitError()


    def initialize_asset(self, asset_dict):
        """ Pass this a valid asset dictionary to set the object's attributes
        with a bunch of exec calls. """

        if type(asset_dict) != dict:
            raise AssetInitError("Asset objects may not be initialized with a '%s' type object!" % type(asset_dict))

        for k, v in asset_dict.items():
            if type(v) == str:
                exec("""self.%s = '%s' """ % (k,v.replace('"','\\"').replace("'","\\'")))
            elif type(v) == datetime:
                exec("""self.%s = '%s' """ % (k,v.strftime(utils.ymd)))
            else:
                exec("self.%s = %s" % (k,v))


    def initialize_from_handle(self):
        """ If we've got a not-None handle, we can initiailze the asset object
        by checking self.assets to see if our handle is a valid key.
        If we can't find a valid key, throw an exception. """

        # sanity warning
        if " " in self.handle:
            self.logger.warn("Asset handle '%s' contains whitespaces. Handles should use underscores." % self.handle)

        self.asset_dict = self.assets.get_asset(self.handle)
        self.initialize_asset(self.asset_dict)

        if self.name is None:
            raise AssetInitError("Asset handle '%s' could not be retrieved!" % self.handle)


    def initialize_from_name(self):
        """ If we've got a not-None name, we can initiailze the asset object
        by checking self.assets to see if we can find an asset whose "name"
        value matches our self.name. """


        # sanity warning
        if "_" in self.name:
            self.logger.warn("Asset name '%s' contains underscores. Names should use whitespaces." % self.name)

        lookup_dict = {}
        for asset_handle in self.assets.get_handles():
            asset_dict = self.assets.get_asset(asset_handle)
            lookup_dict[asset_dict["name"]] = asset_handle

        if self.name in lookup_dict.keys():
            self.handle = lookup_dict[self.name]
            self.initialize_from_handle()

        if self.handle is None:
            raise AssetInitError("Asset handle '%s' could not be retrieved!" % self.handle)


    def serialize(self, return_type=None):
        """ Allows the object to represent itself as JSON by transforming itself
        into a JSON-safe dict. """

        shadow_self = copy(self)

        for banned_attrib in ["logger", "assets"]:
            if hasattr(shadow_self, banned_attrib):
                delattr(shadow_self, banned_attrib)

        if return_type == dict:
            return shadow_self.__dict__

        return json.dumps(shadow_self.__dict__, default=json_util.default)


    #
    # look-up and manipulation methods below
    #

    def get(self, attrib):
        """ Wrapper method for trying to retrieve asset object attributes.
        Returns a None type value if the requested attrib doesn't exist. """

        try:
            return getattr(self, attrib)
        except:
            return None



#
#   model decorators
#

def log_event_exception_manager(log_event_call):
    """ This is a decorator for model lookups. Do not use this decorator to
    decorate other methods: it will fail.

    The basic idea here is to capture exceptions, log them, email them and NOT
    interrupt the request. This is really the only method where we ever want to
    handle exceptions this way. """

    def wrapper(self, *args, **kwargs):
        """ Wraps the incoming call. """
        try:
            return log_event_call(self, *args, **kwargs)
        except Exception as log_event_call_exception:
            err_msg = "Unhandled exception in log_event() method!"
            err_msg += "args: %s, kwargs: %s" % (args, kwargs)
            self.logger.exception(err_msg)
            utils.email_exception(log_event_call_exception)

    return wrapper
