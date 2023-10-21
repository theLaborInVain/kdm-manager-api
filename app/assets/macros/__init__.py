"""

    Macro model management methods, mainly.

"""

from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = True
        Collection.__init__(self,  *args, **kwargs)
