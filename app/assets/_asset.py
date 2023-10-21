"""

    The assets.Asset class definition lives here. It is the base class for any
    object that we want to initialize to represent an individual game asset.

    Use assets.Collection (also in this folder/module) for objects representing
    more than one game asset.

"""

# standard lib imports
from copy import copy
from datetime import datetime
import json

# second party imports
from bson import json_util

# local imports
from app import API, utils

# constants
ATTRIBUTE_DEFAULTS = {
    bool: True,
    datetime: datetime.now(),
    str: 'UNDEFINED',
}


class Asset():
    """ The base class for initializing individual game asset objects.

    Use this any time we need to initialize a specific game asset.

    Ultimately, this should be the base class for the (deprecated) Monster
    class, which was stylistically cool but a bad design.

    """

    def __init__(self, handle=None, name=None,
                version=API.config['DEFAULT_GAME_VERSION']):

        # initialize basic vars
        self.handle = handle
        self.logger = utils.get_logger()
        self.name = name
        self.version = version


    def __repr__(self):
        """ Custom repr for game asset objects. """
        return "%s object '%s' (assets.%s['%s'])" % (
            self.type.title(), self.name, self.type, self.handle
        )


    def initialize(self):
        """ Call this method to initialize the object. """

        if self.handle is not None:
            self.initialize_from_handle()
        elif self.name is not None:
            self.initialize_from_name()
        elif self.handle is None and self.name is None:
            err = (
                "Asset objects must be initialized with 'handle' or 'name' "
                "kwargs."
            )
            raise AssetInitError(err)
        else:
            raise AssetInitError()


    def initialize_asset(self, asset_dict):
        """ Pass this a valid asset dictionary to set the object's attributes
        with a bunch of exec calls. """

#        if type(asset_dict) != dict:
        if not isinstance(dict):
            err = "Assetss may not be initialized with a '%s' type object!"
            raise AssetInitError(err % type(asset_dict))

        # mandatory attribute sanity check!
        for required_attr in ['handle', 'name']:
            if not required_attr in asset_dict.keys():
                raise AttributeError(
                    "Asset dictionary has no '%s' attribute! %s" % (
                        required_attr,
                        asset_dict
                    )
                )

        for k, v in asset_dict.items():
            if type(v) == str:
                exec("""self.%s = '%s' """ % (
                    k,v.replace('"','\\"').replace("'","\\'")
                    )
                )
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
            err = (
                "Asset handle '%s' contains whitespaces. Handles should use "
                "underscores and never have whitespaces. Did you mean 'name'?"
            ) % self.handle
            self.logger.error(err, self.handle)

        self.asset_dict = self.assets.get_asset(self.handle)
        self.initialize_asset(self.asset_dict)

        if self.name is None:
            raise AssetInitError(
                "Asset handle '%s' ('%s') could not be initialized! %s " % (
                    self.name,
                    self.handle,
                    self.asset_dict
                )
            )


    def initialize_from_name(self):
        """ If we've got a not-None name, we can initiailze the asset object
        by checking self.assets to see if we can find an asset whose "name"
        value matches our self.name. """


        # sanity warning
        if "_" in self.name:
            err = (
                "Asset name '%s' contains underscores. Names should use "
                "whitespaces. Did you mean 'handle'?"
            ) % self.name
            self.logger.error(err, self.name)

        lookup_dict = {}
        for asset_handle in self.assets.get_handles():
            asset_dict = self.assets.get_asset(asset_handle)
            lookup_dict[asset_dict["name"]] = asset_handle

        if self.name in lookup_dict.keys():
            self.handle = lookup_dict[self.name]
            self.initialize_from_handle()

        if self.handle is None:
            err = "Asset handle '%s' could not be retrieved!"
            raise AssetInitError(err, self.handle)


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
