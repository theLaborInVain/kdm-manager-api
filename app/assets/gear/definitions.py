'''

    Gear assets live here. Both for the 'core' game and the miscellaneous
    expansions that aren't big enough to justify their own file.

    The Collections object defaults to the dictionary name for 'type' of the
    assets where we can put them in a dictionary named for their location/type
    don't need a 'type' setting.

    Explicit is better than implicit and all that, but...sometimes you do the
    other thing anyway.

'''

barber_surgeon = {
    # barber surgeon
    'almanac': {
        'name': 'Almanac',
        'keywords': ['item','soluble','flammable'],
        'desc': (
            'When you <b>depart</b>, gain +2 insanity.<br/>You cannot gain '
            'disorders.'
        ),
        'affinities': {'right': 'blue'},
        'recipes': [
            {
                'locations': ['barber_surgeon'],
                'resource_types': {'leather': 2},
                'innovations': ['pictograph']
            },
        ],
    },
    'brain_mint': {
        'name': 'Brain Mint',
        'keywords': ['item', 'consumable'],
        'affinities': {'left': 'blue', 'top': 'green'},
        'desc': (
            '<font class="kdm_manager_font">A</font> <b>Consume:</b> Remove '
            'all your tokens and stand up. You may use this while knocked '
            'down. Use once per showdown.',
        ),
        'recipes': [
            {
                'locations': ['barber_surgeon'],
                'resource_handles': {'screaming_brain': 1},
            },
        ],
    },
    'bug_trap': {
        'name': 'Bug Trap',
        'keywords': ['item','soluble'],
        'desc': (
            'At the start of the showdown, roll 1d10. On a 3+, add a <b>Bug '
            'Patch</b> terrain card to the showdown board.'
        ),
        'recipes': [
            {
                'locations': ['barber_surgeon'],
                'resource_handles': {'muscly_gums': 1},
                'resource_types': {'bone':2}
            },
        ],
    },
    'elder_earrings': {
        'name': 'Elder Earrings',
        'keywords': ['item', 'jewelry'],
        'affinities': {'left': 'red', 'right': 'green', 'bottom': 'blue'},
        'desc': (
            'At the start of the <b>showdown</b>, gain +2 survival. +1 Hunt XP '
            'after a showdown.'
        ),
        'recipes': [
            {
                'locations': ['barber_surgeon'],
                'resource_handles': {'shank_bone': 1},
                'resource_types': {'scrap':1}
            },
        ],
    },
    'first_aid_kit': {
        'name': 'First Aid Kit',
        'affinities': {
            'top': 'green', 'left': 'green', 'right': 'green', 'bottom': 'green'
        },
        'keywords': ['item','heavy'],
        'desc': (
            'On <b>Arrival</b>, all survivors gain +3 survival.<br/>'
            '<font class="kdm_font">a</font>: Remove 1 bleeding or negative '
            'attribute token from yourself or an adjacent survivor.'
        ),
        'recipes': [
            {
                'locations': ['barber_surgeon'],
                'resource_types': {
                    'leather': 1,
                    'bone':2
                },
            },
        ],
    },
    'musk_bomb': {
        'name': 'Musk Bomb',
        'keywords': ['item','stinky','thrown','fragile'],
        'desc': (
            'If adjacent to monster when it draws '
            '<font class="kdm_font_10">b</font>, you may spend 2 survival and '
            'archive Musk Bomb to roll 1d10. On a 3+, discard '
            '<font class="kdm_font_10">b</font> without playing it.'
        ),
        'recipes': [
            {
                'locations': ['barber_surgeon'],
                'prefix_text': '7x resources',
                'innovations': ['pottery']
            },
        ],
    },
    'scavenger_kit': {
        'name': 'Scavenger Kit',
        'affinities': {'bottom': 'green'},
        'keywords': ['item','heavy'],
        'rules': ['Unique'],
        'desc': (
            'When you defeat a monster, gain either 1 random basic resource '
            "or 1 random monster resource from that monster's resource deck."
        ),
        'recipes': [
            {
                'locations': ['barber_surgeon'],
                'resource_types': {'scrap': 1},
                'resource_handles': {'pelt': 1}
            },
        ],
    },
    'speed_powder': {
        'name': 'Speed Powder',
        'keywords': ['item','soluble'],
        'desc': (
            '<font class="kdm_font">a</font>: Suffer 2 brain damage. '
            'Gain +1 speed token. Use once per showdown.'
        ),
        'affinities': {'right': 'blue'},
        'recipes': [
            {
                'locations': ['barber_surgeon'],
                'resource_types': {'organ': 2},
                'resource_handles': {'second_heart': 1}
            },
        ],
    },
}

blacksmith = {
    'beacon_shield': {
        'name': 'Beacon Shield',
        'keywords': ['weapon','melee','shield','metal','heavy'],
        'speed': 1,
        'accuracy': 6,
        'strength': 5,
        'rules': ['Block 2'],
        'desc': (
            'Add <font class="inline_shield">2</font> to all hit locations.'
            '<br/><b>Block 2:</b> Spend <font class="kdm_font">a</font> to '
            'ignore 2 hits the next time you are attacked. Lasts until your '
            'next act. You cannot use <b>block</b> more than once per attack.'
        ),
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'bone': 4},
                'resource_handles': {
                    'iron': 2,
                    'leather': 3
                },
            },
        ],
    },
    'dragon_slayer': {
        'name': 'Dragon Slayer',
        'affinities': {'top': 'blue', 'right': 'red'},
        'speed': 1,
        'accuracy': 6,
        'strength': 9,
        'keywords': [
            'weapon','melee','grand weapon','two-handed','heavy','metal'
        ],
        'rules': ['Frail', 'Slow','Sharp','Devastating 1', 'Early Iron'],
        'desc': (
            '<b>Early Iron:</b> When an attack roll result is 1, cancel any '
            'hits and end the attack.'
        ),
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'organ': 3},
                'resource_handles': {
                    'iron': 5,
                },
                'suffix_text': '<b>Paint</b> Required.'
            },
        ],
    },
    'lantern_armor_set': {
        'name': 'Lantern Armor Set',
        'desc': (
            'You feel invincible. On <b>Arrival</b>, gain survival up to the '
            'survival limit.<br/>The extra weight is leverage. All clubs in '
            'your gear grid gain <b>Sharp</b>.'
        ),
    },
    'lantern_cuirass': {
        'name': 'Lantern Cuirass',
        'armor': 5,
        'location': 'body',
        'keywords': ['armor','set','metal','heavy'],
        'desc': '-2 movement.',
        'affinities': {
            'top': 'blue', 'left': 'green', 'right': 'green', 'bottom': 'blue'
        },
        'affinity_bonus': {
            'desc': (
                'When you <b>depart</b>, add '
                '<font class="inline_shield">3</font> to all hit locations '
                'with metal armor.'
            ),
            'requires': {'puzzle': {'green': 2, 'blue': 2} },
        },
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_handles': {
                    'iron': 2,
                    'leather': 5,
                },
            },
        ],
    },
    'lantern_dagger': {
        'name': 'Lantern Dagger',
        'keywords': ['weapon','melee','dagger','finesse','metal'],
        'speed': 2,
        'accuracy': 7,
        'strength': 1,
        'affinities': {'right': 'red'},
        'rules': ['Paired','Sharp','Early Iron'],
        'desc': (
            '<b>Sharp:</b> Add 1d10 strength to each wound attempt.<br/>'
            '<b>Early Iron:</b> When an attack roll result is 1, cancel '
            'any hits and end the attack.'
        ),
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'bone': 2},
                'resource_handles': {
                    'iron': 1,
                    'leather': 4,
                },
            },
        ],
    },
    'lantern_gauntlets': {
        'name': 'Lantern Gauntlets',
        'armor': 5,
        'keywords': ['armor','set','metal','heavy'],
        'affinities': {'left': 'green'},
        'affinity_bonus': {
            'desc': '+2 accuracy with <b>club</b> weapons.',
            'requires': {'puzzle': {'green': 1}},
        },
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_handles': {
                    'iron': 2,
                    'leather': 6,
                },
            },
        ],
    },
    'lantern_glaive': {
        'name': 'Lantern Glaive',
        'keywords': [
            'weapon','melee','spear','axe','two-handed','finesse','metal'
        ],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'rules': ['Reach 2', 'Sharp','Early Iron'],
        'affinities': {'bottom': 'green'},
        'desc': (
            '<b>Sharp:</b> Add 1d10 strength to each wound attempt.<br/>'
            '<b>Early Iron:</b> When an attack roll result is 1, cancel '
            'any hits and end the attack.'
        ),
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'bone': 4},
                'resource_handles': {
                    'iron': 2,
                    'leather': 2,
                },
            },
        ],
    },
    'lantern_greaves': {
        'name': 'Lantern Greaves',
        'keywords': ['armor','set','metal','heavy'],
        'affinity_bonus':{
            'desc': '+2 movement.',
            'requires': {'puzzle': {'red':2,'blue':1}},
        },
        'affinities': {'left': 'red','right': 'red','top': 'blue'},
        'armor': 5,
        'location': 'legs',
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_handles': {
                    'iron': 1,
                    'leather': 5,
                },
            },
        ],
    },
    'lantern_helm': {
        'type': 'blacksmith',
        'name': 'Lantern Helm',
        'keywords': ['armor','set','metal','heavy'],
        'armor': 5,
        'location': 'head',
        'affinities': {'bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'Ear Plugs. You are <b>deaf</b>, -1 accuracy.',
            'requires': {'puzzle': {'blue': 1,}},
        },
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'bone': 7},
                'resource_handles': {
                    'iron': 1,
                },
            },
        ],
    },
    'lantern_mail': {
        'name': 'Lantern Mail',
        'keywords': ['armor','set','metal','heavy'],
        'armor': 5,
        'location': 'waist',
        'affinities': {'right': 'green'},
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'organ': 5},
                'resource_handles': {
                    'iron': 1,
                },
            },
        ],
    },
    'lantern_sword': {
        'name': 'Lantern Sword',
        'affinities': {'left': 'red'},
        'keywords': ['weapon','melee','sword','finesse','metal'],
        'speed': 3,
        'accuracy': 5,
        'strength': 3,
        'desc': (
            '<b>Sharp:</b> Add 1d10 strength to each wound attempt.<br/>'
            '<b>Early Iron:</b> When an attack roll result is 1, cancel any '
            'hits and end the attack.'
        ),
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'bone': 5, 'hide': 3},
                'resource_handles': {
                    'iron': 1,
                },
            },
        ],
    },
    'polishing_lantern': {
        'name': 'Polishing Lantern',
        'min_version': 'core_1_6',
        'keywords': ['item', 'metal', 'lantern'],
        'affinities': {'left': 'red'},
        'rules': ['Ignore Early Iron'],
        'desc': (
            'Spend <font class="kdm_font">a</font> to polish the edge of your '
            "or an adjacent survivor's finesse weapon. It gains +4 strength "
            'for its next attack. Limit once per attack.'
        ),
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'organ': 1, 'scrap': 1},
                'resource_handles': {
                    'iron': 1,
                },
            },
        ],
    },
    'perfect_slayer': {
        'name': 'Perfect Slayer',
        'keywords': [
            'weapon','melee','grand weapon','two-handed',
            'sword', 'heavy', 'finesse', 'metal',
        ],
        'desc': '-2 movement',
        'rules': ['Slow','Sharp','Devastating 2','Irreplaceable'],
        'affinities': {'bottom': 'red'},
        'speed': 3,
        'accuracy': 6,
        'strength': 14,
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'organ': 3},
                'resource_handles': {
                    'iron': 9,
                },
                'suffix_text': '<b>Perfect Crucible</b> Required.',
            },
        ],
    },
    'ring_whip': {
        'name': 'Ring Whip',
        'rules': ['Sharp','Reach 2'],
        'affinities': {'left': 'blue'},
        'keywords': ['weapon','melee','whip','finesse','metal'],
        'desc': (
            '<b>Early Iron:</b> When an attack roll result is 1, cancel any '
            'hits and end the attack.'
        ),
        'speed': 2,
        'accuracy': 5,
        'strength': 0,
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'bone': 3, 'organ': 3},
                'resource_handles': {
                    'iron': 1,
                },
            },
        ],
    },
    'scrap_shield': {
        'name': 'Scrap Shield',
        'keywords': ['weapon','melee','shield','bone','metal'],
        'affinities': {'right': 'red'},
        'rules': ['Block 1'],
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
            '<br/><b>Block 1:</b> Spend <font class="kdm_font">a</font> to '
            'ignore 1 hit the next time you are attacked. Lasts until your '
            'next act. You cannot use <b>block</b> more than once per attack.'
        ),
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
        'recipes': [
            {
                'locations': ['blacksmith'],
                'resource_types': {'bone': 3, 'scrap': 2},
                'resource_handles': {
                    'leather': 3,
                },
            },
        ],
    },
}

core = {
    # bone smith
    'bone_axe': {
        'type': 'bone_smith',
        'name': 'Bone Axe',
        'rules': ['Frail','Savage'],
        'keywords': ['weapon','melee','axe','bone'],
        'recipes': [
            {'locations': ['bone_smith'], 'resource_types': {'bone':1, 'organ':1} },
        ],
        'speed': 2,
        'accuracy': 6,
        'strength': 3,
        'affinities': {'left': 'red',},
        'desc': '<b>Savage:</b> Once per attack, if you critically wound, cause 1 additional wound. This effect does not apply to impervious hit locations.',
    },
    'bone_blade': {
        'type': 'bone_smith',
        'name': 'Bone Blade',
        'rules': ['Frail'],
        'keywords': ['weapon','melee','sword','bone'],
        'recipes': [
            {'locations': ['bone_smith'], 'resource_types': {'bone':1}, },
        ],
        'speed': 2,
        'accuracy': 6,
        'strength': 2,
        'affinities': {'left': 'red'},
        'desc': '<b>Frail:</b> When you attempt to wound a super-dense hit location, this weapon breaks.<br/>Archive this card at the end of the attack.',
    },
    'bone_club': {
        'type': 'bone_smith',
        'name': 'Bone Club',
        'keywords': ['weapon','melee','two-handed','heavy','club','bone'],
        'rules': ['Cumbersome'],
        'recipes': [
            {'locations': ['bone_smith'], 'resource_types': {'bone':3}, },
        ],
        'speed': 2,
        'accuracy': 6,
        'strength': 5,
        'affinities': {'left': 'red', 'right': 'red'},
        'desc': (
            '<b>Cumbersome:</b> Spend <font class="kdm_font">c</font> as an '
            'additional cost to activate this weapon. Ignore Cumbersome if '
            'this weapon is activated indirectly (Pounce, Charge, etc.).'
        ),
    },
    'bone_dagger': {
        'type': 'bone_smith',
        'name': 'Bone Dagger',
        'keywords': ['weapon','melee','dagger','bone'],
        'desc': 'On a <b>Perfect hit</b>, gain +1 survival.<br/><b>Perfect Hit:</b> An attack roll result of a lantern 10.',
        'recipes': [
            {'locations': ['bone_smith'], 'resource_types': {'bone':1}, },
        ],
        'affinities': {'top': 'red'},
        'speed': 3,
        'accuracy': 7,
        'strength': 1,
    },
    'bone_darts': {
        'type': 'bone_smith',
        'name': 'Bone Darts',
        'rules': ['Range: 6', 'Frail'],
        'keywords': ['weapon','ranged','thrown','bone'],
        'recipes': [
            {'locations': ['bone_smith'], 'resource_types': {'bone':1}, },
        ],
        'desc': '<b>Frail:</b> When you attempt to wound a super-dense hit location, this weapon breaks. Archive this card at the end of the attack.',
        'speed': 1,
        'accuracy': 7,
        'strength': 3,
        'affinities': {'left': 'red'},
    },
    'bone_pickaxe': {
        'affinities': {'top': 'green'},
        'type': 'bone_smith',
        'name': 'Bone Pickaxe',
        'keywords': ['item','tool','pickaxe','bone'],
        'desc': 'After Hunt phase setup, place the <b>Mineral Gathering</b> event on any hunt space.',
        'recipes': [
            {
                'locations': ['bone_smith'],
                'innovations': ['ammonia'],
                'resource_types': {'bone': 1},
                'resource_handles': {'leather': 1},
            },
        ],
        'speed': 1,
        'accuracy': 8,
        'strength': 2,
    },
    'bone_sickle': {
        'type': 'bone_smith',
        'name': 'Bone Sickle',
        'keywords': ['item','tool','sickle','bone'],
        'desc': 'After Hunt phase setup, place the <b>Herb Gathering</b> event on any hunt space.',
        'recipes': [
            {
                'locations': ['bone_smith'],
                'innovations': ['ammonia'],
                'resource_types': {'bone': 1},
                'resource_handles': {'leather': 1},
            },
        ],
        'affinities': {'top': 'green'},
        'speed': 2,
        'accuracy': 8,
        'strength': 1,
    },
    'skull_helm': {
        'type': 'bone_smith',
        'name': 'Skull Helm',
        'location': 'head',
        'armor': 3,
        'affinities': {'bottom': 'red'},
        'keywords': ['armor','bone','fragile'],
        'desc': 'When you suffer a severe head injury, the Skull Helm is destroyed. Archive this card.',
        'recipes': [
            {'locations': ['bone_smith'], 'resource_types': {'bone':2} },
            {'locations': ['bone_smith'], 'resource_handles': {'skull':1} },
        ],
    },

    # catarium
    'cat_eye_circlet': {
        'type': 'catarium',
        'name': 'Cat Eye Circlet',
        'keywords': ['item','jewelry','other'],
        'desc': '<font class="kdm_font">a</font>: Reveal the next 3 monster hit locations and put them back in any order.',
        'affinities': {'left': 'blue'},
    },
    'cat_fang_knife': {
        'type': 'catarium',
        'name': 'Cat Fang Knife',
        'keywords': ['weapon','melee','dagger','bone'],
        'speed': 3,
        'accuracy': 6,
        'strength': 2,
        'affinities': {'top': 'red', 'left':'red','right':'red','bottom':'red'},
        'affinity_bonus': {
            'desc':'On a <b>perfect hit</b>, gain +1 strength token. When knocked down, remove all your +1 strength tokens.',
            'requires': {'complete':{'red':3}},
        },
    },
    'cat_gut_bow': {
        'type': 'catarium',
        'name': 'Cat Gut Bow',
        'keywords': ['weapon','ranged','bow','two-handed'],
        'rules': ['Cumbersome', 'Range: 6'],
        'related_rules': ['cumbersome', 'range_x'],
        'desc': (
            '<b>Aim:</b> When you attack, before rolling to hit, you may '
            'reduce the speed of this weapon by 1 to gain +2 accuracy for '
            'that attack.'
        ),
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
        'affinities': {'top': 'blue'},
    },
    'claw_head_arrow': {
        'type': 'catarium',
        'name': 'Claw Head Arrow',
        'keywords': ['item','ammuntion','arrow'],
        'rules': ['Slow','Ammo - Bow'],
        'desc': '<b>Slow, Ammo-Bow:</b> You must have a bow in your gear grid to activate this.<br/>If you hit, monster gains -1 evasion token. Use once per showdown.',
        'speed': 1,
        'accuracy': 6,
        'strength': 6,
        'affinities': {'right': 'blue'},
    },
    'frenzy_drink': {
        'type': 'catarium',
        'name': 'Frenzy Drink',
        'keywords': ['item','consumable','fragile'],
        'desc': '<font class="kdm_font">a</font> <b>Consume:</b> Suffer <b>Frenzy</b> brain trauma. Can be used once per showdown.',
    },
    'king_spear': {
        'type': 'catarium',
        'name': 'King Spear',
        'keywords': ['weapon','melee','spear','heavy','two-handed'],
        'rules': ['Reach 2'],
        'affinities': {'right': 'red'},
        'speed': 2,
        'accuracy': 6,
        'strength': 3,
        'desc': '<b>Reach 2:</b> May attack from 2 spaces away.',
    },
    'lion_beast_katar': {
        'type': 'catarium',
        'name': 'Lion Beast Katar',
        'keywords': ['weapon','melee','katar'],
        'rules': ['Deadly','Paired'],
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
        'desc': '<b>Deadly:</b> +1 luck with this weapon.<br/><b>Paired:</b> When you attack, add the speed of a 2<sup>nd</sup> Lion Beast Katar in your gear grid.',
    },
    'lion_headdress': {
        'type': 'catarium',
        'name': 'Lion Headdress',
        'keywords': ['item','flammable'],
        'rules': ['Accessory'],
        'armor': 1,
        'location': 'head',
        'desc': '<b>Accessory:</b> You may wear this in addition to 1 armor at this hit location',
    },
    'lion_skin_cloak': {
        'type': 'catarium',
        'name': 'Lion Skin Cloak',
        'keywords': ['armor','fur','bone','heavy','flammable'],
        'desc': 'Reduce damage from every hit suffered by 1, to a minimum of 1.',
        'armor': 0,
        'location': 'body',
        'affinities': {'green': 'right'},
    },
    'whisker_harp': {
        'type': 'catarium',
        'name': 'Whisker Harp',
        'keywords': ['item','instrument','noisy'],
        'desc': 'On <b>Arrival</b>, all survivors gain +1 survival.<br/><font class="kdm_font">a</font>: Strum, roll 1d10. On a result of 6+ discard 1 <b>mood</b> currently in play.',
        'affinities': {'left': 'blue'},
    },
    'white_lion_armor_set': {
        'type': 'catarium',
        'name': 'White Lion Armor Set',
        'desc': 'Add <font class="inline_shield">1</font> to all hit locations.<br/>Your weapons are your claws! Gain +1 speed and +2 strength when attacking with daggers or katars.',
    },
    'white_lion_boots': {
        'type': 'catarium',
        'name': 'White Lion Boots',
        'keywords': ['armor','set','fur','heavy'],
        'armor': 2,
        'location': 'legs',
        'affinities': {'right': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'desc': '+1 movement',
            'requires': {'puzzle': {'red': 2}},
        },
    },
    'white_lion_coat': {
        'type': 'catarium',
        'name': 'White Lion Coat',
        'desc': (
            '<b>Pounce:</b> Spend <font class="kdm_manager_font">M</font> and '
            '<font class="kdm_manager_font">A</font> to move 3 spaces in a '
            'straight line. Then, if you moved 3 spaces, activate a melee '
            'weapon with +1 strength.'
        ),
        'armor': 2,
        'location': 'body',
        'affinities': {'top': 'blue'},
    },
    'white_lion_gauntlets': {
        'type': 'catarium',
        'name': 'White Lion Gauntlet',
        'keywords': ['armor','set','fur','heavy'],
        'desc': (
            'When you <b>Pounce</b>, gain +1 accuracy for your next attack '
            'this turn.'
        ),
        'armor': 2,
        'location': 'arms',
    },
    'white_lion_helm': {
        'type': 'catarium',
        'name': 'White Lion Helm',
        'keywords': ['armor','set','fur','heavy'],
        'armor': 2,
        'location': 'head',
        'affinities': {'bottom': 'red'},
        'affinity_bonus': {
            'desc': (
                '<font class="kdm_font">a</font> and 1 survival: Roar. '
                '<b>Non-Deaf Insane</b> survivors gain +2 strength until end '
                'of round. All other survivors gain +1 insanity.'
            ),
            'requires': {
                'puzzle': {'red': 1},
                'complete': {'blue': 1},
            },
        },
    },
    'white_lion_skirt': {
        'type': 'catarium',
        'name': 'White Lion Skirt',
        'keywords': ['armor','set','fur','heavy'],
        'armor':2,
        'location': 'waist',
        'affinities': {'right': 'red', 'left': 'red'},
    },


    # exhausted lantern hoard
    'final_lantern': {
        'type': 'exhausted_lantern_hoard',
        'name': 'Final Lantern',
        'keywords': ['item','other'],
        'rules': ['Vital'],
        'affinities': {'left': 'blue', 'top': 'green'},
        'desc': (
            "On <b>Arrival</b>, all survivors gain the <b>Horripilation</b> "
            "survivor status card. (See the Watcher's AI Deck.) When not "
            "<b>insane</b>, flip this card."
        ),
    },
    'oxidized_beacon_shield': {
        'type': 'exhausted_lantern_hoard',
        'name': 'Oxidized Beacon Shield',
        'keywords': ['weapon','melee','shield','metal','heavy'],
        'speed':1,
        'accuracy':6,
        'strength':6,
        'rules': ['Deflect 2'],
        'desc': 'Add <font class="inline_shield">2</font> to all hit locations.<br/><b>Deflect 2</b>: Spend <font class="kdm_font">a</font>. You now have exactly 2 deflect tokens. The next 2 times you are hit, ignore a hit and and lose 1 deflect token.',
    },
    'oxidized_lantern_dagger': {
        'type': 'exhausted_lantern_hoard',
        'name': 'Oxidized Lantern Dagger',
        'keywords': ['weapon','melee','dagger','finesse','metal'],
        'speed': 3,
        'accuracy': 6,
        'strength': 4,
        'rules': ['Sharp','Paired'],
        'affinities': {'left': 'red', 'right': 'red'},
        'affinity_bonus': {
            'desc': 'On a <b>Perfect hit</b>, gain +1 survival.',
            'requires': {
                'puzzle': {'red': 1},
                'complete': {'red': 1},
            },
        },
    },
    'oxidized_lantern_glaive': {
        'type': 'exhausted_lantern_hoard',
        'name': 'Oxidized Lantern Glaive',
        'keywords': [
            'weapon','melee','spear','axe','two-handed','finesse','metal'
        ],
        'affinities': {'bottom': 'green'},
        'rules': ['Sharp','Reach 2'],
        'speed': 2,
        'accuracy': 5,
        'strength': 6,
        'affinity_bonus':{
            'desc': (
                'On a <b>Perfect hit</b>, the edge sharpens. This weapon '
                'gains +4 strength for this attack.'
            ),
            'requires': {
                'puzzle': {'green': 1},
                'complete': {'red': 1},
            },
        },
    },
    'oxidized_lantern_helm': {
        'type': 'exhausted_lantern_hoard',
        'name': 'Oxidized Lantern Helm',
        'armor': 6,
        'location': 'head',
        'keywords': ['armor','set','metal'],
        'rules': ['Outfit'],
        'related_rules': ['outfit'],
        'affinities': {'bottom': 'blue'},
        'affinity_bonus': {
            'desc': (
                'If you are not deaf, you may ignore effects that target '
                'non-deaf survivors.'
            ),
            'requires':{
                'puzzle': {'blue': 1},
                'complete': {'red': 1},
            },
        },
    },
    'oxidized_lantern_sword': {
        'type': 'exhausted_lantern_hoard',
        'name': 'Oxidized Lantern Sword',
        'keywords': ['weapon','melee','sword','finesse','metal'],
        'affinities': {'right': 'red'},
        'speed': 3,
        'accuracy': 5,
        'strength': 5,
        'rules': ['Sharp','Deflect 1'],
        'desc': '<b>Deflect 1</b>: Spend <font class="kdm_font">a</font>. You now have exactly 1 deflect token. The next 1 time you are hit, ignore a hit and and lose 1 deflect token.',
    },
    'oxidized_ring_whip': {
        'type': 'exhausted_lantern_hoard',
        'name': 'Oxidized Ring Whip',
        'keywords': ['weapon','melee','whip','finesse','metal'],
        'rules': ['Sharp','Reach 2'],
        'affinities': {'left': 'blue'},
        'speed': 2,
        'accuracy': 5,
        'strength': 3,
        'affinity_bonus': {
            'desc': 'Gains <b>Provoke</b> (see Rawhide Whip).',
            'requires': {
                'puzzle': {'blue': 1},
                'complete': {'red': 3},
            },
        },
    },
    "survivors_lantern": {
        'type': 'exhausted_lantern_hoard',
        'name': "Survivor's Lantern",
        'keywords': ['item','lantern'],
        'affinities': {'left': 'red', 'bottom': 'blue', 'right': 'green'},
    },

    # leather worker
    'hunter_whip': {
        'type': 'leather_worker',
        'name': 'Hunter Whip',
        'affinities': {'top': 'blue', 'right': 'blue'},
        'keywords': ['weapon', 'melee','whip','leather'],
        'speed': 3,
        'accuracy': 6,
        'strength': 3,
        'affinity_bonus': {
            'desc': 'On a <b>Perfect hit</b>, discard 1 mood in play.',
            'requires': {'puzzle': {'blue': 2}},
        },
        'recipes': [
            {'locations': ['leather_worker'], 'resource_types': {'leather':2, 'bone': 1}, },
        ],
    },
    'leather_armor_set': {
        'type': 'leather_worker',
        'name': 'Leather Armor Set',
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
            '<br/>You ignore <b>bash</b>.'
        ),
    },
    'leather_boots': {
        'type': 'leather_worker',
        'name': 'Leather Boots',
        'armor': 3,
        'location': 'legs',
        'affinities': {'left': 'green', 'right': 'green'},
        'affinity_bonus': {
            'desc': 'At the end of your act, you may move 1 space.',
            'requires': {'puzzle': {'green': 2}},
        },
        'keywords': ['armor','set','leather'],
        'recipes': [
            {
                'locations': ['leather_worker'],
                'resource_types': {'leather':1, 'hide': 1},
            },
        ],
    },
    'leather_bracers': {
        'type': 'leather_worker',
        'name': 'Leather Bracers',
        'armor': 3,
        'location': 'arms',
        'keywords': ['armor','set','leather'],
        'desc': 'When you <b>depart</b>, gain +2 survival.',
        'affinities': {'right': 'green'},
        'recipes': [
            {'locations': ['leather_worker'], 'resource_types': {'leather':1, 'hide':1} },
        ],
    },
    'leather_cuirass': {
        'type': 'leather_worker',
        'name': 'Leather Cuirass',
        'armor': 3,
        'location': 'body',
        'keywords': ['armor','set','leather'],
        'affinities': {'top': 'red', 'bottom': 'blue'},
        'recipes': [
            {'locations': ['leather_worker'], 'resource_types': {'leather':1, 'bone':1} },
        ],
    },
    'leather_mask': {
        'type': 'leather_worker',
        'name': 'Leather Mask',
        'armor': 3,
        'location': 'head',
        'keywords': ['armor','set','leather'],
        'affinities': {'top': 'blue', 'bottom': 'red'},
        'desc': 'When you <b>depart</b>, gain +2 insanity.',
        'recipes': [
            {'locations': ['leather_worker'], 'resource_types': {'leather':1, 'scrap':1} },
        ],
    },
    'leather_skirt': {
        'type': 'leather_worker',
        'name': 'Leather Skirt',
        'armor':3,
        'location': 'waist',
        'affinities': {'bottom': 'green'},
        'keywords': ['armor','set','leather'],
        'recipes': [
            {'locations': ['leather_worker'], 'resource_types': {'leather':1}, },
        ],
    },
    'round_leather_shield': {
        'type': 'leather_worker',
        'name': 'Round Leather Shield',
        'keywords': ['weapon','melee','shield','leather'],
        'rules': ['Block 1'],
        'speed': 1,
        'accuracy': 8,
        'strength': 1,
        'desc': 'Add <font class="inline_shield">1</font> to all hit locations.<br/><b>Block 1:</b> Spend <font class="kdm_font">a</font> to ignore 1 hit the next time you are attacked. Lasts until your next act. You cannot use <b>block</b> more than once per attack.',
        'affinities': {'top': 'green'},
        'recipes': [
            {'locations': ['leather_worker'], 'resource_types': {'leather':1, 'bone':1, 'hide': 1}, },
        ],
    },

    # mask maker
    'antelope_mask': {
        'type': 'mask_maker',
        'name': 'Antelope Mask',
        'keywords': ['item','mask','bone','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'recipes': [
            {'locations': ['mask_maker'], 'resource_handles': {'pelt':1}, 'resource_types': {'bone': 6, 'organ': 4}, },
        ],
    },
    'death_mask': {
        'type': 'mask_maker',
        'name': 'Death Mask',
        'keywords': ['item','mask','bone','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'desc': 'If you have no affinities, gain +4 luck and suffer -4 to all severe injury rolls.',
        'recipes': [
            {'locations': ['mask_maker'], 'prefix_text': '-1 population', 'resource_types': {'bone': 6, 'organ': 4}, },
        ],
    },
    'god_mask': {
        'type': 'mask_maker',
        'name': 'God Mask',
        'keywords': ['item','mask','bone','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'recipes': [
            {'locations': ['mask_maker'], 'gear_handles': {'founding_stone':1}, 'resource_types': {'bone': 6, 'organ': 4}, },
        ],
    },
    'man_mask': {
        'type': 'mask_maker',
        'name': 'Man Mask',
        'keywords': ['item','mask','bone','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'recipes': [
            {'locations': ['mask_maker'], 'resource_handles': {'skull':1}, 'resource_types': {'bone': 6, 'organ': 4}, },
        ],
    },
    'phoenix_mask': {
        'type': 'mask_maker',
        'name': 'Phoenix Mask',
        'keywords': ['item','mask','bone','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'recipes': [
            {
                'locations': ['mask_maker'],
                'resource_handles': {'small_feathers':1},
                'resource_types': {'bone': 6, 'organ': 4},
            },
        ],
    },
    'white_lion_mask': {
        'type': 'mask_maker',
        'name': 'White Lion Mask',
        'keywords': ['item','mask','bone','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'recipes': [
            {'locations': ['mask_maker'], 'resource_handles': {'shimmering_mane':1}, 'resource_types': {'bone': 6, 'organ': 4}, },
        ],
    },

    # organ grinder
    'dried_acanthus': {
        'type': 'organ_grinder',
        'name': 'Dried Acanthus',
        'keywords': ['item', 'herb', 'consumable'],
        'desc': (
            'When you <b>depart</b>, gain +2 survival. When you suffer a '
            'severe injury, ignore it and archive this card instead.'
        ),
        'recipes': [
            {
                'locations': ['organ_grinder'],
                'resource_handles': {'fresh_acanthus':1}
            },
        ],
    },
    'fecal_salve': {
        'type': 'organ_grinder',
        'name': 'Fecal Salve',
        'keywords': ['item','balm','stinky'],
        'desc': (
            'When you <b>depart</b>, gain +1 survival<br/>'
            '<font class="kdm_font">a</font>: You are not a <b>threat</b> '
            'until you attack. If you have the <b>priority target</b> token, '
            'remove it.'
        ),
        'affinities': {'left': 'blue'},
        'recipes': [
            {'locations': ['organ_grinder'], 'resource_types': {'organ':1} },
        ],
    },
    'lucky_charm': {
        'type': 'organ_grinder',
        'name': 'Lucky Charm',
        'keywords': ['item','jewelry'],
        'affinities': {'left': 'blue', 'right': 'blue'},
        'affinity_bonus':{
            'desc': '+1 luck',
            'requires': {'complete': {'blue': 2}},
        },
        'recipes': [
            {'locations': ['organ_grinder'], 'resource_types': {'organ':1} },
        ],
    },
    'monster_grease': {
        'type': 'organ_grinder',
        'name': 'Monster Grease',
        'keywords': ['item','consumable','soluble','stinky'],
        'desc': 'Gain +1 evasion.',
        'affinities': {'left': 'green'},
        'affinity_bonus': {
            'desc': '+1 evasion',
            'requires': {'complete': {'green': 3}},
        },
        'recipes': [
            {'locations': ['organ_grinder'], 'resource_types': {'organ':1} },
        ],
    },
    'monster_tooth_necklace': {
        'type': 'organ_grinder',
        'name': 'Monster Tooth Necklace',
        'keywords': ['item','jewelry','bone'],
        'desc': 'Gain +1 strength.',
        'affinities': {'right': 'red'},
        'affinity_bonus': {
            'desc': '+1 strength',
            'requires': {'complete': {'red': 2}},
        },
        'recipes': [
            {
                'locations': ['organ_grinder'],
                'resource_types': {'scrap':1, 'bone': 1},
                'prefix_text': '<b>Heat</b> Required.'
            },
        ],
    },
    'stone_noses': {
        'type': 'organ_grinder',
        'name': 'Stone Noses',
        'keywords': ['item','jewelry'],
        'desc': (
            'On <b>Arrival</b>, gain +1 survival, +1 insanity.<br/>'
            '<b>Arrival:</b> At the start of the showdown.'
        ),
    },

    # plumery
    'arc_bow': {
        'type': 'plumery',
        'name': 'Arc Bow',
        'keywords': ['weapon', 'ranged', 'bow', 'two-handed'],
        'speed': 1,
        'accuracy': 6,
        'strength': 9,
        'rules': ['Slow','Range 6'],
        'desc': (
            '<b>Cumbersome:</b> Spend <font class="kdm_font">c</font> as an '
            'additional cost of activating this weapon.'
        ),
        'affinities': {'left': 'red', 'right': 'green'},
        'affinity_bonus': {
            'desc': 'Range +2',
            'requires': {
                'puzzle': {'red': 1, 'green': 1},
                'complete': {'blue': 1},
            }
        },
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'phoenix_whisker': 1,
                    'wishbone': 1,
                },
                'resource_types': {
                    'scrap': 1,
                },
            },
        ],
    },
    'bird_bread': {
        'type': 'plumery',
        'name': 'Bird Bread',
        'keywords': ['item','consumable','soluble'],
        'affinities': {'right': 'green'},
        'desc': (
            '<font class="kdm_font">a</font> <b>Consume:</b> Once per '
            'showdown, add <font class="inline_shield">1</font> to all hit '
            'locations. Gain <b>priority target</b> token. Roll 1d10. On a 1, '
            'reduce your survival to 0.'
        ),
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'pustules': 1,
                },
                'resource_types': {
                    'hide': 3,
                },
            },
        ],
    },
    'bloom_sphere': {
        'type': 'plumery',
        'name': 'Bloom Sphere',
        'keywords': ['item','stinky','other'],
        'affinities': {'left': 'green', 'right': 'blue'},
        'affinity_bonus': {
            'desc': (
                'When you are picked as a target, roll 1d10. On a 6+, the '
                'monster must pick a new target, if possible.'
            ),
            'requires': {'puzzle': {'green': 1, 'blue':1} },
        },
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'small_hand_parasites': 1,
                },
                'resource_types': {
                    'bone': 3,
                },
            },
        ],
    },
    'crest_crown': {
        'type': 'plumery',
        'name': 'Crest Crown',
        'keywords': ['item', 'other'],
        'affinities':
            {'top': 'blue', 'left': 'red', 'right': 'green', 'bottom': 'blue'},
        'desc': (
            '<font class="kdm_font">a</font>: If <b>insane</b>, reshuffle hit '
            'location deck.'
        ),
        'affinity_bonus': {
            'desc': (
                'When you depart, gain +1 insanity and +1 survival for '
                'every <font class="kdm_font_2 affinity_blue_text">h</font> '
                'you have.'
            ),
            'requires': {'puzzle': {'red': 1, 'blue':2}},
        },
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'phoenix_crest': 1,
                },
                'resource_types': {
                    'organ': 6,
                },
            },
        ],
    },
    'feather_mantle': {
        'type': 'plumery',
        'name': 'Feather Mantle',
        'keywords': ['item', 'flammable'],
        'affinities': {'left': 'blue', 'right': 'green', 'bottom': 'red'},
        'desc': (
            'When you suffer <b>knockback</b>, you may ignore <b>collision</b> '
            'with other survivors and reduce movement by up to 3 spaces.'
        ),
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'tail_feathers': 2,
                },
                'resource_types': {
                    'scrap': 1,
                },
            },
        ],
    },
    'feather_shield': {
        'type': 'plumery',
        'name': 'Feather Shield',
        'keywords': ['weapon','melee','shield','flammable'],
        'speed': 3,
        'accuracy': 7,
        'strength': 0,
        'rules': ['Block 1'],
        'affinities': {'top': 'blue'},
        'affinity_bonus':{
            'desc':'Reduce any suffered brain damage by 1 to a minimum of 1.',
            'requires': {'complete': {'red': 1, 'blue': 1, 'green': 1}}
        },
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'small_feathers': 2,
                    'muculent_droppings': 1,
                },
            },
        ],
    },
    'hollow_sword': {
        'type': 'plumery',
        'name': 'Hollow Sword',
        'keywords': ['weapon','melee','sword','bone'],
        'speed': 3,
        'accuracy': 5,
        'strength': 3,
        'rules': ['Frail', 'Paired'],
        'desc': (
            'On a <b>perfect hit</b>, make 1 additional attack roll.'
        ),
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'hollow_wing_bones': 1,
                },
                'resource_types': {
                    'bone': 2,
                    'hide': 2,
                },
            },
        ],
    },
    'hollowpoint_arrow': {
        'type': 'plumery',
        'name': 'Hollowpoint Arrow',
        'keywords': ['item','ammunition','arrow'],
        'speed': 1,
        'accuracy': 6,
        'strength': 11,
        'rules': ['Slow','Ammo - Bow'],
        'related_rules': ['slow'],
        'desc':
            'On a hit, monster gains -1 movement token. Use once per showdown.',
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'hollow_wing_bones': 1,
                },
                'resource_types': {
                    'scrap': 1,
                },
            },
        ],
    },
    'hours_ring': {
        'type': 'plumery',
        'name': 'Hours Ring',
        'keywords': ['item','other'],
        'rules': ['Unique', 'Selfish'],
        'related_rules': ['unique', 'selfish'],
        'desc': (
            'Do not gain any tokens for any reason. Do not gain Hunt XP or '
            'weapon proficiency. <b>Retired</b> wearers can <b>depart</b>.'
        ),
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'shimmering_halo': 1,
                },
                'resource_types': {'organ': 5},
            },
        ],
    },
    'phoenix_armor_set': {
        'type': 'plumery',
        'name': 'Phoenix Armor Set',
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
            '<br/><b>Charge:</b> Spend <font class="kdm_font">c a</font>, '
            'full move in a straight line. At the end of the movement, '
            'activate a melee weapon and attack. Add the number of spaces you '
            'moved to your strength for the attack.'
        ),
    },
    'phoenix_faulds': {
        'type': 'plumery',
        'name': 'Phoenix Faulds',
        'keywords': ['armor','set','feather','metal','flammable'],
        'armor': 4,
        'location': 'waist',
        'desc': 'When you <b>depart</b>, gain +1 insanity.',
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'iron': 1,
                    'leather': 1,
                    'tail_feathers': 1,
                },
                'resource_types': {'organ':1},
            },
        ],
    },
    'phoenix_gauntlet': {
        'type': 'plumery',
        'name': 'Phoenix Gauntlet',
        'armor': 4,
        'location': 'arms',
        'keywords': ['armor','set','feather','metal','flammable'],
        'desc': 'When you <b>depart</b>, gain +1 insanity.',
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_types': {'bone':1},
                'resource_handles': {
                    'iron': 1,
                    'leather': 1,
                    'small_feathers': 1,
                },
            },
        ],
    },
    'phoenix_greaves': {
        'type': 'plumery',
        'name': 'Phoenix Greaves',
        'keywords': ['armor','set','feather','metal','flammable'],
        'affinities': {'right': 'red'},
        'armor': 4,
        'location': 'legs',
        'desc': 'If <b>insane</b>, gain +2 movement.',
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'iron': 1,
                    'leather': 1,
                    'small_feathers': 1,
                },
                'resource_types': {'organ':1},
            },
        ],
    },
    'phoenix_helm': {
        'type': 'plumery',
        'name': 'Phoenix Helm',
        'keywords': ['armor', 'set', 'feather', 'metal', 'flammable'],
        'armor': 4,
        'location': 'head',
        'affinities': {'bottom': 'blue'},
        'affinity_bonus': {
            'desc': (
                'If <b>insane</b> at the start of the showdown, gain +1 evasion '
                'token.'
            ),
            'requires': {
                'puzzle': {'blue':1},
                'complete': {'green': 1, 'red': 1},
            },
        },
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_types': {'bone':1},
                'resource_handles': {
                    'small_feathers': 1,
                    'hollow_wing_bones': 1,
                },
            },
        ],
    },
    'phoenix_plackart': {
        'type': 'plumery',
        'name': 'Phoenix Plackart',
        'keywords': ['armor','set','feather','metal','flammable'],
        'location': 'body',
        'armor': 4,
        'affinities': {'top': 'blue', 'left': 'green', 'right': 'red'},
        'affinity_bonus':{
            'desc': (
                'If <b>insane</b>, ignore the first hit each round and suffer '
                '1 brain damage instead.'
            ),
            'requires':{
                'puzzle': {'red':1, 'blue':1, 'green':1},
            },
        },
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'iron': 1,
                    'leather': 1,
                    'tail_feathers': 1,
                },
                'resource_types': {'hide':1},
            },
        ],
    },
    'sonic_tomahawk': {
        'type': 'plumery',
        'name': 'Sonic Tomahawk',
        'speed': 3,
        'accuracy': 5,
        'strength': 2,
        'affinities': {'left': 'red'},
        'keywords': ['weapon','melee', 'axe','metal'],
        'desc': 'On a <b>perfect hit</b>, make 1 additional attack roll.',
        'affinity_bonus':{
            'desc':'Gain <b>Savage</b> and <b>Paired</b>',
            'requires':{
                'puzzle': {'red': 1},
                'complete': {'green': 2, 'blue': 1},
            },
        },
        'recipes': [
            {
                'locations': ['plumery'],
                'resource_handles': {
                    'hollow_wing_bones': 1,
                    'small_feathers': 1,
                    'iron': 1,
                },
            },
        ],
    },

    # skinnery
    'bandages': {
        'type': 'skinnery',
        'name': 'Bandages',
        'keywords': ['item'],
        'affinities': {'right': 'blue', 'bottom': 'green'},
        'desc': '<font class="kdm_font">a</font>: Remove up to 2 bleeding tokens from yourself or an adjacent survivor.',
    },
    'rawhide_armor_set': {
        'type': 'skinnery',
        'name': 'Rawhide Armor Set',
        'desc': 'Add <font class="inline_shield">1</font> to all hit locations.<br/>When you perform a survival action, roll 1d10. On a result of 6+, gain +1 survival.',
    },
    'rawhide_boots': {
        'type': 'skinnery',
        'armor': 1,
        'location': 'legs',
        'name': 'Rawhide Boots',
        'keywords': ['armor','set','rawhide'],
        'desc': 'When you <b>depart</b>, gain +1 survival',
        'recipes': [
            {'locations': ['skinnery'], 'resource_types': {'hide':1} },
        ],
    },
    'rawhide_drum': {
        'type': 'skinnery',
        'name': 'Rawhide Drum',
        'affinities': {'left': 'green'},
        'keywords': ['item','rawhide','instrument','noisy'],
        'desc': 'On <b>Arrival</b>, all survivors gain +1 insanity.<br/>Inspirational drumming! When you perform <b>encourage</b>, all non-deaf survivors are affected.',
    },
    'rawhide_gloves': {
        'type': 'skinnery',
        'name': 'Rawhide Gloves',
        'location': 'arms',
        'armor': 1,
        'affinities': {'left': 'red'},
        'desc': 'When you <b>depart</b>, gain +1 survival',
        'keywords': ['armor','set','rawhide'],
        'recipes': [
            {'locations': ['skinnery'], 'resource_types': {'hide':1} },
        ],
    },
    'rawhide_headband': {
        'type': 'skinnery',
        'name': 'Rawhide Headband',
        'location': 'head',
        'armor': 1,
        'affinities': {'bottom': 'blue'},
        'keywords': ['armor','set','rawhide',],
        'affinity_bonus': {
            'desc': '<font class="kdm_font">a</font>: reveal the top 2 <font class="kdm_font_10">b</font>. Place them back on top of the deck in any order.',
            'requires': {'puzzle': {'blue': 1}, },
        },
        'recipes': [
            {'locations': ['skinnery'], 'resource_types': {'hide':1} },
        ],
    },
    'rawhide_pants': {
        'type': 'skinnery',
        'name': 'Rawhide Pants',
        'armor': 1,
        'location': 'legs',
        'keywords': ['armor','set','rawhide',],
        'recipes': [
            {'locations': ['skinnery'], 'resource_types': {'hide':1} },
        ],
    },
    'rawhide_vest': {
        'type': 'skinnery',
        'name': 'Rawhide Vest',
        'armor': 1,
        'location': 'body',
        'affinities': {'top': 'blue', 'right': 'red',},
        'keywords': ['armor','set','rawhide',],
        'affinity_bonus': {
            'desc': '+1 Evasion',
            'requires': {'puzzle': {'red': 1, 'blue': 1}, },
        },
        'recipes': [
            {'locations': ['skinnery'], 'resource_types': {'hide':1} },
        ],
    },
    'rawhide_whip': {
        'type': 'skinnery',
        'name': 'Rawhide Whip',
        'keywords': ['weapon','melee','whip','rawhide'],
        'desc': (
            '<b>Provoke:</b> When you wound with this weapon, gain the '
            '<b>priority target</b> token.'
        ),
        'speed': 3,
        'accuracy': 7,
        'strength': 1,
    },


    # stone circle
    'beast_knuckle': {
        'type': 'stone_circle',
        'name': 'Beast Knuckle',
        'keywords': ['weapon', 'melee', 'katar', 'bone'],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'rules': ['Paired'],
        'desc': 'When you wound with this weapon, monster gains -1 toughness until end of the attack.',
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'large_flat_tooth': 1},
                'resource_types': {'pelt': 1},
            },
        ],
    },
    'blood_paint': {
        'type': 'stone_circle',
        'name': 'Blood Paint',
        'keywords': ['item','soluble'],
        'desc': (
            '<font class="kdm_font">a</font>: Activate weapon gear to the left '
            'and right of this card. These are two separate attacks. Cannot be '
            'used with two-handed weapons.'
        ),
        'affinities': {'left': 'paired', 'right': 'paired'},
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'bladder': 1},
                'resource_types': {'organ': 1},
                'innovations': ['paint'],
            },
        ],
    },
    'blue_charm': {
        'type': 'stone_circle',
        'name': 'Blue Charm',
        'keywords': ['item', 'jewelry', 'fragile'],
        'add_affinity': ['blue'],
        'affinity_bonus': {
            'desc': (
                '<b>Unshakeable:</b> When you draw a <b>Trap</b>, roll 1d10. '
                'On a 6+, discard the <b>Trap</b> and reshuffle the deck.'
            ),
            'requires': {'complete': {'blue': 5}},
        },
        'recipes': [
            {'locations': ['stone_circle'], 'resource_types': {'organ': 3}, },
        ],
    },
    'bone_earrings': {
        'type': 'stone_circle',
        'name': 'Bone Earrings',
        'keywords': ['item','jewelry','bone'],
        'desc': (
            'At the start of the showdown, gain +2 speed and +2 strength '
            'tokens if <b>insane</b> and all gear in your gear grid has the '
            '<i>bone</i> keyword.'
        ),
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'shank_bone': 1},
                'resource_types': {'bone': 1},
            },
        ],
    },
    'boss_mehndi': {
        'type': 'stone_circle',
        'name': 'Boss Mehndi',
        'keywords': ['item','soluble'],
        'desc': (
            'Boss is brave. While adjacent to you, <b>insane</b> survivors '
            'gain +1 speed.'
        ),
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'golden_whiskers': 1},
                'resource_types': {'bone': 1},
            },
        ],
    },
    'green_charm': {
        'type': 'stone_circle',
        'name': 'Green Charm',
        'keywords': ['item', 'jewelry', 'fragile'],
        'add_affinity': ['green'],
        'affinity_bonus': {
            'desc': (
                '<b>Undeathable:</b> If you would die, roll 1d10. On a 6+, '
                'you inexplicably survive.'
            ),
            'requires': {'complete': {'green': 5}},
        },
        'recipes': [
            {'locations': ['stone_circle'], 'resource_types': {'organ': 3}, },
        ],
    },
    'lance_of_longinus': {
        'type': 'stone_circle',
        'name': 'Lance of Longinus',
        'keywords': ['melee', 'weapon', 'spear', 'two-handed', 'bone'],
        'rules': ['Irreplaceable', 'Reach 2'],
        'desc': (
            'Each showdown, the first time you wound, the monster gains a -1 '
            'toughness token.'
        ),
        'speed': 2,
        'accuracy': 6,
        'strength': 9,
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'legendary_horns': 1},
                'resource_types': {'organ': 6},
            },
        ],
    },
    'red_charm': {
        'type': 'stone_circle',
        'name': 'Red Charm',
        'keywords': ['item', 'jewelry', 'fragile'],
        'add_affinity': ['red'],
        'affinity_bonus': {
            'desc': (
                '<b>Unstoppable:</b> When you attempt to wound, instead roll '
                '1d10. On a 1-5 fail. On 6-10, wound.'
            ),
            'requires': {'complete': {'red': 5}},
        },
        'recipes': [
            {'locations': ['stone_circle'], 'resource_types': {'organ': 3}, },
        ],
    },
    'screaming_armor_set': {
        'type': 'stone_circle',
        'name': 'Screaming Armor Set',
        'desc': (
            'Add <font class="inline_shield">2</font> to all hit locations.'
            '<br/><b>Skewer:</b> After you <b>slam</b>, spend '
            '<font class="kdm_font">a</font> to move 1 space and activate a '
            'melee weapon with +2 strength. If you wound with a spear, '
            'apply that wound roll result to the next selected hit location '
            'this attack.',
        ),
    },
    'screaming_bracers': {
        'type': 'stone_circle',
        'name': 'Screaming Bracers',
        'armor': 2,
        'keywords': ['armor', 'set', 'fur'],
        'affinities': {'left': 'red', 'top': 'green'},
        'location': 'arms',
        'desc': (
            'On <b>Arrival</b>, if possible, add an <b>Acanthus Plant</b> '
            'terrain card to the showdown. When you activate terrain, you may '
            'add +2 to your roll result.'
        ),
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'pelt': 1},
                'resource_types': {'hide': 1},
            },
        ],
    },
    'screaming_coat': {
        'type': 'stone_circle',
        'name': 'Screaming Coat',
        'affinities': {'top': 'blue', 'left': 'green', 'right': 'blue', 'bottom': 'green'},
        'armor': 2,
        'location': 'body',
        'keywords': ['armor', 'set', 'fur'],
        'desc': (
            '<b>Slam:</b> Spend <font class="kdm_font">c</font> to full move '
            'forward in a straight line. If you move 4+ spaces and stop '
            'adjacent to a monster, it suffers <b>knockback 1</b> and -1 '
            'toughness until the end of the round.'
        ),
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'pelt': 1},
                'resource_types': {'bone': 1},
            },
        ],
    },
    'screaming_horns': {
        'type': 'stone_circle',
        'name': 'Screaming Horns',
        'armor': 3,
        'location': 'head',
        'keywords': ['armor', 'set', 'bone'],
        'affinities': {'bottom': 'blue'},
        'desc': (
            '<font class="kdm_font">a</font>: Scream. Non-deaf <b>insane</b> '
            'survivors gain +1 movement until end of round. All other '
            'survivors gain +1 insanity.'
        ),
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'spiral_horn': 1},
                'resource_types': {'scrap': 1},
            },
        ],
    },
    'screaming_leg_warmers': {
        'type': 'stone_circle',
        'name': 'Screaming Leg Warmers',
        'armor': 2,
        'location': 'legs',
        'keywords': ['armor', 'set', 'fur'],
        'desc': 'On <b>Arrival</b> your feet hurt. Gain +3 insanity. ',
        'affinities': {'top': 'blue', 'right': 'red'},
        'recipes': [
            {'locations': ['stone_circle'], 'resource_handles': {'pelt': 1}, 'resource_types': {'hide': 1}, },
        ],
    },
    'screaming_skirt': {
        'type': 'stone_circle',
        'name': 'Screaming Skirt',
        'armor': 3,
        'location': 'waist',
        'keywords': ['armor', 'set', 'fur'],
        'affinities': {'right': 'green', 'bottom': 'blue'},
        'desc': (
            'Thick, protective fur protects your parts. Add +1 to severe '
            'waist injury roll results.'
        ),
        'recipes': [
            {
                'locations': ['stone_circle'],
                'resource_handles': {'pelt': 1},
            },
        ],
    },
}

rare_gear = {

    'adventure_sword': {
        'name': 'Adventure Sword',
        'keywords': ['weapon','melee','sword','finesse','other'],
        'rules': ['Unique','Irreplaceable'],
        'related_rules': ['unique', 'irreplaceable'],
        'desc': "Your courage is added to this weapon's strength.",
        'speed': 3,
        'accuracy': 6,
        'strength': 0,
    },
    'butcher_cleaver': {
        'name': 'Butcher Cleaver',
        'keywords': ['weapon','melee','axe','other'],
        'rules': ['Paired', 'Sentient', 'Irreplaceable'],
        'speed': 2,
        'accuracy': 5,
        'strength': 5,
        'desc': (
            '<b>Sentient:</b> Must be insane to activate.<br/>'
            '<b>Irreplaceable:</b> When you die, archive this card.'
        ),
    },
    'forsaker_mask': {
        'name': 'Forsaker Mask',
        'keywords': ['item','mask','metal','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'desc': (
            'During the Aftermath, you run off into the darkness never to be '
            'seen again.<hr/>During the Settlement Phase, you may archive this '
            'item to build the <b>Mask Maker</b> location.'
        ),
        'armor': 2,
        'location': 'head',
    },
    'lantern_halberd': {
        'name': 'Lantern Halberd',
        'keywords': ['weapon','melee','two-handed','spear','other'],
        'rules': ['Reach 2','Irreplaceable','Unique'],
        'desc': (
            'After attacking, if standing, you may move up to 2 spaces '
            'directly away from the monster.'
        ),
        'speed': 2,
        'accuracy': 4,
        'strength': 7,
    },
    'muramasa': {
        'name': 'Muramasa',
        'keywords': ['weapon','melee','katana', 'two-handed','other'],
        'rules': ['Frail','Sharp','Sentient','Deadly 2','Unique'],
        'desc': 'When you critically wound with this weapon, gain 2 bleeding tokens.',
        'speed': 6,
        'accuracy': 6,
        'strength': 6,
    },

    # regal / king's man
    'regal_faulds': {
        'name': 'Regal Faulds',
        'keywords': ['armor','bone','metal'],
        'armor': 4,
        'location': 'waist',
        'rules': ['Cursed'],
        'related_rules': ['cursed'],
        'desc': (
            'At the Aftermath, <font class="kdm_manager_font">S</font> '
            "<b>King's Curse</b>."
        ),
    },
    'regal_gauntlet': {
        'name': 'Regal Gauntlet',
        'keywords': ['armor','bone','metal'],
        'armor': 4,
        'location': 'arms',
        'rules': ['Cursed'],
        'related_rules': ['cursed'],
        'desc': (
            'At the Aftermath, <font class="kdm_manager_font">S</font> '
            "<b>King's Curse</b>."
        ),
    },
    'regal_greaves': {
        'name': 'Regal Greaves',
        'keywords': ['armor','bone','metal'],
        'armor': 4,
        'location': 'legs',
        'rules': ['Cursed'],
        'related_rules': ['cursed'],
        'desc': (
            'At the Aftermath, <font class="kdm_manager_font">S</font> '
            "<b>King's Curse</b>."
        ),
    },
    'regal_helm': {
        'name': 'Regal Helm',
        'keywords': ['armor','bone','metal'],
        'armor': 4,
        'location': 'head',
        'rules': ['Cursed'],
        'related_rules': ['cursed'],
        'desc': (
            'At the Aftermath, <font class="kdm_manager_font">S</font> '
            "<b>King's Curse</b>."
        ),
    },
    'regal_plackart': {
        'name': 'Regal Plackart',
        'keywords': ['armor','bone','metal'],
        'armor': 4,
        'location': 'body',
        'rules': ['Cursed'],
        'related_rules': ['cursed'],
        'desc': (
            'At the Aftermath, <font class="kdm_manager_font">S</font> '
            "<b>King's Curse</b>."
        ),
    },

    'steel_shield': {
        'name': 'Steel Shield',
        'keywords': ['weapon','melee','shield','metal','heavy'],
        'rules': ['Irreplaceable',],
        'desc': (
            '-3 movement.<br/>Spend <font class="kdm_font">a</font> or '
            'survival to ignore a hit.'
        ),
        'speed': 1,
        'accuracy': 6,
        'strength': 6,
    },
    'steel_sword': {
        'name': 'Steel Sword',
        'keywords': ['weapon','melee','sword','finesse','metal'],
        'rules': ['Irreplaceable','Slow','Sharp'],
        'desc': (
            'On a <b>Perfect hit</b>, the edge sharpens. Gain +1d10 strength '
            'for the rest of the attack.'
        ),
        'speed': 1,
        'accuracy': 4,
        'strength': 5,
    },
    'thunder_maul': {
        'name': 'Thunder Maul',
        'keywords': ['weapon','melee','club','two-handed','other'],
        'rules': ['Irreplaceable', 'Unique','Cursed'],
        'desc': (
            'On a <b>Perfect hit</b>, the monster is knocked down. Suffer a '
            'severe arm injury. All non-deaf survivors suffer 1 brain damage.'
        ),
        'speed': 2,
        'accuracy': 6,
        'strength': 10,
    },
    'twilight_sword': {
        'name': 'Twilight Sword',
        'keywords': ['weapon','melee','two-handed', 'finesse', 'other'],
        'rules': ['Slow','Cursed','Cumbersome','Sentient','Irreplaceable'],
        'related_rules': [
            'cumbersome', 'cursed', 'devastating_x',
            'irreplaceable', 'slow', 'sentient'
        ],
        'desc': (
            'Gains <b>Devastating 2</b> when fighting the Watcher.<br/>'
            '* Accuracy is 9 - Twilight Sword proficiency level.'
        ),
        'speed': 1,
        'accuracy': '*',
        'strength': 9,
    },
}

weapon_crafter = {
    # blood sheath moves to plumery in 1.6!
    'blood_sheath': {
        'name': 'Blood Sheath',
        'keywords': ['item', 'bone', 'other'],
        'rules': ['Block 1'],
        'related_rules': ['frail', 'sharp', 'super_dense'],
        'desc': (
            'When Rainbow Katana is left of Blood Sheath, it loses '
            '<b>Frail</b> and gains <b>Sharp</b> (add 1d10 strength to '
            'each wound attempt).',
        ),
        'affinities': {'left': 'paired'},
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_handles': {
                    'hollow_wing_bones': 1,
                    'muculent_droppings': 1
                },
                'resource_types': {'organ': 5}
            },
        ],
    },
    'counterweighted_axe': {
        'name': 'Counterweighted Axe',
        'keywords': ['weapon','melee','axe','two-handed'],
        'rules': ['Reach 2'],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'related_rules': ['devastating_x'],
        'affinities': {'top': 'red', 'right': 'green'},
        'affinity_bonus': {
            'desc': (
                'Gains <b>Devastating 1</b>: Whenever you wound, inflict 1 '
                'additional wound.'
            ),
            'requires': {
                'complete': {'green': 1},
                'puzzle': {'red': 1},
            },
        },
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_types': {'bone': 2, 'hide': 1, 'organ': 1}
            },
        ],
    },
    'finger_of_god': {
        'name': 'Finger of God',
        'keywords': ['weapon','melee','spear','two-handed'],
        'rules': ['Reach 2'],
        'speed': 2,
        'accuracy': 5,
        'strength': 5,
        'affinities': {'top': 'red'},
        'affinity_bonus': {
            'desc': (
                'As long as you have 5+ survival, gain +1 accuracy and +1 '
                'strength.'
            ),
            'requires': {
                'complete': {'red': 1, 'blue': 1, 'green': 1},
            },
        },
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_handles': {'phoenix_finger': 1},
                'resource_types': {'bone': 4,}
            },
        ],
    },
    'rainbow_katana': {
        'name': 'Rainbow Katana',
        'keywords': ['weapon','melee','katana','finesse','two-handed'],
        'rules': ['Frail',],
        'speed': 4,
        'accuracy': 4,
        'strength': 4,
        'related_rules': ['deadly'],
        'affinities': {'left': 'red'},
        'affinity_bonus': {
            'desc': 'Gains <b>Deadly</b>.',
            'requires': {
                'complete': {'green': 1, 'blue': 1},
                'puzzle': {'red': 1},
            },
        },
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_handles': {
                    'bird_beak': 1, 'rainbow_droppings': 1
                },
                'resource_types': {'iron': 1, 'bone': 6},
                'suffix_text': '<b>Heat</b> Required.'
            },
        ],
    },
    'scrap_bone_spear': {
        'name': 'Scrap Bone Spear',
        'min_version': 'core_1_6',
        'keywords': ['weapon', 'melee', 'spear', 'bone', 'metal'],
        'speed': 2,
        'accuracy': 6,
        'strength': 3,
        'affinities': {'left': 'green', 'right': 'red'},
        'rules': ['Reach 2', 'Frail'],
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1}},
            'desc': (
                '<b>Barbed 4:</b> On a <b>Perfect hit</b>, gain +4 strength '
                'for the rest of the attack.'
            ),
        },
    },
    'scrap_dagger': {
        'name': 'Scrap Dagger',
        'keywords': ['weapon','melee','dagger','metal'],
        'desc': (
            "On a <b>Perfect hit</b>, the edge sharpens. Gain +2 strength for "
            "the rest of the attack."
        ),
        'speed': 3,
        'accuracy': 7,
        'strength': 2,
        'affinities': {'top': 'red', 'right': 'red'},
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_types': {'scrap': 1, 'bone': 1},
                'suffix_text': '<b>Heat</b> Required.'
            },
        ],
    },
    'scrap_lantern': {
        'name': 'Scrap Lantern',
        'min_version': 'core_1_6',
        'keywords': ['item', 'metal', 'lantern'],
        'desc': 'When you <b>depart</b>, gain +1 survival.',
        'affinities': {'right': 'blue'},
        'affinity_bonus': {
            'desc': '+1 accuracy',
            'requires': {
                'complete': {'red': 1, 'blue': 1},
            },
        },
    },
    'scrap_rebar': {
        'name': 'Scrap Rebar',
        'min_version': 'core_1_6',
        'keywords': ['item', 'metal', 'heavy'],
        'affinities': {'left': 'paired'},
        'desc': (
            'The weapon to the left loses <b>frail</b> and gains '
            '<b>unwieldy</b>. If you attempt to wound a Super-dense location '
            'with the weapon, archive this at the end of the attack.'
        ),
    },
    'scrap_sword': {
        'name': 'Scrap Sword',
        'keywords': ['weapon','melee','sword','metal'],
        'desc': (
            "On a <b>Perfect hit</b>, the edge sharpens. Gain +4 strength for "
            "the rest of the attack."
        ),
        'speed': 2,
        'accuracy': 5,
        'strength': 3,
        'affinities': {'top': 'blue'},
        'affinity_bonus': {
            'desc': 'Gains <b>Deadly</b>.',
            'requires': {
                'complete': {'red': 2, 'blue': 1},
            },
        },
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_types': {'scrap': 1, 'bone': 2},
                'suffix_text': '<b>Heat</b> Required.'
            },
        ],
    },
    'skullcap_hammer': {
        'name': 'Skullcap Hammer',
        'desc': (
            'On a <b>Perfect Hit</b>, the monster is dazed, and gains -1 '
            'speed token until the end of its turn. A monster can be dazed '
            'once per round.'
        ),
        'keywords': ['weapon','melee','club','bone'],
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
        'affinities': {'bottom': 'green'},
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_types': {'scrap': 1, 'bone': 2},
            },
        ],
    },
    'whistling_mace': {
        'name': 'Whistling Mace',
        'keywords': ['weapon','melee','club','bone'],
        'desc': (
            'On a <b>Perfect hit</b>, reveal the next AI card. Place it on top '
            'or bottom of the AI deck.<br/><b>Unwieldy:</b> If any attack roll '
            'results are 1, you hit yourself and suffer 1 damage.'
        ),
        'rules': ['Unwieldy'],
        'speed': 3,
        'accuracy': 6,
        'strength': 3,
        'affinities': {'bottom': 'green'},
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_types': {'organ': 1, 'bone': 2},
            },
        ],
    },
    'zanbato': {
        'name': 'Zanbato',
        'keywords': ['weapon','melee','grand weapon','two-handed','bone'],
        'rules': ['Slow','Frail','Deadly'],
        'speed': 1,
        'accuracy': 6,
        'strength': 6,
        'affinities': {'top': 'red', 'right': 'green'},
        'affinity_bonus': {
            'desc': (
                'Gains <b>Devastating 1:</b> Whenever you wound, inflict 1 '
                'additional wound.'
            ),
            'requires': {
                'complete': {'green': 1},
                'puzzle': {'red': 1},
            },
        },
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_types': {'hide': 2},
                'resource_handles': {'great_cat_bone': 1}
            },
        ],
    },
}

misc_random_other = {
    'portcullis_key': {
        'type': 'other',
        'name': 'Portcullis Key',
        'desc': (
            '<i>This is the key to the portcullis. Without it, you will never '
            'get through.</i>'
        ),
    },
}


starting_gear = {
    'cloth': {
        'name': 'Cloth',
        'keywords': ['armor'],
        'desc': (
            'The Cloth protects your waist. Gain 1 armor point at the waist '
            'hit location.'
        ),
        'armor': 1,
        'location': 'waist',
    },
    'founding_stone': {
        'name': 'Founding Stone',
        'keywords': ['weapon','melee','stone'],
        'desc': (
            'Spend <font class="kdm_font">a</font> to sling the stone from '
            'anywhere on the board! Archive this card for 1 automatic hit '
            'that inflicts a critical wound.<br/><b>Archive:</b> Return this '
            'card to the game box.'
        ),
        'speed': 2,
        'accuracy': 7,
        'strength': 1,
    },
}


tenth_anniversary_survivors = {
    'teleric_eye_tac': {
        'name': 'Teleric Eye Tac',
        'pattern_id': -6,
        'type': 'pattern',
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
        'type': 'pattern',
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
        'type': 'pattern',
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
        'type': 'pattern',
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
        'type': 'pattern',
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
        'type': 'pattern',
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
}


beta_challenge_scenarios = {
    'arm_of_the_first_tree': {
        'keywords': ['weapon', 'melee', 'club'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': 'Arm of the First Tree',
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'desc': (
            'On a <b>Perfect Hit</b>, the monster gains -1 toughness token '
            'until the end of the round. A monster can only suffer this once '
            'per round.'
        ),
    },
    "ayas_spear": {
        'keywords': ['weapon', 'melee', 'spear'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
        'desc': "Pairs with Aya's spear.",
        'name': "Aya's Spear"
    },
    "ayas_sword": {
        'keywords': ['weapon', 'melee', 'sword'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': "Aya's Sword",
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
        'desc': "Pairs with Aya's spear.",
    },
    'cola_bottle_lantern': {
        'keywords': ['item', 'fragile', 'other'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': 'Cola Bottle Lantern',
        'desc': '+1 Accuracy<br/><font class="kdm_font">a</font>: All survivors gain +1 Accuracy until the end of the round. Use once per round.',
    },
    'fairy_bottle': {
        'keywords': ['item', 'fragile', 'other'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': 'Fairy Bottle',
        'desc': 'When you would die for any reason, instead restore all lost armor points and health levels, remove all bleeding tokens and archive this card.',
    },
    'giant_stone_face': {
        'keywords': ['weapon','melee', 'grand', 'heavy', 'two-handed', 'stone'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': 'Giant Stone Face',
        'speed': 1,
        'accuracy': 6,
        'strength': 5,
        'rules': ['Devastating 1'],
        'desc': 'If your attack roll result is a 1, archive this card and place a Giant Stone Face terrain tile in any adjacent square.',
    },
    'petal_lantern': {
        'keywords': ['item', 'lantern', 'other'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': 'Petal Lantern',
        'desc': 'After rolling on the severe injury table, you may spend any amount of survival to add that number to your roll result.',
    },
    'piranha_helm': {
        'keywords': ['armor', 'set', 'rawhide'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': 'Piranha Helm',
        'armor': 2,
        'location': 'head',
        'affinities': {'right': 'red', 'bottom': 'blue'},
    },
    "scouts_tunic": {
        'keywords': ['armor', 'set', 'leather'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': "Scout's Tunic",
        'armor': 2,
        'location': 'head',
        'aux_location': 'body',
        'desc': 'Takes the place of the Leather Mask and Leather Cuirass for completing the leather armor set.',
    },
    'stone_arm': {
        'keywords': ['item', 'stone', 'heavy'],
        'expansion': 'beta_challenge_scenarios',
        'type': 'rare_gear',
        'name': 'Stone Arm',
        'rules': ['Block 1'],
        'desc': 'Ignore <b>1 dismembered arm</b> permanent injury.',
    },

}


white_box = {

    # fade
    'sword_of_silence': {
        'expansion': 'fade',
        'type': 'rare_gear',
        'name': 'Sword of Silence',
        'speed': 2,
        'accuracy': 5,
        'strength': 6,
        'affinities': {'left': 'blue', 'top': 'red', 'right': 'green'},
        'keywords': ['weapon','melee','sword','other'],
        'rules': ['Sentient','Irreplaceable','Unique'],
        'desc': (
            'Gains <b>Sharp</b> if you have 5+ understanding. While your '
            'settlement has this sword, ignore <font class="kdm_font">g</font> '
            '<b>White Secret</b> and <font class="kdm_font">g</font> <b>White '
            'Speaker</b>.'
        ),
    },
    'newborn': {
        'expansion': 'fade',
        'type': 'rare_gear',
        'name': 'Newborn',
        'keywords': ['item','heavy','fragile'],
        'rules': ['Irreplaceable'],
        'desc': (
            'While you have this, all your weapons gain <b>Slow</b>. When you '
            'return to the settlement, archive this and gain +1 population.'
        ),
    },

    # oktoberfest aya

    'afterdeath_brew': {
        'name': 'Afterdeath Brew',
        'expansion': 'oktoberfest_aya',
        'type': 'pattern',
        'pattern_id': -8,
        'keywords': ['item', 'consumable', 'soluble', 'other'],
        'affinities': {'right': 'green'},
        'desc': (
            '<font class="kdm_font">a</font>: You <b>consume</b> this and gain '
            '5 bleeding tokens.<br/> During the Aftermath, roll 1d10 for each '
            'survivor that died from bleeding tokens. On a 9+, the brew saves '
            'their life but makes them <b>deaf</b>.'
        ),
        'recipes': [
            {
                'resource_handles': {
                    'blistering_plasma_fruit': 1,
                    'love_juice': 1,
                    'scrap': 1
                },
                'crafting_process': [
                    (
                        'Boil mixture over <b>heat</b> to remove invasive '
                        'microbes.'
                    ),
                    (
                        'Knead <b>pottery</b> clay to create a cask. Bake, '
                        'then glaze interior with <b>Love Juice</b>.'
                    ),
                    (
                        'Set aside oily residue during skimming. Let cool '
                        'until waxy then shape to create seal.'
                    ),
                ],
            },
        ],
    },

    'brave_dirndl': {
        'name': 'Brave Dirndl',
        'expansion': 'oktoberfest_aya',
        'type': 'pattern',
        'pattern_id': -9,
        'armor': 1,
        'location': 'body',
        'aux_location': 'waist',
        'keywords': ['armor', 'cloth'],
        'affinities': {'right': 'red'},
        'desc': (
            'Once per lifetime, when you are a returning survivor and this is '
            'the only armor you are wearing, gain +1 courage. If your '
            'settlement has <b>Song of the Brave</b>, gain +1 permanent '
            'strength too!'
        ),
        'recipes': [
            {
                'gear_handles': {
                    'cloth': 2,
                    'skullcap_hammer': 1,
                },
                'resource_handles': {
                    'leather': 1,
                },
                'crafting_process': [
                    (
                        'Hear gleeful music of a <b>returning survivor with an '
                        'instrument</b> to inspire design.'
                    ),
                    (
                        'Reclaim hardware from Skullcap Hammer for motions '
                        'used throughout ensemble.'
                    ),
                    (
                        'Use <b>Bone Sickle</b> to properly size choker and '
                        'armlet accessories.'
                    ),
                ],
            },
        ],
    },
    'durendal': {
        'name': 'Durendal',
        'expansion': 'oktoberfest_aya',
        'type': 'pattern',
        'pattern_id': -7,
        'rules': ['Ethereal'],
        'keywords': ['weapon', 'melee', 'sword', 'metal', 'other'],
        'speed': 2,
        'accuracy': 6,
        'strength': 9,
        'affinities': {'bottom': 'red'},
        'desc': (
            'When you depart with  <font class="inline_shield">1</font> or '
            'less at each hit location (after all other departing bonuses), '
            'add armor equal to your courage to all hit locations.'
        ),
        'recipes': [
            {
                'undefined_ingredient': '1 x Other ear or resource, ',
                'resource_handles': {
                    'iron': 2,
                    'leather': 1,
                },
                'crafting_process': [
                    (
                        'Eavesdrop on a sleeping <b>savior</b> to determine '
                        "the blade's dimensions."
                    ),
                    (
                        'Create custom <b>Blacksmith</b> tools with material '
                        'from the other.'
                    ),
                    (
                        'Collect bile off a <b>returning survivor who was '
                        'Regurgitated</b> to cure leather.'
                    ),
                ],
            },
        ],
    },


    # Halloween Ringtail Vixen 2020
    'vixen_tail': {
        'expansion': 'halloween_ringtail_vixen_2020',
        'name': 'Vixen Tail',
        'type': 'pattern',
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
        'type': 'pattern',
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
        'type': 'pattern',
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
    }
}


promo = {

    # rare gear
    'ancient_root': {
        'name': 'Ancient Root',
        'expansion': 'promo',
        'keywords': ['item', 'vegetable', 'heavy', 'consumable', 'other'],
        'affinities': {'left': 'blue'},
        'expansion': 'promo',
        'type': 'rare_gear',
        'desc': (
            "When you are picked as a target while <b>insane</b>, the carrot "
            "shrieks fearfully. Roll 1d10. On a 1, the shrill sound stuns you. "
            "You are <b>doomed</b> for the rest of the monster's action. On a "
            "6+, the harsh note alerts you. Ignore the first hit of the "
            "monster's attack."
        ),
        'recipes': [
            {
                'prefix_text': (
                    'During <font class="kdm_font">g</font> <b>Black '
                    'Harvest</b>, if the Gatherer is <b>insane</b>, they '
                    'follow a shrill echo in the darkness. A Fleshy stalk '
                    'quivers in the ground, its muffled shrieking begs to be '
                    'uprooted. Gain the <b>Ancient Root</b> rare gear.'
                ),
            },
        ],
    },


    #
    # promo
    #

    # strange spot
    'belt_of_gender_swap': {
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Belt of Gender Swap',
        'keywords': ['item','jewelry','other'],
        'rules': ['Cursed'],
        'desc': 'While in your gear grid, change to the opposite sex.',
        'affinities': {'right': 'green', 'bottom': 'green'},
    },

    # pinup sci-fi white speaker
    'blood_plasma_gun': {
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Blood Plasma Gun',
        'speed': 'X',
        'accuracy': '4',
        'strength': 'Z',
        'keywords': ['weapon','ranged','gun','other'],
        'rules': ['Range: X<sup>3</sup>', 'Unique'],
        'desc': (
            'When you activate this, gain 1 bleeding token. X = your bleeding '
            'tokens. Z = X + X + X + X + X'
        ),
    },
    'blood_plasma_katana': {
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Blood Plasma Katana',
        'keywords': ['weapon','melee','katana','other'],
        'speed': 9,
        'accuracy': 6,
        'strength': 9,
        'rules': ['Unique','Sharp','Devastating X'],
        'desc': (
            'When you activate this, gain 1 bleeding token. X = your bleeding '
            'tokens minus 2.'
        ),
    },


    # prismatic warrior of the sun
    'prismatic_lantern': {
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Prismatic Lantern',
        'keywords': ['item','lantern','other'],
        'rules': ['+1 Movement', 'Unique', 'Irreplaceable'],
        'desc': (
            'During the showdown, you may archive this and gain 1 permanent '
            'affinity of any color.'
        ),
    },

    # pinup order knight
    'twilight_thong': {
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Twilight Thong',
        'keywords': ['armor','set','rawhide','other'],
        'rules': ['Outfit'],
        'related_rules': ['outfit'],
        'desc': (
            'Its fabric responds to you; stress causes INTENSE constriction. '
            'Do not suffer brain traumas (ignore this if you have destroyed '
            'genitals).'
        ),
        'location': 'waist',
        'armor': 0,

    },

    # pinup sci-fi twilight knight + gencon 2015
    'dying_lantern': {
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Dying Lantern',
        'keywords': ['item','lantern','other'],
        'rules': ['+1 Evasion'],
        'desc': (
            'You may archive this to gain 1 <b>Skull</b> basic resource and '
            '+3 insanity.'
        ),
    },
    'vibrant_lantern': {
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Vibrant Lantern',
        'keywords': ['item','lantern','other'],
        'rules': ['+1 Accuracy'],
        'desc': (
            'You may archive this to gain 1 <b>Broken Lantern</b> basic '
            'resource and 1 survival.'
        ),
    },

    # beyond the wall
    'cloth_leggings': {
        'expansion': 'promo',
        'type': 'gear_recipe',
        'name': 'Cloth Leggings',
        'keywords': ['item','cloth'],
        'armor': 1,
        'location': 'legs',
        'rules': ['Accessory'],
        'desc': (
            'When you suffer the <b>Bleeding</b> or <b>Bloody thighs</b> '
            'severe injuries, only gain 1 bleeding token.'
        ),
        'affinities': {'bottom': 'green'},
        'recipes': [
            {
                'resource_types': {'hide': 1},
                'gear_handles': {'cloth': 1},
                'innovations': ['ammonia'],
            },
        ],
    },
    'hard_breastplate': {
        'expansion': 'promo',
        'type': 'gear_recipe',
        'name': 'Hard Breastplate',
        'keywords': ['armor','leather','heavy'],
        'armor': 3,
        'location': 'body',
        'rules': ['Outfit'],
        'affinities': {'top': 'red','bottom': 'blue'},
        'affinity_bonus': {
            'desc': "Ignore the first severe injury you suffer each showdown.",
            'requires': {'complete': {'blue': 1, 'green': 1}},
        },
        'recipes': [
            {
                'resource_types': {'bone': 2},
                'resource_handles': {'leather': 1},
                'innovations': ['lantern_oven'],
                'suffix_text': 'or <b>Heat</b>.'
            },
        ],
    },

    # halloween pinup twilight knight
    "jack_o_lantern": {
        'expansion': 'promo',
        'type': 'gear_recipe',
        'name': "Jack O' Lantern",
        'keywords': ['item','consumable','lantern','other'],
        'rules': ['Irreplaceable'],
        'desc': (
            'During the showdown, if you are, <b>insane</b>, when a survivor '
            'dies, gain +10 survival.'
        ),
        'recipes': [
            {
                'resource_types': {'scrap': 1, 'organ': 1},
                'resource_handles': {'skull': 1},
                'innovations': ['memento_mori'],
            },
        ],
    },

    # valentine's day pinup twilight knight
    'scoopy_club': {
        'expansion': 'valentines_day_pinup_twilight_knight',
        'name': 'Scoopy Club',
        'type': 'rare_gear',
        'keywords': ['weapon', 'melee', 'club', 'tool', 'metal'],
        'speed': 1,
        'accuracy': 4,
        'strength': 5,
        'affinities': {'left': 'red', 'right': 'green'},
        'desc': (
            'When you vomit, are vomited on, or are adjacent to vomit '
            '(or puke, bile, <b>Retch</b>, etc.), you fill the club. '
            'For the rest of the lantern year, it <b>Dazes</b> the monster '
            'when it wounds (see Skullcap Hammer).'
        ),
        'recipes': [
            {
                'innovations': ['scrap_smelting'],
                'suffix_text': (
                    'When the settlement innovates <b>Scrap Smelting</b>, '
                    'gain the Scoopy Club rare gear.'
                ),
            },
        ],
    },

    # before the wall
    'tabard': {
        'expansion': 'promo',
        'type': 'gear_recipe',
        'name': 'Tabard',
        'keywords': ['item','cloth'],
        'rules': ['Accessory'],
        'desc': (
            'When you are encouraged, gain +1 insanity if your settlement is '
            '<b>Barbaric</b> or gain +1 survival if your settlement is '
            '<b>Romantic</b>.'
        ),
        'affinities': {'left': 'blue'},
        'location': 'body',
        'armor':1,
        'recipes': [
            {
                'innovations': ['paint'],
                'resource_types': {'organ': 1},
                'gear_handles': {'cloth': 1},
            },
        ],
    },
    'vagabond_armor_set': {
        'expansion': 'promo',
        'type': 'gear_recipe',
        'name': 'Vagabond Armor Set'
    },
    'white_dragon_gauntlets': {
        'expansion': 'promo',
        'type': 'ivory_carver',
        'name': 'White Dragon Gauntlets',
        'armor': 12,
        'keywords': ['armor','set','ivory','metal','heavy'],
        'affinities': {'left': 'red'},
        'affinity_bonus': {
            'desc': (
                'When you <b>Sideswipe</b>, gain +1 accuracy and +5 strength '
                'for your attack next this turn'
            ),
            'requires': {
                'puzzle': {'red': 1},
                'complete': {'red': 2},
            },
        },
    },


    # white speaker nico
    'xmaxe': {
        'expansion': 'promo',
        'type': 'gear_recipe',
        'name': 'Xmaxe',
        'keywords': ['weapon', 'melee','axe','other'],
        'rules': ['Irreplaceable'],
        'desc': "This weapon's strength is equal to your current insanity.",
        'affinities': {
            'top': 'red',
            'left': 'red',
            'right': 'green',
            'bottom': 'green'
        },
        'recipes': [
            {
                'innovations': ['sculpture','storytelling'],
                'resource_types': {'bone': 2,},
                'resource_handles': {'fresh_acanthus': 1, 'leather': 2},
            },
        ],
        'speed': 2,
        'accuracy': 5,
        'strength': 0,
    },


}


generic = {
    'corsair_coat': {
        'expansion': 'generic',
        'type': 'rare_gear',
        'name': 'Corsair Coat',
        'keywords': ['item','leather','metal','other'],
        'rules': ['Ethereal','Unique','Accessory','Unwieldy','Range 5'],
        'location': 'body',
        'armor': 2,
        'affinities': {'left': 'red','bottom': 'blue','right': 'red'},
        'affinity_bonus': {
            'desc': 'After moving from a <b>dash</b>, the coat fires its guns! It attacks with this profile, ignoring your attribute modifiers (4/9/8).',
            'requires': {'puzzle': {'red': 2, 'blue': 1}}
        },
        'recipes': [
            {
                'misc':(
                    "When a Savior shares a well told dream during "
                    '<font class="kdm_se_card">se</font> <b>Weird Dream</b> '
                    'add <b>Corsair Coat</b> rare gear to settlement storage.'
                ),
            },
        ],
    },
}


vignettes_of_death_white_gigalion = {
    'dense_bone_arrows': {
        'expansion': 'vignettes_of_death_white_gigalion',
        'type': 'catarium',
        'name': 'Dense Bone Arrows',
        'speed': 2,
        'accuracy': 5,
        'strength': 6,
        'desc': (
            '(You depart with enough arrows to last. There is no activation '
            'limit.)'
        ),
        'affinities': {'top': 'blue', 'right': 'red'},
        'rules': ['Ammo - Bow', 'Sharp'],
        'keywords': ['item', 'bone', 'ammunition', 'arrow'],
        'recipes': [
            {
                'locations': ['catarium', 'giga_catarium', 'blacksmith'],
                'resource_handles': {
                    'hooked_claw': 1,
                    'great_cat_bone': 3,
                    'leather': 2,
                    'iron': 2,
                },
            },
        ],
    },
    'hooked_claw_knife': {
        'expansion': 'vignettes_of_death_white_gigalion',
        'type': 'catarium',
        'name': 'Hooked Claw Knife',
        'keywords': ['weapon', 'melee', 'dagger', 'bone'],
        'speed': 3,
        'accuracy': 6,
        'strength': 7,
        'affinities': {
            'top': 'red',
            'right': 'red',
            'left': 'red',
            'bottom': 'red'
        },
        'affinity_bonus': {
            'desc': (
                'When your wound causes a reaction where the monster moves, '
                'you tear a chunk of flesh out! It suffers a wound. '
            ),
            'requires': {'complete': {'red': 4},},
        },
        'recipes': [
            {
                'locations': ['catarium', 'giga_catarium'],
                'resource_types': {'organ': 2},
                'resource_handles': {'hooked_claw': 1, 'elder_cat_teeth': 1},
            },
        ],
    },
    'lion_slayer_cape': {
        'expansion': 'vignettes_of_death_white_gigalion',
        'type': 'catarium',
        'name': 'Lion Slayer Cape',
        'armor': 1,
        'location': 'body',
        'desc': (
            'On <b>Arrival</b>, all survivors gain +1 survival. If you are '
            'wearing fur armor, reduce all damage suffered by 1, to a '
            'minimum of 1.'
        ),
        'affinities': {'top': 'red', 'bottom': 'green'},
        'rules': ['Accessory'],
        'keywords': ['item', 'fur', 'bone', 'flammable'],
        'recipes': [
            {
                'locations': ['catarium', 'giga_catarium'],
                'resource_handles': {
                    'hooked_claw': 1,
                    'white_fur': 2,
                    'shimmering_mane': 1,
                },
            },
        ],
    },
    'lovelorn_rock': {
        'expansion': 'vignettes_of_death_white_gigalion',
        'type': 'rare_gear',
        'name': 'Lovelorn Rock',
        'desc': 'You will never be apart.',
        'keywords': ['item', 'heavy', 'bone', 'stone'],
    },
    'oxidized_beast_katar': {
        'expansion': 'vignettes_of_death_white_gigalion',
        'type': 'catarium',
        'name': 'Oxidized Beast Katar',
        'speed': 2,
        'accuracy': 7,
        'strength': 5,
        'keywords': ['weapon', 'melee', 'katar', 'metal', 'bone'],
        'rules': ['Deadly', 'Paired', 'Sharp'],
        'affinities': {'top': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'desc': (
                'On a <b>Perfect hit</b>, the edge sharpens. Gain +4 strength '
                'for this attack.'
            ),
            'requires': {'complete': {'red': 2}},
        },
        'recipes': [
            {
                'endeavors': ['exhausted_lantern_hoard_1_oxidation'],
                'locations': ['catarium', 'giga_catarium'],
                'gear_handles': {
                    'lion_beast_katar': 1,
                },
                'resource_handles': {
                    'hooked_claw': 2,
                    'iron': 1,
                    'shimmering_mane': 1,
                },
                'resource_types': {'bone': 2},
            },
        ],
    },
}

pinups_of_death_2 = {
    'lantern_brassiere': {
        'name': 'Lantern Brassiere',
        'expansion': 'pinups_of_death_2',
        'type': 'rare_gear',
        'armor': 0,
        'location': 'body',
        'keywords': ['armor', 'set', 'metal', 'heavy'],
        'rules': ['Outfit', '-2 movement'],
        'related_rules': ['outfit'],
        'affinities': {
            'top': 'blue', 'right': 'green', 'bottom': 'blue', 'left': 'green',
        },
        'affinity_bonus': {
            'requires': {
                'puzzle': {'blue': 2, 'green': 2},
            },
            'desc': (
                'When you <b>depart</b>, add <font class="inline_shield">2'
                '</font> to all hit locations with metal armor.'
            ),
        },
    },
    'leather_bodysuit': {
        'name': 'Leather Bodysuit',
        'expansion': 'pinups_of_death_2',
        'type': 'rare_gear',
        'armor': 0,
        'location': 'body',
        'keywords': ['armor', 'set', 'leather'],
        'rules': ['Outfit'],
        'related_rules': ['outfit'],
        'affinities': {'top': 'red', 'bottom': 'blue'}
    },
    'rawhide_corset': {
        'name': 'Rawhide Corset',
        'expansion': 'pinups_of_death_2',
        'type': 'rare_gear',
        'armor': 0,
        'location': 'body',
        'keywords': ['armor', 'set', 'rawhide'],
        'rules': ['Outfit'],
        'related_rules': ['outfit'],
        'affinities': {'top': 'blue', 'right': 'red'},
        'affinity_bonus': {
            'requires': {'puzzle': {'blue': 1, 'red': 1}},
            'desc': '+1 evasion',
        },
    },
    'teeth_bikini': {
        'name': 'Teeth Bikini',
        'expansion': 'pinups_of_death_2',
        'type': 'rare_gear',
        'armor': 0,
        'location': 'body',
        'keywords': ['armor', 'set', 'scale'],
        'affinities': {'left': 'red', 'top': 'blue', 'right': 'red'},
        'rules': ['Outfit'],
        'related_rules': ['outfit', 'collision'],
        'affinity_bonus': {
            'requires': {'puzzle': {'blue': 1}, 'complete': {'red': 2}},
            'desc': '+1 accuracy',
        },
        'desc': (
            'When you spend <font class="kdm_font">c</font>, you <b>Shadow '
            'Walk</b> and may move through spaces survivors occupy without '
            'causing <b>collision</b>.'
        ),
    },
}

sunlion_armor_beta = {
    'white_sunlion_mask': {
        'name': 'White Sunlion Mask',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'sunlion_armor_beta',
        'armor': 1,
        'location': 'head',
        'keywords': ['armor', 'set', 'fragile', 'mask'],
        'affinities': {'left': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 2}},
            'desc': (
                'When you <b>Pounce</b> and attack from the blind spot, '
                'add +1d10 strength to the first wound attempt of that '
                'attack.'
            ),
        },
        'recipes': [
            {
                'gear_handles': {'white_lion_helm': 1, },
                'resource_types': {'organ': 1},
                'innovations': ['paint']
            },
        ],
    },
}

halloween_survivors_series_2 = {
    'big_bite_costume': {
        'type': 'pattern',
        'pattern_id': -18,
        'expansion': 'halloween_survivors_series_2',
        'name': 'Big Bite Costume',
        'keywords': ['item'],
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
        ),
        'affinities': {'top': 'green', 'bottom': 'red'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1, 'green': 1}},
            'desc': (
                'On <b>Arrival</b>, trick or treat! Roll 1d10: 1-5 survivors '
                'gain a bleeding token. 6+, survivors gain +6 insanity.'
            ),
        },
        'recipes': [
            {
                'resource_handles': {
                    'leather': 1,
                    'organ': 2,
                    'skull': 1,
                },
                'crafting_process': [
                    (
                        'Listen to the tragic tale of a <b>dismembered</b> '
                        "survivor's brush with the croc."
                    ),
                    (
                        'Imagine the feet of a of a cold-blooded opportunist.'
                    ),
                    (
                        'Find a blood-crusted <b>Broken Lantern</b>.'
                    ),
                ],
            },
        ],
    },
    'gold_cat_costume': {
        'type': 'pattern',
        'pattern_id': -15,
        'expansion': 'halloween_survivors_series_2',
        'name': 'Gold Cat Costume',
        'keywords': ['item'],
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
        ),
        'affinities': {'left': 'red', 'bottom': 'blue'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1, 'blue': 1}},
            'desc': (
                'On <b>Arrival</b>, trick or treat! Roll 1d10: 1-5 survivors '
                'gain a -1 strength token. 6+ survivors gain a +1 strength '
                'token.'
            ),
        },
    },
    'retching_costume': {
        'type': 'pattern',
        'pattern_id': -17,
        'expansion': 'halloween_survivors_series_2',
        'name': 'Retching Costume',
        'keywords': ['item'],
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
        ),
        'affinities': {'right': 'red', 'bottom': 'blue'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1, 'blue': 1}},
            'desc': (
                'On <b>Arrival</b>, trick or treat! Roll 1d10: 1-5 survivors '
                'lose <font class="inline_shield">1</font> to all locations. '
                '6+, survivors gain <font class="inline_shield">1</font> to '
                'all locations.'
            ),
        },
    },
    'screaming_costume': {
        'type': 'pattern',
        'pattern_id': -16,
        'expansion': 'halloween_survivors_series_2',
        'name': 'Screaming Costume',
        'keywords': ['item'],
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
        ),
        'affinities': {'left': 'green', 'right': 'blue'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1, 'blue': 1}},
            'desc': (
                'On <b>Arrival</b>, trick or treat! Roll 1d10: 1-5 survivors '
                'gain a -1 movement token. 6+ survivors gain a +1 movement '
                'token.'
            ),
        },
    },
}

grimmory = {
    'gusk_knife_blindside': {
        'name': 'Gusk Knife (Blindside)',
        'type': 'beta_gear_recipe',
        'expansion': 'grimmory',
        'keywords': ['weapon', 'melee', 'dagger', 'shield', 'bone'],
        'speed': 3,
        'accuracy': 6,
        'strength': 5,
        'affinities': {'bottom': 'green'},
        'desc': (
            'If paired, this gains <b>Grimstep</b> & <b>Blindside</b>.<br/>'
            '<b>Blindside:</b> When you wound the monster from its blind spot, '
            'all of its reflex reactions become failure reactions until this '
            'attack ends.'
        ),
        'rules': ['Paired', 'Block 1'],
        'recipes': [
            {
                'prefix_text': '1x Dense Bone from a level 3 Gorm',
                'resource_types': {'organ': 1, 'scrap': 1},
            },
            {
                'prefix_text': '1x bone resource from a level 3 monster',
                'resource_handles': {'perfect_bone': 1},
                'resource_types': {'organ': 1, 'scrap': 1},
            },
        ],
    },
    'gusk_knife_grimstep': {
        'name': 'Gusk Knife (Grimstep)',
        'type': 'beta_gear_recipe',
        'expansion': 'grimmory',
        'keywords': ['weapon', 'melee', 'dagger', 'shield', 'bone'],
        'speed': 3,
        'accuracy': 6,
        'strength': 5,
        'affinities': {'bottom': 'green'},
        'desc': (
            'If paired, this gains <b>Grimstep</b> & <b>Blindside</b>.<br/>'
            '<b>Grimstep:</b> When you are attacking and block a hit, you may '
            'move up to 6 <b>consecutive</b> spaces. If you do, your next '
            'wound attempt this attack gains strength equal to the number of '
            'spaces moved.'
        ),
        'rules': ['Paired', 'Block 1'],
        'recipes': [
            {
                'prefix_text': '1x Dense Bone from a level 3 Gorm',
                'resource_types': {'organ': 1, 'scrap': 1},
            },
            {
                'prefix_text': '1x bone resource from a level 3 monster',
                'resource_handles': {'perfect_bone': 1},
                'resource_types': {'organ': 1, 'scrap': 1},
            },
        ],
    },
}

pascha = {
    'ashen_shears': {
        'name': 'Ashen Shears',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'pascha',
        'keywords': ['weapon', 'melee', 'scissors', 'two-handed', 'bone'],
        'rules': ['Slow', 'Frail', 'Block 1'],
        'speed': 1,
        'accuracy': 6,
        'strength': 6,
        'affinities': {'top': 'red', 'right': 'green'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1, 'green': 1}},
            'desc': 'This gains <b>Cleavage 3</b>.'
        },
        'recipes': [
            {
                'locations': ['weapon_crafter'],
                'resource_handles': {'perfect_hide': 1},
                'resource_types': {'organ': 1, 'scrap': 3},
            },
        ],
    },
}

willow = {
    'refined_lantern_sword': {
        'name': 'Refined Lantern Sword',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'pascha',
        'keywords': ['weapon', 'melee', 'sword', 'finesse', 'metal'],
        'rules': ['Sharp', 'Refined'],
        'speed': 3,
        'accuracy': 5,
        'strength': 5,
        'affinities': {'left': 'red', 'right': 'blue'},
        'desc': (
            '<b>Refined:</b> When this fails to wound, you may reroll the '
            'wound attempt. Limit, once per attack.'
        ),
        'recipes': [
            {
                'prefix_text': '1x <font class="kdm_manager_font">E</font>',
                'innovations': ['scrap_smelting'],
                'gear_handles': {'lantern_sword': 1},
                'resource_handles': {'perfect_bone': 1},
                'suffix_text': '5x Resource from a level 3 monster',
            },
        ],
    },
}

doll = {
    'needle_sword': {
        'name': 'Needle Sword',
        'beta': True,
        'type': 'beta_gear',
        'expansion': 'doll',
        'keywords': ['weapon', 'melee', 'sword'],
        'speed': 3,
        'accuracy': 2,
        'strength': 1,
        'rules': ['Cursed', 'Frail'],
        'desc': 'On a <b>Perfect hit</b>, the monster suffers a wound.',
        'affinity_bonus': {
            'requires': {'complete': {'green': 3}},
            'desc': 'This gains +1 <b>Perfect hit</b> range.',
        },
        'recipes': [
            {
                'prefix_text': (
                    'If you reach <b>The Finale</b>, you may instead find the '
                    'ruins of a broken doll. Gain the <b>Mechanical Heart</b> '
                    'and <b>Needle Sword</b> beta gear. Limit, once per '
                    'campaign. (Hunt Event 100)'
                )
            },
        ]
    },
    'mechanical_heart': {
        'name': 'Mechanical Heart',
        'beta': True,
        'type': 'beta_gear',
        'expansion': 'doll',
        'keywords': ['item', 'metal', 'heavy'],
        'affinities':
            {
                'top': 'green',
                'right': 'green',
                'bottom': 'green',
                'left': 'green'
            },
        'rules': ['Cursed', 'Center'],
        'desc': (
            'Add <font class="inline_shield">9</font> to all hit locations. '
            'Reduce damage you suffer to 1. You can no longer remove your '
            'armor gear or gain armor points.'
        ),
        'recipes': [
            {
                'prefix_text': (
                    'If you reach <b>The Finale</b>, you may instead find the '
                    'ruins of a broken doll. Gain the <b>Mechanical Heart</b> '
                    'and <b>Needle Sword</b> beta gear. Limit, once per '
                    'campaign. (Hunt Event 100)'
                )
            },
        ]
    },
}




white_sunlion_armor = {
    'white_sunlion_mask_2022': {
        'expansion': 'white_sunlion_armor',
        'type': 'gear_recipe',
        'name': 'White Sunlion Mask',
        'armor': 2,
        'location': 'head',
        'keywords': ['armor', 'mask'],
        'rules': ['Accessory'],
        'affinities': {'left': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 2}},
            'desc': (
                'When you <b>Pounce</b> and attack from the blind spot, '
                'add +4 strength for the attack.'
            ),
        },
        'recipes': [
            {
                'resource_handles': {
                    'bleeding_corpse_lily': 1, 'golden_whiskers': 1
                },
                'resource_types': {'bone': 1},
            },
        ],
    },
    'beast_kunai': {
        'expansion': 'white_sunlion_armor',
        'type': 'gear_recipe',
        'name': 'Beast Kunai',
        'keywords': ['melee', 'dagger', 'tool', 'bone'],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'affinities': {'bottom': 'red'},
        'desc': (
            'At the end of your attack with any melee weapon, '
            'you may place yourself in any unoccupied space adjacent '
            'to the monster.'
        ),
        'recipes': [
            {
                'resource_handles': {
                    'bleeding_corpse_lily': 1, 'lion_claw': 1, 'perfect_bone': 1
                },
            },
        ],
    },
}

screaming_sun_armor = {
    'screaming_oni_mask': {
        'name': 'Screaming Oni Mask',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'screaming_sun_armor',
        'armor': 2,
        'location': 'head',
        'keywords': ['armor', 'bone', 'mask'],
        'affinities': {'left': 'blue'},
        'desc': (
            '<font class="kdm_manager_font">A</font>: Scold. '
            'Non-deaf knocked down survivors suffer &#9733; brain damage '
            'and stand. Limit, once per roud.'
        ),
        'recipes': [
            {
                'resource_handles': {
                    'spiral_horn': 1,
                    'skull': 1,
                    'perfect_bone': 1
                },
            },
        ],
    },
}


erza_of_dedheim = {
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

halloween_survivor_flower_knight_costume = {
    'flower_costume': {
        'type': 'seed_pattern',
        'pattern_id': -23,
        'expansion': 'halloween_survivor_flower_knight_costume',
        'name': 'Flower Costume',
        'keywords': ['item'],
        'desc': (
            'Add <font class="inline_shield">1</font> to all hit locations.'
        ),
        'affinities': {'left': 'green', 'right': 'green'},
        'affinity_bonus': {
            'requires': {'puzzle': {'green': 1, 'blue': 1}},
            'desc': (
                'On <b>Arrival</b>, trick or treat! Roll 1d10: 1-5 survivors '
                'gain a -1 luck token. 6+ survivors gain a +1 luck '
                'token.'
            ),
        },
        'recipes': [
            {
                'resource_handles': {
                    'lantern_bloom': 1, 'leather': 1, 'sighing_bloom': 1
                },
                'crafting_process': [
                    (
                        'A survivor with '
                        '<span class="kd deck_icon" deck="D">D</span> '
                        '<b>Flower Addiction</b> huffs pollen at the '
                        'settlement edge.'
                    ),
                    (
                        'You cup a Sighing Bloom to your ear. Its rustling '
                        'petals whisper of a delightful design.'
                    ),
                    (
                        'Before the haze lifts, strip and curl Lantern Bloom '
                        'petals and sew them together into leather.'
                    ),
                ],
            },
        ],
    },
}
