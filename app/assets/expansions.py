"""

    All known expansions are defined here.

    Each expansion belongs to one of four groups:
        - quarry
        - nemesis
        - enhancement

    Any expansion that DOES NOT include a quarry or nemesis monster belongs to
    the enhancement group: it's the catch-all.

"""

from datetime import datetime


expansions_of_death = {

    # Kickstarter 1 expansions

    "dragon_king": {
        "name": "Dragon King",
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
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_year': 8,
        'late_intro_event': 'dbk_rumbling_in_the_dark',
        "flair": {
            "color": "EAE40A",
            "bgcolor": "C3C8AB",
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
    },

    "gorm": {
        "name": "Gorm",
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_ly': 1,
        'late_intro_event': 'gorm_approaching_storm',
        "flair": {
            "color": "EAE40A",
            "bgcolor": "958C83",
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
    },

    "green_knight_armor": {
        "name": "Green Knight Armor",
        "ui": {"pretty_category": "Enhancement"},
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
        "ui": {"pretty_category": "Nemesis"},
        'maximum_intro_year': 5,
        'late_intro_event': 'mh_hanged_man',
        "flair": {
            "color": "E8cE55",
            "bgcolor": "8D0000",
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
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_ly': 2,
        'late_intro_event': 'spid_young_rivals',
        "flair": {
            "color": "333",
            "bgcolor": "C0B870",
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
        "ui": {"pretty_category": "Quarry"},
        'maximum_intro_ly': 8,
        'late_intro_event': 'ss_promise_under_the_sun',
        "flair": {
            "color": "000",
            "bgcolor": "ECD77E",
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


product_lines = {

    # discreet/distinct product lines

    'generic': {
        'released': datetime(2016, 3, 1),
        'name': 'Generic',
        'ui': {'pretty_category': 'Enhancement'},
        'subtitle': (
            'Adds gear from the KD <i>Generic</i> line.'
        ),
    },

    # Echoes of Death

    "echoes_of_death": {
        "released": datetime(2018, 7, 1), # Gencon 2018
        "name": "Echoes of Death",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "333",
            "bgcolor": "fafafa",
        },
        'strain_milestones': [
            'giants_strain',
            'ethereal_culture_strain',
            'trepanning_strain',
            'opportunist_strain'
        ],
    },

    "echoes_of_death_2": {
        "released": datetime(2019, 8, 1), # Gencon 2019
        "name": "Echoes of Death 2",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "333",
            "bgcolor": "fafafa",
        },
        'strain_milestones': [
            'memetic_symphony',
            'marrow_transformation',
            'surgical_sight',
            'hyper_cerebellum',
        ],
    },


    # white box

    "fade": {
        "name": "Fade",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2016, 8, 4),
        'basic_hunt_event': ['baby_and_the_sword'],
        'help': [
            {
                'type': 'store',
                'tip': (
                    'Though she ships in a White Box, Fade is expansion '
                    'content, '
                    '<a href="https://shop.kingdomdeath.com/products/fade-2" '
                    'target="top">according to the Kingdom Death store</a>. '
                    'For this reason, Fade is separate from other White Box '
                    'content in the Manager.'
                ),
            },
        ],
    },

    "percival": {
        "name": "Percival",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2016, 8, 4),
        'basic_hunt_event': ['dead_warrior'],
        'help': [
            {
                'type': 'store',
                'tip': (
                    'Though she ships in a White Box, Percival is expansion '
                    'content, <a '
                    'href="https://shop.kingdomdeath.com/products/percival-1" '
                    'target="top">according to the Kingdom Death store</a>. '
                    'For this reason, Percival is separate from other White '
                    'Box content in the Manager.'
                ),
            },
        ],
    },

    "sword_hunter": {
        "name": "Sword Hunter",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 8, 1),
        'basic_hunt_event': ['sword_in_the_stone'],
    },




    # Vignettes of Death

    'vignettes_of_death_white_gigalion': {
        'released': datetime(2019, 8, 1),
        'name': 'Vignettes of Death: White Gigalion',
        'ui': {'pretty_category': 'Quarry'},
        'flair': {
            'color': 'fff',
            'bgcolor': '000'
        },
        'strain_milestones': ['somatotropin_surge'],
        'quarries': ['white_gigalion'],
    },

}


miscellaneous = {

    # anything that's not part of a product line or group of related things
    # gets filed here

    "beta_challenge_scenarios": {
        "released": datetime(2016, 2, 1),
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
        "released": datetime(2016, 8, 16),
        "name": "Promo",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "FFF",
            "bgcolor": "4EC6F0",
        },
        "subtitle": (
            'Adds promotional events, gear, Abilities & Impairments, etc.) '
            'to Settlement and Survivor Sheet drop-down lists. '
            'Collects the following releases: '
            "Allison the Twilight Knight, "
            'Before the Wall, '
            'Beyond the Wall, '
            "Black Friday Ninja, "
            "Detective Twilight Knight, "
            'Halloween Pinup Twilight Knight, '
            "Pinup Easter Aya, "
            "Pinup Easter Twilight Knight, "
            "Pinup Devil Satan (Halloween 2018), "
            'Pinup Order Knight, '
            'Pinup Sci-fi Twilight Knight, '
            "Pinup Sci-fi White Speaker, "
            'Pinup Warrior of the Sun, '
            'Pinup Wet Nurse, '
            "Pinups of Death, "
            "Valentine's Day Pinup Twilight Knight, "
            'White Speaker, '
            "White Speaker Nico, "
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

    'santa_satan': {
        'released': datetime(2018, 12, 25),
        'name': 'Santa Satan (promo)',
        'ui': {'pretty_category': 'Enhancement'},
        'strain_milestones': ['atmospheric_strain'],
        'subtitle': (
            "This promo release from Holiday 2018 contains the <i>Atmostpheric "
            "Strain</i> milestone."
        ),
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
        "released": datetime(2018,5,1),
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
        "released": datetime(2018,5,15),
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
