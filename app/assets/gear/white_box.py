'''

    Gear from White Box expansions lives here.

'''

white_box_2024 = {
    'goblinsnarfer': {
        'expansion': 'gunborg',
        'name': 'Goblinsnarfer',
    },


}

white_box_2023 = {

    # helebore a frozen survivor
    'cold_face_dagger': {
        'name': 'Cold Face Dagger',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'hellebore',
        'speed': 2,
        'accuracy': 7,
        'strength': 0,
        'keywords': ['weapon', 'melee', 'dagger', 'ice', 'stone'],
        'rules': ['Melting 4'],
        'related_rules': ['melting_x'],
        'desc': (
            'If you are <b>Insulated</b>, your warm hands can better clutch '
            'the blade. This gains +1 speed.'
        ),
        'recipes': [
            {
                'endeavor_tokens': 1,
                'gear_handles': {'founding_stone': 1},
            },
        ],
    },

    # deathcrown inheritor aya
    'heartstop_arrows': {
        'name': 'Heartstop Arrows',
        'type': 'pattern',
        'expansion': 'death_crown_inheritor_aya',
        'speed': 1,
        'accuracy': 4,
        'strength': 9,
        'keywords': ['item', 'ammunition', 'arrow', 'fragile', 'other'],
        'rules': ['Ammo - Heartbow, Campaign Limit 5'],
        'desc': (
            'When you wound with this, the monster is knocked down.'
        ),
        'recipes': [
            {
                'resource_handles': [
                    {'leather': 2},
                    {'undying_heart': 1},
                    {'phoenix_eye': 1},
                ],
            },
        ],
    },
    'heartbow': {
        'name': 'Heartbow',
        'type': 'pattern',
        'expansion': 'death_crown_inheritor_aya',
        'speed': 2,
        'accuracy': 7,
        'strength': 7,
        'keywords': ['weapon', 'ranged', 'bow', 'two-handed', 'other'],
        'rules': ['Cumbersome', 'Range: 4'],
        'affinities': {'top': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 2}},
            'desc': (
                'If you have no non-red affinities, this loses '
                '<b>Cumbersome</b> and gains <b>Sharp</b>.'
            ),
        },
        'recipes': [
            {
                'resource_handles': [
                    {'perfect_bone': 2},
                    {'undying_heart': 1},
                    {'phoenix_whisker': 1},
                ],
            },
        ],
    },

    # lunar twilight knight
    'fish_of_abundance':  {
        'expansion': 'lunar_twilight_knight',
        'type': 'rare_gear',
        'name': 'Fish of Abundance',
        'keywords': ['item', 'consumable'],
        'desc': (
            'On <b>Arrival</b>, gain +1 luck token. Whenever you are knocked '
            'down, flip all your luck tokens.'
        ),
    },

    # Vitanvox
    'banshee_bedlah':  {
        'expansion': 'vitanvox',
        'beta': True,
        'type': 'beta_gear_recipe',
        'name': 'Banshee Bedlah',
        'armor': 1,
        'location': 'body',
        'keywords': ['armor', 'set', 'cloth', 'jewelry'],
        'rules': ['Banshee Dura 5'],
        'related_rules': ['banshee_dura_x'],
        'affinities': {'top': 'red', 'right': 'green', 'left': 'red'},
        'desc': (
            'Do not gain <font class="kdm_manager_font">M</font> '
            'or <font class="kdm_manager_font">A</font> at the start of your '
            'act. You cannot spend survival.'
        ),
        'recipes': [
            {
                'resource_handles':  {'scrap': 2},
                'resource_types': {'cloth': 2},
                'innovations': ['forbidden_dance'],
            },
        ],
    },
    'banshee_loincloth':  {
        'expansion': 'vitanvox',
        'beta': True,
        'type': 'beta_gear_recipe',
        'name': 'Banshee Loincloth',
        'armor': 1,
        'location': 'waist',
        'keywords': ['armor', 'set', 'cloth', 'jewelry'],
        'related_rules': ['banshee_dura_x'],
        'affinities': {'top': 'red', 'right': 'red', 'bottom': 'green'},
        'affinity_bonus': {
            'desc': (
                'Increase the effect of your <b>Banshee Dura</b> by 1 for '
                'every <font class="kd affinity_red_text" >&#9724; &#9724;'
                '</font> you have.'
            ),
            'requires': {'complete': {'green': 1},},
        },
        'recipes': [
            {
                'resource_handles':  {'perfect_organ': 1, 'leather': 1},
                'resource_types': {'cloth': 2},
                'innovations': ['forbidden_dance'],
            },
        ],
    },


    #gnostin
    'stonesmasher': {
        'expansion': 'gnostin_stonesmasher',
        'beta': True,
        'type': 'beta_gear_recipe',
        'name': 'Stonesmasher',
        'keywords': ['weapon', 'melee', 'club', 'heavy', 'bone'],
        'speed': 1,
        'accuracy': 6,
        'strength': 8,
        'rules': ['Savage', 'Demolish', 'Irreplaceable'],
        'affinities': {'top': 'green', 'bottom': 'green'},
        'desc': (
            'This gains +4 luck when attacking a knocked down monster.'
        ),
        'recipes': [
            {
                'resource_handles':  {
                    'large_flat_tooth': 2, 'legendary_horns': 1
                },
                'resource_types': {'bone': 2},
            },
        ],
    },

    #lolowen
    'lagomorph_kanabo': {
        'expansion': 'lolowen',
        'name': 'Lagomorph Kanabo',
        'type': 'seed_pattern',
        'pattern_id': 41,
        'keywords':  ['weapon', 'melee', 'club', 'heavy', 'bone', 'metal'],
        'rules': ['Surpass 5'],
        'related_rules': ['surpass_x', 'rush'],
        'speed': 3,
        'accuracy': 5,
        'strength': 3,
        'affinities': {'top': 'red', 'left': 'red'},
        'affinity_bonus': {
            'desc': (
                'When you <b>Rush</b> with this, double your wound attempt '
                'total on the first selected hit location.'
            ),
            'requires': {
                'puzzle': {'red': 1},
                'complete': {'red': 2},
            },
        },
        'recipes': [
            {
                'resource_types': {'bone': 1},
                'resource_handles': {'broken_lantern': 2},
                'innovations': ['scrap_smelting'],
                'crafting_process': [
                    (
                        'Sift through the settlement storage to find the '
                        'sturdiest femur bone.'
                    ),
                    (
                        'Hammer metal studs into the hardy bone using a '
                        '<b>club weapon</b>.'
                    ),
                    (
                        'Coat the studded bone with metal using '
                        '<b>Scrap Smelting</b> to create a vicious cudgel.'
                    ),
                ],
            },
        ],
    },

    # mist raikin armor
    'petrichor_stechhelm': {
        'name': 'Petrichor Stechhelm',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'mist_raikin_armor',
        'armor': 5,
        'location': 'head',
        'keywords': ['armor', 'set', 'metal'],
        'related_rules': ['charged_token'],
        'affinities': {'left': 'blue', 'bottom': 'green'},
        'affinity_bonus': {
            'desc':(
                'When you suffer damage from <b>Current X</b>, gain a '
                '<b>Charged</b> token.'
            ),
            'requires': {'puzzle': {'blue': 1}},
        },
        'recipes': [
            {'resource_handles': {'iron': 2}}
        ],
    },
    'petrichor_sleeves': {
        'name': 'Petrichor Sleeves',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'mist_raikin_armor',
        'armor': 5,
        'location': 'arms',
        'keywords': ['armor', 'set', 'fur', 'metal'],
        'related_rules': ['charged_token'],
        'affinities': {'left': 'green'},
        'affinity_bonus': {
            'desc':(
                '<font class="kdm_manager_font">M</font>'
                '<font class="kdm_manager_font">A</font>: '
                'Static Wash. If you have a metal weapon in your gear grid, '
                'gain a <b>Charged</b> token.'

            ),
            'requires': {'complete': {'red': 1, 'blue': 2}},
        },
        'recipes': [
            {'resource_handles': {'iron': 1, 'perfect_hide': 2}}
        ],
    },

}

white_box_2022 = {

    # badar
    'toxicimitar': {
        'name': 'Toxicimitar',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'badar',
        'keywords': ['weapon', 'melee', 'scimitar', 'other'],
        'rules': ['Sharp', 'Cleave'],
        'related_rules': ['sharp', 'cleave', 'sealed'],
        'sealed_gear': True,
        'speed': 2,
        'accuracy': 6,
        'strength': 2,
        'affinities': {'top': 'blue'},
        'desc': (
            'The blade is toxic. On <b>Arrival</b>, lose '
            '<font class="inline_shield">1</font> at all hit locations. '
            'When this wounds the monster the 3rd time, it gains a -1 movement '
            'and -1 evasion token.<br/>'
            '<b>Sealed</b> - gain the <b>Crescent Step</b> '
            '<span class="kd deck_icon" deck="SF">SF</span>'
        ),
        'recipes': [
            {
                'prefix_text':
                    '1x <b>Venom Sac</b> from a level 3 Spidicules',
                'resource_types': {'iron': 1, 'bone': 1},
            },
            {
                'prefix_text':
                    '1x <b>Organ</b> resource from a level 3 monster',
                'resource_handles': {'perfect_organ': 1},
                'resource_types': {'iron': 1, 'bone': 1},
            },
        ],
    },

    # novice
    'novice_dagger': {
        'name': 'Novice Dagger',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'novice',
        'speed': 3,
        'accuracy': 7,
        'strength': 1,
        'keywords': ['weapon', 'melee', 'dagger', 'bone'],
        'affinities': {'left': 'blue', 'right': 'red'},
        'desc': (
            'If you are a <b>Novice</b> when you critically wound '
            'with this, inflict 1 additional wound and gain a deflect '
            'token. Limit once per attack.'
        ),
        'recipes': [
            {
                'endeavor_tokens': 1,
                'resource_handles': {'perfect_bone': 1},
            },
        ],
    },

}

white_box_2019 = {

    #sword hunter
    'excalibur': {
        'name': 'Excalibur',
        'expansion': 'sword_hunter',
        'type': 'rare_gear',
        'speed': 2,
        'accuracy': 4,
        'strength': 4,
        'expansion': 'sword_hunter',
        'keywords': ['weapon', 'melee', 'sword', 'heavy', 'metal', 'other'],
        'rules': ['Savage', 'Unique'],
        'desc': (
            'When you die, you cease to exist (ignore death principle) and '
            'this gains +2 permanent strength (note this on the settlement '
            'record sheet).'
        ),
        'affinities': {'left': 'blue'},
    },

    # Halloween White Speaker 2019 - has a footnote on the card!
    'black_ghost_dagger': {
        'name': 'Black Ghost Dagger',
        'expansion': 'halloween_white_speaker_2019',
        'type': 'pattern',
        'pattern_id': -10,
        'keywords': ['weapon', 'melee', 'dagger', 'metal', 'other'],
        'affinities': {'top': 'blue', 'bottom': 'red'},
        'footnote': {
            'char': '1',
            'desc': (
                "This gains +10 strength when attacking a monster with 10+ "
                "toughness."
            ),
        },
        'speed': 3,
        'accuracy': 7,
        'strength': 2,
        'desc': 'Gains <b>Sharp</b> when attacking &#127875; monsters.',
        'affinity_bonus': {
            'desc': 'Gains <b>Deflect 1</b>',
            'requires': {
                'puzzle': {
                    'red': 1,
                    'blue': 1,
                },
            }
        },
        'recipes': [
            {
                'resource_handles': {
                    'dark_water': 3,
                    'iron': 2,
                },
                'crafting_process': [
                    (
                        'Boil <b>Nightmare Corn</b> in Dark Water over '
                        '<b>Heat</b> to create syrup infused with paranoia.'
                    ),
                    (
                        'Isolate a <b>survivor with +10 insanity</b> in a '
                        '<b>hovel</b> with the dagger. Their deranged '
                        'outbursts will chip the dagger, revealing its final '
                        'shape.'
                    ),
                    (
                        'A survivor with <b>Blotted Out consumes</b> the '
                        'syrup. Their inevitable regurgitation of of syrup '
                        'and fearful bile is used to patinate the weapon.'
                    ),
                ],
            },
        ],
    },

}

white_box_2018 = {

    # pinup devil satan halloween 2018
    'hope_stealer': {
        'expansion': 'pinup_devil_satan',
        'type': 'rare_gear',
        'name': 'Hope Stealer',
        'speed': 2,
        'accuracy': 6,
        'strength': 0,
        'keywords': ['weapon','melee','spear','two-handed','other'],
        'rules': ['Unique','Sentient','Reach 2'],
        'desc': (
            "At the end of the showdown, you die. Your settlement's death "
            "count is added to this weapon's strength."
        ),
        'recipes': [
            {
                'prefix_text': (
                    "If you're <b>insane</b> when you pull the <b>Adventure "
                    "Sword</b> from the grimacing stone face, you hear a "
                    "distant cackle.<br/>You're holding a much different "
                    "weapon!<br/> Gain the <b>Hope Stealer</b> instead. "
                    "<br/>(Hunt Event 85)"
                ),
            },
        ],
    },

    # white speaker 2018
    'bloodskin': {
        'expansion': 'white_speaker_2018',
        'type': 'rare_gear',
        'name': 'Bloodskin',
        'keywords': ['item','consumable','other'],
        'affinities': {'top': 'green','bottom': 'green'},
        'desc': (
            'When you <b>depart</b>, you fill the bloodskin and gain 2 '
            'bleeding tokens. At the start of each of each of your acts, '
            'remove 1 bleeding token.'
        ),
    },
    'speaker_cult_knife': {
        'expansion': 'white_speaker_2018',
        'type': 'rare_gear',
        'name': 'Speaker Cult Knife',
        'keywords': ['weapon','melee','steel','dagger','fist & tooth'],
        'speed': 3,
        'accuracy': 6,
        'strength': 4,
        'rules': ['Deadly','Sharp'],
        'affinities': {'top': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'desc': (
                'While <b>insane</b>, and not wearing armor or accessories, '
                'gain +2 evasion, +2 strength.'
            ),
            'requires': {'puzzle': {'red': 2}},
        },
    },

}

white_box_2017 = {

    # detective twilight knight
    'detective_cap': {
        'expansion': 'detective_twilight_knight',
        'type': 'promo',
        'name': 'Detective Cap',
        'armor':2,
        'location': 'head',
        'keywords': ['armor','accessory','other'],
        'affinities': {
            'left': 'red', 'top': 'blue', 'right': 'red', 'bottom': 'blue'
        },
        'desc': (
            'You must <b>investigate</b> if a choice to investigate arises. '
            'When you would roll to investigate, pick any result. If you are a '
            'returning survivor, you leave your hardboiled life behind and '
            'retire.'
        ),
    },
    'twilight_revolver': {
        'expansion': 'detective_twilight_knight',
        'type': 'promo',
        'name': 'Twilight Revolver',
        'speed': 1,
        'accuracy': 6,
        'strength': 10,
        'keywords': ['weapon','ranged','metal','finesse','other'],
        'affinities': {'left': 'red', 'right': 'blue'},
        'rules': ['Cursed', 'Sentient', 'Range 8'],
        'desc': (
            '<font class="kdm_font">c</font> <font class="kdm_font">a</font> '
            'and 1 survival: Make an attack using this weapon. This attack has '
            '<b>Range 3</b> and gains -2 Accuracy, +5 speed. Ignore <font '
            'class="kdm_font_10">e</font> <b>WOUND</b> for this attack. Limit, '
            'once per showdown.'
        ),
    },

}

white_box_2016 = {

    # allison the twilight knight
    'blue_lantern': {
        'expansion': 'allison_the_twilight_knight',
        'type': 'rare_gear',
        'name': 'Blue Lantern',
        'keywords': ['item', 'lantern', 'order', 'other'],
        'rules': ['Sentient', 'Cursed'],
        'desc': (
            '<font class="kdm_font">a</font>: Suffer 2d10 brain damage and '
            'reveal HL cards until you reveal the the trap. Put them back in '
            'the same order. Limit, once per showdown.'
        ),
    },
    'dormant_twilight_cloak': {
        'expansion': 'allison_the_twilight_knight',
        'type': 'rare_gear',
        'name': 'Dormant Twilight Cloak',
        'keywords': ['item','heavy','order','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'desc': (
            'Ignore <b>sentient</b> on all gear. You cannot <b>depart</b> with '
            'this if you have 3+ understanding.'
        ),
        'affinities': {'top': 'blue'},
        'location': 'head',
        'armor': 3,
    },

    # pinup wet nurse
    'nightmare_breast_pump': {
        'expansion': 'pinup_wet_nurse',
        'name': 'Nightmare Breast Pump',
        'affinities': {'top': 'blue'},
        'keywords': ['item','noisy','fragile','other'],
        'rules': ['Sentient','Irreplaceable','Female Only'],
        'desc': (
            "The pump mimics a baby's cries, stimulating your milk glands. As "
            "a returning survivor, gain +1 to your intimacy rolls this "
            "settlement phase."
        ),
    },

    # black friday ninja
    'black_friday_lantern': {
	'expansion': 'black_friday_ninja',
        'type': 'promo',
        'name': 'Black Friday Lantern',
        'desc': (
            'On <b>Arrival</b> (at the start of the showdown), you may archive '
            'this and ambush the monster. limit, once per campaign.'
        ),
        'keywords': ['item', 'lantern', 'other'],
        'rules': ['+1 Evasion'],
    },
}
