'''
    Expansions of Death 1 gear definitions live in this file.

'''

#
#   Dung Beetle Knight
#

black_harvest = {
    'calcified_digging_claw': {
        'expansion': 'dung_beetle_knight',
        'name': 'Calcified Digging Claw',
        'affinities': {'left': 'green'},
        'speed': 1,
        'accuracy': 4,
        'strength': 5,
        'keywords': ['weapon', 'melee', 'katar', 'pickaxe'],
        'rules': ['Paired', 'Sharp'],
        'desc': (
            'During the <b>Mineral Gathering</b> story event, you may reroll '
            'one of your d10.'
        ),
    },
    'calcified_greaves': {
        'expansion': 'dung_beetle_knight',
        'name': 'Calcified Greaves',
        'keywords': ['item', 'bone', 'heavy'],
        'affinities': {'left': 'green'},
        'desc': (
            '-1 movement. Add <font class="inline_shield">3</font> to all '
            'hit locations.'
        ),
        'affinity_bonus': {
            'requires': {'puzzle': {'green': 1}, 'complete': {'blue': 1}},
            'desc': 'Add +2 to <b>Ripple Pattern</b> roll results.',
        },
    },
    'calcified_shoulder_pads': {
        'expansion': 'dung_beetle_knight',
        'name': 'Calcified Shoulder Pads',
        'keywords': ['item', 'bone', 'heavy'],
        'affinities': {'right': 'green'},
        'desc': (
            'Add <font class="inline_shield">3</font> to all hit locations.'
        ),
        'affinity_bonus': {
            'requires': {'puzzle': {'green': 1}, 'complete': {'green': 1}},
            'desc': (
                '<b>Ripple Pattern:</b> When you are attacked, roll 1d10. On a '
                '10+, ignore 1 hit.'
            ),
        },
    },
    'calcified_zanbato': {
        'expansion': 'dung_beetle_knight',
        'name': 'Calcified Zanbato',
        'keywords': ['weapon','melee','grand','two-handed','bone','heavy'],
        'rules': ['Slow','Deadly'],
        'speed': 1,
        'accuracy': 5,
        'strength': 8,
        'affinities': {'top': 'red', 'right': 'green'},
        'affinity_bonus': {
            'desc': (
                'Gains <b>Devastating 1:</b> Whenever you wound, inflict 1 '
                'additional wound.'
            ),
            'requires': {
                'puzzle': {'red': 1},
                'complete': {'green': 1},
            },
        },
    },
}

wet_resin_crafter = {
    'century_greaves': {
        'expansion': 'dung_beetle_knight',
        'name': 'Century Greaves',
        'keywords': ['item', 'bone', 'mineral', 'heavy'],
        'affinities': {'left': 'green'},
        'desc': (
            '-1 movement. Add <font class="inline_shield">1</font> to all hit '
            'locations.'
        ),
        'affinity_bonus': {
            'requires': {'puzzle': {'green': 1}, 'complete': {'blue': 1}},
            'desc': 'Add +1 to <b>Ripple Pattern</b> roll results.',
        },
    },
    'century_shoulder_pads': {
        'expansion': 'dung_beetle_knight',
        'name': 'Century Shoulder Pads',
        'keywords': ['item', 'bone', 'mineral', 'heavy'],
        'affinities': {'right': 'green'},
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
        ),
        'affinity_bonus': {
            'requires': {'puzzle': {'green': 1}, 'complete': {'green': 1}},
            'desc': (
                '<b>Ripple Pattern:</b> When you are attacked, roll 1d10. On a '
                '10+, ignore 1 hit.'
            ),
        },
    },
    'dbk_errant_badge': {
        'expansion': 'dung_beetle_knight',
        'name': 'DBK Errant Badge',
        'keywords': ['item', 'jewelry', 'knight'],
        'rules': ['Unique'],
        'affinities': {'right': 'red'},
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations. At '
            'the start of the showdown, draw 1 tactics card.'
        ),
    },
    'digging_claw': {
        'expansion': 'dung_beetle_knight',
        'name': 'Digging Claw',
        'speed': 1,
        'accuracy': 4,
        'strength': 5,
        'keywords': ['weapon', 'melee', 'katar', 'pickaxe', 'bone', 'mineral'],
        'rules': ['Paired'],
        'affinities': {'right': 'green'},
        'desc': (
            'During the <b>Mineral Gathering</b> story event, you may reroll '
            'one of your d10.'
        ),
    },
    'rainbow_wing_belt': {
        'expansion': 'dung_beetle_knight',
        'name': 'Rainbow Wing Belt',
        'keywords': ['item', 'flammable'],
        'affinities': {'top': 'red', 'right': 'green', 'bottom': 'blue'},
        'affinity_bonus': {
            'requires': {'complete': {'red': 2, 'blue': 1, 'green': 1}},
            'desc': (
                'When any of your attack rolls are 1, you may reroll them. '
                'Limit, once per attack.'
            ),
        },
    },
    'rolling_armor_set': {
        'expansion': 'dung_beetle_knight',
        'name': 'Rolling Armor Set',
    },
    'rubber_bone_harness': {
        'expansion': 'dung_beetle_knight',
        'name': 'Rubber Bone Harness',
        'keywords': ['item', 'bone', 'leather'],
        'affinities': {
            'top': 'red', 'right': 'green', 'bottom': 'blue', 'left': 'green',
        },
        'desc': (
            'Once per showdown, you may convert all of your negative attribute '
            'tokens to positive attribute tokens of the same type.'
        ),
    },
    'scarab_circlet': {
        'expansion': 'dung_beetle_knight',
        'name': 'Scarab Circlet',
        'keywords': ['item', 'bone', 'jewelry', 'other'],
        'affinities': {'top': 'blue', 'bottom': 'blue'},
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations. '
            'During the showdown, when your survival is reduced to 0, gain '
            '+1 strength token.'
        ),
    },
    'seasoned_monster_meat': {
        'expansion': 'dung_beetle_knight',
        'name': 'Seasoned Monster Meat',
        'keywords': ['item', 'consumable'],
        'affinities': {'top': 'green', 'right': 'red'},
        'desc': 'When you <b>depart</b>, gain +3 survival.',
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1}},
            'desc': (
                '<b><font class="kdm_manager_font">A</font> Consume:</b> '
                'Gain +3 survival and +1 strength token. Limit, once per '
                'showdown.'
            ),
        },
    },
    'the_beetle_bomb': {
        'expansion': 'dung_beetle_knight',
        'name': 'The Beetle Bomb',
        'affinities': {'top': 'blue', 'bottom': 'red'},
        'keywords': ['item', 'thrown', 'fragile'],
        'rules': ['Unique'],
        'desc': (
            '<font class="kdm_manager_font">A</font><b>:</b> If adjacent to '
            'the monster, roll 1d10. On a 6+, the monster gains -1 accuracy '
            'and -1 evasion tokens. Limit, once per showdown.'
        ),
    },
}


dbk_rare_gear = {
    'calcified_juggernaut_blade': {
        'expansion': 'dung_beetle_knight',
        'type': 'rare_gear',
        'name': 'Calcified Juggernaut Blade',
        'keywords': ['weapon', 'melee', 'grand', 'bone', 'other'],
        'speed': 1,
        'accuracy': 5,
        'strength': 9,
        'affinities': {'right': 'red', 'left': 'red'},
        'rules': ['Slow', 'Block 1'],
        'desc': 'This weapon gains +1 strength for each token you have.',
    },
    'hidden_crimson_jewel': {
        'expansion': 'dung_beetle_knight',
        'type': 'rare_gear',
        'name': 'Hidden Crimson Jewel',
        'keywords': ['item', 'jewelry', 'other'],
        'rules': ['Unique', 'Irreplaceable'],
        'affinities': {
            'top': 'red', 'right': 'red', 'bottom': 'red', 'left': 'red',
        },
        'desc': 'Once per game phase, you may reroll one d10.',
    },
    'regenerating_blade': {
        'expansion': 'dung_beetle_knight',
        'type': 'rare_gear',
        'name': 'Regenerating Blade',
        'keywords': ['item', 'mineral', 'other'],
        'affinities': {'left': 'green', 'right': 'blue'},
        'desc': (
            'During the Settlement Phase, you may archive this to remove the '
            '<b>Dismembered Arm</b> or <b>Dismembered Leg</b> permanent injury '
            'from one survivor.'
        ),
    },
    'trash_crown': {
        'expansion': 'dung_beetle_knight',
        'type': 'rare_gear',
        'name': 'Trash Crown',
        'armor': 4,
        'location': 'head',
        'keywords': ['item', 'jewelry', 'fragile', 'other'],
        'affinities': {'left': 'blue', 'bottom': 'red'},
        'desc': (
            '<b><font class="kdm_manager_font">A</font>:</b> Reveal the next 4 '
            'hit location cards and discard 3 that are not <b>traps</b>. Place '
            'remaining cards on top of the deck in any order.'
        ),
    },
}



#
#   Dragon King
#

dragon_king = {
    'blast_shield': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Blast Shield',
        'speed': 1,
        'accuracy': 7,
        'strength': 4,
        'keywords': ['weapon','melee','shield','metal'],
        'rules': ['Block 1'],
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
            '<br/><b>Block 1</b>. The first time you block a hit each '
            'showdown, gain the priority target token.'
        ),
    },
    'blast_sword': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Blast Sword',
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'keywords': ['weapon','melee','sword','bone'],
        'rules': ['Block 1'],
        'desc': (
            'When you spend <font class="kdm_font">a</font> to block with this '
            'weapon, gain +1 survival.'
        ),
        'affinities': {'bottom': 'red', 'top': 'green'},
    },
    'blue_power_core': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Blue Power Core',
        'keywords': ['item','jewelry'],
        'desc': 'All nuclear gear cards in your gear grid gain <b>Deadly 2</b>.'
    },
    'celestial_spear': {
        'expansion': 'dragon_king',
        'type': 'rare_gear',
        'name': 'Celestial Spear',
        'affinities': {'top': 'blue'},
        'speed': 2,
        'accuracy': 5,
        'strength': 4,
        'keywords': ['weapon','melee','spear','metal'],
        'rules': ['Reach 2'],
        'desc': (
            'Gain +5 strength when attacking with this weapon if you have a '
            '<b>constellation</b>.'
        ),
    },
    'dragon_armor_set': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Dragon Armor Set',
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
            '<br/><b>Charge:</b> Spend <font class="kdm_font">c a</font>. You '
            'leap into the air! Place your survivor on an unoccupied space '
            'exactly five spaces away in a straight line, then activate a '
            'melee weapon and attack with +2 accuracy and +5 strength.'
        ),
    },
    'dragon_belt': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Dragon Belt',
        'armor': 4,
        'location': 'waist',
        'keywords': ['armor', 'set', 'metal'],
        'affinities': {'left': 'red', 'bottom': 'blue'},
        'affinity_bonus': {
            'desc': (
                'You are not knocked down from suffering a heavy injury.'
            ),
            'requires': {
                'puzzle': {'blue': 1, 'red': 1},
            },
        },
    },
    'dragon_bite_bolt': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Dragon Bite Bolt',
        'keywords': ['item', 'ammunition', 'arrow'],
        'speed': 1,
        'accuracy': 6,
        'strength': 6,
        'rules': ['Slow', 'Ammo - Bow', 'Devastating 1'],
        'desc': (
            'If you wound the monster, it suffers <b>knockback 5</b>. Use '
            'once per showdown.'
        ),
    },
    'dragon_boots': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Dragon Boots',
        'armor': 4,
        'location': 'legs',
        'keywords': ['armor', 'set', 'metal'],
        'desc': 'Gain +2 movement during your act.',
        'affinities': {'top': 'green', 'right': 'red'},
    },
    'dragon_chakram': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Dragon Chakram',
        'keywords': ['weapon', 'ranged', 'thrown', 'bone'],
        'speed': 2,
        'accuracy': 6,
        'strength': 3,
        'rules': ['Range: 3'],
        'desc': (
            'If you hit, the monster gains -1 evasion until the end of the '
            'round. Limit, once per attack.'
        ),
    },
    'dragon_gloves': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Dragon Gloves',
        'affinities': {'top': 'blue', 'right': 'green'},
        'armor': 4,
        'location': 'arms',
    },
    'dragon_mantle': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Dragon Mantle',
        'armor': 4,
        'location': 'body',
        'keywords': ['armor','set','metal'],
        'affinities': {
            'top': 'red', 'right': 'blue', 'bottom': 'green', 'left': 'green'
        },
        'affinity_bonus': {
            'desc': (
                'At the start of the showdown, you beat your chest mightily '
                'and gain survival up to the survival limit.'
            ),
            'requires': {
                'puzzle': {'red': 1, 'blue': 1, 'green': 2},
            },
        },
    },
    'dragon_vestments': {
        'expansion': 'dragon_king',
        'type': 'rare_gear',
        'name': 'Dragon Vestments',
        'keywords': ['item','silk','other'],
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
            '<br/>When you gain a random fighting art, select a Dragon '
            'Trait one instead.'
        ),
    },
    'dragonskull_helm': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Dragonskull Helm',
        'armor': 4,
        'location': 'head',
        'keywords': ['armor', 'set', 'bone', 'metal'],
        'affinities': {'right': 'red', 'left': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'desc': (
                'Gain +1 to all severe <font class="kdm_font_2">b</font> '
                'injury roll results. Ignore <b>shattered jaw</b> severe '
                '<font class="kdm_font_2">b</font> injury result. '
            ),
            'requires': {
                'puzzle': {'red': 2}
            },
        },
    },
    'hazmat_shield': {
        'expansion': 'dragon_king',
        'type': 'rare_gear',
        'name': 'Hazmat Shield',
        'keywords': ['weapon', 'melee', 'shield', 'metal', 'heavy'],
        'speed': 2,
        'accuracy': 4,
        'strength': 7,
        'rules': ['Block 2'],
        'desc': (
            'Add <font class="inline_shield">2</font> to all hit locations. '
            'When the monster performs <b>Unseen Agony</b> or <b>Meltdown</b>, '
            'roll 1d10. On a 2+, you suffer no damage.'
        ),
    },
    'husk_of_destiny': {
        'expansion': 'dragon_king',
        'type': 'rare_gear',
        'name': 'Husk of Destiny',
        'desc': 'Your destiny is fulfilled. You are always <b>Insane</b>.',
        'keywords': ['item','other'],
        'rules': ['Cursed'],
    },
    'nuclear_knife': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Nuclear Knife',
        'keywords': ['weapon', 'melee', 'dagger', 'nuclear'],
        'speed': 3,
        'accuracy': 6,
        'strength': 3,
        'affinities': {
            'top': 'blue', 'right': 'red', 'bottom': 'green', 'left': 'blue',
        },
        'affinity_bonus': {
            'desc': (
                '<font class="kdm_font">a</font>: Edge ignites! Suffer 3 '
                'brain damage. Your next attack with this weapon gains '
                '<b>devastating 1</b>. Limit, once per round.'
            ),
            'requires': {
                'puzzle': {'green': 1, 'red': 1, 'blue': 1},
            },
        },
    },
    'nuclear_scythe': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Nuclear Scythe',
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'affinities': {'top': 'red', 'left': 'blue', 'bottom': 'red'},
        'keywords': ['weapon', 'melee', 'scythe', 'two-handed', 'nuclear'],
        'rules': ['Reach 2'],
        'affinity_bonus': {
            'desc': (
                '<font class="kdm_font">a</font>: Edge ignites! Suffer 3 '
                'brain damage. Your next attack with this weapon gains '
                '<b>devastating 1</b>. Limit, once per round.'
            ),
            'requires': {
                'puzzle': {'red': 2, 'blue': 1},
            },
        },
    },
    'red_power_core': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Red Power Core',
        'keywords': ['item','jewelry'],
        'desc': 'All nuclear gear cards in your gear grid gain <b>Sharp</b>.',
    },
    'regal_edge': {
        'expansion': 'dragon_king',
        'type': 'rare_gear',
        'name': 'Regal Edge',
        'keywords': ['weapon','melee','sword','metal'],
        'affinities': {'top': 'green', 'left': 'red'},
        'rules': ['Sharp'],
        'speed': 1,
        'accuracy': 5,
        'strength': 2,
        'desc': (
            'Gain +1 speed and +4 strength when attacking with this '
            'weapon if you have a <b>Constellation</b>.'
        ),
    },
    'shielded_quiver': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Shielded Quiver',
        'keywords': ['item','leather'],
        'desc': (
            'You may activate and gain the benefits of each arrow gear in '
            'your grid one additional time each showdown.'
        ),
    },
    'talon_knife': {
        'expansion': 'dragon_king',
        'type': 'dragon_armory',
        'name': 'Talon Knife',
        'keywords': ['weapon','melee','katar','bone'],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'affinities': {'top': 'blue','left': 'blue'},
        'rules': ['Paired'],
        'desc': (
            'If all of your attack rolls hit, gain <b>Savage</b> and '
            '<b>Deadly</b> until the end of your attack.'
        ),
    },
}


#
#   Green Knight
#

green_knight_armor_gear = {
    'fetorsaurus': {
        'expansion': 'green_knight_armor',
        'name': 'Fetorsaurus',
        'keywords': ['weapon','set','melee','shield','metal'],
        'rules': ['Block 2'],
        'desc': (
            'Add <font class="inline_shield">2</font> to all hit locations.'
            '<br/>While you carry this, reduce &#9733; by 1.'
        ),
        'recipes': [
            {
                'locations': ['blacksmith'],
                'gear_handles': {
                    'beacon_shield': 1,
                    'sleeping_virus_flower': 1,
                    'life_elixir': 1
                },
                'resource_handles': {'underplate_fungus': 1,},
            },
        ],
        'speed': 2,
        'accuracy': 5,
        'strength': 9,
        'affinities': {
            'left': 'blue',
            'bottom': 'green',
        },
    },
    'green_boots': {
        'expansion': 'green_knight_armor',
        'name': 'Green Boots',
        'armor': 5,
        'location': 'legs',
        'keywords': ['armor','set','bone','heavy','metal'],
        'desc': 'You may use the <b>Tumble</b> fighting art.',
        'affinities': {
            'top': 'green',
            'left': 'green',
        },
        'affinity_bonus': {
            'desc': 'You successfully tumble on 2+ instead of 6+.',
            'requires': {'puzzle': {'green': 2}, },
        },
        'recipes': [
            {
                'innovations': ['forbidden_dance'],
                'resource_types': {'bone': 3},
                'resource_handles': {'iron': 1},
                'gear_handles': {'flower_knight_badge': 1, 'calcified_greaves': 1},
            },
        ],
    },
    'green_faulds': {
        'expansion': 'green_knight_armor',
        'name': 'Green Faulds',
        'armor': 5,
        'location': 'waist',
        'keywords': ['armor','set','metal','other'],
        'desc': '+1 Evasion.',
        'affinities': {'top': 'blue', 'right': 'green'},
        'affinity_bonus': {
            'desc': 'After drawing hit locations from an attack, you may discard 1 First Strike hit location card.',
            'requires': {'puzzle': {'blue': 1, 'green': 1}, },
        },
        'recipes': [
            {
                'innovations': ['choreia'],
                'resource_handles': {'lantern_bloom': 1, 'elytra': 1, 'gormite': 1, 'scell': 1},
            },
        ],
    },
    'green_gloves': {
        'expansion': 'green_knight_armor',
        'name': 'Green Gloves',
        'armor': 5,
        'location': 'arms',
        'keywords': ['armor','set','metal'],
        'desc': '+2 Strength.',
        'affinities': {'right': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'desc': '+6 Luck when attempting to wound <b>Parry</b> hit locations.',
            'requires': {
                'puzzle': {'red': 2},
            },
        },
        'recipes': [
            {
                'innovations': ['scrap_smelting','albedo'],
                'gear_handles': {'hunters_heart': 1},
                'resource_handles': {'iron': 1, 'jiggling_lard': 1},
            },
        ],
    },
    'green_helm': {
        'expansion': 'green_knight_armor',
        'name': 'Green Helm',
        'armor': 5,
        'location': 'head',
        'keywords': ['armor','set','bone','metal'],
        'affinities': {'left': 'red', 'bottom': 'green'},
        'desc': '+1 Luck.<br/>When a monster attacks you, you may elect to take a hit on the head and roll 1d10. On a 6+, ignore the hit. If adjacent, it suffers 1 wound.',
        'recipes': [
            {
                'misc': "Old Master on the settlement's Quarry List.",
                'resource_handles': {'scell': 1, 'beetle_horn': 1, },
                'gear_handles': {'dbk_errant_badge': 1},
            },
        ],
    },
    'green_plate': {
        'expansion': 'green_knight_armor',
        'name': 'Green Plate',
        'armor': 5,
        'location': 'body',
        'keywords': ['armor','set','metal','gormskin'],
        'desc': 'At the start of the showdown, draw 3 tactics cards.',
        'affinities': {'top': 'green', 'left': 'green', 'right': 'blue', 'bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'When you attack, the extra weight grants leverage. Your weapon gains the <i>club</i> keyword.',
            'requires': {
                'puzzle': {'blue': 2, 'green': 2},
            },
        },
        'recipes': [
            {
                'innovations': ['citrinitas'],
                'gear_handles': {'lion_knights_left_claw': 1},
                'resource_handles': {'iron': 2, 'leather': 3, 'scarab_shell': 1},
            },
        ],
    },
    'griswaldo': {
        'expansion': 'green_knight_armor',
        'name': 'Griswaldo',
        'keywords': ['weapon','set','melee','sword','finesse','bone','metal'],
        'rules': ['Sharp','Deadly','Savage'],
        'desc': 'When you wound, <b>Block 2</b> with Fetorsaurus for free.',
        'speed': 3,
        'accuracy': 4,
        'strength': 15,
        'affinities': {'top': 'red', 'right': 'green'},
        'recipes': [
            {
                'misc': 'Survivor with <b>True Blade</b>.',
                'innovations': ['rubedo'],
                'gear_handles': {'calcified_juggernaut_blade': 1},
                'resource_handles': {'gormite': 1, 'stomach_lining': 1, 'iron': 1},
            },
        ],
    },
}



#
#   gorm
#

gorm = {

    # gormery

    'acid_tooth_dagger': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Acid-Tooth Dagger',
        'keywords': ['weapon','melee','dagger','bone'],
        'affinities': {'top': 'red', 'bottom': 'red'},
        'speed': 2,
        'accuracy': 7,
        'strength': 2,
        'rules': ['Paired'],
        'desc': (
            'On a <b>Perfect hit</b>, a wound attempt in your attack '
            'automatically succeeds.'
        ),
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'acid_gland': 1},
                'resource_types': {'bone': 2}
            },
        ],
    },
    'armor_spikes': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Armor Spikes',
        'keywords': ['item','bone','heavy'],
        'desc': (
            'If adjacent to the monster when you suffer a severe body injury, '
            'the monster suffers a wound. Limit, once per round.'
        ),
        'affinities': {'bottom': 'blue'},
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'stout_vertebrae': 1},
                'resource_types': {'scrap': 1}
            },
        ],
    },
    'black_sword': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Black Sword',
        'keywords': ['weapon','melee','sword','heavy'],
        'speed': 3,
        'accuracy': 5,
        'strength': 10,
        'desc': (
            'On a <b>Perfect hit</b>, gain +1 survival. If you are a Sword '
            "Master, you understand this weapon's potential. It gains +20 "
            'strength.'
        ),
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'gormite': 1, 'handed_skull': 1},
            },
        ],
    },
    'gaxe': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Gaxe',
        'keywords': ['weapon','melee','axe','bone'],
        'desc': (
            'Each showdown, the first time you critically wound the monster, '
            'it gains -1 evasion token.'
        ),
        'speed': 1,
        'accuracy': 6,
        'strength': 4,
        'affinities': {'top': 'red', 'left': 'red'},
        'affinity_bonus': {
            'desc': 'Gains +1 speed and <b>Savage</b>',
            'requires': {'complete': {'red': 1}},
        },
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'dense_bone': 1, 'stout_hide': 1},
            },
        ],
    },
    'gorment_armor_set': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Gorment Armor Set',
    },
    'gorment_boots': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Gorment Boots',
        'armor': 2,
        'location': 'legs',
        'keywords': ['armor','set','gormskin','heavy'],
        'desc': (
            'Other survivors may move through but not end movement in a space '
            'you occupy.'
        ),
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'stout_hide': 1},
                'resource_types': {'bone': 1}
            },
        ],
    },
    'gorment_mask': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Gorment Mask',
        'keywords': ['armor','set','gormskin','heavy'],
        'location': 'head',
        'armor': 2,
        'affinities': {'top': 'blue', 'bottom': 'green'},
        'affinity_bonus': {
            'desc': (
                'If your courage is higher than &#9733;, ignore intimidate '
                'actions.'
            ),
            'requires': {'puzzle': {'blue': 1, 'green': 1}},
        },
        'recipes': [
            {
                'locations': ['gormery'],
                'resource_handles': {'stout_hide': 1, 'handed_skull': 1},
            },
        ],
    },
    'gorment_sleeves': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Gorment Sleeves',
        'keywords': ['armor','set','gormskin','heavy'],
        'location': 'arms',
        'armor': 2,
        'affinities': {'right': 'green'},
        'affinity_bonus': {
            'desc': 'You may <b>Guard</b> without spending survival.',
            'requires': {'complete': {'green': 2}},
        },
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'stout_hide': 1, },
                'resource_types': {'bone':1}
            },
        ],
    },
    'gorment_suit': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Gorment Suit',
        'keywords': ['armor','set','gormskin','heavy'],
        'location': 'body',
        'aux_location': 'waist',
        'armor': 2,
        'affinities': {'left': 'green'},
        'affinity_bonus': {
            'desc': (
                '<b>Guard:</b> At the end of your attack, if you are standing '
                'and have a shield in your gear grid, spend 1 survival to move '
                '3 spaces directly away from the monster and <b>Block 1</b> '
                'for free.'
            ),
            'requires': {
                'puzzle': {'green': 1},
                'complete': {'blue': 1, 'red': 1},
            },
        },
    },
    'gorn': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Gorn',
        'keywords': ['item','instrument','gormskin'],
        'desc': (
            '<font class="kdm_font">a</font>: All non-deaf knocked down '
            'survivors stand and gain +<font class="inline_shield">1</font> '
            'to all hit locations.<br/>Use once per showdown.'
        ),
        'affinities': {'bottom': 'blue'},
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'stout_heart': 1, },
                'resource_types': {'bone':3}
            },
        ],
    },
    'greater_gaxe': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Greater Gaxe',
        'keywords': ['weapon','melee','axe','two-handed','heavy'],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'rules': ['Deadly', 'Reach 2'],
        'affinities': {'left': 'red'},
        'affinity_bonus': {
            'desc': (
                'On a <b>Perfect hit</b>, the edge sharpens. Gain +4 strength '
                'for the rest of the attack.'
            ),
            'requires': {'complete': {'green': 1,'red': 1}},
        },
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'dense_bone': 1, 'jiggling_lard': 1},
            },
        ],
    },
    'knuckle_shield': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Knuckle Shield',
        'keywords': ['weapon','melee','shield','gormskin'],
        'speed': 3,
        'accuracy': 7,
        'strength': 1,
        'rules': ['Block 1'],
        'desc': (
            'Once per round, if you wound with this weapon, <b>Block 1</b> '
            'for free.'
        ),
        'affinities': {'bottom': 'red'},
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'mammoth_hand': 1, },
                'resource_types': {'bone':2}
            },
        ],
    },
    'pulse_lantern': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Pulse Lantern',
        'keywords': ['item','lantern','gormskin','fragile'],
        'desc': (
            '<font class="kdm_font">a</font>: Once per showdown, roll 1d10. '
            'On a result of 4+, the monster is knocked down and all survivors '
            'gain -1 accuracy token.'
        ),
        'affinities': {'top': 'red',},
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'milky_eye': 1, 'active_thyroid': 1},
            },
        ],
    },
    'regeneration_suit': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Regeneration Suit',
        'keywords': ['item','gorm'],
        'armor': 2,
        'location': 'body',
        'rules': ['Accessory'],
        'affinities': {'top': 'green', 'left': 'green', 'bottom': 'green'},
        'affinity_bonus': {
            'desc': (
                'At the end of the showdown, remove any permanent injuries '
                'you suffered this showdown.'
            ),
            'requires': {'complete': {'green': 2}, 'puzzle': {'green': 1}},
        },
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'stomach_lining': 1, 'jiggling_lard': 1},
            },
        ],
    },
    'rib_blade': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Rib Blade',
        'keywords': ['weapon','melee','grand','bone'],
        'speed': 1,
        'accuracy': 6,
        'strength': 5,
        'rules': ['Slow','Deadly'],
        'affinities': {'right': 'blue'},
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {'meaty_rib': 1,},
                'resource_types': {'hide':1},
            },
        ],
    },
    'riot_mace': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Riot Mace',
        'keywords': ['weapon','melee','club'],
        'speed': 2,
        'accuracy': 5,
        'strength': 5,
        'rules': ['Deadly'],
        'desc': (
            'When you critically wound, the next time a monster would draw AI, '
            'it performs <b>Basic Action</b> instead.'
        ),
        'affinities': {'left': 'blue'},
        'recipes': [
            {
                'locations':['gormery'],
                'resource_handles': {
                    'pure_bulb': 1,
                    'stout_kidney': 1,
                    'dense_bone': 1,
                    'jiggling_lard': 1
                },
            },
        ],
    },

    # gormchymist

    'healing_potion': {
       'type': 'gormchymist',
       'name': 'Healing Potion',
       'expansion': 'gorm',
       'keywords': ['item','consumable','fragile'],
       'desc': 'At the end of the showdown, if you suffered any permanent injuries, you may archive this card and remove one of your choice.',
       'affinities': {'bottom':'red'},
    },
    'life_elixir': {
        'type': 'gormchymist',
        'name': 'Life Elixir',
        'expansion': 'gorm',
        'keywords': ['item','consumable','stinky'],
        'desc': 'Each showdown, the first time you would die from a severe injury, ignore that injury.',
    },
    'power_potion': {
        'type': 'gormchymist',
        'name': 'Power Potion',
        'expansion': 'gorm',
        'keywords': ['item','consumable'],
        'affinities': {'top':'green'},
        'desc': '<font class="kdm_font">a</font> <b>Consume:</b> Once per showdown, gain +1 strength token for each <font class="affinity_green_text">&#9632;</font> you have.', 
    },
    'steadfast_potion': {
        'type': 'gormchymist',
        'name': 'Steadfast Potion',
        'expansion': 'gorm',
        'keywords': ['item','consumable','heavy'],
        'desc': (
            'When you ignore a hit with <b>Block</b>, gain +1 strength token. '
            'When you are knocked down, lose all your +1 strength tokens.'
        ),
        'affinities': {'top': 'red'},
    },
    'wisdom_potion': {
        'type': 'gormchymist',
        'expansion': 'gorm',
        'name': 'Wisdom Potion',
        'keywords': ['item','consumable','other'],
        'affinities': {'right': 'blue'},
        'affinity_bonus': {
            'desc': (
                'Play the showdown with the top card of the hit location deck '
                'revealed.'
            ),
            'requires': {'complete': {'blue':1}, 'puzzle': {'blue':1}},
        },
    },
}



#
#   lion knight
#

lion_knight = {
    'hideous_disguise': {
        'expansion': 'lion_knight',
        'type': 'rare_gear',
        'name': 'Hideous Disguise'
    },
    "lion_knights_left_claw": {
        'expansion': 'lion_knight',
        'type': 'rare_gear',
        'name': "Lion Knight's Left Claw"
    },
    "lion_knights_right_claw": {
        'expansion': 'lion_knight',
        'type': 'rare_gear',
        'name': "Lion Knight's Right claw"
    },
    'lion_knight_badge': {
        'expansion': 'lion_knight',
        'type': 'rare_gear',
        'name': 'Lion Knight Badge'
    },
}




spidicules = {
    # rare gear
    'grinning_visage': {
        'keywords': ['weapon', 'melee', 'shield'],
        'desc': """When you wound with this shield, you may spend 1 survival to add <font class="inline_shield">1</font> to all hit locations.<br/>Limit, once per attack.""",
        'expansion': 'spidicules',
        'type': 'rare_gear',
        'name': 'Grinning Visage',
        'affinities': {'top': 'green', 'bottom': 'red'},
        'rules': ['Unique','Block 1'],
        'speed': 2,
        'accuracy': 7,
        'strength': 4,
    },

    # silk mill
    'amber_edge': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Amber Edge',
        'speed': 1,
        'accuracy': 6,
        'strength': 4,
        'keywords': ['weapon','melee','scimiatar','amber'],
        'rules': ['Slow'],
        'desc': 'At the end of each attack, if you wounded the monster, make an additional attack with this weapon.',
    },
    'amber_poleaxe': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Amber Poleaxe',
        'speed': 2,
        'accuracy': 6,
        'strength': 3,
        'keywords': ['weapon','melee','axe','spear','two-handed','amber'],
        'rules': ['Reach 2'],
        'desc': 'When a monster collides with you, roll 1d10. On a 6+, the monster suffers one wound.',
        'affinities': {'bottom': 'green'},
    },
    'blue_ring': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Blue Ring',
        'keywords': ['item','jewelry','amber'],
        'armor': 2,
        'location': 'arms',
        'rules': ['Unique','Accessory'],
        'affinities': {'left': 'blue','right':'blue','bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'If you are the monster controller when the monster draws <font class="kdm_font_10">b</font>, draw 1 extra card. Select 1 to play and discard the other.',
            'requires': {
                'puzzle': {'blue': 3},
            },
        },
    },
    'green_ring': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Green Ring',
        'keywords': ['item','jewelry','amber'],
        'armor': 2,
        'location': 'arms',
        'rules': ['Unique','Accessory'],
        'affinities': {'top': 'green','right':'green','bottom': 'green'},
        'affinity_bonus': {
            'desc': 'The first time you are attacked each round, gain <font class="inline_shield">3</font> to all hit locations if you are monster controller.',
            'requires': {
                'puzzle': {'green': 3},
            },
        },
    },
    'hooded_scrap_katar': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Hooded Scrap Katar',
        'speed': 2,
        'accuracy': 7,
        'strength': 4,
        'keywords': ['weapon','melee','katar','metal'],
        'affinities': {'left': 'blue'},
        'rules': ['Paired'],
        'desc': 'If you hit 4 or more times in a single attack with this weapon, the monster suffers 1 wound before hit locations are drawn.',
    },
    'red_ring': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Red Ring',
        'keywords': ['item','jewelry','amber'],
        'armor': 2,
        'location': 'arms',
        'rules': ['Unique','Accessory'],
        'affinities': {'top': 'red','left':'red','bottom': 'red'},
        'affinity_bonus': {
            'desc': 'If you gain a bleeding token while monster controller, monster suffers 1 wound. Limit twice per round.',
            'requires': {
                'puzzle': {'red': 3},
            },
        },
    },
    'silk_armor_set': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Armor Set',
        'desc': 'Add <font class="inline_shield">1</font> to all hit locations.<br/>Whenever you are attacked, after hit locations are rolled, you may change 1 hit location dice to the result of your choice.',
    },
    'silk_body_suit': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Body Suit',
        'keywords': ['item','silk','flammable'],
        'rules': ['Unique'],
        'desc': 'Reduce damage from every hit suffered by 2, to a minimum of 1. You may not have any heavy or metal armor in your gear grid.',
    },
    'silk_bomb': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Bomb',
        'keywords': ['item','thrown','silk','amber','fragile'],
        'desc': '<font class="kdm_font">a</font>: Until the end of the round, all survivors ignore knockback and bash. Archive after use.' ,
    },
    'silk_boots': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Boots',
        'armor': '3',
        'location': 'legs',
        'keywords': ['armor','set','silk','flammable'],
        'affinities': {'top': 'green','right': 'green'},
        'affinity_bonus': {
            'desc': '+1 movement. Once per round, you may spend 1 survival to gain 2 insanity.',
            'requires': {
                'puzzle': {'green': 2},
            },
        },
    },
    'silk_robes': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Robes',
        'armor': '3',
        'location': 'body',
        'keywords': ['armor','set','silk','flammable'],
        'affinities': {'top': 'red','right': 'blue','bottom': 'red'},
        'desc': 'When you depart, gain 1 survival.',
        'affinity_bonus': {
            'desc': '<font class="kdm_font">a</font>: add <font class="inline_shield">1</font> to all hit locations. Use once per showdown.' ,
            'requires': {
                'puzzle': {'red': 2, 'blue': 1},
            },
        },
    },
    'silk_sash': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Sash',
        'armor': '3',
        'location': 'legs',
        'keywords': ['armor','set','silk','flammable'],
        'affinities': {'left': 'green','bottom': 'green'},
        'desc': 'When you depart, gain 1 survival.',
        'affinity_bonus': {
            'desc': '<font class="kdm_font">a</font>: add <font class="inline_shield">1</font> to all hit locations. Use once per showdown.' ,
            'requires': {
                'puzzle': {'green': 2},
            },
        },
    },
    'silk_turban': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Turban',
        'armor': '3',
        'location': 'head',
        'keywords': ['armor','set','silk','flammable'],
        'affinities': {'left': 'blue','right': 'green'},
        'affinity_bonus': {
            'desc': """<font class="kdm_font">a</font>: Turn the monster to face away from you. Use only during the survivors' turn.""",
            'requires': {
                'puzzle': {'green': 1, 'blue': 1,},
            },
        },
    },
    'silk_whip': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Whip',
        'speed': 2,
        'accuracy': 6,
        'strength': 3,
        'keywords': ['weapon','melee','whip','silk'],
        'affinities': {'right': 'blue', 'bottom': 'green'},
        'affinity_bonus': {
            'desc': 'On a <b>Perfect hit</b>, you may archive a mood in play instead of drawing a hit location.',
            'requires': {
                'puzzle': {'blue': 1, 'green': 1},
            },
        },
    },
    'silk_wraps': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Silk Wraps',
        'armor': 3,
        'location': 'arms',
        'affinities': {'left': 'green','bottom': 'red'},
        'keywords': ['armor','set','silk','flammable'],
    },
    'throwing_knife': {
        'expansion': 'spidicules',
        'type': 'silk_mill',
        'name': 'Throwing Knife',
        'speed': 4,
        'accuracy': 9,
        'strength': 2,
        'keywords': ['weapon','ranged','thrown'],
        'rules': ['Range: 4'],
        'affinities': {'right': 'red'},
        'desc': 'At the end of your attack, gain +1 accuracy token for each <b>Perfect hit</b>. When knocked down, remove all your +1 accuracy tokens.',
    },
    'the_weaver': {
        'expansion': 'spidicules',
        'type': 'rare_gear',
        'name': 'The Weaver',
        'keywords': ['weapon', 'melee', 'sword', 'amber'],
        'speed': 3,
        'accuracy': 6,
        'strength': 2,
        'affinities': {'top':'red','left': 'red'},
        'rules': ['Unique'],
        'desc': 'When you wound a monster, add <font class="inline_shield">1</font> to a random hit location.',
    },
}

lion_god = {
    'ancient_lion_claws': {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': 'Ancient Lion Claws',
        'keywords': ['item','fur','heavy'],
        'armor': 2,
        'location': 'arms',
        'affinities': {'top': 'red', 'right': 'red'},
        'rules': ['Unique','Accessory','-1 evasion'],
        'desc': '+2 strength while attacking with daggers or katars. You may move up to 2 additional spaces when you <b>pounce</b>.',
    },
    'bone_witch_mehndi': {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': 'Bone Witch Mehndi',
        'keywords': ['item','soluble','symbol','other'],
        'affinities': {'left': 'green', 'top': 'blue', 'right': 'red'},
        'affinity_bonus': {
            'desc': (
                'At the start of your act, you may spend 3 insanity to gain 1 '
                'survival or 1 survival to gain 3 insanity.'
            ),
            'requires': {'puzzle': {'green':1,'blue':1,'red':1}},
        },
    },
    "butchers_blood": {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': "Butcher's Blood",
        'keywords': ['item','soluble','symbol','other'],
        'add_affinity': ['blue'],
        'affinities': {'left': 'red', 'top': 'red'},
        'affinity_bonus': {
            'desc': (
                'For every 10 insanity you have, gain +1 speed and '
                '+1 strength.'
            ),
            'requires': {'complete': {'blue': 2}, 'puzzle': {'red': 1}},
        },
    },
    'death_mehndi': {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': 'Death Mehndi',
        'keywords': ['item','soluble','symbol','other'],
        'rules': ['Cursed'],
        'desc': (
            'On a <b>Perfect hit</b>, gain 1d10 insanity. -4 to all brain '
            'trauma rolls.'
        ),
        'add_affinity': ['blue','green','red'],
    },
    'glyph_of_solitude': {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': 'Glyph of Solitude',
        'keywords': ['item','soluble','symbol','other'],
        'add_affinity': ['red'],
        'affinities': {'right': 'green','bottom': 'green'},
        'affinity_bonus': {
            'desc': "+2 accuracy. You are <b>deaf</b>. You cannot <b>encourage</b>.",
            'requires': {'complete': {'red': 2}, 'puzzle': {'green': 1}},
        },
    },
    'golden_plate': {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': 'Golden Plate',
        'keywords': ['item','metal','heavy'],
        'rules': ['Unique', '-1 evasion'],
        'affinities': {'left': 'red','top': 'red','right': 'red','bottom':'red'},
        'affinity_bonus': {
            'desc': """When you <b>depart</b>, gain + <font class="inline_shield">2</font> to all locations wearing fur armor.""",
            'requires': {'complete': {'red': 4},},
        },
    },
    'lantern_mehndi': {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': 'Lantern Mehndi',
        'keywords': ['item','soluble','symbol','other'],
        'add_affinity': ['red'],
        'affinities': {'bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'You may start the showdown in any unoccupied board space.',
            'requires': {'complete': {'red': 2}, 'puzzle': {'blue': 1}},
        },
    },
    'lion_god_statue': {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': 'Lion God Statue',
        'keywords': ['item','stone','heavy'],
        'rules': ['Unique', '-1 evasion'],
        'affinities': {'left': 'red', 'top': 'blue'},
        'affinity_bonus': {
            'desc': """Gain +1 strength for each <font class="affinity_red_text">&#9632;</font> you have.""",
            'requires': {'puzzle': {'red': 1}},
        },
    },
    "necromancers_eye": {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': "Necromancer's Eye",
        'keywords': ['item','set','jewelry','other'],
        'location': 'head',
        'armor': 2,
        'rules': ['Unique', 'Accessory'],
        'desc': 'Ignore the effects of <b>blind</b>.',
        'affinities': {'bottom': 'blue'},
        'affinity_bonus': {
            'desc': """<font class="kdm_font">a</font>: Reveal the next 4 monster hit locations. Put them back in any order.""",
            'requires': {'puzzle': {'blue': 1}},
        },
    },
}




manhunter = {
    'deathpact': {
        'expansion': 'manhunter',
        'type': 'manhunter_gear',
        'name': 'Deathpact',
        'affinities': {'top': 'blue', 'right': 'red'},
        'keywords': ['item', 'metal', 'fragile'],
        'rules': ['Unique'],
        'desc': (
            'At the start of your act, gain +1 survival.<br/>Once per '
            'campaign, you may fire the gun to automatically hit and inflict '
            'a critical wound.'
        ),
    },
    "hunters_heart": {
        'expansion': 'manhunter',
        'type': 'manhunter_gear',
        'name': "Hunter's Heart",
        'keywords': ['item', 'consumable', 'metal', 'heavy'],
        'rules': ['Unique'],
        'desc': (
            'If you die, the heart crawls back to the settlement. Roll 1d10. '
            'On a 7+, it regrows you.<br/> During the settlement phase, you '
            'may archive this to <font class="kdm_font">g</font> <b>Bleeding '
            'Heart</b>.'
        ),
    },
    "manhunters_hat": {
        'expansion': 'manhunter',
        'type': 'manhunter_gear',
        'name': "Manhunter's Hat",
        'affinities': {'top': 'red', 'left': 'red', 'bottom': 'blue'},
        'armor': 2,
        'location': 'head',
        'keywords': ['item', 'rawhide', 'leather'],
        'rules': ['Unique', 'Accessory'],
        'affinity_bonus': {
            'desc': (
                'Ignore the first severe <font class="kdm_font_2">b</font> '
                'injury you suffer each showdown.'
            ),
            'requires': {'puzzle': {'blue': 1}, 'complete': {'red': 1}},
        },
    },
    'reverberating_lantern': {
        'expansion': 'manhunter',
        'type': 'manhunter_gear',
        'name': 'Reverberating Lantern',
        'keywords': ['item','tool','lantern'],
        'rules': ['Unique'],
        'affinities': {'top': 'green', 'right': 'blue'},
        'desc': (
            'At the start of any hunt turn, before an event is revealed, you '
            'may <font class="kdm_font">g</font> <b>Sonorous Rest</b>. <br/>'
            'Limit, once per hunt.'
        ),
    },
    'tool_belt': {
        'expansion': 'manhunter',
        'type': 'manhunter_gear',
        'name': 'Tool Belt',
        'keywords': ['item', 'metal', 'fragile'],
        'rules': ['Unique'],
        'desc': """If you have no weapons in your gear grid, gain +3 evasion.<br/>Tools in your gear grid lose <b>frail</b>. Tools with attack profiles gain +1 speed, +3 accuracy and <b>sharp</b>.""",
        'affinities': {'top': 'blue', 'right': 'green'},
    },
}


#
#   Flower Knight
#

flower_knight_rare_gear = {
    'flower_knight_helm': {
        'expansion': 'flower_knight',
        'type': 'rare_gear',
        'name': 'Flower Knight Helm',
        'keywords': ['armor','heavy'],
        'rules': ['+1 Accuracy'],
        'armor': 3,
        'location': 'head',
        'affinities': {'bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'While you are being attacked the monster has -1 speed.',
            'requires': {
                'puzzle': {'blue': 1},
                'complete': {'green': 3},
            },
        },
    },
    'replica_flower_sword': {
        'expansion': 'flower_knight',
        'type': 'rare_gear',
        'name': 'Replica Flower Sword',
        'keywords': ['weapon', 'melee', 'grand', 'sword'],
        'speed': 2,
        'accuracy': 6,
        'strength': 6,
        'affinities': {'left': 'green', 'top': 'red', 'right': 'red'},
        'rules': ['Devastating 1'],
        'desc': 'You cannot dodge.',
        'affinity_bonus': {
            'desc': 'Gains <b>Sharp</b>, +1 Evasion.',
            'requires': {
                'puzzle': {'green': 1},
                'complete': {
                    'red': 1,
                    'green': 2,
                },
            },
        },
    },
}

sense_memory_gear = {
    'flower_knight_badge': {
        'expansion': 'flower_knight',
        'name': 'Flower Knight Badge',
        'keywords': ['item', 'jewelry', 'badge'],
        'rules': ['Unique'],
        'desc': (
            'At the start of the showdown, draw 1 tactics card and gain +1 '
            'evasion token.'
        ),
        'affinities': {'top': 'blue'},
    },
    'satchel': {
        'expansion': 'flower_knight',
        'type': 'sense_memory_gear',
        'name': 'Satchel',
        'keywords': ['item', 'heavy', 'stinky'],
        'affinities': {'top': 'green', 'left': 'green', 'bottom': 'green'},
        'desc': (
            'You may <b>depart</b> with one resource card. If that resource '
            'is <b>Perishable</b>, it is not destroyed.'
        ),
    },
    'sleeping_virus_flower': {
        'expansion': 'flower_knight',
        'type': 'rare_gear',
        'name': 'Sleeping Virus Flower',
        'keywords': ['item','flammable'],
        'affinities': {
            'left': 'blue', 'right': 'blue', 'top': 'blue', 'bottom': 'blue'
        },
        'rules': ['+1 Luck', 'Cursed'],
        'desc': (
            'When you die, a flower bloomes from your corpse. Add '
            '<font class="kdm_font">g</font> <b>A Warm Virus</b> to the '
            'timeline next year. You are the guest.'
        ),
    },
    'vespertine_arrow': {
        'expansion': 'flower_knight',
        'type': 'sense_memory_gear',
        'name': 'Vespertine Arrow',
        'keywords': ['item','ammunition','arrow'],
        'speed': 2,
        'accuracy': 6,
        'strength': 0,
        'rules': ['Ammo - Bow', 'Deadly 4'],
        'desc': (
            'Archive after use. If your attack misses, place a '
            '<b>Flower Patch</b> terrain tile adjacent to the monster.'
        ),
    },
    'vespertine_bow': {
        'expansion': 'flower_knight',
        'type': 'sense_memory_gear',
        'name': 'Vespertine Bow',
        'keywords': ['weapon', 'ranged', 'bow', 'two-handed', 'other'],
        'speed': 3,
        'accuracy': 6,
        'strength': 6,
        'rules': ['Range: 5', 'Deadly'],
        'desc': (
            'Before each attack, you may choose for Vespertine Bow to have '
            '<b>slow</b>, +4 accuracy, and <b>Range: 9</b> for that attack.'
        ),
        'affinities': {'left': 'blue', 'right': 'green'},
    },
    'vespertine_cello': {
        'expansion': 'flower_knight',
        'type': 'sense_memory_gear',
        'name': 'Vespertine Cello',
        'keywords': ['item', 'instrument', 'noisy', 'other'],
        'rules': ['Unique'],
        'desc': (
            'At start of showdown, all other survivors with an instrument '
            'in their gear grid gain +1 luck token.'
        ),
        'affinities': {'bottom': 'blue'},
    },
    'vespertine_foil': {
        'expansion': 'flower_knight',
        'type': 'sense_memory_gear',
        'name': 'Vespertine Foil',
        'keywords': ['weapon', 'melee', 'sword', 'fragile'],
        'speed': 4,
        'accuracy': 5,
        'strength': 1,
        'affinities': {'left': 'red', 'right': 'blue'},
        'desc': (
            'At the beginning of each settlement phase, archive this unless '
            'you spend 1 Flower resource.'
        ),
        'affinity_bonus': {
            'desc': 'Gains <b>deadly 2</b>.',
            'requires': {
                'puzzle': {'blue': 1, 'red': 1},
            },
        },
    },
}



#
#   Slenderman!!!1
#

light_forging = {
    'dark_water_vial': {
        'expansion': 'slenderman',
        'name': 'Dark Water Vial',
        'keywords': ['item','consumable','gloomy','fragile'],
        'affinities': {'bottom': 'green'},
        'desc': (
            '<font class="kdm_font">a</font> <b>Consume:</b> You are knocked '
            'down and cannot gain bleeding tokens until the end of the round. '
            'Use once per showdown.'
        ),
    },
    'gloom_bracelets': {
        'expansion': 'slenderman',
        'name': 'Gloom Bracelets',
        'keywords': ['item','jewelry','gloomy','fragile','heavy'],
        'rules': ['Accessory'],
        'desc': (
            'When you <b>depart</b>, gain +2 insanity. When you suffer a '
            'severe arm injury, archive this card.'
        ),
        'affinities': {'left': 'red', 'right': 'red', 'bottom': 'blue'},
        'armor': 6,
        'location': 'arms',
    },
    'gloom_coated_arrow': {
        'expansion': 'slenderman',
        'name': 'Gloom-Coated Arrow',
        'rules': ['Ammo - Bow','Cumbersome','Deadly'],
        'keywords': ['item','ammunition','arrow','gloomy'],
        'desc': (
            'After attempting to wound each hit location, place it on top of '
            'the deck instead of in the discard pile. Use once per showdown.'
        ),
        'speed': 5,
        'accuracy': 6,
        'strength': 5,
    },
    'gloom_cream': {
        'expansion': 'slenderman',
        'name': 'Gloom Cream',
        'keywords': ['item','consumable','balm','gloomy','stinky','other'],
        'affinities': {
            'left': 'red','top':'blue', 'right':'red', 'bottom': 'blue'
        },
        'affinity_bonus': {
            'desc': (
                'When you <b>Depart</b>, gain -3 Hunt XP, -1 understanding. '
                'If you have no understanding, die instantly.'
            ),
            'requires': {
                'complete': {'blue': 2},
                'puzzle': {'red': 2},
            },
        },
    },
    'gloom_hammer': {
        'expansion': 'slenderman',
        'name': 'Gloom Hammer',
        'rules': ['Unique','Sentient','Reach 2','Deadly'],
        'keywords': ['weapon','melee','club','two-handed','gloomy','other'],
        'affinities': {'top': 'blue', 'left': 'red'},
        'speed': 2,
        'accuracy': 7,
        'strength': 13,
        'desc': (
            'When you wound, end your attack (cancel reactions). Gain the '
            'monster controller tile and full move the monster directly away '
            'from you.'
        ),
    },
    'gloom_katana': {
        'expansion': 'slenderman',
        'name': 'Gloom Katana',
        'keywords': [
            'weapon','melee','katana','two-handed','finesse','gloomy','other'
        ],
        'desc': (
            "Your insanity is added to this weapon's strength. When Gloom "
            "Sheath is right of this in your gear grid, Gloom Katana gains "
            "<b>Savage</b>."
        ),
        'affinities': {'right': 'paired'},
        'speed': 4,
        'accuracy': 5,
        'strength': 0,
    },
    'gloom_mehndi': {
        'expansion': 'slenderman',
        'name': 'Gloom Mehndi',
        'keywords': ['item','gloomy','soluble'],
        'affinities': {'left': 'blue', 'right': 'red', 'bottom': 'red'},
        'desc': (
            'When you <b>depart</b>, gain <font class="inline_shield">1</font> '
            'to all hit locations. When you gain the <b>Crystal Skin</b> '
            'ability, gain the <b>Crystal Sword Mold</b> strange resource.'
        ),
    },
    'gloom_sheath': {
        'expansion': 'slenderman',
        'name': 'Gloom Sheath',
        'keywords': ['item','gloomy','other'],
        'rules': ['Block 1'],
        'affinity_bonus': {
            'desc': 'At the start of your act, gain +1 insanity.',
            'requires': {
                'puzzle': {'red': 1},'complete': {'blue': 1},
            },
        },
        'affinities': {'top': 'red'}
    },
    'raptor_worm_collar': {
        'expansion': 'slenderman',
        'name': 'Raptor-Worm Collar',
        'keywords': ['item','jewelry','gloomy'],
        'desc': (
            'You may <b>encourage</b> without spending survival. When you '
            '<b>encourage</b> a survivor, they suffer 2 brain damage.'
        ),
        'affinities': {'right': 'red', 'bottom': 'green'},

    },
    'slender_ovule': {
        'expansion': 'slenderman',
        'name': 'Slender Ovule',
        'keywords': ['item','jewelry','gloomy','other'],
        'rules': ['Unique'],
        'desc': 'When you <b>depart</b>, gain +3 insanity.',
        'affinities': {'top': 'blue', 'right': 'green', 'bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'Monsters and survivors adjacent to you have -1 luck.',
            'requires': {
                'puzzle': {'blue': 1, 'green': 1},
            },
        },
    },
}


#
#   Sunstalker
#

sunstalker_rare_gear = {
    'eye_patch': {
        'expansion': 'sunstalker',
        'type': 'rare_gear',
        'name': 'Eye Patch',
        'keywords': ['item', 'leather'],
        'desc': (
            'While you wear this, you are <b>blind</b> in one eye '
            '(-1 accuracy), if you are already <b>blind</b>, gain +2 strength '
            'for being a badass instead.'
        ),
        'affinities': {'top': 'green', 'bottom': 'red'},
    },
    "gods_string": {
        'expansion': 'sunstalker',
        'type': 'rare_gear',
        'name': "God's String",
        'keywords': ['item', 'other'],
        'rules': ['Unique'],
        'desc': (
            "When a bow is below God's string, it gains <b>sharp</b>, and its "
            "range is increased by 1."
        ),
        'affinities': {'bottom': 'paired',},
    },

}

sacred_pool = {
    'apostle_crown': {
        'expansion': 'sunstalker',
        'name': 'Apostle Crown',
        'armor': 3,
        'location': 'head',
        'keywords': ['item', 'jewelry', 'other'],
        'rules': ['Unique', 'Accessory'],
        'affinities': {'bottom': 'blue','right':'red'},
        'desc': (
            'At the start of your act, if you have any +1 strength tokens, '
            'reveal the next 4 monster hit locations and put them back in any '
            'order.'
        ),
        'recipes': [
            {
                'locations': [{'handle':'sacred_pool', 'level':3}],
                'resource_handles': {'legendary_horns': 1, 'phoenix_crest': 1},
            },
        ],
    },
    'prism_mace': {
        'expansion': 'sunstalker',
        'name': 'Prism Mace',
        'affinities': {
            'left': 'red', 'top': 'green', 'right': 'blue', 'bottom': 'green'
        },
        'speed': 3,
        'strength': 6,
        'accuracy': 10,
        'rules': ['Unique','Block 1'],
        'desc': (
            'When you wound with this you may <b>block 1</b> for free and '
            'discard 1 mood in play if you have any +1 strength tokens.'
        ),
        'recipes': [
            {
                'locations': [{'handle':'sacred_pool', 'level':3}],
                'resource_handles': {
                    'iron': 4, 'shimmering_halo': 1, 'elder_cat_teeth': 2
                },
            },
        ],
    },
    'sun_vestments': {
        'expansion': 'sunstalker',
        'name': 'Sun Vestments',
        'affinities': {'right': 'red'},
        'keywords': ['item', 'silk', 'flammable'],
        'desc': 'Ignore <b>Cumbersome</b>',
        'affinity_bonus': {
            'requires': {'complete': {'red': 2}},
            'desc': (
                'When you have any +1 strength tokens, increase the range of '
                'your <b>Perfect hits</b> by 1.'
            ),
        },
        'recipes': [
            {
                'locations': [
                    {'handle':'sacred_pool', 'level':2}
                ],
                'resource_handles': {
                    'golden_whiskers': 1,
                    'pustules': 2
                },
                'resource_types': {'hide': 6}
            },
        ],
    },
    'sunring_bow': {
        'expansion': 'sunstalker',
        'name': 'Sunring Bow',
        'affinities': {'right': 'red', 'left': 'red'},
        'recipes': [
            {
                'locations': [{'handle':'sacred_pool', 'level':2}],
                'resource_handles': {'bladder': 1, 'phoenix_whisker': 1},
                'resource_types': {'bone': 6},
            },
        ],
        'speed': 2,
        'accuracy': 4,
        'strength': 4,
        'rules': ['Range: 5', 'Unique', 'Cumbersome'],
        'keywords': ['weapon', 'ranged', 'two-handed', 'bone'],
        'affinity_bonus': {
            'desc': (
                'On a <b>Perfect hit</b>, do not draw a hit location. Monster '
                'suffers 1 wound.'
            ),
            'requires': { 'puzzle': {'red': 2}},
        },
    },
}

skyreef_sanctuary = {
    'cycloid_scale_armor': {
        'expansion': 'sunstalker',
        'name': 'Cycloid Scale Armor',
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
            '<br/><b>Prismatic:</b> Your complete affinities and incomplete '
            'affinity halves count as all colors.'
        ),
        'rules': ['prismatic'],
    },
    'cycloid_scale_hood': {
        'expansion': 'sunstalker',
        'name': 'Cycloid Scale Hood',
        'location': 'head',
        'armor': 2,
        'keywords': ['armor','set','scale'],
        'affinities': {'bottom': 'blue'},
        'desc': (
            'Whenever you spend <font class="kdm_font">c</font>, the scales\' '
            "colors shift. Gain +1 evasion until your next act."
        ),
        'recipes': [
            {
                'locations': ['skyreef_sanctuary'],
                'resource_handles': {'cycloid_scales': 1, 'prismatic_gills': 1},
                'resource_types': {'hide': 1}
            },
        ],
    },
    'cycloid_scale_jacket': {
        'expansion': 'sunstalker',
        'name': 'Cycloid Scale Jacket',
        'armor': 2,
        'location': 'body',
        'keywords': ['armor','set','scale'],
        'affinities': {'left': 'red', 'right': 'red', 'top': 'blue'},
        'affinity_bonus': {
            'desc': '+1 Accuracy',
            'requires': {'puzzle': {'blue': 1}, 'complete': {'red': 2} },
        },
        'desc': (
            'When you spend <font class="kdm_font">c</font>, you '
            '<b>Shadow Walk</b> and may move through spaces survivors occupy '
            'without causing <b>collision</b>.'
        ),
    },
    'cycloid_scale_shoes': {
        'expansion': 'sunstalker',
        'name': 'Cycloid Scale Shoes',
        'keywords': ['armor','set','scale'],
        'armor': 2,
        'location': 'legs',
        'affinities': {'top': 'blue', 'left': 'green'},
        'affinity_bonus': {
            'desc': (
                '<font class="kdm_font">c</font>: You are not a threat until '
                'you attack. If you have the <b>priority target</b> token, '
                'gain +2 survival and remove it.'
            ),
            'requires': {'puzzle': {'blue': 1, 'green':1}}
        },
    },
    'cycloid_scale_skirt': {
        'expansion': 'sunstalker',
        'name': 'Cycloid Scale Skirt',
        'keywords': ['armor','set','scale'],
        'armor': 2,
        'location': 'waist',
        'affinities': {'top': 'blue', 'bottom': 'green'},
        'affinity_bonus': {
            'desc': (
                'When you <b>depart</b>, gain survival equal to the number of '
                '<font class="affinity_blue_text">&#9632;</font> you have.'
            ),
            'requires': {'puzzle': {'green': 1}, 'complete': {'blue': 3}},
        },
    },
    'cycloid_scale_sleeves': {
        'expansion': 'sunstalker',
        'name': 'Cycloid Scale Sleeves',
        'keywords': ['armor','set','scale'],
        'armor': 2,
        'location': 'armos',
        'affinities': {'left': 'blue', 'right': 'blue'},
        'desc': (
            'When you <b>Shadow Walk</b> and attack a monster from its blind '
            'spot, your weapon gains +1 accuracy and <b>Sharp</b> for that '
            'attack.'
        ),
    },
    'denticle_axe': {
        'expansion': 'sunstalker',
        'name': 'Denticle axe',
        'speed': 2,
        'accuracy': 6,
        'strength': 5,
        'keywords': ['weapon','melee','axe','scale'],
        'affinities': {'right': 'red', 'bottom': 'blue'},
        'affinity_bonus': {
            'desc': (
                'When attacking from the blind spot, the attack gains +2 '
                'strength and the first successful wound attempt gains '
                '<b>devastating 1</b>.'
            ),
            'requires': {
                'puzzle': {'blue':1},
                'complete': {'blue': 1,'red': 1},
            },
        },
    },
    'ink_blood_bow': {
        'expansion': 'sunstalker',
        'name': 'Ink Blood Bow',
        'keywords': ['weapon', 'ranged', 'bow', 'two-handed', 'other'],
        'rules': ['Range: 7', 'Deadly', 'Cumbersome'],
        'affinities': {'top': 'red', 'right': 'blue'},
        'speed': 2,
        'accuracy': 7,
        'strength': 8,
        'desc': (
            'Gains +1 strength for each bleeding token you have. Loses '
            '<b>cumbersome</b> when in darkness.'
        ),
    },
    'ink_sword': {
        'expansion': 'sunstalker',
        'name': 'Ink Sword',
        'keywords': ['weapon','melee','sword','fragile'],
        'speed': 4,
        'strength': 4,
        'accuracy': 4,
        'rules': ['Reach 3','Deadly 3'],
        'desc': 'You may only attack with this while ind arkness.',
        'affinities': {'bottom': 'blue'},
    },
    'quiver_and_sunstring': {
        'expansion': 'sunstalker',
        'name': 'Quiver and Sunstring',
        'keywords': ['item', 'leather', 'scale'],
        'affinities': {'left': 'red', 'right': 'blue'},
        'desc': (
            'You may carry up to 3 arrow gear cards outside of your grid. '
            '(All arrows you carry must be different.)'
        ),
        'affinity_bonus': {
            'desc': 'All your bows gain +2 range.',
            'requires': {
                'complete': {'blue': 2, 'red': 1},
            },
        },
    },
    'shadow_saliva_shawl': {
        'expansion': 'sunstalker',
        'name': 'Shadow Saliva Shawl',
        'affinities': {'top': 'green', 'bottom': 'green'},
        'affinity_bonus': {
            'desc': '+1 Evasion. All weapons gain <b>slow</b>',
            'requires': {'puzzle': {'green': 2}, 'complete': {'green': 2} }
        },
        'keywords': ['item','balm','stinky','other'],
        'rules': ['+2 Evasion'],
        'desc': (
            "Cannot ear if you have heavy, soluble, or shield gear, or any "
            'gear with <font class="inline_shield">3</font> or higher printed '
            "on it."
        ),
    },
    'skleaver': {
        'expansion': 'sunstalker',
        'name': 'Skleaver',
        'speed': 1,
        'accuracy': 5,
        'strength': 10,
        'keywords': ['weapon','melee','grand','heavy','two-handed','bone'],
        'desc': (
            'On the first <b>Perfect hit</b> each attack, this gains '
            '<b>devastating 1</b> until the end of the attack.'
        ),
        'affinities': {'top': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'desc': 'Loses the heavy keyword',
            'requires': {'puzzle': {'red': 1}, 'complete': {'red': 2}}
        },
    },
    'sky_harpoon': {
        'expansion': 'sunstalker',
        'name': 'Sky Harpoon',
        'affinities': {'left': 'red'},
        'speed': 2,
        'accuracy': 5,
        'strength': 5,
        'rules': ['Reach 3', 'Savage'],
        'desc': (
            'Once per showdown, if monster is in reach, roll 1d10. On a '
            '6+, you skewer it! It suffers 1 wound. Move it up to 3 spaces '
            'towards you.'
        ),
    },
    'sun_lure_and_hook': {
        'expansion': 'sunstalker',
        'name': 'Sun Lure and Hook',
        'keywords': ['item','tool'],
        'affinities': {'bottom': 'blue'},
        'desc': (
            'When you <b>depart</b>, gain +1 survival. After Hunt Phase setup, '
            'place the <b>Sky Fishing</b> event on any space.'
        ),
    },
    'sunshark_arrows': {
        'expansion': 'sunstalker',
        'name': 'Sunshark Arrows',
        'speed': 1,
        'accuracy': 4,
        'strength': 6,
        'keywords': ['items', 'ammunition', 'arrow', 'soluble'],
        'rules': ['Sharp','Ammo - Bow'],
        'desc': (
            '<b>Activation Limit 3:</b> May activate this up to 3 times per '
            'showdown (use tokens to track).'
        ),
    },
    'sunshark_bow': {
        'expansion': 'sunstalker',
        'name': 'Sunshark Bow',
        'keywords': ['weapon', 'melee', 'ranged', 'bow', 'two-handed'],
        'rules': ['Sharp', 'Range: 1'],
        'speed': 3,
        'accuracy': 6,
        'strength': 0,
        'affinities': {'bottom': 'red'},
        'affinity_bonus': {
            'desc': 'Gains +4 strength and <b>slow</>.',
            'requires': {
                'puzzle': {'red': 1},
                'complete': {'red': 2},
            }
        },
    },
    'sunspot_dart': {
        'expansion': 'sunstalker',
        'name': 'Sunspot Dart',
        'speed': 4,
        'accuracy': 7,
        'strength': 3,
        'affinities': {'right': 'red'},
        'keywords': ['weapon', 'ranged', 'thrown'],
        'rules': ['Range: 5', 'Deadly', 'Activation Limit 3'],
        'desc': (
            'When you hit, there is an inspiring flash! Survivors adjacent to '
            'the monster gain +1 survival.'
        ),
    },
    'sunspot_lantern': {
        'expansion': 'sunstalker',
        'name': 'Sunspot Lantern',
        'keywords': ['item', 'lantern'],
        'affinities': {'left': 'green', 'right': 'green'},
        'rules': ['+1 Accuracy'],
        'desc': (
            'You cast a 1 space shadow directly away from the monster. If the '
            'shadow can be cast in two spaces, decide which space has it '
            'until you move.'
        ),
    },
}
