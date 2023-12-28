'''

	White box expansions are organized here in chronological order.

'''

from datetime import datetime
from app import API
TIMEZONE = API.config['TIMEZONE']

white_box_2012 = {

    'holiday_white_speaker_nico': {
        'released': datetime(2012, 7, 1, 12, tzinfo=TIMEZONE),
        'name': 'Holiday White Speaker Nico',
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

}


white_box_2016 = {
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
    "fade": {
        "name": "Fade",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2016, 8, 4, 12, tzinfo=TIMEZONE),
        'basic_hunt_event': ['baby_and_the_sword'],
        'subscriber_level': 2,
    },
    "percival": {
        "name": "Percival",
        "ui": {"pretty_category": "White Box"},
        "released": datetime(2016, 8, 4, 12, tzinfo=TIMEZONE),
        'basic_hunt_event': ['dead_warrior'],
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

}

white_box_2017 = {

    'detective_twilight_knight': {
        'name': 'Detective Twilight Knight',
        'released': datetime(2017, 8, 31, 12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

}

white_box_2018 = {
    'pinup_devil_satan': {
        'name': "Pinup Devil Satan",
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2018, 10, 31, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },
    'white_speaker_2018': {
        'name': "White Speaker",
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2018, 11, 22, 12, tzinfo=TIMEZONE),
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
}

white_box_2019 = {
    'valentines_day_pinup_twilight_knight': {
        'name': "Valentine's Day Pinup Twilight Knight",
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2019, 2, 14, 12, tzinfo=TIMEZONE),
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
}

white_box_2020 = {
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
}

white_box_2021 = {
    'halloween_survivors_series_2': {
        'name': 'Halloween Survivors - Series II',
        'ui': {'pretty_category': 'White Box'},
        'released': datetime(2021, 11, 25, 12, tzinfo=TIMEZONE),
        'subscriber_level': 2,
    },
}

white_box_2022 = {

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
    'novice': {
        'name': 'Novice',
        'released': datetime(2022,12,25,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

}

white_box_2023 = {

    'hellebore': {
        'name': 'Hellebore - A Frozen Survivor',
        'released': datetime(2023,1,31,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },
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
    'lunar_twilight_knight': {
        'name': 'Lunar Twilight Knight',
        'released': datetime(2023,2,28,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

    # vitanvox - 2023-03-31
    'vitanvox': {
        'name': 'Vitanvox',
        'released': datetime(2023,3,31,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

    # skrelle - 2023-03-31

    # gnostin stonesmasher - 2023-05-02

    # lolowen - 2023-05-02

    # mist raikin armor - 2023-06-12


    # cockroach queen - 2023-12-25

    'cockroach_queen':{
        'name': 'Cockroach Queen',
        'released': datetime(2023,12,25,12, tzinfo=TIMEZONE),
        'ui': {'pretty_category': 'White Box'},
        'subscriber_level': 2,
    },

}
