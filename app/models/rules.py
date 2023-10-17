from app.assets import rules
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = rules
        models.AssetCollection.__init__(self,  *args, **kwargs)

