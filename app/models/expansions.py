"""

    The class object for working with the expansion assets is here, as well as
    the object init code for working with an individual expansion as an object.

"""

from app.assets import expansions
from app import models, utils


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        """ Expansion assets are organized in assets/expansions.py according to
        release date, so when we initialize an asset dict from expansions.py, we
        manually add a "meta" style key to indicate their release date. """

        self.root_module = expansions
        models.AssetCollection.__init__(self,  *args, **kwargs)


class Expansion(models.GameAsset):
    """ This is the base class for all expansions. Private methods exist for
    enabling and disabling expansions (within a campaign/settlement). """

    def __init__(self, *args, **kwargs):
        models.GameAsset.__init__(self,  *args, **kwargs)

        self.assets = Assets()
        self.baseline()
        self.initialize()


    def baseline(self):
        """ Default some attributes for self. Everything here is subject
        to overwrite by the self.initialize() call. """

        self.survivor_special_attributes = []
