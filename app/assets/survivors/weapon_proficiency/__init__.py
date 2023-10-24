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
