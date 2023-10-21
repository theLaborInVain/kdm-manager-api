"""

    A pseudo model whose assets are limited to the 'weapon_specializations' dict
    in the /app/assets/abilities_and_impairments.py module.

"""

from .._collection import Collection

from ..abilities_and_impairments import weapon_specializations

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.type_override = "weapon_specialization"
        self.assets = weapon_specializations
        Collection.__init__(self,  *args, **kwargs)
