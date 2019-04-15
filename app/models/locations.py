from app.assets import locations
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = locations
        models.AssetCollection.__init__(self,  *args, **kwargs)
