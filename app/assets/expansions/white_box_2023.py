'''

    2023 White Boxes here

'''

from datetime import datetime
from app import API
TIMEZONE = API.config['TIMEZONE']

white_box_2023 = {

    # hellebore - 2023-01-31
    'hellebore': {
        'name': 'Hellebore - A Frozen Survivor',
        'released': datetime(2023,1,31,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

    # death crown inheritor aya - 2023-02-28
    'death_crown_inheritor_aya': {
        'name': 'Death Crown Inheritor Aya',
        'released': datetime(2023,2,28,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'flair': {
            'bgcolor': 'C55745',
            'color': 'FFF'
        },
        'subscriber_level': 2,
    },

    # lunar twilight knight - 2023-02-28
    'lunar_twilight_knight': {
        'name': 'Lunar Twilight Knight',
        'released': datetime(2023,2,28,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

    # vitanvox - 2023-03-31

    # skrelle - 2023-03-31

    # gnostin stonesmasher - 2023-05-02

    # lolowen - 2023-05-02

    # mist raikin armor - 2023-06-12

}
