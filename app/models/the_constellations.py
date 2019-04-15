"""

    This is the class object code for creating a small, pseudo asset collection
    of information about The Constellations (in the Dragon King expansion).

"""


from app.assets import the_constellations
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
#        self.assets = survivor_sheet_options.the_constellations
#        self.type_override = "the_constellations"
        self.is_game_asset = False
        self.root_module = the_constellations
        models.AssetCollection.__init__(self,  *args, **kwargs)
