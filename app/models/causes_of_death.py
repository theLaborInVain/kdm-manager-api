from app.assets.survivors import cause_of_death
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
#        self.type_override = "cause_of_death"
#        self.assets = survivor_sheet_options.causes_of_death
        self.root_module = cause_of_death
        models.AssetCollection.__init__(self,  *args, **kwargs)
