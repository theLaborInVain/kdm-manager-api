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
        'released': datetime(2023, 7, 31, 12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': "Quarry"},
        'quarries': ['crimson_crocodile'],
        'timeline_add': [
            {'ly': 0, 'handle': 'gc_devour_the_white_lion'},
            {'ly': 1, 'handle': 'first_crimson_day'},
        ],
        'timeline_rm': [
            {'ly': 1, 'handle': 'core_first_day'},
        ],
        "flair": {
            "border_color": "DAD4D8",
            "bgcolor": "B78086",
            'color': 'fff',
        },
        'help': [
            {
                'type': 'game_assets',
                'tip': (
                    'References to the <b>Groomed Nail</b> and the '
                    '<b>Groomed Nails</b> resource are believed to be '
                    'synonymous.'
                ),
            },
        ],
    },

    'smog_singers': {
        'name': 'Smog Singers',
        'released': datetime(2023, 7, 31, 12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': "Quarry"},
        'quarries': ['smog_singers'],
        'timeline_add': [
            {'ly': 2, 'handle': 'gc_death_of_song'},
        ],
        'maximum_intro_ly': 2,
        'late_intro_event': 'gc_death_of_song',
        "flair": {
            "border_color": "7F7A6A",
            "bgcolor": "A6A292",
            'color': 'FFF',
        },
    },
}
