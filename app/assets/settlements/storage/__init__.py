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

from app.assets.locations import gear, resources, location

class Assets(Collection):
    ''' Assets here (see imports above) come from the assets.locations package.
    '''

    def __init__(self, *args, **kwargs):
        ''' Technically, the locations themselves are the game assets. The items
        in this collection are...not the same.'''

        self.is_game_asset = False
        Collection.__init__(self,  *args, **kwargs)


class Storage(Asset):
    """ This is what is called a 'location' elsewhere, basically an object
    that represents a group of items in storage. """


    def __init__(self, *args, **kwargs):
        raise AttributeError(kwargs)
        self.version = kwargs.get('version', API.config['DEFAULT_GAME_VERSION'])
        self.assets = Assets(self.version)
        Asset.__init__(self,  *args, **kwargs)


    def get_collection(self):
        """ Uses self.handle to return a dictionary of the gear/resource asset
        handles that are organized under this location in settlement storage.

        self.handle is something like 'basic_resources' or 'sacred_pool'

        We use asset collections here to get the assets whose 'sub_type' attrib
        matches to self.handle.

        November 2023: we might not need this anymore.
        """

        if self.sub_type == 'gear':
            asset_collection = KingdomDeathGear.Assets(self.version)
            return asset_collection.get_assets_by_sub_type(self.handle)
        if self.sub_type == 'resources':
            asset_collection = KingdomDeathResources.Assets(self.version)
            return asset_collection.get_assets_by_sub_type(self.handle)

        self.logger.error(self.asset_dict)
        err_msg = "'%s' is not a valid 'sub_type' for storage asset: %s" % (
            self.sub_type,
            self
        )
        raise ValueError(err_msg)

