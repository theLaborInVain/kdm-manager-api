'''

    Includes gear from all Gambler's Chest expansions.

'''


#
#   Crimson Crocodile
#

crimson_crockery = {

    # weapons
    'blood_compass_lantern': {
        'expansion': 'crimson_crocodile',
        'name': 'Blood Compass Lantern',
        'keywords': ['item', 'lantern', 'other'],
        'affinities': {'right': 'blue', 'bottom': 'blue'},
        'desc': (
            'Before making a wound attempt, you may gain 1 bleeding token to '
            'discard all hit locations from your attack and draw that many to '
            'replace them. Limit once per round.'
        ),
        'recipes': [
            {
                'resource_handles': {'groomed_nails': 1, 'skull': 1},
                'resource_types': {'scrap': 1},
            },
        ],
    },

    'bloodglass_cleaver': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodglass Cleaver',
        'keywords': ['weapon', 'melee', 'axe', 'bone'],
        'speed': 3,
        'accuracy': 6,
        'strength': 0,
        'affinities': {'right': 'red', 'bottom': 'red'},
        'rules': ['Honed 5'],
        'related_rules': ['guardless', 'honed_x'],
        'desc': (
            'While this is equipped, you are <b>guardless</b>. <br/>'
            '<b>Guardless:</b> You cannot dodge or ignore hits.'
        ),
        'recipes': [
            {
                'resource_handles': {'flat_vein': 1, 'veined_glass': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },

    'bloodglass_dagger': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodglass Dagger',
        'keywords': ['weapon', 'melee', 'dagger', 'bone'],
        'speed': 3,
        'accuracy': 6,
        'strength': 0,
        'affinities': {'right': 'red'},
        'rules': ['Honed 3'],
        'related_rules': ['honed_x', 'parry', 'super_dense'],
        'desc': (
            '<b>Honed 3:</b> This has +3 strength until its edge is ruined '
            'after wounding a <b>Parry</b> or <b>Super-dense</b> hit location. '
        ),
        'recipes': [
            {
                'resource_handles': {'veined_glass': 1},
            },
        ],
    },

    'bloodglass_katar': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodglass Katar',
        'keywords': ['weapon', 'melee', 'katar', 'bone'],
        'speed': 2,
        'accuracy': 6,
        'strength': 0,
        'affinities': {'bottom': 'green'},
        'rules': ['Honed 4', 'Paired'],
        'related_rules': ['guardless', 'honed_x', 'paired'],
        'desc': (
            'While you have 3+ bleeding tokens, you gain +2 evasion and '
            'are <b>guardless</b>.'
        ),
        'recipes': [
            {
                'resource_handles': {'pale_fingers': 1, 'veined_glass': 1},
            },
        ],
    },

    'bloodglass_longsword': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodglass Longsword',
        'keywords': ['weapon', 'melee', 'sword', 'two-handed', 'heavy', 'bone'],
        'speed': 2,
        'accuracy': 6,
        'strength': 0,
        'affinities': {'right': 'blue', 'left': 'red'},
        'rules': ['Honed 3', 'Reach 2'],
        'related_rules': ['honed_x', 'reach'],
        'affinity_bonus': {
            'desc': (
                'If you have 3+ bleeding tokens, the Honed Edge cannot be '
                'ruined.'
            ),
            'requires': {
                'puzzle': {'red': 1, 'blue': 1},
            },
        },
        'recipes': [
            {
                'resource_handles': {'immortal_tongue': 1, 'veined_glass': 1},
                'reqource_types': {'bone': 1},
            },
        ],
    },

    'bloodglass_saw': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodglass Saw',
        'keywords': ['weapon', 'melee', 'saw', 'two-handed', 'bone'],
        'speed': 2,
        'accuracy': 7,
        'strength': 0,
        'affinities': {'top': 'blue'},
        'rules': ['Honed 4', 'Savage'],
        'related_rules': ['honed_x', 'savage'],
        'desc': (
            '<b>Saw:</b> Spend <font class="kdm_manager_font">M</font>. For '
            'the rest of the round, your attacks with this weapon gain +2 luck.'
        ),
        'recipes': [
            {
                'resource_handles': {'crimson_bone': 1, 'veined_glass': 2},
            },
        ],
    },

    'crimson_bow': {
        'expansion': 'crimson_crocodile',
        'name': 'Crimson Bow',
        'keywords': ['weapon', 'ranged', 'bow', 'two-handed'],
        'speed': 2,
        'accuracy': 6,
        'strength': 3,
        'affinities': {'right': 'red', 'top': 'blue'},
        'rules': ['Cumbersome', 'Range 5'],
        'related_rules': ['cumbersome', 'range_x', 'deadly'],
        'affinity_bonus': {
            'desc': (
                'This gains +2 strength and <b>Deadly</b> while attacking from '
                "the monster's facing."
            ),
            'requires': {
                'puzzle': {'red': 1},
                'complete': {'blue': 1},
            },
        },
        'recipes': [
            {
                'resource_handles': {
                    'irregular_optic_nerve': 1, 'crimson_bone': 1
                },
            },
        ],
    },

    'crocbone_hammer': {
        'expansion': 'crimson_crocodile',
        'name': 'Crocbone Hammer',
        'keywords': ['weapon', 'melee', 'club', 'bone'],
        'speed': 2,
        'accuracy': 7,
        'strength': 2,
        'affinities': {'right': 'red', 'bottom': 'green'},
        'related_rules': ['clobber_x', 'super_dense'],
        'desc': (
            '<b>Clobber 4:</b> Gain +4 strength while attempting to wound a '
            '<b>Super-dense</b> hit location.'
        ),
        'recipes': [
            {
                'resource_handles': {'crimson_bone': 1},
                'resource_types': {'bone': 1},
            },
        ],
    },

    'finger_darts': {
        'expansion': 'crimson_crocodile',
        'name': 'Finger Darts',
        'keywords': ['weapon', 'ranged', 'thrown', 'consumable'],
        'speed': 2,
        'accuracy': 7,
        'strength': 2,
        'affinities': {'right': 'green', 'left': 'blue'},
        'rules': ['Range: 4'],
        'related_rules': ['range_x'],
        'affinity_bonus': {
            'desc': (
                '<font class="kdm_manager_font">A</font> <b>Consume:</b> '
                'Devour the scum from under a fingernail to gain '
                '+&#9733; insanity.'
            ),
            'requires': {
                'puzzle': {'green': 1, 'blue': 1},
            },
        },
        'recipes': [
            {
                'resource_handles': {'pale_fingers': 1},
                'resource_types': {'scrap': 1},
            },
        ],
    },

    'giggling_scythe': {
        'expansion': 'crimson_crocodile',
        'name': 'Giggling Scythe',
        'keywords': [
            'weapon', 'melee', 'grand', 'scythe', 'two-handed', 'bone'
        ],
        'speed': 3,
        'accuracy': 5,
        'strength': 8,
        'affinities': {'top': 'blue'},
        'rules': ['Sharp', 'Reach: 2', 'Unique'],
        'related_rules': ['reach_x'],
        'desc': (
            'When you critically wound, automatically critically wound all '
            'remaining hit locations in your attack.'
        ),
        'recipes': [
            {
                'resource_handles': {
                    'perfect_bone': 2,
                    'perfect_hide': 2,
                    'veined_glass': 13
                },
            },
        ],
    },

    # armor
    'crimson_dress': {
        'expansion': 'crimson_crocodile',
        'name': 'Crimson Dress',
        'armor': 2,
        'location': 'chest',
        'keywords': ['armor', 'set', 'flesh'],
        'affinities': {'right': 'red', 'left': 'blue'},
        'desc': (
            '<b>Immortal Spin:</b> Spend '
            '<font class="kdm_manager_font">A</font>'
            '<font class="kdm_manager_font">M</font> '
            'to move 3 spaces forward. Then if you moved 3 spaces, active '
            'a melee weapon with +1 strength for each bleeding token you have.'
        ),
        'recipes': [
            {
                'resource_handles': {'crimson_fin': 1},
                'resource_types': {'hide': 1},
            },
        ],
    },

    'crimson_faulds': {
        'expansion': 'crimson_crocodile',
        'name': 'Crimson Faulds',
        'armor': 2,
        'location': 'waist',
        'keywords': ['armor', 'set', 'flesh'],
        'affinities': {'bottom': 'green'},
        'desc': (
            'When you <b>depart</b>, gain a bleeding token. It requires one '
            'more bleeding token to kill you.'
        ),
        'recipes': [
            {
                'resource_handles': {'pale_flesh': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },

    'crimson_guard': {
        'expansion': 'crimson_crocodile',
        'name': 'Crimson Guard',
        'armor': 2,
        'location': 'arms',
        'keywords': ['armor', 'set', 'flesh'],
        'affinities': {'top': 'green', 'left': 'red'},
        'desc': (
            'When you <b>depart</b>, a pale scab hardens on your forearm. Gain '
            'a bleeding token and add <font class="inline_shield">1</font> '
            'to the arms hit location.'
        ),
        'recipes': [
            {
                'resource_handles': {'pale_flesh': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },

    'crimson_helm': {
        'expansion': 'crimson_crocodile',
        'name': 'Crimson Helm',
        'armor': 2,
        'location': 'head',
        'keywords': ['armor', 'set', 'bone'],
        'affinities': {'right': 'red'},
        'desc': (
            '<b>Mindlock 1:</b> Spend <font class="kdm_manager_font">A</font>, '
            'you now have exactly 1 mindlock token. When you suffer brain '
            'damage, ignore it and lose 1 mindlock token.'
        ),
        'recipes': [
            {
                'resource_handles': {'crimson_bone': 1},
                'resource_types': {'hide': 1},
            },
        ],
    },

    'crimson_slippers': {
        'expansion': 'crimson_crocodile',
        'name': 'Crimson Slippers',
        'armor': 2,
        'location': 'legs',
        'keywords': ['armor', 'set', 'flesh'],
        'affinities': {'left': 'red'},
        'recipes': [
            {
                'resource_handles': {'pale_flesh': 1},
                'resource_types': {'bone': 1},
            },
        ],
    },

    # misc
    # crimson_pearls
    # crocodileyes

}

crimson_crocodile_misc_gear = {
    'bloody_cloth': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloody Cloth',
        'type': 'starting_gear',
        'keywords': ['armor', 'cloth'],
        'armor': 1,
        'desc': (
            'When you <b>depart</b>, gain +1 insanity. You may use this as '
            'armor for for any hit location.'
        ),
    },
}


#
#   smog singers
#
