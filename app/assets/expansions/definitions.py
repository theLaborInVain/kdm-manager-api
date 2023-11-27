"""

    All known expansions are defined here.

"""

from datetime import datetime
from app import API
TIMEZONE = API.config['TIMEZONE']

white_box = {

    'holiday_white_speaker_nico': {
        'released': datetime(2012, 7, 1, 12, tzinfo=TIMEZONE),
        'name': 'Holiday White Speaker Nico',
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

}


miscellaneous = {

    # anything that's not part of a product line or group of related things
    # gets filed here

    "beta_challenge_scenarios": {
        "released": datetime(2016, 2, 1, 12, tzinfo=TIMEZONE),
        "name": "Beta Challenge Scenarios",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "FFF",
            "bgcolor": "4EC6F0",
        },
        "enforce_survival_limit": False,
        "subtitle": (
            "Enables abilities & impairments, disorders, items etc. included "
            "in the (cancelled) Beta Challenge Scenarios."
            ),
        "special_rules": [
            {
            "name": "Survival Limit Warning!",
            "desc": (
                "Survival Limit is not automatically enforced by the Manager "
                "when Beta Challenge Scenarios content is enabled."
            ),
            "bg_color": "F87217",
            "font_color": "FFF",
            },
        ],
        'help': [
            {
                'type': 'rules',
                'tip': (
                    "The Survival Limit is not enforced on any survivor's "
                    "sheet when this expansion content is enabled for a "
                    "settlement!"
                ),
            },
        ],
    },

    "promo": {
        "released": datetime(2015, 9, 2, 12, tzinfo=TIMEZONE),
        "name": "Promo",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "FFF",
            "bgcolor": "4EC6F0",
        },
        "subtitle": (
            'Adds promotional events, gear, Abilities & Impairments, etc. '
            'to Settlement and Survivor Sheet drop-down lists. '
            'Collects the following releases: '
            'Before the Wall, ' # 2016-08-16 - white box hard plastic
            'Beyond the Wall, ' # 2016-08-16 - white box hard plastic
            'Halloween Pinup Twilight Knight, '
            "Pinup Easter Aya, " # 2019-04-22
            'Pinup Order Knight, '
            'Pinup Sci-fi Twilight Knight, '
            "Pinup Sci-fi White Speaker, "
            'Pinup Warrior of the Sun, '
            "Pinups of Death, " # 2016-03-25
            'White Speaker.'    # 2018
        ),
        'help': [
            {
                'type': 'poots',
                'tip': (
                    'According to <a href="http://us1.campaign-archive2.com'
                    '/?u=1f4d6d8b08474b282855b8143&id=b967080e9f&e=c4a658a777" '
                    'target="top">KDU #18</a>, "Promo cards are intended as '
                    'light-hearted content that is created for fun and should '
                    'not be taken seriously in the context of Monster. Promos '
                    'are not considered official additions to the rules and '
                    'players should add them at the discretion of each player '
                    'group."'
                ),
            },
            {
                'type': 'gear',
                'tip': (
                    'Most Promo gear cards are <b>Rare Gear</b>, but '
                    'a few of them have recipes! If you are looking for a '
                    'specific gear card and cannot find it, make sure to check '
                    'both locations!'
                ),
            },
        ],
    },


    # potsun enhancements
    'sunlion_armor_beta': {
        'released': datetime(2021, 11, 25, 12, tzinfo=TIMEZONE),
        'name': 'Sunlion Armor (Beta)',
        'ui': {'pretty_category': 'Enhancement'},
        'subscriber_level': 2,
    },
    'white_sunlion_armor': {
        'name': 'White Sunlion Armor',
        'released': datetime(2022, 11, 25, 12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'Enhancement'},
        'subtitle': (
            'Augments <b>People of the Sun</b> campaign; includes '
            '<b>Bleeding Corpse Lily</b> terrain and Strange Resource.'
        ),
        'subscriber_level': 2,
    },


    # screaming sun / oni armor
    'screaming_sun_armor': {
        'name': 'Screaming Sun Armor',
        'released': datetime(2022, 11, 25, 12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'Enhancement'},
        'subscriber_level': 2,
    },

}


collection = {

    # 'pseudo' expansion content, used to include items from the Users' KD
    # collection lists in campaigns

    "kd_collection_fighting_arts_and_disorders": {
        "type": 'pseudo',
        "released": datetime(2018, 5, 1, tzinfo=TIMEZONE),
        "name": "Fighting Arts & Disorders",
        "ui": {"pretty_category": "KD Collection"},
        "flair": {
            "color": "FFF",
            "bgcolor": "000",
        },
        "subtitle": (
            "Check this box to include the Fighting Arts and Disorders from "
            "the expansions in your KD Collection in this campaign."
        ),
    },

    "kd_collection_settlement_events": {
        "type": 'pseudo',
        "released": datetime(2018, 5, 15, tzinfo=TIMEZONE),
        "name": "Settlement Events",
        "ui": {"pretty_category": "KD Collection"},
        "flair": {
            "color": "FFF",
            "bgcolor": "000",
        },
        "subtitle": (
            "Check this box to include the Settlement Events from the "
            "expansions in your KD Collection in this campaign."
        ),
    },

}
