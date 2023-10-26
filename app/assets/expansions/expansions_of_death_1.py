"""

    Expansions from the "Expansions of Death 1" collection, i.e. Item 22.

    These are the ones from the first Kickstarter.

"""

from datetime import datetime
from app import API
TIMEZONE = API.config['TIMEZONE']

expansions_of_death_1 = {

    "dragon_king": {
        "name": "Dragon King",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_ly': 8,
        'late_intro_event': 'dk_glowing_crater',
        "flair": {
            "color": "E8cE55",
            "bgcolor": "6260A9",
        },
        "quarries": ["dragon_king"],
        "always_available": {
            "location": ["Dragon Armory"],
        },
        "timeline_add": [
            {"ly": 8, "handle": "dk_glowing_crater"},
        ],
        'help': [
            {
                'type': 'game_assets',
                'tip': (
                    'The "Destiny Husk" referenced on p.5 of the rules is '
                    'understood to refer to the <b>Husk of Destiny</b> '
                    'Rare Gear.'
                )
            },
        ],
    },

    "dung_beetle_knight": {
        "name": "Dung Beetle Knight",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_year': 8,
        'late_intro_event': 'dbk_rumbling_in_the_dark',
        "flair": {
            "color": "EAE40A",
            "bgcolor": "928F7C",
            'border_color': "C1BCB8",
        },
        "quarries": ["dung_beetle_knight"],
        "always_available": {
            "location": ["Wet Resin Crafter"],
            "innocation": ["Subterranean Agriculture"],
        },
        "timeline_add": [
            {"ly": 8, "handle": "dbk_rumbling_in_the_dark"},
        ],
        "help": [
            {
                "type": "storage",
                "tip": (
                    '<i>Calcified</i> gear is selectable from the <b>Black '
                    'Harvest</b> section of the Settlement Storage controls.'
                ),
            },
            {
                "type": "storage",
                "tip": (
                    'The "Regenerating Blade" is <b>Rare Gear</b> and can be '
                    'found in that section of the Settlement Storage controls.'
                ),
            },
        ],
    },

    "flower_knight": {
        "name": "Flower Knight",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_year': 5,
        'late_intro_event': 'fk_crones_tale',
        "flair": {
            "color": "EAE40A",
            "bgcolor": "4E7D49",
        },
        "quarries": ["flower_knight"],
        "timeline_add": [
            {"ly": 5, "handle": "fk_crones_tale"}
        ],
        "help": [
            {
                "type": "storage",
                "tip": (
                    '<i>Vespertine</i> and other expansion-specific gear is '
                    'organized under the <b>Sense Memory</b> heading in the '
                    'Settlement Storage controls.'
                ),
            },
        ],
    },

    "gorm": {
        "name": "Gorm",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_ly': 1,
        'late_intro_event': 'gorm_approaching_storm',
        "flair": {
            "color": "F3E2AF",
            "bgcolor": "78413A",
            'border_color': "A6756A",
        },
        "quarries": ["gorm"],
        "always_available": {
            "location": ["Gormery", "Gormchymist"],
            "innovation": ["Nigredo"],
        },
        "timeline_add": [
            {"ly": 1, "handle": "gorm_approaching_storm"},
            {"ly": 2, 'handle': 'gorm_gorm_climate'},
        ],
        "help": [
            {
                "type": "events",
                "tip": (
                    'The Story event <b>The Approaching Storm</b> is added '
                    'automatically to new settlements, but if you have to '
                    'remove or move it, be careful to look for it near events '
                    'whose title starts with "T", rather than "A".'
                ),
            },
        ],
    },

    "green_knight_armor": {
        "name": "Green Knight Armor",
        "ui": {"pretty_category": "Enhancement"},
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "subtitle": (
            "Crafting GKA items requires DBK, Flower Knight, Lion Knight and "
            "Gorm expansions!"
        ),
        "always_available": {
            "location": ["Green Knight Armor"],
        },
        "flair": {
            "color": "000",
            "bgcolor": "94C9AB",
        },
        "help": [
            {
                'type': 'storage',
                'tip': (
                    'Crafting Green Knight Armor requires resources, gear and '
                    'innovations from the <b>Dung Beetle Knight</b>, <b>Flower '
                    'Knight</b>, <b>Lion Knight</b> and <b>Gorm</b> expansions.'
                ),
            },
            {
                'type': 'game_assets',
                'tip': (
                    'The recipe for <i>Fetorsaurus</i> includes a reference '
                    'to the non-existent "Elixir of Life" gear. This is '
                    'generally understood to mean the <b>Gorm</b> expansion\'s '
                    '"Life Elixir" gear.'
                ),
            },
        ],
    },

    "lion_god": {
        "name": "Lion God",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_ly': 13,
        'late_intro_event': 'lgod_the_silver_city',
        "flair": {
            "color": "E8cE55",
            "bgcolor": "712C2B",
        },
        "quarries": ["lion_god"],
        "always_available": {
            "innovation": ["The Knowledge Worm"],
        },
        "timeline_add": [
            {"ly": 13, "handle": "lgod_silver_city"},
        ],
    },

    "lion_knight": {
        "name": "Lion Knight",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Nemesis"},
        'maximum_intro_year': 6,
        'late_intro_event': 'lk_uninvited_guest',
        "flair": {
            "color": "666",
            "bgcolor": "FCF78F",
        },
        "quarries": ["lion_knight"],
        "always_available": {
            "innovation": ["Stoic Statue"],
        },
        "special_showdowns": ["lion_knight"],
        "timeline_add": [
            {"ly":  6, "handle": "lk_uninvited_guest"},
            {"ly":  8, "handle": "lk_places_everyone"},
            {
                "ly":  8,
                "sub_type": "special_showdown",
                "name": "Special Showdown - Lion Knight Lvl 1"
            },
            {"ly": 12, "handle": "lk_places_everyone"},
            {
                "ly": 12,
                "sub_type": "special_showdown",
                "name": "Special Showdown - Lion Knight Lvl 2"
            },
            {"ly": 16, "handle": "lk_places_everyone"},
            {
                "ly": 16,
                "sub_type": "special_showdown",
                "name": "Special Showdown - Lion Knight Lvl 3"
            },
        ],
    },

    "lonely_tree": {
        "name": "Lonely Tree",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Nemesis"},
        "nemesis_monsters": ["lonely_tree"],
        "special_showdowns": ["lonely_tree"],
        "flair": {
            "color": "EAE40A",
            "bgcolor": "958C83",
        },
        'help': [
            {
                'type': 'game_assets',
                'tip': (
                    'AI card references to "Lonely Fruit" are generally '
                    'understood to refer to the monster\'s "Nightmare Fruit" '
                    'AI card.'
                ),
            },
            {
                'type': 'game_assets',
                'tip': (
                    'References to "Festering Blood Fruit" are generally '
                    'understood to refer to "Blistering Plasma Fruit".'
                ),
            },
            {
                'type': 'game_assets',
                'tip': (
                    'The Basic Action card for the Lonely Tree refers to an '
                    'action called "germinate", which is generally understood '
                    'to refer to "Growth", i.e. the Lonely Tree\'s Instinct.'
                ),
            },
        ],
    },

    "manhunter": {
        "name": "Manhunter",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Nemesis"},
        'maximum_intro_year': 5,
        'late_intro_event': 'mh_hanged_man',
        "flair": {
            "color": "eee",
            "bgcolor": "7AB7E0",
            'border_color': 'CCE3F7',
        },
        "nemesis_monsters": ["manhunter"],
        "special_showdowns": ["manhunter"],
        "always_available": {
            "innovation": ["War Room", "Settlement Watch", "Crimson Candy"],
        },
        "timeline_add": [
            {"ly": 5,  "handle": "mh_hanged_man"},
            {
                "ly": 5,
                "sub_type": "special_showdown",
                "name": "Special Showdown - Manhunter"
            },
            {
                "ly": 10,
                "sub_type": "special_showdown",
                "name": "Special Showdown - Manhunter"
            },
            {
                "ly": 16,
                "sub_type": "special_showdown",
                "name": "Special Showdown - Manhunter"
            },
            {
                "ly": 22,
                "sub_type": "special_showdown",
                "name": "Special Showdown - Manhunter"
            },
        ],
    },

    "slenderman": {
        "name": "Slenderman",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Nemesis"},
        'maximum_intro_ly': 6,
        'late_intro_event': 'slender_its_already_here',
        "flair": {
            "color": "fff2b7",
            "bgcolor": "BEA9CB",
        },
        "nemesis_monsters": ["slenderman"],
        "rm_nemesis_monsters": ["kings_man"],
        "always_available": {
            "innovation": ["Dark Water Research"],
        },
        "timeline_add": [
            {"ly": 6, "handle": "slender_its_already_here"},
            {
                "ly": 9,
                "sub_type": "nemesis_encounter",
                "name": "Nemesis Encounter"
            },
        ],
        "timeline_rm": [
            {"ly": 6, "handle": "core_armored_strangers"},
            {
                "ly": 9,
                "sub_type": "nemesis_encounter",
                "name": "Nemesis Encounter: King's Man Lvl 1"
            },
        ],
    },
    "spidicules": {
        "name": "Spidicules",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_ly': 2,
        'late_intro_event': 'spid_young_rivals',
        "flair": {
            "color": "333",
            "bgcolor": "AB9D23",
            'border_color': 'D2CD97',
        },
        "quarries": ["spidicules"],
        "always_available": {
            "location": ["Silk Mill"],
            "innovation": ["Legless Ball","Silk-Refining"],
        },
        "timeline_add": [
            {"ly": 2, "handle": "spid_young_rivals"},
        ],
        "timeline_rm": [
            {"ly": 2, "handle": "core_endless_screams"},
        ],
    },

    "sunstalker": {
        "name": "Sunstalker",
        "released": datetime(2016, 2, 16, 12, tzinfo=TIMEZONE),
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_ly': 8,
        'late_intro_event': 'ss_promise_under_the_sun',
        "flair": {
            "color": "666",
            "bgcolor": "F5E99D",
            'border_color': 'DDD099',
        },
        "quarries": ["sunstalker"],
        "always_available": {
            "location": ["Skyreef Sanctuary"],
            "innovation": ["Umbilical Bank"],
        },
        "timeline_add": [
            {"ly": 8, "handle": "ss_promise_under_the_sun"},
        ],
    },
}
