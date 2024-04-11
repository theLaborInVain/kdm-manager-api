"""

    Character assets are introduced in the May 2023 "Lolowen" White Box
    expansion; additional rules are applied in the July 2023 "Gambler's Chest"
    expansion.

"""

from .._collection import Collection

# definition imports
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)

