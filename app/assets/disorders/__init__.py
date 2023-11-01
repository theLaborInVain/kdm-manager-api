"""

    The class method for creating the Disorders asset collection lives here.

"""

from .._collection import Collection

# definition imports
from .definitions import *
from .gamblers_chest import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)

