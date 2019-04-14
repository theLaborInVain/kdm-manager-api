"""
    Farting Arts collection object is managed here.

"""

from app.assets import fighting_arts
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = fighting_arts
        models.AssetCollection.__init__(self,  *args, **kwargs)
