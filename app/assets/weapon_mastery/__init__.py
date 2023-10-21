"""
    A pseudo model that imports the 'weapon_mastery' dict from the A&I
    asset dictionary (/app/assets/abilities_and_impairments.py).

    This is highly irregular--hopefully we don't have too many like this.

"""

from .._collection import Collection

from ..abilities_and_impairments import weapon_mastery

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.assets = weapon_mastery
        Collection.__init__(self,  *args, **kwargs)
