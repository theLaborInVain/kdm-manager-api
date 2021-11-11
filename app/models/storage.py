"""

    Methods for working with individual Storage objects inclue the private one
    defined here, i.e. get_collection(), which allows you to use an initialized
    Storage "location" to get a list of all items that live at that location.

"""


from app.assets import storage
from app import API, models, utils


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
        # initialize the AssetCollection at an arbitrary version, defaulting to
        #   whatever the current/HEAD version of the game is
        self.version = kwargs.get('version', API.config['DEFAULT_GAME_VERSION'])
        self.assets = Assets(self.version)
        self.initialize()


    def get_collection(self):
        """ Creates a dictionary of the gear/resource assets that live in this
        location. """

        if self.sub_type == 'gear':
            A = models.gear.Assets(self.version)
        elif self.sub_type == 'resources':
            A = models.resources.Assets(self.version)
        else:
            self.logger.error(self.asset_dict)
            err_msg = "'%s' is not a valid 'sub_type' for storage asset: %s" % (
                self.sub_type,
                self
            )
            raise ValueError(err_msg)

        return A.get_assets_by_sub_type(self.handle)
