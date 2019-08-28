"""

    This Assets object has a unique method called add_strain_fighting_arts()
    that loops through ALL known fighting arts and adds them to the asset
    if appropriate.

    This replaces some hard-coding that we used to have in the
    assets/strain_milestones.py file, which was dirty af.

"""

from app.assets import strain_milestones, fighting_arts
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.root_module = strain_milestones

        self.warn_on_missing_mandatory_attribute = True
        self.mandatory_attributes = {'milestone_condition': "UNDEFINED!",}

        models.AssetCollection.__init__(self,  *args, **kwargs)
        self.add_strain_fighting_arts()


    def add_strain_fighting_arts(self):
        """ Looks through ALL fighting arts for ones whose 'strain_milestone'
        value matches the handle of the asset. Adds them. """

        FightingArts = models.fighting_arts.Assets()

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
