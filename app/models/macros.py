"""

    Macro model management methods, mainly.

"""

from app.assets import macros
from app import models

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        self.root_module = macros
        models.AssetCollection.__init__(self,  *args, **kwargs)
