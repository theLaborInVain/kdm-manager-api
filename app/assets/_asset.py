"""

    The assets.Asset class definition lives here. It is the base class for any
    object that we want to initialize to represent an individual game asset.

    Use assets.Collection (also in this folder/module) for objects representing
    more than one game asset.

"""

# standard lib imports
from copy import copy
from datetime import datetime
import importlib
import json

# second party imports
from bson import json_util

# local imports
from app import API, utils


class Asset():
    """ The base class for initializing individual game asset objects.

    Use this any time we need to initialize a specific game asset.

    Ultimately, this should be the base class for the (deprecated) Monster
    class, which was stylistically cool but a bad design.

    """

    def __init__(self, handle=None, collection_obj=None, force=False):
        """ Starting in October 2023, assets must be initialized with an already
        initialized Collection object as the 'collection_obj' kwarg.

        This gets us off the hook for processing version info: in theory, the
        collection itself is initialized at the target version and we just use
        that for our asset.

        Finally, set 'force' to initialize without a 'collection_obj' at the
        API's default game version. But don't say I didn't warn you. """

        # initialize basic vars
        self.collection_obj = collection_obj
        self.force = force
        self.handle = handle
        self.loaded = False
        self.logger = utils.get_logger()
        self.name = None

        self.load()


    def __repr__(self):
        """ Custom repr for game asset objects. """
        return "%s object '%s' (package: %s, handle: '%s')" % (
            getattr(self, 'type', 'UNDEFINED ASSET TYPE'),
            getattr(self, 'name', None),
            self.__module__,
            getattr(self, 'handle', None)
        )


    def load(self):
        """ Call this method to initialize the object. """

        # bail if we're already loaded
        if self.loaded:
            warn = '%s game asset object already loaded!'
            self.logger.info(warn, self.__module__)
            return

        # die if there's no self.handle
        if self.handle is None:
            err = "Asset objects require 'handle' kwarg to initialize!"
            raise AttributeError(err)

        # make sure we have a collection_obj to get the asset from
        if (
            not hasattr(self.collection_obj, 'type') and
            self.collection_obj is None
        ):
            self._initialize_asset_collection_obj()

        # deprecated / legacy support:
        if hasattr(self, 'assets'):
            self._legacy_init()

        # otherwise, load from the asset's module
        self.asset = self.collection_obj.get_asset(self.handle)

        # set some object attributes for laziness
        self.name = self.asset['name']

        self.loaded = True


    #
    #   private/deprecated methods
    #

    def _initialize_asset_collection_obj(self):
        ''' Log a detailed complaint if we're here because that means that we
        are trying to initialize without a collection object. Fail if self.force
        isn't set during init of the asset. '''

        default_game_version = API.config['DEFAULT_GAME_VERSION']

        # always log a warning when doing this
        warn = "%s asset '%s' initialized without a collection_obj!"
        warn = warn % (self.__module__, self.handle)
        self.logger.warning(warn)

        # if force isn't set, log a warning and raise an exception
        if not self.force:
            err = warn + (
                " Use 'force' kwarg to bypass this exception and initialize"
                " the asset at default Kingdom Death version '%s'"
            )
            raise AttributeError(err % default_game_version)

        # if we're still here, assuming we're forcing
        warn = 'self.force = %s; initializing %s collection_obj...'
        self.logger.warning(warn, self.force, self.__module__)
        asset_package = importlib.import_module(self.__module__)
        self.collection_obj = asset_package.Assets(
             assets_version = default_game_version
        )


    def _legacy_init(self):
        ''' This is basically the cold feed method for assets and, as of October
        2023 is fully deprecated.

        The basic scenario that this used to accomodate was one where we had an
        asset definition dict that we wanted to use to bootstrap an asset
        without having to mess around with a collection.

        Since that is never the case anymore, this method's days are numbered.
        '''

#        warn = 'DEPRECATION WARNING: %s game asset attrib set explicitly!'
#        self.logger.warning(warn, self.__module__)

        asset_dict = self.assets.get_asset(self.handle)

        if not isinstance(asset_dict, dict):
            err = "Assets may not be initialized with a '%s' type object!"
            raise TypeError(err % type(asset_dict))

        # this is hellish and badly needs refactoring/deprecation
        for key, value in asset_dict.items():
            if isinstance(value, str):
                exec("""self.%s = '%s' """ % (
                    key, value.replace('"','\\"').replace("'","\\'")
                    )
                )
            elif isinstance(value, datetime):
                exec("""self.%s = '%s' """ % (key, value.strftime(utils.ymd)))
            else:
                setattr(self, key, value)

        if self.name is None:
            raise AttributeError(
                "Asset handle '%s' ('%s') could not be initialized! %s " % (
                    self.name,
                    self.handle,
                    asset_dict
                )
            )


    def serialize(self, return_type=None):
        """ Allows the object to represent itself as JSON by transforming itself
        into a JSON-safe dict. """

        shadow_self = copy(self)

        for banned_attrib in ["logger", "assets", 'collection_obj']:
            if hasattr(shadow_self, banned_attrib):
                delattr(shadow_self, banned_attrib)

        if return_type == dict:
            return shadow_self.__dict__

        return json.dumps(shadow_self.__dict__, default=json_util.default)
