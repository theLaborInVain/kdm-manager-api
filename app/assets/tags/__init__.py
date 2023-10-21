"""

    Tags are not a game asset, so we don't expose them as one via the API,
    though they can be looked up as if they were game assets.

"""

from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        Collection.__init__(self,  *args, **kwargs)
        self.set_default_max_values()
