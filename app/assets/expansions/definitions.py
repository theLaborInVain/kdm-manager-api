"""

    All known expansions are defined here.

"""

from datetime import datetime
from app import API
TIMEZONE = API.config['TIMEZONE']

from .echoes_of_death import echoes_of_death
from .expansions_of_death_1 import expansions_of_death_1
from .gamblers_chest import gamblers_chest
from .white_box_2023 import white_box_2023

white_box = {

    # 2016 white box

    "fade": {
        "name": "Fade",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2016, 8, 4, 12, tzinfo=TIMEZONE),
        'basic_hunt_event': ['baby_and_the_sword'],
        'subscriber_level': 2,
    },

    'allison_the_twilight_knight': {
        'name': 'Allison the Twilight Knight',
        "released": datetime(2016, 8, 16, 12, tzinfo=TIMEZONE),
        'subtitle': (
            'As released in the White Box Hard Plastic Collection.'
        ),
        'ui': {'pretty_category': 'White Box'},
        'url': (
            'https://www.kickstarter.com/projects/poots/kingdom-death-monster/'
            'posts/381921/'
        ),
        'subscriber_level': 2,
    },

    'pinup_wet_nurse': {
        'name': 'Pinup Wet Nurse',
        'released': datetime(2016, 10, 31, 12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

    'black_friday_ninja': {
        'name': 'Black Friday Ninja',
        'released': datetime(2016, 11, 24, 12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

    "tenth_anniversary_white_speaker": {
        "name": "10th Anniversary White Speaker",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 10, 9, 12, tzinfo=TIMEZONE),
        'strain_milestones': ['plot_twist'],
        'subscriber_level': 2,
    },

    "tenth_anniversary_survivors": {
        "name": "10th Anniversary Survivors",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 10, 9, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },

    # 2019 White Box
    "oktoberfest_aya": {
        "name": "Oktoberfest Aya",
        'subtitle': (
            'Includes crafting recipes that require <b>Lonely Tree</b>.'
        ),
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 10, 31, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
        'help': [
            {
                'type': 'gear',
                'tip': (
                    'The recipe for <b>Afterdeath Brew</b> requires the '
                    '<b>Blistering Plasma Fruit</b> Strange Resource from the '
                    '<i>Lonely Tree</i> expansion. Enabling <i>Oktoberfest '
                    'Aya</i> for a settlement that does not also have '
                    '<i>Lonely Tree</i> enabled will prevent the Manager from '
                    'displaying the recipe correctly!'
                ),
            }
        ],
    },

    "halloween_white_speaker_2019": {
        "name": "Halloween White Speaker",
        'subtitle': (
            'Includes crafting recipes that require <b>Slenderman</b>.'
        ),
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 10, 31, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },

    'holiday_white_speaker_nico': {
        'released': datetime(2012, 7, 1, 12, tzinfo=TIMEZONE),
        'name': 'Holiday White Speaker Nico',
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

    "percival": {
        "name": "Percival",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2016, 8, 4, 12, tzinfo=TIMEZONE),
        'basic_hunt_event': ['dead_warrior'],
        'subscriber_level': 2,
    },

    'santa_satan': {
        'released': datetime(2018, 12, 25, 12, tzinfo=TIMEZONE),
        'name': 'Santa Satan',
        'ui': {'pretty_category': 'White Box'},
        'strain_milestones': ['atmospheric_change'],
        'subscriber_level': 2,
        'subtitle': (
            'This promo release from Holiday 2018 contains the &#128917; '
            '<i>Atmostpheric Change</i> Strain Milestone.'
        ),
        'help': [
            {
                'type': 'event',
                'tip': (
                    'The &#128917; <i>Atmospheric Change</i> Strain Milestone '
                    'condition requires one of two story events from separate '
                    'expansion content: '
                    'the <font class=kdm_font>g</font> <b>Story in the '
                    'Snow</b> story event belongs to the <i>White Speaker '
                    'Nico</i> expansion and the <font class=kdm_font>g</font> '
                    '<b>Necrotoxic Mistletoe</b> story event is from the '
                    '<i>Flower Knight</i> expansion.'
                ),
            },
        ],
    },

    # 2019 whiteboxes
    'valentines_day_pinup_twilight_knight': {
        'name': "Valentine's Day Pinup Twilight Knight",
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2019, 2, 14, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },
    'swashbuckler': {
        'name': 'Swashbuckler',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2016, 3, 1, 12, tzinfo=TIMEZONE),
        'subtitle': (
            'One of the few figures from the <i>Generic</i> line that also '
            'includes game content.'
        ),
        'subscriber_level': 2,
    },
    'easter_pinup_twilight_knight': {
        'name': "Easter Pinup Twilight Knight",
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2019, 4, 22, 12, tzinfo=TIMEZONE),
        'subtitle': 'Adds <b>Gibbering Haremite</b> vermin only.',
        'subscriber_level': 2,
    },
    "sword_hunter": {
        "name": "Sword Hunter",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 8, 1, 12, tzinfo=TIMEZONE),
        'basic_hunt_event': ['sword_in_the_stone'],
        'subscriber_level': 2,
    },
    'vignettes_of_death_white_gigalion': {
        'released': datetime(2019, 8, 1, 12, tzinfo=TIMEZONE),
        'name': 'Vignettes of Death: White Gigalion',
        'ui': {'pretty_category': 'Quarry'},
        'flair': {
            'color': 'fff',
            'bgcolor': '000'
        },
        'strain_milestones': ['somatotropin_surge'],
        'quarries': ['white_gigalion'],
    },

    # 2020 whiteboxes
    "halloween_ringtail_vixen_2020": {
        'name': 'Halloween Ringtail Vixen',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2020, 10, 31, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },

    'pinups_of_death_2': {
        'name': 'Pinups of Death II',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2020, 11, 1, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },

    'winter_solstice_lucy': {
        'name': 'Winter Solstice Lucy',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2020, 12, 22, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },

    'halloween_survivors_series_2': {
        'name': 'Halloween Survivors - Series II',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2021, 11, 25, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },

    'grimmory': {
        'released': datetime(2022,3,1, 12, tzinfo=TIMEZONE),
        'name': 'Grimmory',
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
    'pascha': {
        'name': 'Pascha',
        'released': datetime(2022,4,22,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
    'willow': {
        'name': 'Willow',
        'released': datetime(2022,4,22,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
    'badar': {
        'name': 'Badar',
        'released': datetime(2022,5,31,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'sealed_gear': True,
        'subscriber_level': 2,
    },
    'doll': {
        'name': 'Doll',
        'released': datetime(2022,8,9,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
    'summer_cyrus': {
        'name': 'Summer Cyrus',
        'released': datetime(2022,8,9,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
    'summer_aya': {
        'name': 'Summer Aya',
        'released': datetime(2022,9,30,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
    'summer_goth_twilight_knight': {
    'name': 'Summer Goth - Twilight Knight',
        'released': datetime(2022,9,30,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

    # halloween 2022
    'reapokratis': {
        'name': 'Reapokratis',
        'released': datetime(2022,10,31,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
    'erza_of_dedheim': {
        'name': 'Erza of Dedheim',
        'released': datetime(2022,10,31,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
    'halloween_survivor_flower_knight_costume': {
        'name': 'Halloween Survivor - Flower Knight Costume',
        'released': datetime(2022,10,31,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subtitle': (
            'Includes crafting recipes that require <b>Flower Knight</b>.'
        ),
        'subscriber_level': 2,
    },


    # elgnirk the chaos elf - 2022-12-25
    'elgnirk_the_chaos_elf': {
        'name': 'Elgnirk, The Chaos Elf',
        'released': datetime(2022,12,25,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        "flair": {
            "color": "FFF",
            "bgcolor": "00833B",
        },
        'subscriber_level': 2,
    },

    # novice - 2022-12-25
    'novice': {
        'name': 'Novice',
        'released': datetime(2022,12,25,12, tzinfo=TIMEZONE),
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
            'Before the Wall, ' #2016-08-16 - white box hard plastic
            'Beyond the Wall, ' #2016-08-16 - white box hard plastic
#            "Black Friday Ninja, "  #2016-11-24
            "Detective Twilight Knight, " #2017-08-31
            'Halloween Pinup Twilight Knight, '
            "Pinup Easter Aya, " #2019-04-22
            "Pinup Devil Satan (Halloween 2018), "
            'Pinup Order Knight, '
            'Pinup Sci-fi Twilight Knight, '
            "Pinup Sci-fi White Speaker, "
            'Pinup Warrior of the Sun, '
            "Pinups of Death, " #2016-03-25
            'White Speaker.'
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



#
#   Only bogus/pseudo content below here
#

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
