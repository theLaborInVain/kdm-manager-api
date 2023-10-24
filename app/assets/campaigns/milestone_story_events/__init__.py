"""

    Milestone story events are basically a settlement sheet pseudo asset.

"""

from app.assets._collection import Collection

from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)
