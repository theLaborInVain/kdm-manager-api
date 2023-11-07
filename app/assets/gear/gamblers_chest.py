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
    'crimson_pearls': {
        'expansion': 'crimson_crocodile',
        'name': 'Crimson Pearls',
        'keywords': ['item', 'jewelry', 'oterh'],
        'affinities': {'top': 'red', 'bottom': 'red'},
        'desc': (
            'On <b>Arrival</b>, gain 3 bleeding tokens. Your <b>Fist & '
            'Tooth</b> attacks gain +1 strength for each of your bleeding '
            'tokens.'
        ),
        'recipes': [
            {
                'resource_handles': {'blood_stool': 1, 'crimson_bone': 1},
            },
        ],
    },

    'crocodileyes': {
        'expansion': 'crimson_crocodile',
        'name': 'Crocodileyes',
        'armor': 2,
        'location': 'legs',
        'keywords': ['item', 'soluble'],
        'affinities': {'left': 'red'},
        'related_rules': ['foresight'],
        'desc': (
            'Gain +&#9733; strength if you have no <b>Foresight</b>.<br/>'
            '<b>Foresight:</b> When there are revealed '
            '<span class="kd deck_icon deck="AI">AI</span> or '
            '<span class="kd deck_icon deck="HL">HL</span> cards on top of '
            'decks.'
        ),
        'recipes': [
            {
                'resource_handles': {'eye_of_immortal': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },
}

crimson_crocodile_pattern_gear = {

    'blood_drinker': {
        'expansion': 'crimson_crocodile',
        'type': 'pattern',
        'name': 'Blood Drinker',
        'keywords': ['weapon', 'melee', 'bone', 'axe', 'other'],
        'speed': 2,
        'accuracy': 6,
        'strength': 6,
        'affinities': {'right': 'blue', 'bottom': 'red'},
        'desc': (
            'When you wound the monster, remove one of your bleeding tokens.'
        ),
        'affinity_bonus': {
            'desc': (
                'This weapon gains +3 strength for each of your bleeding '
                'tokens.'
            ),
            'requires': {'puzzle': {'red': 1}, 'complete': {'blue': 1}},
        },
        'recipes': [
            {
                'resource_handles': {'vampire_fang': 1},
                'resource_types': {'organ': 1, 'bone': 1}
            },
        ],
    },

    'diamond_scab_katar': {
        'expansion': 'crimson_crocodile',
        'type': 'pattern',
        'name': 'Diamond Scab Katar',
        'keywords': ['weapon', 'melee', 'bone', 'katar'],
        'speed': 3,
        'accuracy': 6,
        'strength': 4,
        'affinities': {'right': 'red', 'bottom': 'green'},
        'rules': ['Paired', 'Sharp', 'Clobber: 4'],
        'related_rules': ['paired', 'sharp', 'clobber_x'],
        'affinity_bonus': {
            'desc': (
                'On a <b>Perfect Hit</b>, the monster gains -1 toughness '
                'until end of the attack.'
            ),
            'requires': {'puzzle': {'red': 1}, 'complete': {'green': 1}},
        },
        'recipes': [
            {
                'resource_handles': {'diamond_scabs': 1},
                'resource_types': {'organ': 2, 'perfect_resource': 1}
            },
        ],
    },

    'dome_buster': {
        'expansion': 'crimson_crocodile',
        'type': 'pattern',
        'name': 'Dome Buster',
        'keywords': ['weapon', 'melee', 'grand', 'club', 'heavy'],
        'speed': 1,
        'accuracy': 5,
        'strength': 12,
        'affinities': {'bottom': 'blue'},
        'related_rules': ['surpass_x'],
        'desc': (
            '<b>Surpass 5:</b> When your successful wound attempt total '
            "surpasses the monster's toughness by 5 or more, the monster "
            'suffers an additional wound.'
        ),
        'recipes': [
            {
                'resource_handles': {'secret_stone': 1},
                'resource_types': {'bone': 4}
            },
        ],
    },

    'immortal_arm': {
        'expansion': 'crimson_crocodile',
        'type': 'pattern',
        'name': 'Immortal Arm',
        'keywords': ['weapon', 'melee', 'bone', 'shield'],
        'speed': 2,
        'accuracy': 7,
        'strength': 7,
        'affinities': {'top': 'red', 'left': 'red'},
        'related_rules': ['locked', 'deflect_x', 'disarm'],
        'desc': (
            'On arrival, add <font class="inline_shield">2</font> to the arms '
            'hit location. <b>Locked:</b> This cannot be disarmed.'
        ),
        'affinity_bonus': {
            'desc': (
                'This gains the fist & tooth keyword. When you attack with '
                'fist & tooth, <b>Deflect 1</b>.'
            ),
            'requires': {'puzzle': {'red': 2}},
        },
        'recipes': [
            {
                'resource_handles': {'diffuser_heart': 1},
                'resource_types': {'organ': 1, 'bone': 2}
            },
        ],
    },

    'fear_spear': {
        'expansion': 'crimson_crocodile',
        'type': 'pattern',
        'name': 'Fear Spear',
        'keywords': ['weapon', 'melee', 'bone', 'spear'],
        'speed': 2,
        'accuracy': 6,
        'strength': 5,
        'affinities': {'left': 'green', 'right': 'red'},
        'rules': ['Reach 2', 'Sharp'],
        'related_rules': ['reach_x', 'sharp'],
        'affinity_bonus': {
            'desc': (
                'When you gain insanity during the showdown, you may gain '
                '0 or +3 instead.'
            ),
            'requires': {'puzzle': {'red': 1}, 'complete': {'blue': 1}}
        },
        'recipes': [
            {
                'resource_handles': {'crimson_gland': 1},
                'resource_types': {'bone': 2, 'hide': 1}
            },
        ],
    },


    # seed pattern
    'fingernail_whip': {
        'expansion': 'crimson_crocodile',
        'type': 'seed_pattern',
        'name': 'Fingernail Whip',
        'pattern_id': 9,
        'keywords': ['seed', 'weapon', 'melee', 'whip', 'bone', 'other'],
        'affinities': {'right': 'blue', 'left': 'red'},
        'speed': 2,
        'accuracy': 5,
        'strength': 4,
        'rules': ['Heroic'],
        'related_rules': ['heroic', 'super_dense', 'razor_sharp'],
        'affinity_bonus': {
            'desc': (
                'This weapon gains <b>Razor Sharp</b> against '
                '<b>Super-dense</b> hit locations.'
            ),
            'requires': {'puzzle': {'red': 1}, 'complete': {'blue': 1}},
        },
        'recipes': [
            {
                'resource_handles': {'groomed_nails': 1, 'veined_glass': 1, },
                'resource_types': {'hide': 1, },
                'locations': ['crimson_crockery'],
                'innovations': ['paint'],
                'crafting_process': [
                    (
                        'A <b>survivor who fought the Crimson Crocodile</b> '
                        'stress-dreams fractals of blood.'
                    ),
                    (
                        'Forgo sleep to shave nails down with a stone file '
                        'and mix with <b>Paint</b> until dark red.'
                    ),
                    (
                        'Pick an imagined fractal to birth at the '
                        '<b>Crimson Crockery</b>.'
                    ),
                ],
            },
        ],
    },
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
