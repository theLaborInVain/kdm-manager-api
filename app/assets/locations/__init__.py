"""

    LOCATIONS!

"""

from .._asset import Asset
from .._collection import Collection
from .definitions import *


class Assets(Collection):
    """ Collection object model for Locations. """

    def __init__(self, *args, **kwargs):
        """ Locations use the base class method to enforce their data model. """

        self.data_model = {
            'selectable': bool,
        }

        Collection.__init__(self,  *args, **kwargs)

