"""
    Principles are a tricky asset, since they're essentially optional rules
    to which conditional rules apply.

    To be clear: the asset we're talking abou there is NOT an innovation.
    Rather, assets in this package are the opportinity to set a principle.

    So, rather than 'Survival of the Fittest', for example, a principle is
    'New Life', i.e. the milestory story event that allows a principle to be
    selected, etc.

"""

from app.assets import innovations

from .._asset import Asset
from .._collection import Collection
from .definitions import *


INNOVATIONS = innovations.Assets()


class Assets(Collection):
    ''' Principles AssetCollections have a special method to get mutually
    exclusive principles. '''

    def __init__(self, *args, **kwargs):
        ''' Vanilla init. '''
        self.is_game_asset = False
        Collection.__init__(self, *args, **kwargs)


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

        This is ONLY USED BY world.py. DO NOT use this elsewhere.
        """


        output = {}
        for p_dict in self.get_dicts():
            alternatives = []
            for option in p_dict["option_handles"]: # 'romantic,'graves', etc.
                alternatives_list = [
                    INNOVATIONS.get_asset(option)["name"],
                    option
                ]
                alternatives.append(alternatives_list)

            if p_dict['name'] in output.keys():
                final_alternatives = alternatives
                for alt_list in output[p_dict['name']]:
                    if alt_list not in final_alternatives:
                        final_alternatives.append(alt_list)
                output[p_dict['name']] = tuple(final_alternatives)
            else:
                output[p_dict["name"]] = tuple(alternatives)

        return output


    def request_response(self):
        ''' Overrides the default method. Returns a 299. '''
        return utils.HTTP_299
