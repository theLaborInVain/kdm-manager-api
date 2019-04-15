"""

    Rules sets are meta/organizational dictionaries that describe a particular
    rules set or edition of the game.

"""


from app.assets import rules_sets
from app import models

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):

        self.is_game_asset = False
        self.root_module = rules_sets
        models.AssetCollection.__init__(self,  *args, **kwargs)
