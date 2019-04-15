"""

    Survivor Special Attributes are a pseudo asset: they're essentially
    pointers to multiple assets or flags that indicate that certain rules
    apply to a survivor.

"""


from app.assets.survivors import special_attributes
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
#        self.assets = survivor_sheet_options.survivor_special_attributes
#        self.type_override = "special_attribute"
        self.root_module = special_attributes
        models.AssetCollection.__init__(self,  *args, **kwargs)
