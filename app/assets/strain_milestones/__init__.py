"""

    This Assets object has a unique method called add_strain_fighting_arts()
    that loops through ALL known fighting arts and adds them to the asset
    if appropriate.

    This replaces some hard-coding that we used to have in the
    assets/strain_milestones.py file, which was dirty af.

"""

from .._asset import Asset
from .._collection import Collection
from .definitions import *

from .. import fighting_arts

class Assets(Collection):

    def __init__(self, *args, **kwargs):

        self.warn_on_missing_mandatory_attribute = True
        self.mandatory_attributes = {'milestone_condition': "UNDEFINED!",}

        Collection.__init__(self,  *args, **kwargs)
        self.add_strain_fighting_arts()


    def add_strain_fighting_arts(self):
        """ Looks through ALL fighting arts for ones whose 'strain_milestone'
        value matches the handle of the asset. Adds them. """

        FightingArts = fighting_arts.Assets()

        for strain_asset_dict in self.get_dicts():

            strain_asset_handle = strain_asset_dict['handle']

            sfa_list = set()

            for fa_dict in FightingArts.get_dicts():
                fa_milestone = fa_dict.get('strain_milestone', False)
                if fa_milestone == strain_asset_handle:
                    sfa_list.add(fa_dict['handle'])

            self.assets[strain_asset_handle]['fighting_arts'] = list(
                sorted(sfa_list)
            )
