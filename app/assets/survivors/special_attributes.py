
'''

    This is a pseudo asset used on Survivor records to basicall set random
    flags that aren't part of the Survivor data model.

    Important! there is a class definition at the bottom of this file!!!

'''

from .._asset import Asset
from .._collection import Collection

special_attributes = {
    'potsun_purified': {
        'name': 'Purified',
        'epithet': 'purified',
        'title_tip': 'This survivor is Purified.',
    },
    'potsun_sun_eater': {
        'name': 'Sun Eater',
        'epithet': 'sun_eater',
        'title_tip': 'This survivor is a Sun Eater.',
    },
    'potsun_child_of_the_sun': {
        'name': "Child of the Sun",
        'epithet': 'child_of_the_sun',
        'title_tip': 'This survivor is a Child of the Sun.',
    },
    'potstars_scar':{
        'name': 'Scar',
        'title_tip': 'This survivor has a scar.',
    },
    'potstars_noble_surname':{
        'name': 'Noble surname',
        'title_tip': 'This survivor has a Noble surname.',
    },
    'potstars_reincarnated_surname': {
        'name': 'Reincarnated surname',
        'title_tip': 'This survivor has a Reincarnated surname.',
    },
}

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        Collection.__init__(self,  *args, **kwargs)
