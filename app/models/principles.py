"""
    Principles are a tricky asset, since they're essentially optional rules
    to which conditional rules apply.

"""

from app.assets import principles
from app import models


class Assets(models.AssetCollection):


    def __init__(self, *args, **kwargs):
        self.root_module = principles
        models.AssetCollection.__init__(self,  *args, **kwargs)


    def get_mutually_exclusive_principles(self):
        """ Returns a dictionary object listing game asset names for the
        mutually exclusive principle pairs.

        Looks like this:

            {'New Life': (
                ['Protect the Young', 'protect_the_young'],
                ['Survival of the Fittest', 'survival_of_the_fittest']
            ),
            'Society': (
                ['Accept Darkness', 'accept_darkness'],
                ['Collective Toil', 'collective_toil']
            ),

        """

        output = {}
        for p_dict in self.get_dicts():
            alternatives = []
            for option in p_dict["option_handles"]:
                alternatives_list = [self.get_asset(option)["name"], option]
                alternatives.append(alternatives_list)
            output[p_dict["name"]] = tuple(alternatives)

        return output
