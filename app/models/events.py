from app.assets import events
from app import models

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = events
        models.AssetCollection.__init__(self,  *args, **kwargs)
