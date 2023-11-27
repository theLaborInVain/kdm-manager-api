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

chorusseum = {
    'energy_drum': {
        'expansion': 'smog_singers',
        'name': 'Energy Drum',
        'keywords': ['item', 'instrument', 'noisy'],
        'affinities': {'left': 'blue'},
        'desc': (
            '<font class="kdm_manager_font">A</font>: Spend 1 survival to play '
            'this. An adjacent survivor gains '
            '<font class="kdm_manager_font">A</font>, which they must spend '
            'immediately. Limit once per round.'
        ),
        'recipes': [
            {
                'resource_handles': {'gaseous_belly': 1, 'vocal_chords': 1},
            },
        ],
    },
    'hamfluter': {
        'expansion': 'smog_singers',
        'name': 'Hamfluter',
        'keywords': ['weapon', 'melee', 'club', 'instrument', 'noisy'],
        'speed': 1,
        'accuracy': 6,
        'strength': 3,
        'affinities': {'top': 'red'},
        'desc': (
            '<b>Ballad of Perfection [7]:</b> Spend '
            '<font class="kdm_manager_font">A</font> and archive 7 cards from '
            'the wound stack to perform. All survivors increase their '
            '<b>Perfect hit</b> range by 1.'
        ),
        'affinity_bonus': {
            'desc': (
                'This whistles while you swing. Gain +1 survival and +1 '
                'insanity when you attack.'
            ),
            'requires': {'complete': {'red': 1, 'blue': 1},},
        },
        'recipes': [
            {
                'resource_handles': {'whistle_tooth': 1},
                'resource_types': {'bone': 1},
            },
        ],
    },
    'harpy_harp': {
        'expansion': 'smog_singers',
        'name': 'Harpy Harp',
        'keywords': ['item', 'instrument', 'noisy'],
        'affinities': {'bottom': 'red', 'left': 'green'},
        'desc': 'You ignore <b>Overwhelming Darkness</b>.',
        'affinity_bonus': {
            'desc': (
                'Your noisy weapons gain +1 strength for each instrument in '
                'your gear grid.'
            ),
            'requires': {'puzzle': {'red': 1, 'green': 1},},
        },
        'recipes': [
            {
                'resource_handles': {'singing_tongue': 1, 'whistle_tooth': 1},
                'resource_types': {'scrap': 1},
            },
        ],
    },
    'peace_dagger': {
        'expansion': 'smog_singers',
        'name': 'Peace Dagger',
        'keywords': ['weapon', 'melee', 'dagger', 'instrument', 'noisy'],
        'speed': 3,
        'accuracy': 6,
        'strength': 2,
        'affinities': {'top': 'blue', 'right': 'red', 'left': 'green'},
        'desc': (
            '<b>Ballad of Peace [3]:</b> Spend '
            '<font class="kdm_manager_font">A</font> and archive 3 cards from '
            'the wound stack to perform. '
            'In the <b>Aftermath</b>, if you did not attack this showdown, '
            'gain +1 <font class="kdm_manager_font">E</font>.'
        ),
        'recipes': [
            {
                'resource_handles': {'fluted_bone': 1, 'tail_fat': 1},
                'resource_types': {'hide': 1},
            },
        ],
    },
    'pipa': {
        'expansion': 'smog_singers',
        'name': 'Pipa',
        'keywords': ['weapon', 'melee', 'club', 'instrument', 'noisy'],
        'speed': 2,
        'accuracy': 6,
        'strength': 0,
        'affinities': {
            'top': 'red', 'right': 'red', 'botton': 'red', 'left': 'red'
        },
        'related_rules': ['savage'],
        'desc': (
            '<b>Ballad of Peace [6]:</b> Spend '
            '<font class="kdm_manager_font">A</font> and archive 6 cards from '
            'the wound stack to perform. '
            "All survivors weapons gain <b>savage</b>."
        ),
        'affinity_bonus': {
            'desc': '+4 strength',
            'requires': {'puzzle': {'red': 2},},
        },
        'recipes': [
            {
                'resource_handles': {'fluted_severed_head': 1, 'pink_flesh': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },
    'razor_cymbals': {
        'expansion': 'smog_singers',
        'name': 'Razor Cymbals',
        'keywords': ['weapon', 'melee', 'katar', 'instrument', 'noisy'],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'affinities': {'top': 'red', 'botton': 'blue',},
        'rules': ['Paired'],
        'related_rules': ['paired'],
        'desc': (
            'Make attack rolls one at a time. For each hit, the monster '
            'suffers -1 evasion until the end of this attack.'
        ),
        'recipes': [
            {
                'resource_handles': {'delicate_hand': 1},
                'resource_types': {'scrap': 1},
            },
        ],
    },
    'singing_heart': {
        'expansion': 'smog_singers',
        'name': 'Singing Heart',
        'keywords': ['item', 'lantern', 'instrument', 'noisy'],
        'affinities': {'left': 'paired'},
        'desc': (
            'The weapon to the left gains noisy and +1 accuracy.'
        ),
        'related_rules': ['dazed'],
        'affinity_bonus': {
            'desc': (
                'You may archive this to smash it, creating a vexing wave '
                'of white noise. Discard all moods in play. The monster is '
                '<b>dazed</b>.'
            ),
            'requires': {'complete': {'red': 1, 'blue': 1, 'green': 1},},
        },
        'recipes': [
            {
                'resource_handles': {'singing_tongue': 1},
                'resource_types': {'bone': 1, 'scrap': 1},
            },
        ],
    },
    'spear_of_life': {
        'expansion': 'smog_singers',
        'name': 'Spear of Life',
        'keywords': ['weapon', 'melee', 'spear', 'two-handed'],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'rules': ['Reach 2'],
        'related_rules': ['reach_x'],
        'affinities': {'left': 'green'},
        'affinity_bonus': {
            'desc': (
                'When another survivor dies from bleeding tokens, roll 1d10. '
                'On a 7+, your dart saves them! They suffer -1 permanent '
                'evasion and remove up to 3 bleeding tokens.'
            ),
            'requires': {'puzzle': {'green': 1},},
        },
        'recipes': [
            {
                'resource_handles': {'fluted_bone': 1, 'whistle_tooth': 1},
                'resource_types': {'hide': 1},
            },
        ],
    },
    'spinning_sword': {
        'expansion': 'smog_singers',
        'name': 'Spinning Sword',
        'keywords': ['weapon', 'melee', 'sword'],
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
        'affinities': {'right': 'green', 'left': 'green',},
        'rules': ['Paired'],
        'related_rules': ['paired'],
        'desc': (
            'Gain +2 evasion against ranged attacks for each of your spinning '
            'swords.'
        ),
        'recipes': [
            {
                'resource_handles': {'fluted_bone': 1},
                'resource_types': {'bone': 1},
            },
        ],
    },

    # armor
    'singing_boots': {
        'expansion': 'smog_singers',
        'name': 'Singing Boots',
        'keywords': ['armor', 'set', 'flesh'],
        'armor': 3,
        'location': 'legs',
        'affinities': {'top': 'green', 'left': 'blue'},
        'affinity_bonus': {
            'desc': (
                'At the end of your act, you may move up to 3 spaces away from '
                'the monster.'
            ),
            'requires': {'puzzle': {'green': 1}, 'complete': {'blue': 1},},
        },
        'recipes': [
            {
                'resource_handles': {'pink_flesh': 1},
                'resource_types': {'hide': 1},
            },
        ],
    },
    'singing_breastplate': {
        'expansion': 'smog_singers',
        'name': 'Singing Breastplate',
        'keywords': ['armor', 'set', 'flesh'],
        'armor': 3,
        'location': 'body',
        'affinities': {'top': 'blue', 'right': 'red'},
        'desc': (
            '<b>Hit Song:</b> spend '
            '<font class="kdm_manager_font">M</font>'
            '<font class="kdm_manager_font">A</font> to full move forward '
            'and attack. If you moved at least 4 spaces, the first time you '
            'wound during this attack, <b>encourage</b> all survivors.'
        ),
        'recipes': [
            {
                'resource_handles': {'pink_flesh': 1},
                'resource_types': {'bone': 1},
            },
        ],
    },
    'singing_cap': {
        'expansion': 'smog_singers',
        'name': 'Singing Cap',
        'keywords': ['armor', 'set', 'flesh'],
        'armor': 3,
        'location': 'head',
        'affinities': {'top': 'green', 'bottom': 'blue'},
        'affinity_bonus': {
            'desc': (
                'When you are attacked and suffer more than 1 hit, ignore '
                '1 hit.'
            ),
            'requires': {'puzzle': {'green': 1, 'blue': 1}, },
        },
        'recipes': [
            {
                'resource_handles': {'gaseous_belly': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },
    'singing_gloves': {
        'expansion': 'smog_singers',
        'name': 'Singing Gloves',
        'keywords': ['armor', 'set', 'flesh'],
        'armor': 3,
        'location': 'arms',
        'affinities': {'left': 'green', 'right': 'blue'},
        'desc': 'Reduce the cost of perfoming your Ballads by 1.',
        'recipes': [
            {
                'resource_handles': {'delicate_hand': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },
    'singing_pantaloons': {
        'expansion': 'smog_singers',
        'name': 'Singing Pantaloons',
        'keywords': ['armor', 'set', 'flesh'],
        'armor': 3,
        'location': 'waist',
        'affinities': {'bottom': 'green'},
        'recipes': [
            {
                'resource_handles': {'pink_flesh': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },

}

smog_singer_pattern_gear = {
    'saxe': {
        'expansion': 'smog_singers',
        'type': 'pattern',
        'name': 'Saxe',
        'keywords': [
            'weapon', 'melee', 'axe', 'bone', 'metal', 'instrument', 'noisy'
        ],
        'speed': 2,
        'accuracy': 7,
        'strength': 8,
        'affinities': {'left': 'red',},
        'desc': (
            '<b>Ballad of Blues [8]:</b> Spend '
            '<font class="kdm_manager_font">A</font> and archive 8 cards from '
            'the wound stack to perform. '
            'The monster and all survivors shed a tear. Archive all moods in '
            'play.'
        ),
        'recipes': [
            {
                'resource_handles': {'crystallized_song': 1},
                'resource_types': {'bone': 2, 'organ': 1},
            },
        ],
    },
    'drum_of_hope': {
        'expansion': 'smog_singers',
        'type': 'pattern',
        'name': 'Drum of Hope',
        'keywords': [
            'weapon', 'melee', 'club', 'axe', 'bone', 'instrument', 'noisy'
        ],
        'speed': 1,
        'accuracy': 6,
        'strength': 9,
        'affinities': {'top': 'red', 'right': 'red', 'bottom': 'red'},
        'rules': ['Slow'],
        'related_rules': ['slow'],
        'desc': (
            '<b>Ballad of Smash [6]:</b> Spend '
            '<font class="kdm_manager_font">A</font> and archive 6 cards from '
            'the wound stack to perform.'
            'All <font class="kdm_manager_font">R</font> Wound become '
            '<font class="kdm_manager_font">R</font> Failure. End this ballad '
            'at the end of the round if you fail to hit with this weapon.'
        ),
        'recipes': [
            {
                'resource_handles': {'belly_steel': 1},
                'resource_types': {'perfect': 1, 'bone': 1},
            },
        ],
    },
    'Discordian': {
        'expansion': 'smog_singers',
        'type': 'pattern',
        'name': 'Discordian',
        'keywords': [
            'weapon', 'melee', 'sword', 'metal', 'instrument', 'noisy'
        ],
        'speed': 1,
        'accuracy': 6,
        'strength': 9,
        'affinities': {'right': 'red', 'left': 'green',},
        'rules': ['Unwieldy', 'Sharp'],
        'related_rules': ['sharp', 'unwieldy', 'finesse', 'deflect_x'],
        'desc': (
            '<b>Ballad of Swordpolka [5]:</b> Spend '
            '<font class="kdm_manager_font">A</font> and archive 5 cards from '
            'the wound stack to perform.'
            "All survivors' swords gain finesse and <b>Deflect 1</b>. If "
            'they already have <b>Deflect</b>, increase it by 1.'
        ),
        'recipes': [
            {
                'resource_handles': {'foreskin_hood': 1},
                'resource_types': {'hide': 1, 'bone': 2},
            },
        ],
    },
    'curse_hammer': {
        'expansion': 'smog_singers',
        'type': 'pattern',
        'name': 'Curse Hammer',
        'keywords': [
            'weapon', 'melee', 'grand', 'club', 'instrument', 'heavy', 'noisy'
        ],
        'speed': 2,
        'accuracy': 7,
        'strength': 12,
        'affinities': {'top': 'blue', },
        'desc': 'When you wound with this, gain -1 strength token.',
        'affinity_bonus': {
            'desc': (
                '<b>Ballad of Inversion [7]:</b> Spend '
                '<font class="kdm_manager_font">A</font> and archive 7 cards '
                'from the wound stack to perform.'
                'Flip all your negative attribute tokens.'
            ),
            'requires': {'complete': {'blue': 1}, 'puzzle': {'blue': 1}, },
        },
        'recipes': [
            {
                'resource_handles': {'fused_feet': 1},
                'resource_types': {'organ': 2, 'bone': 1},
            },
        ],
    },

    # seed
    'hushing_harmonium': {
        'expansion': 'smog_singers',
        'type': 'seed_pattern',
        'name': 'Hushing Harmonium',
        'pattern_id': 15,
        'keywords': ['seed', 'weapon', 'melee', 'instrument', 'metal', 'other'],
        'affinities': {'right': 'green', 'bottom': 'green'},
        'speed': 1,
        'accuracy': 7,
        'strength': 0,
        'related_rules': ['hushed'],
        'desc': (
            '<b>Ballad of Silence [12]:</b> Spend '
            '<font class="kdm_manager_font">A</font> and archive 12 cards from '
            'the wound stack to perform. All other survivors are <b>hushed</b> '
            'and are not threats.'
        ),
        'recipes': [
            {
                'resource_handles': {
                    'singing_tongue': 1,
                    'broken_lantern': 1,
                    'vocal_chords': 1,
                },
                'innovations': ['drums'],
                'crafting_process': [
                    (
                        'A <b>survivor who fought the Smog Singers</b> '
                        'seeks emotional relief through silence.'
                    ),
                    (
                        'They play <b>Drums</b> until they discover one sound '
                        'that crushes all others.'
                    ),
                    (
                        'They play until <b>deaf</b>, scrunching and pushing '
                        'the sound into a metal cage.'
                    ),
                ],
            },
        ],
    },
}

smog_singers_rare_gear =  {
    'smog_lantern': {
        'expansion': 'smog_singers',
        'name': 'Smog Lantern',
        'type': 'rare_gear',
        'keywords': ['item', 'lantern'],
        'rules': ['Vital'],
        'related_rules': ['vital'],
        'affinities': {
            'top': 'green',
            'right': 'green',
            'bottom': 'green',
            'left': 'green'
        },
        'desc': (
            'A cherished keepsake from your friends in the sky. You will never '
            'forget them.'
        ),
    },

}
