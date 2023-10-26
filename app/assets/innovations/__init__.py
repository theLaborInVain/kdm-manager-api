"""

    Innovations are an extremely complex asset, since they tie into so many of
    the game's other systems and since they include principles and weapon
    proficiencies, each of which behave irregularly and have their own special
    rules and business logic.

    This module contains the asset collection object code as well as methods
    for getting information about principles, proficiencies, etc.

    Check the principles.py file in app/assets and app/models for more on
    principles.

    Weapon masteries also have their own asset assets/models module.

"""

from .._asset import Asset
from .._collection import Collection

from .definitions import *
from .weapon_masteries import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)

        # manual addition of weapon masteries
#        for m in abilities_and_impairments.weapon_mastery.keys():
#            wm = abilities_and_impairments.weapon_mastery[m]
#            wm["handle"] = m
#            wm["type"] = "weapon_mastery"
#            self.assets[m] = wm


class Innovation(Asset):
    """ This is the base class for all innovations."""

    def __init__(self, *args, **kwargs):
        Asset.__init__(self,  *args, **kwargs)
        self.assets = Assets()
        self.initialize()
