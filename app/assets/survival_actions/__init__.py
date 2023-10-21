'''

    Survival actions have to be a game asset because of all the rules and
    business logic that hang onto them.

    Mostly they work as a collection, however, so there is no method to
    initialize an individual one.

'''


from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)

