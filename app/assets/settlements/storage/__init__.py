"""

    Storage is a pseudo asset that basically allows us to build settlement
    storage views programmatically without junking up the locations package.

    There is no definitions.py in this package because it takes its definitions
    from the assets.locations package.

"""

from app import API

from app.assets._asset import Asset
from app.assets._collection import Collection

from app.assets import gear as KingdomDeathGear
from app.assets import resources as KingdomDeathResources

from app.assets.locations import gear, resources

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        Collection.__init__(self,  *args, **kwargs)


class Storage(Asset):
    """ This is what is called a 'location' elsewhere, basically an object
    that represents a group of items in storage. """


    def __init__(self, *args, **kwargs):
        # initialize the AssetCollection at an arbitrary version, defaulting to
        #   whatever the current/HEAD version of the game is; theory being, 
        self.version = kwargs.get('version', API.config['DEFAULT_GAME_VERSION'])
        self.assets = Assets(self.version)
        Asset.__init__(self,  *args, **kwargs)


    def get_collection(self):
        """ Creates a dictionary of the gear/resource assets that live in this
        location. """

        if self.sub_type == 'gear':
            asset_collection = KingdomDeathGear.Assets(self.version)
        elif self.sub_type == 'resources':
            asset_collection = KingdomDeathResources.Assets(self.version)
        else:
            self.logger.error(self.asset_dict)
            err_msg = "'%s' is not a valid 'sub_type' for storage asset: %s" % (
                self.sub_type,
                self
            )
            raise ValueError(err_msg)

        return asset_collection.get_assets_by_sub_type(self.handle)
