"""

    The A&I module does not define a method for initializing an individual A&I
    asset because, so far, there is no reason to do so.

"""

# asset module imports
from .._asset import Asset
from .._collection import Collection
from .definitions import *

from app.assets.weapon_masteries.definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        """ The init method for the A&I asset collection calls the
        set_default_max_values() methods from the base class. """

        Collection.__init__(self,  *args, **kwargs)
        self.set_default_max_values()
