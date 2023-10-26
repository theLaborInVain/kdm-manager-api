"""

    The Collection class definition is here. Initialize one of these to work
    with a specific collection of game assets.

    Note that a 'collection' is not a module. Many game assets span multiple
    files.

"""

# standard lib imports
from collections import OrderedDict
from copy import copy
from datetime import datetime
import importlib
import inspect
import json

# second-party imports
from bson import json_util
import flask

# KDM API imports
from app import API, utils
from app.assets.versions import definitions as versions_definitions


class Collection():
    """ The base class for game asset objects, i.e. working with the dict assets
    in the assets/ folder.

    Most Asset() objects that use this as their base class will define their own
    self.assets dict, e.g. in their __init__() method. But is not mandatory:
    review the __init__ method of this class carefully before writing custom
    __init__ code in in an individual Asset() object module. """


    def __init__(self, assets_version=API.config['DEFAULT_GAME_VERSION'],
                asset_logger=False):
        """ All Assets() objects must base-class this guy to get access to the
        full range of AssetCollection methods, i.e. all of the common/ubiquitous
        ones.

        self.mandatory_attributes is deprecated and in the process of being
        killed off.
        """

        # init both loggers
        self.logger = utils.get_logger()
        self.asset_logger = asset_logger
        if self.asset_logger:
            self.asset_logger = utils.get_logger(
                log_level='DEBUG', log_name='asset_collection'
            )
            self.asset_logger.debug('Asset logger initialized!')

        # set self.version, which MUST be a version handle. Die if it's not
        self.version = assets_version
        if not isinstance(self.version, str):
            err = "'asset_version' must be a version handle, 'not %s' / %s"
            raise AttributeError(err % (self.version, type(self)))

        # asset debugger 
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        caller_func = calframe[2][1]
        if self.asset_logger:
            self.asset_logger.debug(
                'Initializing %s.%s() at KD:M version %s. Caller: %s',
                self.__module__, self.__class__.__name__,
                self.version,
                caller_func
            )

        # set the game_asset attrib first (default to True)
        if not hasattr(self, 'is_game_asset'):
            self.is_game_asset = True

        # set some misc attributes
        self.type = self.__module__.split('.')[-1]

        # set self.root_module
        if hasattr(self, 'root_module'):
            self._set_root_module()

        # now that we've set the root module, set attribs and assets from it
        self._set_assets_from_root_module()

        #
        # IMPORTANT! self.assets must be set by this point no matter what!
        #


        # type override - be careful!
        if hasattr(self, "type_override"):
            self._set_override_type()

        # set the default 'type_pretty' value, selector text, etc. DO NOT
        # call this method before you have a sub_type
        self.set_ui_attribs()

        # force all assets to have a 'handle' (that matches their key)
        for a in self.assets.keys():
            self.assets[a]["handle"] = a

        # enforce mandatory_attributes dictionary now, if we're doing that:
        if hasattr(self, 'mandatory_attributes'):
            warn_on = False
            if hasattr(self, "warn_on_missing_mandatory_attribute"):
                warn_on = True
            self.enforce_mandatory_attributes(warn_on)

        # finally, enforce the self.data_model, if it exists
        self.enforce_data_model()

        self._initialized = True


    def __repr__(self):
        """ Complicated __repr__ for asset collections which are...complex."""

        self.logger = utils.get_logger()

        if not hasattr(self, 'type'):
            warn = "%s module %s object does not have a 'type' attribute!"
            self.logger.warning(warn, self.__class__.__name__, self.__module__)
            return 'AssetCollection object (no type; %s assets)' % (
                len(getattr(self, 'assets', []))
            )

        return "AssetCollection object '%s' (%s assets)" % (
            self.type,
            len(getattr(self, 'assets', []))
        )



    def enforce_data_model(self):
        """ If the collection is initialized with a self.data_model dict, we
        check all assets in self.assets to make sure they have a value for each
        key in the dict (and that it is the right type).

        DEPRECATED. Should be replaced with something like how we do models.
        """

        # defaults
        attr_defaults = {
            bool: True,
            datetime: datetime.now(),
            str: 'UNDEFINED',
        }

        # iterate thru the data model
        for attr_name, attr_type in getattr(self, 'data_model', {}).items():
            attr_default = attr_defaults[attr_type]

            # iterate through all asset dicts
            for asset_dict in self.get_dicts():
                asset_handle = asset_dict['handle']
                if attr_name not in asset_dict.keys():
                    self.assets[asset_handle][attr_name] = attr_default


    def enforce_mandatory_attributes(self, warn_on_missing_attr=False):
        """ This method checks each asset in the collection against a dictionary
        defined in the app/assets/whatever/__init__.py file for the collection.

        These dictionaries are simple and each key has one value, which is also
        teated as the default value:

           {'keywords': [], 'desc': ""}

        That dict would enforce those attributes being defined as the exact
        value specified.
        """

        for mandatory_attribute in self.mandatory_attributes.keys():
            for a_dict in self.get_dicts():
                if mandatory_attribute not in a_dict.keys():

                    # warn if we're warning
                    if warn_on_missing_attr:
                        err = "Asset '%s' missing mandatory attr: '%s'!"
                        self.logger.warning(
                            err, a_dict['handle'], mandatory_attribute
                        )

                    self.assets[
                        a_dict['handle']
                    ][mandatory_attribute] = self.mandatory_attributes[
                        mandatory_attribute
                    ]

    #
    #   get / set / filter methods here
    #

    def _set_root_module(self):
        ''' This is broken out to be its own function so we can kill it off.
        Allows overriding the default module, for purposes of importing assets.
        Really hate this. '''

        warn = "DEPRECATION WARNING! Overriding module for '%s' to '%s'"
        self.logger.warning(warn, self.__module__, self.root_module)
        self.root_module = importlib.import_module(self.root_module.__name__)
        self.type = self.root_module.__name__.split('.')[-1]
        warn = "Type for '%s' assets overriden to '%s'"
        self.logger.warning(warn, self.__module__, self.type)


    def _set_override_type(self):
        ''' A private, depracted method for overriding the default 'type' attr
        for the collection. This should never be necessary and the goal will be
        to kill this off in 2023. '''

        warn = "DEPRECATION WARNING! %s has 'self.type_override' attribute. "
        warn += "%s assets will have type '%s' instead of default value: '%s'"
        self.logger.warning(
            warn, self, self.__module__, self.type_override, self.type
        )

        if self.type == self.type_override:
            err = 'Attempting to override an identical default. Please fix.'
            raise AttributeError(err)

        self.type = self.type_override
        for a in self.assets.keys():
            if not isinstance(self.assets[a], dict):
                self.logger.error(self.assets)
                err = (
                    "AssetCollection object self.assets() dict should be a "
                    "dictionary of dictionaries, not %s."
                )
                raise TypeError(err % type(self.assets[a]))
            self.assets[a]["type"] = self.type_override


    def _validate_root_module(self):
        ''' Loads the self.root_module. Sanity checks it. Logs verbose failures
        for easy identification/resolution of asset definition errors.

        Returns a dictionary of asset dictionaries.
        '''

        package = importlib.import_module(self.__module__)
        if hasattr(self, 'root_module'):
            package = self.root_module

        package_path = package.__name__
        package_name = package.__name__.split('.')[-1]

        if self.asset_logger:
            self.asset_logger.debug(' - Validating %s package...', package_path)

        # ban private packages / remind not to __init__() twice
        if package_name.startswith('_'):
            curframe = inspect.currentframe()
            caller = inspect.getouterframes(curframe, 1)[3][1]
            err = "Assets cannot be loaded from private packages! "
            err += "Root module '%s' cannot be used. Caller: %s"
            err += 'Did you initialize twice? e.g. Collection().__init__() ?'
            raise AttributeError(err % (package_name, caller))


        asset_definitions = [
            dict_handle for dict_handle in package.__dict__
            if (
                isinstance(package.__dict__[dict_handle], dict) and
                not dict_handle.startswith('_') # avoid built-in/private dicts
            )
        ]
        if self.asset_logger:
            self.asset_logger.debug(
                ' - Package contains %s definitions', len(asset_definitions)
            )

        output = {}
        asset_count = 0
        for asset_definition_name in asset_definitions:

            asset_definition = package.__dict__[asset_definition_name]

            # check types here; these can ONLY be strings, i.e. asset handle
            for asset_handle in asset_definition.keys():

                # bomb out if the asset_handle isn't a str
                if not isinstance(asset_handle, str):
                    err = "%s module '%s' asset handle '%s' %s is not str type!"
                    raise AttributeError(
                        err % (
                            package_path,
                            asset_definition_name,
                            asset_handle,
                            type(asset_handle)
                        )
                    )

                # load the individual asset dict
                asset_count += 1
                asset = asset_definition[asset_handle]

                # validate / sanity / unit test the assets
                if 'sub_type' in asset.keys():
                    err = "%s module '%s' asset includes 'sub_type' key! \n"
                    err += "Asset definitions may not define 'sub_type': %s \n"
                    err += 'Original definition is: %s'
                    raise AttributeError(
                        err % (package_path, asset_handle, asset,
                        asset_definition)
                    )

                if 'name' not in asset.keys():
                    err = "Asset has no 'name' attribute! %s"
                    self.logger.warning(err, asset)

            output[asset_definition_name] = asset_definition

        if self.asset_logger:
            self.asset_logger.debug(' - Package defines %s assets', asset_count)
        return output


    def _set_assets_from_root_module(self):

        """ This is the vanilla AssetCollection initialization method. You feed
        it a 'module' value (which should be something from the assets/ folder)
        and it creates a self.assets dictionary by iterating through the module.

        If you need to do custom asset initialization, that is a fine and a good
        thing to do, but do it in the actual massets/whatever/__init__.py file.

        Important! Adjusting the self.assets dict before calling this method
        will overwrite any adjustments because this method starts self.assets as
        a blank dict!

        Finally, as of October 2021, this method supports the kwarg 'version',
        which allows the assets to be updated to 'version'.
        """

        asset_dictionaries = self._validate_root_module()

        all_assets = {}

        for asset_def_handle, definition_dict in asset_dictionaries.items():

            # iterate through the assets; make a new one to preserve the def
            for asset_handle, asset in definition_dict.items():
                new_asset = copy(asset)
                new_asset['handle'] = asset_handle
                new_asset['sub_type'] = asset.get("type", asset_def_handle)
                new_asset["type"] = self.type  # override with module attribute

                # add it back to self.assets
                all_assets[asset_handle] = new_asset

        # sort on name, allowing for the possibility of duplicate names
        self.assets = OrderedDict()
        list_of_dicts = [all_assets[handle] for handle in all_assets]
        for asset in sorted(list_of_dicts, key = lambda i: i['name']):
            self.assets[asset['handle']] = asset

        # now step through versions and update until target
        self.patch_assets_to_current()

        # set the laziness attribute self.handles
        self.handles = sorted(self.assets.keys())

        if self.asset_logger:
            self.asset_logger.debug(' - %s assets loaded!', self.type)
            for asset in all_assets:
                self.asset_logger.debug(' - %s', asset)
                for key, value in all_assets[asset].items():
                    self.asset_logger.debug('   `- %s: %s', key, value)



    def patch_assets_to_current(self):
        """ Updates self.assets with all version updates between baseline and
        'target'. Is basically a cumulative patch. Uses self.version, a str
        version handle. """

        try:
            target_vers_dict = versions_definitions.VERSIONS[self.version]
        except KeyError as error:
            msg = "Version handle '%s' not found in %s -> %s" % (
                self.version, versions_definitions.VERSIONS.keys(), error
            )
            self.logger.error(msg)
            raise
        for v_key in versions_definitions.VERSIONS.keys():
            v_dict = versions_definitions.VERSIONS[v_key]
            if v_dict['released'] <= target_vers_dict['released']:
                if (
                    v_dict.get('assets', None) is not None and
                    v_dict['assets'].get(self.type, None) is not None
                ):
                    updates = v_dict['assets'][self.type]
                    for asset_handle in v_dict['assets'].get(self.type, {}):
                        self.assets[asset_handle].update(updates[asset_handle])
                        self.assets[asset_handle]['patch_level'] = v_key


    def set_default_max_values(self, default_max=1):
        """ Use this with asset collections where there is a 'max' attribute,
        e.g. Abilities & Impairments or similar. Calling this method sets
        the 'max' key/value for each asset in the collection to the
        'default_max' value. """

        for d in self.get_dicts():

            asset_max = d.get("max", None)
            asset_handle = d["handle"]

            if asset_max is None:
                self.assets[asset_handle]["max"] = default_max
            elif asset_max is False:
                self.assets[asset_handle]["max"] = 666


    def set_ui_attribs(self, capitalize=True):
        """ Iterates over self.assets; adds the "type_pretty" and 'sub_type_pretty'
        to all assets in the AssetCollection.assets dict """

        for h in self.assets.keys():

            #
            #   init
            #
            a_dict = self.get_asset(handle=h)
            if a_dict.get('type', None) is None:
                raise AttributeError("%s asset has no 'type' attribute! %s" % (self, a_dict))

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

            # special extra text for Secret fighting arts
            if a_dict.get('sub_type', None) == 'secret_fighting_art':
                parenthetical.append('Secret')

            if a_dict.get('sub_type', None) == 'strain':
                parenthetical.append('Strain')

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
        raise_exception_if_not_found=True, exclude_keys=[]):

        """ Return an asset dict based on a handle. Return None if the handle
        cannot be retrieved. """

        asset = copy(self.assets.get(handle, None))     # return a copy

        # implement backoff logic
        if asset is None and backoff_to_name:
            asset = copy(self.get_asset_from_name(handle))

        # if the asset is still None, we want to raise an expception
        if asset is None and raise_exception_if_not_found:
            if not backoff_to_name:
                curframe = inspect.currentframe()
                calframe = inspect.getouterframes(curframe, 2)
                caller_function = calframe[1][3]
                msg = (
                    "%s() -> get_asset() "
                    "The handle '%s' could not be found in %s!"
                ) % (caller_function, handle, self.get_handles() )
                self.logger.error(msg)
            elif backoff_to_name:
                msg = "After backoff to name lookup, asset handle '%s' is not\
                in %s and could not be retrieved." % (handle, self.get_names())
                self.logger.error(msg)
            raise utils.InvalidUsage(msg, status_code=500)

        for key in exclude_keys:
            del asset[key]

        # finally, return the asset (or the NoneType)
        return asset


    def get_asset_from_name(self, name, case_sensitive=False,
            raise_exception_if_not_found=True):
        """ Tries to return an asset dict by looking up "name" attributes within
        the self.assets. dict. Returns None if it fails.

        By default, the mactching here is NOT case-sensitive: everything is
        forced to upper() to allow for more permissive matching/laziness.

        DEPRECATED in October 2023.
        """

        # fail if we don't get a str
        if not isinstance(name, str):
            err = "get_asset_from_name() 'name' kwarg must be 'str'! Not: %s"
            if raise_exception_if_not_found:
                raise TypeError(err % (type(name)))
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
        return None


    def get_dicts(self):
        """ Dumps a list of dicts where each dict is an asset dict. """
        output = []
        for h in sorted(self.get_handles()):
            output.append(self.get_asset(h))
        return output


    def get_sorted_assets(self):
        """ Returns the asset collections 'assets' dict as an OrderedDict. """

        output = OrderedDict()
        for n in self.get_names():
            asset_dict = self.get_asset_from_name(n)
            output[asset_dict['handle']] = asset_dict
        return output


    def get_assets_by_type(self, asset_type=None):
        """ Returns a list of asset handles whose 'type' attribute matches
        the 'asset_type' kwarg value."""

        handles = []
        for a_dict in self.get_dicts():
            a_type = a_dict.get('type', None)
            if a_type == asset_type:
                handles.append(a_dict['handle'])
        return handles


    def get_assets_by_sub_type(self, sub_type=None):
        """ Returns a list of asset handles whose 'sub_type' attribute matches
        the 'sub_type' kwarg value."""

        handles = []
        for a_dict in self.get_dicts():
            sub = a_dict.get('sub_type', None)
            if sub == sub_type:
                handles.append(a_dict['handle'])
        return handles


    #
    #   get lists of things
    #

    def get_handles(self):
        """ Dumps all asset handles, i.e. the list of self.assets keys. """

        try:
            return sorted(self.assets, key=lambda x: self.assets[x]['name'])
        except Exception as err:
            self.logger.warning('get_handles() error: %s', err)
            return sorted(self.assets.keys())


    def get_names(self):
        """ Dumps all asset 'name' attributes, i.e. a list of name values. """
        try:
            for h in self.get_handles():
                if isinstance(self.assets[h], list):
                    err = '%s Asset (%s) is a list! %s'
                    raise TypeError(err % (self, h, self.assets[h]))
            return [copy(self.assets[h]["name"]) for h in self.get_handles()]
        except KeyError as e:
            self.logger.error("Asset does not have 'name' key!")
            self.logger.error("Assets without 'name' keys follow...")
            for handle in self.get_handles():
                if self.assets[handle].get('name', None) is None:
                    self.logger.error(self.assets[handle])
            raise e


    def get_types(self):
        """ Dumps a list of all asset 'type' attributes. """

        subtypes = set()
        for a in self.get_handles():
            a_dict = self.get_asset(a)
            subtypes.add(a_dict.get('type', None))
        return subtypes


    def get_sub_types(self):
        """ Dumps a list of all asset 'sub_type' attributes. """

        subtypes = set()
        for a in self.get_handles():
            a_dict = self.get_asset(a)
            subtypes.add(a_dict.get('sub_type', None))
        return sorted(subtypes)


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



    def filter(self, filter_attrib=None, filtered_attrib_values=[],
                reverse=False):
        """ Starting in October 2023, this is cancelled.

        Usually you can use get_assets_by_type or get_assets_by_sub_type.
        """

        err = "%s.filter() is no longer supported!"
        raise AttributeError(err % self.__module__)


    #
    #   no set/get/filter methods below this point!
    #

    def request_response(self, a_name=None, a_handle=None):
        """ Processes a JSON request for a specific asset collection,
        initializes the collection (if it can) and then dumps the self.assets
        dict as a Flask response.

        As of October 2023, this method supports individual lookups, but that
        is deprecated: those need to go to assets.Asset (in the _asset.py
        module).

        """

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


        # START FALLBACK

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

        # END FALLBACK

        # finally, do lookups and create a response based on the outcome
        warn = (
            'DEPRECATED: do not use assets.Collection for individual asset '
            'lookups! Request was %s' % flask.request
        )
        self.logger.warning(warn)

        if a_handle is not None:
            asset_dict = self.get_asset(a_handle)
        elif a_name is not None:
            asset_dict = self.get_asset_from_name(a_name)

        if asset_dict is None:
            return utils.http_404

        return flask.Response(
            response=json.dumps(asset_dict, default=json_util.default),
            status=200,
            mimetype="application/json"
        )
