
from app.assets import strain_milestones
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = strain_milestones
        models.AssetCollection.__init__(self,  *args, **kwargs)

