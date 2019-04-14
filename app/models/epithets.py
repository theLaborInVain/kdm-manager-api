"""

    Epithets, or "tags" as they're called in Advanced KDM Manager, are not a
    game asset, so we don't expose them as one via the API, though they can
    be looked up as if they were game assets.

"""

from app.assets import epithets
from app import models

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        self.root_module = epithets
        models.AssetCollection.__init__(self,  *args, **kwargs)
        self.set_default_max_values()
