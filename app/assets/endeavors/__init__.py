"""
    The Endeavors asset collection has a number of irregular assets. Be careful
    writing any custom code here.

"""

from .._collection import Collection

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)

