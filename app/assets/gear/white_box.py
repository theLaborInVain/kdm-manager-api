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

    #longclaw lenore
    'longclaw':{
        'name': 'Longclaw',
        'type': 'pattern',
        'expansion': 'longclaw_lenore',
        'speed': 3,
        'accuracy': 6,
        'strength': 3,
        'keywords': ['weapon', 'melee', 'bone', 'katar'],
        'rules': ['Reach 2', 'Deadly', 'Sharp'],
        'related_rules': ['reach_x', 'pounce'],
        'affinities': {'right': 'red', 'bottom': 'blue'},
        'affinity_bonus': {
            'desc': (
                'When you <b>Pounce</b> with this, cancel reactions '
                'on one <span class="kd deck_icon" deck="HL">HL</span> of your '
                'choice.'
            ),
            'requires': {'puzzle': {'red': 1,}, 'complete': {'blue': 1} },
        },
        'recipes': [
            {
                'resource_handles': {'overgrown_dewclaw': 1, 'iron': 2},
                'resource_types': {'bone': 2, 'hide': 2,},
                'innovations': ['nightmare_training'],
            },
        ],
    },
    'undying_lantern': {
        'name': 'Undying Lantern',
        'type': 'beta_gear_recipe',
        'expansion': 'longclaw_lenore',
        'beta': True,
        'keywords': ['item', 'lantern', 'other'],
        'related_rules': ['undeathable'],
        'desc': (
            'When you have the same name as the player controlling you, gain '
            '<b>Undeathable</b> during lantern years 1-7.'
        ),
        'recipes': [
            {
                'prefix_text': (
                    'Gain this the first time you name a survivor after '
                    'yourself. Limit once per campaign.'
                ),
            },
        ],
    },

    # dark of star
    'cenobite_leotard': {
        'name': 'Cenobite Leotard',
        'type': 'beta_gear_recipe',
        'expansion': 'dark_of_star',
        'beta': True,
        'armor': 2,
        'location': 'chest',
        'keywords': ['amor', 'leather', 'metal'],
        'affinities': {'top': 'blue'},
        'desc': 'Ignore the <b>frenzy</b> brain trauma.',
        'affinity_bonus': {
            'desc': (
                'On <b>Arrival</b>, gain a death token for each permanent '
                'injury you have recorded.'
            ),
            'requires': {'puzzle': {'blue': 1}, 'complete': {'red': 1}},
        },
        'recipes': [
            {
                'resource_handles': {'leather': 2},
                'resource_types': {'scrap': 1},
            }
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

    'sighing_acanthus_hat': {
        'name': 'Sighing Acanthus Hat',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'summer_cyrus',
        'keywords': ['herb', 'flammable'],
        'location': 'head',
        'armor': 1,
        'affinities': {'right': 'blue'},
        'rules': ['Accessory'],
        'affinity_bonus': {
            'desc': (
                'When you draw the trap, gain a reroll token. If wearing no '
                'armor, gain 2.'
            ),
            'requires': {
                'puzzle': {'blue': 1},
                'complete': {'red': 1},
            },
        },
        'recipes': [
            {
                'resource_handles': {
                    'fresh_acanthus': 2,
                    'black_lichen': 1,
                },
                'suffix_text':
                    '1 x <b>Sighing Bloom</b> or 1 x <b>Perfect Organ</b>',
            },
        ],
    },
    'acanthus_underwear': {
        'name': 'Acanthus Underwear',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'summer_cyrus',
        'keywords': ['underwear', 'herb', 'flammable'],
        'location': 'body',
        'aux_location': 'waist',
        'armor': 1,
        'affinities': {'right': 'green', 'left': 'blue'},
        'rules': ['Accessory'],
        'affinity_bonus': {
            'desc': (
                '+1 strength and +1 evasion for each reroll token you have.'
            ),
            'requires': {
                'puzzle': {'green': 1, 'blue': 1},
            },
        },
        'recipes': [
            {
                'endeavor_tokens': 1, 'resource_handles': {'fresh_acanthus': 1}
            },
        ],
    },
    'sighing_sarong': {
        'name': 'Sighing Sarong',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'summer_cyrus',
        'keywords': ['overwear', 'cloth'],
        'location': 'waist',
        'aux_location': 'legs',
        'armor': 2,
        'affinities': {'left': 'green'},
        'rules': ['Accessory'],
        'desc': 'On <b>Arrival</b>, gain a reroll token.',
        'recipes': [
            {
                'endeavor_tokens': 1,
                'resource_handles': {'fresh_acanthus': 1},
                'suffix_text':
                    '1 x <b>Sighing Bloom</b> or 1 x <b>Perfect Organ</b>',
            },
        ],
    },


    'survival_spear': {
        'name': 'Survival Spear',
        'beta': True,
        'type': 'beta_gear',
        'expansion': 'summer_aya',
        'keywords': ['weapon', 'melee', 'spear', 'two-handed'],
        'speed': 2,
        'accuracy': 6,
        'strength': 3,
        'affinities': {'top': 'red', 'right': 'red', 'left': 'green'},
        'rules': ['Reach 2', 'Unique'],
        'desc': (
            'This gains a +1 strength token after each time the wielder '
            'performs a survival action.'
        ),
        'affinity_bonus': {
            'desc': (
                'On <b>Arrival</b>, gain <span class="kd deck_icon" deck="SR">'
                'SR</span> <b>Fresh Kill</b>.'
            ),
            'requires': {
                'puzzle': {'red': 2, 'green': 1},
            },
        },
        'recipes': [
            {
                'prefix_text': (
                    'When you scavenge a <b>Survivor Corpse</b> and roll a '
                    '10+, gain the <b>Survival Spear</b> beta gear.<br/>'
                    'Limit, once per campaign.'
                ),
            },
        ],
    },


    # summer goth
    'blackstar_bikini': {
        'name': 'Blackstar Bikini',
        'type': 'seed_pattern',
        'pattern_id': -21,
        'expansion': 'summer_goth_twilight_knight',
        'armor': 2,
        'location': 'body',
        'aux_location': 'waist',
        'keywords': ['armor', 'seed', 'void fabric', 'other'],
        'rules': ['+1 Evasion'],
        'affinities': {'right': 'green', 'left': 'green'},
        'desc': (
            'When you are hit roll 1d10. On a 7+, you narrowly avoid it. '
            'Ignore the hit.'
        ),
        'recipes': [
            {
                'resource_handles': {
                    'leather': 1,
                    'perfect_hide': 1,
                    'cocoon_membrane': 1,
                },
                'events': ['oxidation'],
                'crafting_process': [
                    (
                        'During <font class="kdm_manager_font">S</font> '
                        '<b>Oxidation</b>, a survivor with <b>Analyze</b> '
                        'realizes the potential of the fabric.'
                    ),
                    (
                        'The survivor rubs the fabric on the smooth surface of '
                        'the <b>Final Lantern</b>.'
                    ),
                    (
                        'They press a finger to their eye and cut out the '
                        'delicate straps of a dizzying garment.'
                    ),
                ],
            },
        ],
    },
    'ghost_garters_arms': {
        'name': 'Ghost Garters - Arms',
        'type': 'seed_pattern',
        'pattern_id': 30,
        'expansion': 'summer_goth_twilight_knight',
        'armor': 1,
        'location': 'arms',
        'keywords': ['seed', 'void fabric', 'other'],
        'rules': ['Accessory'],
        'affinities': {'top': 'red', 'bottom': 'blue'},
        'desc': (
            'When you wound the monster add '
            '<font class="inline_shield">1</font> to all hit locations. '
            'Limit, once per round unless you are not wearing arm armor.'
        ),
        'recipes': [
            {
                'endeavors': 1,
                'resource_handles': {
                    'lantern_tube': 1,
                },
                'events': ['lantern_research'],
                'crafting_process': [
                    (
                        'During <font class="kdm_manager_font">S</font> '
                        '<b>Lantern Research</b>, an <b>insane</b> survivor '
                        'sees shadowy hands in the light.'
                    ),
                    (
                        'They chase the shadow from lantern to lantern, '
                        'trapping it in folds of void fabric.'
                    ),
                    (
                        'Survivors pull the cloth taut around the shadow '
                        'hands and cut, revealing gloves.'
                    ),
                ],
            },
        ],
    },
    'ghost_garters_legs': {
        'name': 'Ghost Garters - Legs',
        'type': 'seed_pattern',
        'pattern_id': 29,
        'expansion': 'summer_goth_twilight_knight',
        'armor': 1,
        'location': 'legs',
        'keywords': ['seed', 'void fabric', 'other'],
        'rules': ['Accessory'],
        'affinities': {'top': 'blue', 'bottom': 'red'},
        'desc': (
            'When you wound the monster you may remove a bleeding token. '
            'Limit, once per round unless you are not wearing leg armor.'
        ),
        'recipes': [
            {
                'resource_handles': {
                    'perfect_hide': 1,
                    'black_lichen': 1,
                },
                'locations': ['exhausted_lantern_hoard'],
                'crafting_process': [
                    (
                        'A <b>Secretive</b> survivor searches deep inside the '
                        '<b>Exhausted Lantern Hoard</b>.'
                    ),
                    (
                        'They wrap themselves in discarded pieces of black '
                        'fabric and drift off in darkness.'
                    ),
                    (
                        'Awake, a new sense of calm guides their steady hand '
                        'as they sew fabric stockings.'
                    ),
                ],
            },
        ],
    },

    'gloom_cowl': {
        'name': 'Gloom Cowl',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'reapokratis',
        'armor': 3,
        'location': 'head',
        'keywords': ['armor', 'gloomy', 'leather'],
        'add_affinity': ['blue', 'red'],
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1, 'blue': 1}},
            'desc': (
                'Your attacks gain +2 accuracy when attacking a monster you '
                'are adjacent to.'
            ),
        },
        'recipes': [
            {
                'resource_handles': {
                    'dark_water': 1,
                    'leather': 1,
                },
                'resource_types': {
                    'scrap': 1
                },
            },
            {
                'resource_handles': {
                    'perfect_organ': 1,
                    'leather': 1,
                },
                'resource_types': {
                    'scrap': 1
                },
            },
        ],
    },


    # erza of dedheim
    'ghostlink_pumpkin': {
        'name': 'Ghostlink Pumpkin',
        'type': 'seed_pattern',
        'pattern_id': 31,
        'expansion': 'erza_of_dedheim',
        'keywords': ['item', 'consumable'],
        'affinities': {'right': 'green', 'left': 'green'},
        'desc': (
            '<font class="kdm_manager_font">A</font> Consume: '
            'Suffer <b>frenzy</b> and become <b>doomed</b> until end of round. '
            'Convert all your attribute tokens to +1 strength tokens. '
            'Limit, once per showdown.'
        ),
        'recipes': [
            {
                'resource_handles': {
                    'black_lichen': 1,
                    'muculent_droppings': 1,
                },
                'innovations': ['graves'],
                'crafting_process': [
                    (
                        'A hungry survivor mixes droppings and lichen together '
                        'into a pungent slurry.'
                    ),
                    (
                        'It is not tasty. They abandon their creation atop '
                        'some <b>Graves</b> after a single bite.'
                    ),
                    (
                        'Harvest the plant that eventually sprouts from the '
                        'discarded meal with a <b>sickle</b>.'
                    ),
                ],
            },
        ],
    },
    'scythe_of_doom': {
        'name': 'Scythe of Doom',
        'type': 'seed_pattern',
        'pattern_id': 32,
        'expansion': 'erza_of_dedheim',
        'keywords': [
            'weapon', 'melee', 'scythe', 'grand', 'two-handed', 'other'
        ],
        'affinities': {'left': 'blue'},
        'speed': 2,
        'accuracy': 5,
        'strength': 13,
        'rules': ['Doombound', 'Devastating 2', 'Deadly', 'Sharp'],
        'desc': (
            '<b>Doombound:</b> When you become <b>doomed</b>, place a doom '
            'token on this. You must archive a doom token to activate this. '
        ),
        'recipes': [
            {
                'resource_handles': {
                    'iron': 3,
                    'leather': 1,
                },
                'resource_types': {'bone': 1},
                'locations': ['blacksmith'],
                'crafting_process': [
                    (
                        'A survivor returns from <b>Golden Ember</b> (Hunt '
                        'Event 73) with a skull.'
                    ),
                    (
                        'A <b>Possessed</b> survivor becomes jealous while '
                        'speaking with the long dead skull.'
                    ),
                    (
                        "They steal away the skull's golden ember, lodging "
                        "it into a <b>Blacksmith</b>'s prototype."
                    ),
                ],
            },
        ],
    },
    'robes_of_dedheim': {
        'name': 'Robes of Dedheim',
        'type': 'seed_pattern',
        'pattern_id': 33,
        'expansion': 'erza_of_dedheim',
        'armor': 2,
        'location': 'chest',
        'keywords': ['armor', 'rawhide', 'other'],
        'affinities': {'top': 'red', 'right': 'red'},
        'rules': ['Outfit'],
        'related_rules': ['doomed', 'outfit'],
        'desc': (
            'When you become <b>doomed</b>, before any actions are resolved, '
            'gain +1 evasion token.'
        ),
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 2}},
            'desc': '+2 speed',
        },
        'recipes': [
            {
                'resource_types': {'cloth': 1, 'hide': 1},
                'crafting_process': [
                    (
                        'The blackened sweat of a <b>Traumatized survivor</b> '
                        'permanently stains a cloth.'
                    ),
                    (
                        'A visiting <b>Bone Witch</b> binds the cloth to the '
                        'hide of a monster that died of fear.'
                    ),
                    (
                        'Survivor and bestial traumas blend to form a garb '
                        'suffused with nervous energy.'
                    ),
                ],
            },
        ],
    },

}



white_box_2020 = {

    # Halloween Ringtail Vixen 2020
    'vixen_tail': {
        'expansion': 'halloween_ringtail_vixen_2020',
        'name': 'Vixen Tail',
        'type': 'seed_pattern',
        'pattern_id': -12,
        'keywords': ['item','fur','flammable','other'],
        'affinities': {'bottom': 'green'},
        'desc': (
            'The bushy tail heightens your awareness. If you are insane, you '
            'cannot be <b>ambushed</b>.'
        ),
        'recipes': [
            {
                'resource_handles': {'crab_spider': 1, 'leather': 1},
                'resource_types': {'scrap': 1},
                'gear_handles': {'monster_grease': 1},
                'crafting_process': [
                    (
                        'Retrieve the fur baby blanket saved from '
                        '&#x1f516; <b>Infant Adrift</b>.'
                    ),
                    (
                        'Use a <b>Crab Spider</b> to eat vicious mites '
                        'that have burrowed in the fur blanket.'
                    ),
                    (
                        'Comb and fluff fur, then lightly oil with '
                        '<b>Monster Grease</b>.'
                    ),
                ],
            },
        ],
    },

    'brazen_bat': {
        'expansion': 'halloween_ringtail_vixen_2020',
        'name': 'Brazen Bat',
        'type': 'seed_pattern',
        'pattern_id': -11,
        'keywords': ['weapon','melee','club'],
        'speed': 2,
        'accuracy': 5,
        'strength': 6,
        'affinities': {'right': 'red'},
        'desc': (
            'Gains <b>Sharp</b> when attacking &#127875; monsters.<br/>'
            'If you are not wearing any head armor, you feel a spirit of '
            'rebellion! You may ignore the first '
            '<font class="kdm_font_10">e</font> during your first attack each '
            'round.'
        ),
        'recipes': [
            {
                'gear_handles': {'dried_acanthus': 1,},
                'resource_types': {'scrap': 1, 'bone': 2,},
                'crafting_process': [
                    (
                        'Create a lathe with spare bones. A survivor with '
                        '<b>Rhythm Chaser</b> cranks it.'
                    ),
                    (
                        'Use <b>Scrap Smelting</b> to heat lantern shards '
                        'and place in a pile.'
                    ),
                    (
                        'Crush Dried Acanthus and mix with urine to create a '
                        'sealant.'
                    ),
                ],
            },
        ],
    },

    # winter solstice lucy
    'grim_muffler': {
        'expansion': 'winter_solstice_lucy',
        'name': 'Grim Muffler',
        'type': 'seed_pattern',
        'pattern_id': -14,
        'keywords': ['item','cloth','fur','heavy'],
        'armor': 1,
        'location': 'chest',
        'affinities': {'right': 'blue'},
        'rules': ['Accessory'],
        'desc': (
            'One of your gear loses the noisy keyword, as you hide it in this '
            'cloak.'
        ),
        'affinity_bonus': {
            'requires': {'complete': {'blue': 1}},
            'desc': 'Ignore survival loss from cold hunt events.'
        },
        'recipes': [
            {
                'gear_handles': {'cloth': 1,},
                'resource_types': {'hide': 1, 'organ': 1},
                'crafting_process': [
                    (
                        'Harvest healthy tendons from a fresh <b>Organ</b> '
                        'obtained <b>last showdown</b>.'
                    ),
                    (
                        'Pluck hairs from <b>15 survivors</b>. One fidgets '
                        'too much, record <b>Bald</b> on their sheet.'
                    ),
                    (
                        "Plug a sleeping survivor's ears with hair and "
                        'scream to test sound suppression. '
                    ),
                ],
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

    #tenth anniversary survivors

    'teleric_eye_tac': {
        'name': 'Teleric Eye Tac',
        'pattern_id': -6,
        'type': 'seed_pattern',
        'expansion': 'tenth_anniversary_survivors',
        'keywords': ['item', 'jewelry', 'other'],
        'affinities': {'right': 'blue'},
        'desc': (
            '<font class="kdm_font">a</font>: Roll 3 hit location dice and '
            'note the results. The next time you are hit, use one of these '
            'results. (Discard the remaining noted results.)'
        ),
        'recipes': [
            {
                'gear_handles': {
                    'cat_eye_circlet':1,
                },
                'resource_handles': {
                    'golden_whiskers': 1,
                    'sinew': 1
                },
                'crafting_process': [
                    (
                        'Spin Circlet on <b>Lion Tail</b> until lens comes '
                        'free. Invert the lens and replace in Circlet.'
                    ),
                    (
                        'Melt Golden Whiskers with <b>Heat</b> to form focal '
                        'point beads to hang on back.'
                    ),
                    (
                        'Soak the work in <b>Ammonia</b> to provide rigidity '
                        'and give color.'
                    ),
                ],
            },
        ],
    },
    'tempered_spear': {
        'type': 'seed_pattern',
        'pattern_id': -3,
        'expansion': 'tenth_anniversary_survivors',
        'name': 'Tempered Spear',
        'speed': 2,
        'accuracy': 5,
        'strength': 5,
        'keywords': ['weapon','melee','spear','finesse','metal'],
        'rules': ['Reach 2'],
        'affinities': {
            'top': 'red',
            'right': 'blue',
            'bottom': 'red',
            'left': 'blue'
        },
        'affinity_bonus': {
            'desc': (
                'Add +1 to your Spear Specialization roll results with '
                'this weapon'
            ),
            'requires': {
                'puzzle': {'red': 2, 'blue': 2},
            },
        },
        'recipes': [
            {
                'gear_handles': {
                    'scrap_sword':1,
                },
                'resource_types': {
                    'bone': 2,
                },
                'resource_handles': {
                    'cloth': 1,
                    'leather': 1,
                },
                'crafting_process': [
                    (
                        'Drive a pointed bone into the tang of the Scrap '
                        'Sword, splintering it.'
                    ),
                    (
                        'Combine marrow and scrap into a steaming slurry '
                        'using <b>Scrap Smelting</b>. Beware of fumes.'
                    ),
                    (
                        'Use steaming slurry and <b>Bone Club</b> to reform '
                        'sword into a multi-pointed blade.'
                    ),
                ],
            },
        ],
    },
    'plated_shield': {
        'type': 'seed_pattern',
        'pattern_id': -2,
        'expansion': 'tenth_anniversary_survivors',
        'name': 'Plated Shield',
        'keywords': ['weapon', 'melee', 'shield', 'finesse', 'metal'],
        'speed': 1,
        'accuracy': 8,
        'strength': 3,
        'rules': ['Frail', 'Deflect 1'],
        'desc': '<b>Sharp</b> while you have any deflect tokens.',
        'recipes': [
            {
                'gear_handles': {
                    'monster_grease': 1,
                    'round_leather_shield': 1,
                },
                'resource_handles': {
                    'scrap': 3,
                },
                'crafting_process': [
                    (
                        'Compare blood pooling in a stone eye socket to blood '
                        'running off <b>Stone Noses</b>.'
                    ),
                    (
                        'Remove impact-absorbing material from a Round Leater '
                        'Shield.'
                    ),
                    (
                        'Polish spiral scrap plating with Monster Grease while '
                        'wearing <b>metal arm armor</b>.'
                    ),
                ],
            },
        ],
    },
    'tempered_axe': {
        'type': 'seed_pattern',
        'pattern_id': -4,
        'expansion': 'tenth_anniversary_survivors',
        'name': 'Tempered Axe',
        'keywords': ['weapon', 'melee', 'axe', 'finesse', 'metal'],
        'affinities': {'bottom': 'red'},
        'speed': 2,
        'accuracy': 6,
        'strength': 6,
        'rules': ['Paired'],
        'desc': (
            'When you use Axe Specialization, your second attempt to wound the '
            'selected hit location gains <b>Sharp</b>.'
        ),
        'recipes': [
            {
                'gear_handles': {
                    'bone_axe':1,
                },
                'resource_types': {
                    'bone': 1,
                },
                'resource_handles': {
                    'scrap': 1,
                    'leather': 1,
                },
                'crafting_process': [
                    (
                        'Hollow out Bone Axe by soaking in <b>Ammonia</b> and '
                        'scraping with bone tools. '
                    ),
                    (
                        'Combine marrow and scrap into a steaming slurry using '
                        '<b>Scrap Smelting</b>. Beware of fumes. '
                    ),
                    (
                        'Coat entire axe with steaming slurry and fill hollow '
                        'head with scrap for heft.'
                    ),
                ],
            },
        ],
    },
    'tempered_dagger': {
        'type': 'seed_pattern',
        'pattern_id': -5,
        'expansion': 'tenth_anniversary_survivors',
        'name': 'Tempered Dagger',
        'keywords': ['weapon', 'melee', 'dagger', 'finesse', 'metal'],
        'affinities': {'bottom': 'blue'},
        'speed': 3,
        'accuracy': 7,
        'strength': 4,
        'rules': ['Paired'],
        'desc': (
            'While using Dagger Specialization, you may discard all other '
            'drawn hit locations to gain that much luck for your second '
            'attempt to wound that hit location.'
        ),
        'recipes': [
            {
                'gear_handles': {
                    'scrap_dagger':1,
                },
                'resource_types': {
                    'bone': 1,
                },
                'resource_handles': {
                    'scrap': 1,
                    'leather': 1,
                },
                'crafting_process': [
                    (
                        'Consult a disgruntled aesthete complaining about '
                        'Scrap Dagger design.'
                    ),
                    (
                        'Combine marrow and scrap into a steaming slurry '
                        'using <b>Scrap Smelting</b>. Beware of fumes.'
                    ),
                    (
                        'Soften Scrap Dagger in slurry and fully reform. '
                        'Sharpen with <b>Founding Stone</b>.'
                    ),
                ],
            },
        ],
    },
    'vault_key_earrings': {
        'type': 'seed_pattern',
        'pattern_id': -1,
        'expansion': 'tenth_anniversary_survivors',
        'name': 'Vault Key Earrings',
        'keywords': ['item', 'jewelry', 'fragile'],
        'affinities': {'right': 'green'},
        'desc': (
            'While you have this in your gear grid, choose one of your '
            'disorders and ignore its effects.'
        ),
        'recipes': [
            {
                'resource_types': {
                    'bone': 1,
                },
                'resource_handles': {
                    'broken_lantern': 1,
                    'cyclops_fly': 1,
                },
                'crafting_process': [
                    (
                        'Consult with a survior that has <b>Fear of the '
                        "Dark</b> to understand the key's shape."
                    ),
                    (
                        '<b>Heat</b> and fold the Broken Lantern innards '
                        'to shape a key that unlocks the mind.'
                    ),
                    (
                        'Brush thin coats of Cyclops Fly paste with <b>fur '
                        'armor</b> bristles.'
                    ),
                ],
            },
        ],
    },

    # Halloween White Speaker 2019 - has a footnote on the card!
    'black_ghost_dagger': {
        'name': 'Black Ghost Dagger',
        'expansion': 'halloween_white_speaker_2019',
        'type': 'seed_pattern',
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
