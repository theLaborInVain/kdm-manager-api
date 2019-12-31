"""

    Methods for working with individual Storage objects inclue the private one
    defined here, i.e. get_collection(), which allows you to use an initialized
    Storage "location" to get a list of all items that live at that location.

"""


from app.assets import storage
from app.models import gear, resources
from app import models, utils

Gear = gear.Assets()
Resources = resources.Assets()

#
#   general object methods
#


def handle_to_item_object(handle=None):
    """ The authoritative way to turn a storage handle into a game asset
    object. If you see this happening on the fly anywhere, then we've
    failed. """

    if handle in Gear.handles:
        return gear.Gear(handle)
    elif handle in Resources.handles:
        return resources.Resource(handle)

    err = 'Unknown game asset handle: %s' % handle
    raise utils.InvalidUsage(err)


#
#   Asset collection
#

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        self.root_module = storage
        models.AssetCollection.__init__(self,  *args, **kwargs)


#
#   Object
#

class Storage(models.GameAsset):
    """ This is what is called a 'location' elsewhere, basically an object
    that represents a group of items in storage. """


    def __init__(self, *args, **kwargs):
        models.GameAsset.__init__(self,  *args, **kwargs)
        self.assets = Assets()
        self.initialize()


    def get_collection(self):
        """ Creates a dictionary of the gear/resource assets that live in this
        location. """

        if self.sub_type == 'gear':
            A = Gear
        elif self.sub_type == 'resources':
            A = Resources
        else:
            self.logger.error(self.asset_dict)
            err_msg = "'%s' is not a valid 'sub_type' for storage asset: %s" % (
                self.sub_type,
                self
            )
            raise ValueError(err_msg)

        return A.get_assets_by_sub_type(self.handle)
