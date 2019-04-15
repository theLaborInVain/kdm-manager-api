from app.assets import rules
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False  # we're hiding this from the indexer for now
        self.root_module = rules
        models.AssetCollection.__init__(self,  *args, **kwargs)

