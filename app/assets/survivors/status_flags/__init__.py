"""

    This is a made-up asset class that allows us to roll up certain A&Is into
    booleans that we can set on a survivor sheet.

    The handles in the definitions.py file here basically correspond to
    attributes of an A&I asset.

"""

from app.assets._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
#        self.root_module = status_flags
        Collection.__init__(self,  *args, **kwargs)
