"""

    This is basically a reference collection where the handles correspond to
    gear handles and we use the lookups here to learn about curses.

"""

from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        Collection.__init__(self,  *args, **kwargs)
