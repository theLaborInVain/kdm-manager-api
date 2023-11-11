"""

    Class definitions for gear: the asset collection and the individual gear
    object class methods are here.

"""

from .._asset import Asset
from .._collection import Collection

# multiple gear definition imports
from .definitions import *
from .expansions_of_death_1 import *
from .gamblers_chest import *


class Assets(Collection):

    def __init__(self, *args, **kwargs):
        """ In release 1.0.0, the init method for the gear asset collection uses
        the 'mandatory_attributes' attr instead of custom code. """

        self.mandatory_attributes = {'keywords': [], 'rules': [], 'desc': "",}
        Collection.__init__(self,  *args, **kwargs)
        self.set_gear_vars()


    def set_gear_vars(self):
        """ Updates assets with assorted values. """

        gear_list = self.get_dicts()
        for g_dict in gear_list:
            handle = g_dict['handle']

            if g_dict.get('affinity_bonus', None) is not None:
                self.assets[handle]['affinity_bonus']['total_required'] = 0
                for affinity_type in ['puzzle', 'complete']:
                    req = g_dict['affinity_bonus']['requires'].get(
                        affinity_type, {}
                    )
                    for value in req.values():
                        self.assets[handle]['affinity_bonus']['total_required'] += value


    def get_all_rules(self):
        """ Returns a set of all keywords for all assets. """

        rules = set()
        for a_dict in self.get_dicts():
            rules = keywords.union(a_dict['rules'])
        return sorted(keywords)


class Gear(Asset):
    ''' A vanilla asset.'''

    def __init__(self, *args, **kwargs):
        ''' Nothing special here. '''
        Asset.__init__(self,  *args, **kwargs)
