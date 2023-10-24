'''

    This is a weird asset, since it basically collects survivor attributes.

    Loads the definitions.

'''

from .._collection import Collection
from .definitions import *


class Assets(Collection):
    ''' Survivor 'assets' are those that are defined in the beta challenge
    scenarios or the vignettes expansions. '''

    def __init__(self, *args, **kwargs):
        ''' This needs a refactor. '''

        self.is_game_asset = True
        self.type_override = "survivors"
        Collection.__init__(self, *args, **kwargs)
