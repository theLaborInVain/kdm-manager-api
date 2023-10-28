"""

    Weapon proficiency as a survivor sheet asset that basically links back to
    an A&I handle representing either a weapon specialization or a mastery.

    A weapon proficiency is added to a survivor record as the
    'weapon_proficiency_type' attribute. Using the handle stored as that attrib
    gets you back to these definitions.

"""

from app.assets._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        Collection.__init__(self,  *args, **kwargs)

        self._validate_assets()


    def _validate_assets(self):
        ''' Cheaper than a data model. Kinda kludgey. Iterates assets in the
        collection, throws an error if they're missing something. '''

        for a_dict in self.get_dicts():
            for required in ['specialist_ai', 'master_ai']:
                if a_dict.get(required, None) is None:
                    err = 'Weapon proficiency asset %s/%s does not have %s!'
                    raise AttributeError(
                        err % (a_dict['handle'], a_dict['name'], required)
                    )
