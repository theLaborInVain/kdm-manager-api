"""

    All known expansions are defined here.

"""

from datetime import datetime
import pytz

USCENTRAL = pytz.timezone('US/Central')

expansions_of_death = {

    # Kickstarter 1 expansions

    "dragon_king": {
        "name": "Dragon King",
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2016, 2, 16, 12, tzinfo=USCENTRAL),
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


gamblers_chest = {

    'arc_survivors': {
        'pillars': 3,
        'name': 'Arc Survivors',
        'released': datetime(2023, 7, 31, 12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': "Advanced KDM"},
        'flair': {'bgcolor': '41A165'},
        'always_available': {
            'location': ['forum'],
        },
    },

    'crimson_crocodile': {
        'name': 'Crimson Crocodile',
        'release': datetime(2023, 7, 31, 12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': "Quarry"},
        'quarries': ['crimson_crocodile'],
    },

}


product_lines = {


    # Echoes of Death

    "echoes_of_death": {
        "released": datetime(2018, 7, 1, 12, tzinfo=USCENTRAL), # Gencon 2018
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
        "released": datetime(2019, 8, 1, 12, tzinfo=USCENTRAL), # Gencon 2019
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

    "echoes_of_death_3": {
        "released": datetime(2020, 11, 27, 12, tzinfo=USCENTRAL), # Black Friday 2020
        "name": "Echoes of Death 3",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "333",
            "bgcolor": "fafafa",
        },
        'strain_milestones': [
            'ashen_claw_strain',
            'carnage_worms',
            'material_feedback_strain',
            'sweat_stained_oath',
        ],
        'help': [
            {
                'type': 'gear',
                'tip': (
                    'The <b>Twilight Sword</b> cannot be named by survivors '
                    'with the <b>Sword Oath</b> Fighting Art because it does '
                    'not have the <i>sword</i> keyword.'
                ),
            },
        ],
    },


    # white box
    "tenth_anniversary_white_speaker": {
        "name": "10th Anniversary White Speaker",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 10, 9, 12, tzinfo=USCENTRAL),
        'strain_milestones': ['plot_twist'],
    },

    "tenth_anniversary_survivors": {
        "name": "10th Anniversary Survivors",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 10, 9, 12, tzinfo=USCENTRAL),
    },

    "fade": {
        "name": "Fade",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2016, 8, 4, 12, tzinfo=USCENTRAL),
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

    "oktoberfest_aya": {
        "name": "Oktoberfest Aya",
        'subtitle': (
            'Includes crafting recipes that require <b>Lonely Tree</b>.'
        ),
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 10, 31, 12, tzinfo=USCENTRAL),
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
        "released": datetime(2019, 10, 31, 12, tzinfo=USCENTRAL),
    },

    "halloween_ringtail_vixen_2020": {
        'name': 'Halloween Ringtail Vixen',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2020, 10, 31, 12, tzinfo=USCENTRAL),
    },

    'holiday_white_speaker_nico': {
        'released': datetime(2012, 7, 1, 12, tzinfo=USCENTRAL),
        'name': 'Holiday White Speaker Nico',
        'ui': {'pretty_category': 'White Box'},
    },

    "percival": {
        "name": "Percival",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2016, 8, 4, 12, tzinfo=USCENTRAL),
        'basic_hunt_event': ['dead_warrior'],
    },

    'santa_satan': {
        'released': datetime(2018, 12, 25, 12, tzinfo=USCENTRAL),
        'name': 'Santa Satan',
        'ui': {'pretty_category': 'White Box'},
        'strain_milestones': ['atmospheric_change'],
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
        'released': datetime(2019, 2, 14, 12, tzinfo=USCENTRAL),
    },
    'swashbuckler': {
        'name': 'Swashbuckler',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2016, 3, 1, 12, tzinfo=USCENTRAL),
        'subtitle': (
            'One of the few figures from the <i>Generic</i> line that also '
            'includes game content.'
        ),
    },
    'easter_pinup_twilight_knight': {
        'name': "Easter Pinup Twilight Knight",
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2019, 4, 22, 12, tzinfo=USCENTRAL),
        'subtitle': 'Adds <b>Gibbering Haremite</b> vermin only.',
    },
    "sword_hunter": {
        "name": "Sword Hunter",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2019, 8, 1, 12, tzinfo=USCENTRAL),
        'basic_hunt_event': ['sword_in_the_stone'],
    },
    'vignettes_of_death_white_gigalion': {
        'released': datetime(2019, 8, 1, 12, tzinfo=USCENTRAL),
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
    'pinups_of_death_2': {
        'name': 'Pinups of Death II',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2020, 11, 1, 12, tzinfo=USCENTRAL),
    },

    'winter_solstice_lucy': {
        'name': 'Winter Solstice Lucy',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2020, 12, 22, 12, tzinfo=USCENTRAL),
    },

    'halloween_survivors_series_2': {
        'name': 'Halloween Survivors - Series II',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2021, 11, 25, 12, tzinfo=USCENTRAL),
    },

    'grimmory': {
        'released': datetime(2022,3,1, 12, tzinfo=USCENTRAL),
        'name': 'Grimmory',
        'ui': {'pretty_category': 'White Box'},
    },
    'pascha': {
        'name': 'Pascha',
        'released': datetime(2022,4,22,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },
    'willow': {
        'name': 'Willow',
        'released': datetime(2022,4,22,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },
    'badar': {
        'name': 'Badar',
        'released': datetime(2022,5,31,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },
    'doll': {
        'name': 'Doll',
        'released': datetime(2022,8,9,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },
    'summer_cyrus': {
        'name': 'Summer Cyrus',
        'released': datetime(2022,8,9,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },
    'summer_aya': {
        'name': 'Summer Aya',
        'released': datetime(2022,9,30,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },
    'summer_goth_twilight_knight': {
    'name': 'Summer Goth - Twilight Knight',
        'released': datetime(2022,9,30,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },

    # halloween 2022
    'reapokratis': {
        'name': 'Reapokratis',
        'released': datetime(2022,10,31,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },
    'erza_of_dedheim': {
        'name': 'Erza of Dedheim',
        'released': datetime(2022,10,31,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },
    'halloween_survivor_flower_knight_costume': {
        'name': 'Halloween Survivor - Flower Knight Costume',
        'released': datetime(2022,10,31,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
        'subtitle': (
            'Includes crafting recipes that require <b>Flower Knight</b>.'
        ),
    },


    # elgnirk the chaos elf - 2022-12-25
    'elgnirk_the_chaos_elf': {
        'name': 'Elgnirk, The Chaos Elf',
        'released': datetime(2022,12,25,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
        "flair": {
            "color": "FFF",
            "bgcolor": "00833B",
        },
    },

    # novice - 2022-12-25
    'novice': {
        'name': 'Novice',
        'released': datetime(2022,12,25,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },

    # hellebore - 2023-01-31
    'hellebore': {
        'name': 'Hellebore - A Frozen Survivor',
        'released': datetime(2023,1,31,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },

    # death crown inheritor aya - 2023-02-28
    'death_crown_inheritor_aya': {
        'name': 'Death Crown Inheritor Aya',
        'released': datetime(2023,2,28,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
        'flair': {
            'bgcolor': 'C55745',
            'color': 'FFF'
        },
    },

    # lunar twilight knight - 2023-02-28

    # vitanvox - 2023-03-31

    # skrelle - 2023-03-31

    # gnostin stonesmasher - 2023-05-02

    # lolowen - 2023-05-02

    # mist raikin armor - 2023-06-12

}


miscellaneous = {

    # anything that's not part of a product line or group of related things
    # gets filed here

    "beta_challenge_scenarios": {
        "released": datetime(2016, 2, 1, 12, tzinfo=USCENTRAL),
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

    'allison_the_twilight_knight': {
        'name': 'Allison the Twilight Knight',
        "released": datetime(2016, 8, 16, 12, tzinfo=USCENTRAL),
        'subtitle': (
            'As released in the White Box Hard Plastic Collection.'
        ),
        'ui': {'pretty_category': 'White Box'},
        'url': (
            'https://www.kickstarter.com/projects/poots/kingdom-death-monster/'
            'posts/381921/'
        ),
    },

    'pinup_wet_nurse': {
        'name': 'Pinup Wet Nurse',
        'released': datetime(2016, 10, 31, 12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'White Box'},
    },

    "promo": {
        "released": datetime(2015, 9, 2, 12, tzinfo=USCENTRAL),
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
            'Before the Wall, '
            'Beyond the Wall, '
            "Black Friday Ninja, "
            "Detective Twilight Knight, "
            'Halloween Pinup Twilight Knight, '
            "Pinup Easter Aya, "
#            "Pinup Easter Twilight Knight, "
            "Pinup Devil Satan (Halloween 2018), "
            'Pinup Order Knight, '
            'Pinup Sci-fi Twilight Knight, '
            "Pinup Sci-fi White Speaker, "
            'Pinup Warrior of the Sun, '
            "Pinups of Death, "
#            "Valentine's Day Pinup Twilight Knight, "
            'White Speaker.'
#            "White Speaker Nico, "
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
        'released': datetime(2021,11,25, 12, tzinfo=USCENTRAL),
        'name': 'Sunlion Armor (Beta)',
        'ui': {'pretty_category': 'Enhancement'},
    },
    'white_sunlion_armor': {
        'name': 'White Sunlion Armor',
        'released': datetime(2022,11,25,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'Enhancement'},
        'subtitle': (
            'Augments <b>People of the Sun</b> campaign; includes '
            '<b>Bleeding Corpse Lily</b> terrain and Strange Resource.'
        ),
    },


    # screaming sun / oni armor
    'screaming_sun_armor': {
        'name': 'Screaming Sun Armor',
        'released': datetime(2022,11,25,12, tzinfo=USCENTRAL),
        'ui': {'pretty_category': 'Enhancement'},
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
