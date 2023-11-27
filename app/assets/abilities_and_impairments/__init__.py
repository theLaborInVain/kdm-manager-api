"""

    The A&I module does not define a method for initializing an individual A&I
    asset because, so far, there is no reason to do so.

"""

# asset module imports
from app.assets.innovations.weapon_masteries import *

from .._asset import Asset
from .._collection import Collection
from .definitions import *


class Assets(Collection):
    ''' Collection class method for Abilities and Impairments. '''

    def __init__(self, *args, **kwargs):
        """ The init method for the A&I asset collection calls the
        set_default_max_values() methods from the base class. """

        Collection.__init__(self,  *args, **kwargs)
        self.set_sub_type()
        self.set_default_max_values()


    def set_sub_type(self):
        '''Also ets a var called 'ai_type' which is a human-friendly
        representaiton of whether it's an ability, injury, etc. '''

        crosswalk = {
            'ability': 'ability',
            'curse': 'curse',
            'impairment': 'impairment',
            'severe_injury': 'severe injury',
        }

        for ai_dict in self.get_dicts():
            handle = ai_dict['handle']

            # default to ability if it's not defined or unknown
            if ai_dict.get('sub_type', None) not in crosswalk.keys():
                ai_dict['sub_type'] = 'ability'

            # set ai_type attr
            ai_dict['ai_type'] = crosswalk[ai_dict['sub_type']]

            # copy back to self.assets
            self.assets[handle] = ai_dict
