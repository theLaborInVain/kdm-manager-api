'''

    This is an unusual asset, since it is a basically just a list of strings.

    There is no way to initialize an individual object for these, since that
    has been unnecessary up to this point.

'''

from app.assets._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)
