"""

    The class method for creating the Disorders asset collection lives here.

"""

from app import models
from app.assets import disorders

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = disorders
        models.AssetCollection.__init__(self,  *args, **kwargs)

