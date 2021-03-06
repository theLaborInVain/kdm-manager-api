"""

    Game versions are tracked here.

"""

from datetime import datetime

VERSIONS = {
    'core_1_3': {
        'major': 1,
        'minor': 3,
        'patch': 1,
        'released': datetime(2015,9,1),
        'desc': 'Original Kickstarter release',
        'name': 'Original Kickstarter release',
    },
    'core_1_4': {
        'major': 1,
        'minor': 4,
        'released': datetime(2016,4,18),
        'desc': "1.4 ruleset announced via Kickstarter.",
        'name': "1.4 ruleset announced via Kickstarter.",
        'url': (
            'https://www.kickstarter.com/'
            'projects/poots/kingdom-death-monster/posts/1727733'
        ),
    },
    'core_1_5': {
        'major': 1,
        'minor': 5,
        'released': datetime(2017,10,1),
        'desc': "Kickstarter 1.5 release.",
        'name': "Kickstarter 1.5 release.",
    },
    'core_1_6': {
        'major': 1,
        'minor': 6,
        'released': datetime(2020,11,27),
        'desc': 'Version 1.6, announced Black Friday 2020.',
        'name': 'Version 1.6, announced Black Friday 2020.'
    },
}
