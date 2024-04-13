'''

    Starting Octobner 2023, rules are a game asset.

    Ultimately, they will be a paywalled game asset, but that will come later.

'''

from .._collection import Collection

from .definitions import *
from .expansions_of_death_1 import *
from .gamblers_chest import *
from .white_box import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)

