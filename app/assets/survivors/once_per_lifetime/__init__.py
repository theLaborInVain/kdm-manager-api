
'''

    This asset represents a survivor attribute that can be toggled on or off
    to reflect whether they have done a 'once per lifetime' event.

'''

from app.assets._collection import Collection

from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = True
        Collection.__init__(self,  *args, **kwargs)
