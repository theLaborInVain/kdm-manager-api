"""

    Class definitions for gear: the asset collection and the individual gear
    object class methods are here.

"""


from app.assets import gear
from app import models, utils

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        """ In release 1.0.0, the init method for the gear asset collection uses
        the 'mandatory_attributes' attr instead of custom code. """

        self.root_module = gear

        self.mandatory_attributes = {
            'keywords': list(),
            'rules': list(),
            'desc': str(),
        }

        models.AssetCollection.__init__(self,  *args, **kwargs)


    def get_all_rules(self):
        """ Returns a set of all keywords for all assets. """

        rules = set()
        for a_dict in self.get_dicts():
            rules = keywords.union(a_dict['rules'])
        return sorted(keywords)


class Gear(models.GameAsset):

    def __repr__(self):
        return "%s object '%s' (assets.%s['%s'])" % (
            self.type.title(),
            self.name,
            self.type,
            self.handle
        )

    def __init__(self, *args, **kwargs):
        models.GameAsset.__init__(self,  *args, **kwargs)
        self.assets = Assets()
        self.initialize()


