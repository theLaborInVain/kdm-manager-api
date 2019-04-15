from app.assets import survival_actions
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module=survival_actions
        models.AssetCollection.__init__(self,  *args, **kwargs)

