from app.assets.survivors import weapon_proficiency
from app import models
import utils


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
#        self.type_override = "weapon_proficiency"
#        self.assets = survivor_sheet_options.weapon_proficiency
        self.root_module = weapon_proficiency
        models.AssetCollection.__init__(self,  *args, **kwargs)
