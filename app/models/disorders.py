"""

    The class method for creating the Disorders asset collection lives here.

"""

from app import models

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        models.AssetCollection.__init__(self,  *args, **kwargs)

