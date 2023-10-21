"""

    Farting Arts collection object is managed here.

"""

from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)
