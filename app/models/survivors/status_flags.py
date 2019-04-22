"""

    Status flags are used in the campaign summary to show that a survivor can or
    cannot do something. This module lets you access them programmatically.

"""


from app.assets.survivors import status_flags
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = status_flags
        models.AssetCollection.__init__(self,  *args, **kwargs)
