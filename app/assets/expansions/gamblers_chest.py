'''

    The Gambler's Chest, i.e. Item 100, announced during the second Kickstarter
    (i.e. Kickstarter 1.5 in 2016), and delivered seven years later in 2023.

'''

from datetime import datetime
from app import API
TIMEZONE = API.config['TIMEZONE']

gamblers_chest = {

#    'arc_survivors': {
#        'pillars': 3,
#        'name': 'Arc Survivors',
#        'released': datetime(2023, 7, 31, 12, tzinfo=TIMEZONE),
#        'ui': {'pretty_category': "Advanced KDM"},
#        'flair': {'bgcolor': '41A165'},
#        'always_available': {
#            'location': ['forum'],
#        },
#    },

    'crimson_crocodile': {
        'name': 'Crimson Crocodile',
        'release': datetime(2023, 7, 31, 12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': "Quarry"},
        'quarries': ['crimson_crocodile'],
    },

}

