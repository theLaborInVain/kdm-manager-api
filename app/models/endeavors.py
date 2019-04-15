"""
    The Endeavors asset collection has a number of irregular assets. Be careful
    writing any custom code here.

"""


from app.assets import endeavors
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = endeavors
        models.AssetCollection.__init__(self,  *args, **kwargs)

