"""

    A pseudo model whose assets are limited to the 'weapon_specializations' dict
    in the /app/assets/abilities_and_impairments.py module.

"""


from app.assets import abilities_and_impairments
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.type_override = "weapon_specialization"
        self.assets = abilities_and_impairments.weapon_specializations
        models.AssetCollection.__init__(self,  *args, **kwargs)
