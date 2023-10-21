"""

    This is the class object code for creating a small, pseudo asset collection
    of information about The Constellations (in the Dragon King expansion).

"""

from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        Collection.__init__(self,  *args, **kwargs)
