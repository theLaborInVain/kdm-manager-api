"""
    A pseudo model that imports the 'weapon_mastery' dict from the A&I
    asset dictionary (/app/assets/abilities_and_impairments.py).

"""

from app.assets import abilities_and_impairments
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.assets = abilities_and_impairments.weapon_mastery
        self.type_override = "weapon_mastery"
        models.AssetCollection.__init__(self,  *args, **kwargs)
