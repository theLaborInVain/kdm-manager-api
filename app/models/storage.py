"""

    Methods for working with individual Storage objects inclue the private one
    defined here, i.e. get_collection(), which allows you to use an initialized
    Storage "location" to get a list of all items that live at that location.

"""


from app.assets import storage
from app.models import gear, resources
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        self.root_module = storage
        models.AssetCollection.__init__(self,  *args, **kwargs)


class Storage(models.GameAsset):

    def __init__(self, *args, **kwargs):
        models.GameAsset.__init__(self,  *args, **kwargs)
        self.assets = Assets()
        self.initialize()


    def get_collection(self):
        """ Creates a dictionary of the gear/resource assets that live in this
        location. """

        if self.sub_type == 'gear':
            A = gear.Assets()
        elif self.sub_type == 'resources':
            A = resources.Assets()
        else:
            self.logger.error(self.asset_dict)
            err_msg = "'%s' is not a valid 'sub_type' for storage asset: %s" % (
                self.sub_type,
                self
            )
            raise ValueError(err_msg)

        return A.get_assets_by_sub_type(self.handle)



