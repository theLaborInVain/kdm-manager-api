"""

    Game versions are tracked here.

    This asset is an ordered dict because we use it in an uninitialized fashion
    during the initialization of the models module (and thus can't initialize
    it without a circular import etc.).

"""

from collections import OrderedDict
from datetime import datetime

VERSIONS = OrderedDict({
    'core_1_3': {
        'major': 1,
        'minor': 3,
        'patch': 1,
        'released': datetime(2015,9,1),
        'desc': 'Original Kickstarter release.',
        'name': 'Original Kickstarter release.',
        'assets': {
            'abilities_and_impairments': {
                "club_specialization": {
                    "name": "Specialization - Club",
                    "desc": (
                        "All clubs in your gear grid gain <b>paired</b>. "
                        "Cannot use this with two-handed clubs."
                    ),
                },
                "mastery_club": {
                "name": "Mastery - Club",
                "desc": (
                    "If you are a Club Master, all Clubs in your gear grid "
                    "gain <b>Savage</b>. On a <b>Perfect hit</b> with a Club, "
                    "gain <i>+3 strength</i> until the end of the attack."
                ),
                "weapon_proficiency": "club",
                "weapon_name": "club",
                "current_survivor": {
                    "abilities_and_impairments": ["club_specialization"]},
                "new_survivor": {
                    "abilities_and_impairments": ["club_specialization"]},
                'epithet': 'club_master',
                },
            }
        },
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
        'name': 'Version 1.6, announced Black Friday 2020.',
        'assets': {
            'gear': {
                'blood_sheath': {
                    'sub_type': 'plumery',
                    'recipes': [
                        {
                            'locations': ['plumery'],
                            'resource_handles': {
                                'hollow_wing_bones': 1, 'muculent_droppings': 1
                            },
                            'resource_types': {'organ': 5}
                        },
                    ],
                },
                'blue_charm': {
                    'sub_type': 'barber_surgeon',
                    'recipes': [
                        {
                            'locations': ['barber_surgeon'],
                            'resource_types': {'organ': 3},
                        },
                    ],
                },
                'boss_mehndi': {
                    'recipes': [
                        {
                            'locations': ['stone_circle'],
                            'resource_handles': {'beast_steak': 1},
                            'resource_types': {'bone': 1},
                        },
                    ],
                },
                'brain_mint': {
                    'sub_type': 'stone_circle',
                    'recipes': [
                        {
                            'locations': ['stone_circle'],
                            'resource_handles': {'screaming_brain': 1},
                        },
                    ],
                },
                'bug_trap': {
                    'recipes': [
                        {
                            'locations': ['barber_surgeon'],
                            'resource_handles': {'perfect_organ': 1},
                            'resource_types': {'bone':2}
                        },
                    ],
                },
                'cloth_leggings': {
                    'keywords': ['item', 'cloth', 'set'],
                    'desc': (
                        'When you suffer the <b>Bleeding</b> or <b>Bloody '
                        'Thighs</b> severe leg injuries, the leggings help '
                        'staunch the bleeding. You instead gain 1 bleeding '
                        'token.'
                    ),
                },
                'counterweighted_axe': {
                    'affinities': {'top': 'red'},
                    'affinity_bonus': {
                        'desc': (
                            'On a <b>Perfect hit</b>, monster suffers 1 wound, '
                            'do not draw a hit location. Limit once per attack.'
                        ),
                        'requires': {
                            'puzzle': {'red': 1},
                        },
                    },
                },
                'dragon_slayer': {
                    'recipes': [
                        {
                            'locations': ['blacksmith'],
                            'resource_types': {'organ': 3},
                            'resource_handles': {
                                'iron': 5,
                            },
                        },
                    ],
                },
                'elder_earrings': {
                    'sub_type': 'stone_circle',
                    'desc': (
                        'On <b>Arrival</b>, gain +2 survival. During the '
                        '<b>Aftermath</b>, gain +1 Hunt XP.'
                    ),
                    'recipes': [
                        {
                            'locations': ['stone_circle'],
                            'resource_handles': {'shank_bone': 1},
                            'resource_types': {'scrap':1}
                        },
                    ],
                },
                'final_lantern': {
                    'keywords': ['item', 'lantern', 'other'],
                },
                'finger_of_god': {
                    'sub_type': 'plumery',
                    'recipes': [
                        {
                            'locations': ['plumery'],
                            'resource_handles': {'phoenix_finger': 1},
                            'resource_types': {'bone': 4,}
                        },
                    ],
                },
                'first_aid_kit': {
                    'recipes': [
                        {
                            'locations': ['barber_surgeon'],
                            'resource_types': {
                                'leather': 1,
                            },
                            'resource_handles': {
                                'perfect_bone': 1
                            },
                        },
                    ],
                },
                'green_charm': {
                    'sub_type': 'barber_surgeon',
                    'recipes': [
                        {
                            'locations': ['barber_surgeon'],
                            'resource_types': {'organ': 3},
                        },
                    ],
                },
                'hollow_sword': {
                    'speed': 2,
                    'strength': 5,
                    'keywords': ['weapon', 'melee', 'sword', 'dagger', 'bone'],
                    'rules': ['Frail'],
                    'desc': (
                        "This weapon gains strength equal to the monster's "
                        'damage attribute.'
                    ),
                },
                'lantern_dagger': {
                    'recipes': [
                        {
                           'locations': ['blacksmith'],
                           'resource_types': {'bone': 2},
                           'resource_handles': {
                               'iron': 1,
                               'leather': 3,
                            },
                        },
                    ],
                },
                'lantern_halberd': {
                    'keywords': [
                        'weapon', 'melee', 'two-handed',
                        'spear', 'lantern', 'other'
                    ],
                },
                'lantern_sword': {
                    'recipes': [
                        {
                            'locations': ['blacksmith'],
                            'resource_types': {'bone': 4, 'hide': 3},
                            'resource_handles': {
                                'iron': 1,
                            },
                        },
                    ],
                },
                'monster_grease': {
                    'keywords': [
                        'item', 'consumable', 'soluble', 'stinky', 'flammable'
                    ],
                    'recipes': [
                        {
                           'locations': ['organ_grinder'],
                           'resource_types': {'organ': 2}
                        },
                    ],
                },
                'oxidized_lantern_glaive': {
                    'desc': (
                        '<b>Barbed 4:</b> On a <b>Perfect hit</b>, gain +4 '
                        'strength for the rest of the attack.'
                    ),
                },
                'rainbow_katana': {
                    'sub_type': 'plumery',
                    'recipes': [
                        {
                            'locations': ['plumery'],
                            'resource_handles': {
                                'bird_beak': 1, 'rainbow_droppings': 1
                            },
                            'resource_types': {'iron': 1, 'bone': 6},
                            'suffix_text': '<b>Heat</b> Required.'
                        },
                    ],
                },
                'red_charm': {
                    'sub_type': 'barber_surgeon',
                    'recipes': [
                        {
                            'locations': ['barber_surgeon'],
                            'resource_types': {'organ': 3},
                        },
                    ],
                },
                'ring_whip': {
                    'recipes': [
                        {
                            'locations': ['blacksmith'],
                            'resource_types': {'bone': 3, 'organ': 2},
                            'resource_handles': {
                                'iron': 1,
                            },
                        },
                    ],
                },
                'scrap_dagger': {
                    'desc': (
                        '<b>Barbed 2:</b> On a <b>Perfect hit</b>, gain +2 '
                        'strength for the rest of the attack.'
                    ),
                },
                'scrap_sword': {
                    'desc': (
                        '<b>Barbed 4:</b> On a <b>Perfect hit</b>, gain +4 '
                        'strength for the rest of the attack.'
                    ),
                },
                'screaming_bracers': {
                    'desc': (
                        'When you activate terrain, you may add +2 to your '
                        'roll result.'
                    ),
                },
                'screaming_skirt': {
                    'armor': 2,
                    'recipes': [
                        {
                            'locations': ['stone_circle'],
                            'resource_handles': {'pelt': 1},
                            'resource_types': {'hide': 1},
                        },
                    ],
                },
                'screaming_horns': {
                    'armor': 2,
                    'desc': (
                        '<font class="kdm_font">a</font>: Scream. Non-deaf '
                        '<b>insane</b> survivors gain +1 movement until end of '
                        'round. All other non-deaf survivors gain +1 insanity.'
                    ),
                },
                'scavenger_kit': {
                    'recipes': [
                        {
                            'locations': ['barber_surgeon'],
                            'resource_types': {'scrap': 1},
                            'resource_handles': {'perfect_hide': 1}
                        },
                    ],
                },
                'screaming_armor_set': {
                    'desc': (
                        'Add <font class="inline_shield">1</font> to all hit '
                        'locations. <br/><b>Skewer:</b> After you <b>slam</b>, '
                        'spend <font class="kdm_font">a</font> to move 1 space '
                        'and activate a melee weapon with +2 strength. If you '
                        'wound with a spear, apply that wound roll result to '
                        'the next selected hit location this attack.',
                    ),
                },
                'skullcap_hammer': {
                    'recipes': [
                        {
                            'locations': ['weapon_crafter'],
                            'resource_handles': {'skull': 1},
                            'resource_types': {'hide': 1 },
                        },
                    ],
                },
                'sonic_tomahawk': {
                    'strength': 6,
                    'affinity_bonus':{
                        'desc':'Gain <b>Savage</b> and <b>Paired</b>',
                        'requires':{
                            'puzzle': {'red': 1},
                            'complete': {'red': 1, 'blue': 1},
                        },
                    },
                },
                'speed_powder': {
                    'sub_type': 'stone_circle',
                    'recipes': [
                        {
                            'locations': ['stone_circle'],
                            'resource_types': {'organ': 2},
                            'resource_handles': {'second_heart': 1}
                        },
                    ],
                },
                'steel_sword': {
                    'desc': (
                        '<b>Barbed 1d10:</b> On a <b>Perfect hit</b>, gain '
                        '+1d10 strength for the rest fo the attack.'
                    ),
                },
                'vespertine_bow': {
                    'strength': 1,
                },
                'zanbato': {
                    'recipes': [
                        {
                            'locations': ['weapon_crafter'],
                            'resource_handles': {'perfect_bone': 1},
                            'resource_types': {
                                'scrap': 3,
                                'hide': 1,
                            },
                        },
                    ],
                },
                # next gear
            },
            'disorders': {
                'vermin_obsession': {
                    'flavor_text': 'You love insects.',
                    'survivor_effect': (
                        'While there is a <b>Bug Patch</b> terrain tile on the '
                        'showdown board, you are so overwhelmed that you '
                        'cannot spend survival.'
                    ),
                },
            },
            # next asset class
            'locations': {
                'organ_grinder': {
                    'name': 'Organ Grinder',
                    'endeavors': [
                        'organ_grinder_augury',
                        'organ_grinder_stone_noses',
                        'organ_grinder_build_barber_surgeon',
                    ],
                },
            },
        },
    },
    # core 1.7
})
