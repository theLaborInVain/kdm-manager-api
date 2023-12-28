"""

    The class object for working with the expansion assets is here, as well as
    the object init code for working with an individual expansion as an object.

"""

from .. import gear as Gear

from .._asset import Asset
from .._collection import Collection

from .definitions import *

from .echoes_of_death import echoes_of_death
from .expansions_of_death_1 import expansions_of_death_1
from .gamblers_chest import gamblers_chest
from .white_box import (
    white_box_2012,
    white_box_2016,
    white_box_2017,
    white_box_2018,
    white_box_2019,
    white_box_2020,
    white_box_2021,
    white_box_2022,
    white_box_2023
)

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        """ Expansion assets are organized in assets/expansions.py according to
        release date, so when we initialize an asset dict from expansions.py, we
        manually add a "meta" style key to indicate their release date. """

        Collection.__init__(self,  *args, **kwargs)
        self.set_expansion_vars()


    def set_expansion_vars(self):
        """ Touch up each asset with some convenience data. """

        gear_object = Gear.Assets()
        gear_list = gear_object.get_dicts()

        expansions_list = self.get_dicts()
        for e_dict in expansions_list:
            handle = e_dict['handle']

            self.assets[handle]['pattern_gear'] = []
            self.assets[handle]['beta_gear'] = []

            for gear in gear_list:
                if (
                    gear.get('expansion', None) == handle and
                    gear.get('sub_type', None) in ['pattern', 'seed_pattern']
                ):
                    self.assets[handle]['pattern_gear'].append(gear['handle'])

                if (
                    gear.get('expansion', None) == handle and
                    gear.get('beta', False)
                ):
                    self.assets[handle]['beta_gear'].append(gear['handle'])


class Expansion(Asset):
    """ This is the base class for all expansions. Private methods exist for
    enabling and disabling expansions (within a campaign/settlement). """

    def __init__(self, *args, **kwargs):
        Asset.__init__(self,  *args, **kwargs)

        self.assets = Assets()
        self.baseline()
        self.initialize()


    def baseline(self):
        """ Default some attributes for self. Everything here is subject
        to overwrite by the self.initialize() call. """

        self.survivor_special_attributes = []
