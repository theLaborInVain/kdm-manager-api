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



from copy import copy

from app.assets import abilities_and_impairments, innovations
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = innovations
        models.AssetCollection.__init__(self,  *args, **kwargs)

        # manual addition of weapon masteries
        for m in abilities_and_impairments.weapon_mastery.keys():
            wm = abilities_and_impairments.weapon_mastery[m]
            wm["handle"] = m
            wm["type"] = "weapon_mastery"
            self.assets[m] = wm



class Innovation(models.GameAsset):
    """ This is the base class for all innovations."""

    def __init__(self, *args, **kwargs):
        models.GameAsset.__init__(self,  *args, **kwargs)
        self.assets = Assets()
        self.initialize()


