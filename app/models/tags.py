"""

    Tags are not a game asset, so we don't expose them as one via the API,
    though they can be looked up as if they were game assets.

"""

from app import models

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        models.AssetCollection.__init__(self,  *args, **kwargs)
        self.set_default_max_values()
