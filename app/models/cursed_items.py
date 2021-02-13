"""

    This is basically a reference collection where the handles correspond to gear
    handles and we use the lookups here to learn about curses.

"""

from app import models
from app.assets import cursed_items


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = cursed_items
        self.is_game_asset = False
        models.AssetCollection.__init__(self,  *args, **kwargs)
