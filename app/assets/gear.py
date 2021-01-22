core = {
    # barber surgeon
    'almanac': {
        'type': 'barber_surgeon',
        'name': 'Almanac',
        'keywords': ['item','soluble','flammable'],
        'desc': 'When you <b>depart</b>, gain +2 insanity.<br/>You cannot gain disorders.',
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
        'type': 'barber_surgeon',
        'name': 'Brain Mint',
        'keywords': ['item','consumable'],
        'affinities': {'left': 'blue', 'top': 'green'},
        'desc': '<font class="kdm_font">a</font> <b>Consume:</b> Remove all your tokens and stand up. You may use this while knocked down. Use once per showdown.', 
        'recipes': [
            {'locations': ['barber_surgeon'], 'resource_handles': {'screaming_brain': 1}, },
        ],
    },
    'bug_trap': {
        'type': 'barber_surgeon',
        'name': 'Bug Trap',
        'keywords': ['item','soluble'],
        'desc': 'At the start of the showdown, roll 1d10. On a 3+, add a <b>Bug Patch</b> terrain card to the showdown board.',
        'recipes': [
            {'locations': ['barber_surgeon'], 'resource_handles': {'muscly_gums': 1}, 'resource_types': {'bone':2}},
        ],
    },
    'elder_earrings': {
        'type': 'barber_surgeon',
        'name': 'Elder Earrings',
        'keywords': ['item','jewelry'],
        'affinities': {'left': 'red', 'right': 'green', 'bottom': 'blue'},
        'desc': 'At the start of the <b>showdown</b>, gain +2 survival. +1 Hunt XP after a showdown.',
        'recipes': [
            {'locations': ['barber_surgeon'], 'resource_handles': {'shank_bone': 1}, 'resource_types': {'scrap':1}},
        ],
    },
    'first_aid_kit': {
        'type': 'barber_surgeon',
        'name': 'First Aid Kit',
        'affinities': {'top': 'green', 'left': 'green', 'right': 'green', 'bottom': 'green'},
        'keywords': ['item','heavy'],
        'desc': 'On <b>Arrival</b>, all survivors gain +3 survival.<br/><font class="kdm_font">a</font>: Remove 1 bleeding or negative attribute token from yourself or an adjacent survivor.',
        'recipes': [
            {'locations': ['barber_surgeon'], 'resource_types': {'leather': 1, 'bone':2}, },
        ],
    },
    'musk_bomb': {
        'type': 'barber_surgeon',
        'name': 'Musk Bomb',
        'keywords': ['item','stinky','thrown','fragile'],
        'desc': 'If adjacent to monster when it draws <font class="kdm_font_10">b</font>, you may spend 2 survival and archive Musk Bomb to roll 1d10. On a 3+, discard <font class="kdm_font_10">b</font> without playing it.',
        'recipes': [
            {'locations': ['barber_surgeon'], 'prefix_text': '7x resources', 'innovations': ['pottery']},
        ],
    },
    'scavenger_kit': {
        'type': 'barber_surgeon',
        'name': 'Scavenger Kit',
        'affinities': {'bottom': 'green'},
        'keywords': ['item','heavy'],
        'rules': ['Unique'],
        'desc': "When you defeat a monster, gain either 1 random basic resource or 1 random monster resource from that monster's resource deck.",
        'recipes': [
            {'locations': ['barber_surgeon'], 'resource_types': {'scrap': 1}, 'resource_handles': {'pelt': 1}},
        ],
    },
    'speed_powder': {
        'type': 'barber_surgeon',
        'name': 'Speed Powder',
        'keywords': ['item','soluble'],
        'desc': '<font class="kdm_font">a</font>: Suffer 2 brain damage. Gain +1 speed token. Use once per showdown.',
        'affinities': {'right': 'blue'},
        'recipes': [
            {'locations': ['barber_surgeon'], 'resource_types': {'organ': 2}, 'resource_handles': {'second_heart': 1}},
        ],
    },

    # blacksmith
    'beacon_shield': {
        'type': 'blacksmith',
        'name': 'Beacon Shield',
        'keywords': ['weapon','melee','shield','metal','heavy'],
        'speed': 1,
        'accuracy': 6,
        'strength': 5,
        'rules': ['Block 2'],
        'desc': 'Add <font class="inline_shield">2</font> to all hit locations.<br/><b>Block 2:</b> Spend <font class="kdm_font">a</font> to ignore 2 hits the next time you are attacked. Lasts until your next act. You cannot use <b>block</b> more than once per attack.'

    },
    'dragon_slayer': {
        'type': 'blacksmith',
        'name': 'Dragon Slayer',
        'affinities': {'top': 'blue', 'right': 'red'},
        'speed': 1,
        'accuracy': 6,
        'strength': 9,
        'keywords': ['weapon','melee','grand weapon','two-handed','heavy','metal'],
        'rules': ['Frail', 'Slow','Sharp','Devastating 1', 'Early Iron'],
        'desc': '<b>Early Iron:</b> When an attack roll result is 1, cancel any hits and end the attack.',
    },
    'lantern_armor_set': {
        'type': 'blacksmith',
        'name': 'Lantern Armor Set',
        'desc': 'You feel invincible. On <b>Arrival</b>, gain survival up to the survival limit.<br/>The extra weight is leverage. All clubs in your gear grid gain <b>Sharp</b>.',
    },
    'lantern_cuirass': {
        'type': 'blacksmith',
        'name': 'Lantern Cuirass',
        'armor': 5,
        'location': 'body',
        'keywords': ['armor','set','metal','heavy'],
        'desc': '-2 movement.',
        'affinities': {'top': 'blue', 'left': 'green', 'right': 'green', 'bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'When you <b>depart</b>, add <font class="inline_shield">3</font> to all hit locations with metal armor.',
            'requires': {'puzzle': {'green': 2, 'blue': 2}},
        },
    },
    'lantern_dagger': {
        'type': 'blacksmith',
        'name': 'Lantern Dagger',
        'keywords': ['weapon','melee','dagger','finesse','metal'],
        'speed': 2,
        'accuracy': 7,
        'strength': 1,
        'affinities': {'right': 'red'},
        'rules': ['Paired','Sharp','Early Iron'],
        'desc': '<b>Sharp:</b> Add 1d10 strength to each wound attempt.<br/><b>Early Iron:</b> When an attack roll result is 1, cancel any hits and end the attack.',
    },
    'lantern_gauntlets': {
        'type': 'blacksmith',
        'name': 'Lantern Gauntlets',
        'armor': 5,
        'keywords': ['armor','set','metal','heavy'],
        'affinities': {'left': 'green'},
        'affinity_bonus': {
            'desc': '+2 accuracy with <b>club</b> weapons.',
            'requires': {'puzzle': {'green': 1}},
        },
    },
    'lantern_glaive': {
        'type': 'blacksmith',
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
    },
    'lantern_greaves': {
        'type': 'blacksmith',
        'name': 'Lantern Greaves',
        'keywords': ['armor','set','metal','heavy'],
        'affinity_bonus':{
            'desc': '+2 movement.',
            'requires': {'puzzle': {'red':2,'blue':1}},
        },
        'affinities': {'left': 'red','right': 'red','top': 'blue'},
        'armor': 5,
        'location': 'legs',
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
    },
    'lantern_mail': {
        'type': 'blacksmith',
        'name': 'Lantern Mail',
        'keywords': ['armor','set','metal','heavy'],
        'armor': 5,
        'location': 'waist',
        'affinities': {'right': 'green'},
    },
    'lantern_sword': {
        'type': 'blacksmith',
        'name': 'Lantern Sword',
        'affinities': {'left': 'red'},
        'keywords': ['weapon','melee','sword','finesse','metal'],
        'speed': 3,
        'accuracy': 5,
        'strength': 3,
        'desc': '<b>Sharp:</b> Add 1d10 strength to each wound attempt.<br/><b>Early Iron:</b> When an attack roll result is 1, cancel any hits and end the attack.',
    },
    'perfect_slayer': {
        'type': 'blacksmith',
        'name': 'Perfect Slayer',
        'keywords': ['weapon','melee','grand weapon','two-handed','sword','heavy','finesse','metal'],
        'desc': '-2 movement',
        'rules': ['Slow','Sharp','Devastating 2','Irreplaceable'],
        'affinities': {'bottom': 'red'},
        'speed': 3,
        'accuracy': 6,
        'strength': 14,
    },
    'ring_whip': {
        'type': 'blacksmith',
        'name': 'Ring Whip',
        'rules': ['Sharp','Reach 2'],
        'affinities': {'left': 'blue'},
        'keywords': ['weapon','melee','whip','finesse','metal'],
        'desc': '<b>Early Iron:</b> When an attack roll result is 1, cancel any hits and end the attack.',
        'speed': 2,
        'accuracy': 5,
        'strength': 0,
    },
    'scrap_shield': {
        'type': 'blacksmith',
        'name': 'Scrap Shield',
        'keywords': ['weapon','melee','shield','bone','metal'],
        'affinities': {'right': 'red'},
        'rules': ['Block 1'],
        'desc': 'Add <font class="inline_shield">1</font> to all hit locations.<br/><b>Block 1:</b> Spend <font class="kdm_font">a</font> to ignore 1 hit the next time you are attacked. Lasts until your next act. You cannot use <b>block</b> more than once per attack.',
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
    },

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
        'desc': '<b>Cumbersome:</b> Spend <font class="kdm_font">c</font> as an additional cost to activate this weapon. Ignore Cumbersome if this weapon is activated indirectly (Pounce, Charge, etc.).',
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
        'rules': ['Cumbersome','Range: 6'],
        'desc': '<b>Aim:</b> When you attack, before rolling to hit, you may reduce the speed of this weapon by 1 to gain +2 accuracy for that attack.',
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
            '<b>Pounce:</b> Spend <font class="kdm_font">c</font> and <font '
            'class="kdm_font">a</font> to move 3 spaces in a straight line. '
            'Then, if you moved 3 spaces, activate a melee weapon with +1 '
            'strength.'
        ),
        'armor': 2,
        'location': 'body',
        'affinities': {'top': 'blue'},
    },
    'white_lion_gauntlets': {
        'type': 'catarium',
        'name': 'White Lion Gauntlet',
        'keywords': ['armor','set','fur','heavy'],
        'desc': 'When you <b>Pounce</b>, gain +1 accuracy for your next attack this turn.',
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
            'desc': '<font class="kdm_font">a</font> and 1 survival: Roar. <b>Non-Deaf Insane</b> survivors gain +2 strength until end of round. All other survivors gain +1 insanity.',
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
        'desc': "On <b>Arrival</b>, all survivors gain the <b>Horripilation</b> survivor status card. (See the Watcher's AI Deck.) When not <b>insane</b>, flip this card.",
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
        'keywords': ['weapon','melee','spear','axe','two-handed','finesse','metal'],
        'affinities': {'bottom': 'green'},
        'rules': ['Sharp','Reach 2'],
        'speed': 2,
        'accuracy': 5,
        'strength': 6,
        'affinity_bonus':{
            'desc': 'On a <b>Perfect hit</b>, the edge sharpens. This weapon gains +4 strength for this attack.',
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
        'affinities': {'bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'If you are not deaf, you may ignore effects that target non-deaf survivors.',
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
        'accurady': 5,
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
            {'locations': ['mask_maker'], 'resource_handles': {'small_feather':1}, 'resource_types': {'bone': 6, 'organ': 4}, },
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
        'keywords': ['item','herb','consumable'],
        'desc': 'When you <b>depart</b>, gain +2 survival. When you suffer a severe injury, ignore it and archive this card instead.',
        'recipes': [
            {'locations': ['organ_grinder'], 'resource_handles': {'fresh_acanthus':1} },
        ],
    },
    'fecal_salve': {
        'type': 'organ_grinder',
        'name': 'Fecal Salve',
        'keywords': ['item','balm','stinky'],
        'desc': 'When you <b>depart</b>, gain +1 survival<br/><font class="kdm_font">a</font>: You are not a <b>threat</b> until you attack. If you have the <b>priority target</b> token, remove it.',
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
        'desc': '<b>Cumbersome:</b> Spend <font class="kdm_font">c</font> as an additional cost of activating this weapon.',
        'affinities': {'left': 'red', 'right': 'green'},
        'affinity_bonus': {
            'desc': 'Range +2',
            'requires': {
                'puzzle': {'red': 1, 'green': 1},
                'complete': {'blue': 1},
            }
        },
    },
    'bird_bread': {
        'type': 'plumery',
        'name': 'Bird Bread',
        'keywords': ['item','consumable','soluble'],
        'affinities': {'right': 'green'},
        'desc': '<font class="kdm_font">a</font> <b>Consume:</b> Once per showdown, add <font class="inline_shield">1</font> to all hit locations. Gain <b>priority target</b> token. Roll 1d10. On a 1, reduce your survival to 0.',
    },
    'bloom_sphere': {
        'type': 'plumery',
        'name': 'Bloom Sphere',
        'keywords': ['item','stinky','other'],
        'affinities': {'left': 'green', 'right': 'blue'},
        'affinity_bonus': {
            'desc': 'When you are picked as a target, roll 1d10. On a 6+, the monster must pick a new target, if possible.',
            'requires': {'puzzle': {'green': 1, 'blue':1}},
        },
    },
    'crest_crown': {
        'type': 'plumery',
        'name': 'Crest Crown',
        'keywords': ['item', 'other'],
        'affinities': {'top': 'blue', 'left': 'red', 'right': 'green', 'bottom': 'blue'},
        'desc': '<font class="kdm_font">a</font>: If <b>insane</b>, reshuffle hit location deck.',
        'affinity_bonus': {
            'desc': 'When you depart, gain +1 insanity and +1 survival for every <font class="kdm_font_2 affinity_blue_text">h</font> you have.',
            'requires': {'puzzle': {'red': 1, 'blue':2}},
        },
    },
    'feather_mantle': {
        'type': 'plumery',
        'name': 'Feather Mantle',
        'keywords': ['item', 'flammable'],
        'affinities': {'left': 'blue', 'right': 'green', 'bottom': 'red'},
        'desc': 'When you suffer <b>knockback</b>, you may ignore <b>collision</b> with other survivors and reduce movement by up to 3 spaces.',
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
    },
    'hollow_sword': {
        'type': 'plumery',
        'name': 'Hollow Sword',
        'keywords': ['weapon','melee','sword','bone'],
        'speed': 3,
        'accuracy': 5,
        'strength': 3,
        'rules': ['Frail','Paired'],
        'desc': 'On a <b>perfect hit</b>, make 1 additional attack roll.',
    },
    'hollowpoint_arrow': {
        'type': 'plumery',
        'name': 'Hollowpoint Arrow',
        'keywords': ['item','ammunition','arrow'],
        'speed': 1,
        'accuracy': 6,
        'strength': 11,
        'rules': ['Slow','Ammo - Bow'],
        'desc': 'On a hit, monster gains -1 movement token. Use once per showdown.',
    },
    'hours_ring': {
        'type': 'plumery',
        'name': 'Hours Ring',
        'keywords': ['item','other'],
        'rules': ['Unique','Selfish'],
        'desc': 'Do not gain any tokens for any reason. Do not gain Hunt XP or weapon proficiency. <b>Retired</b> wearers can <b>depart</b>.',
    },
    'phoenix_armor_set': {
        'type': 'plumery',
        'name': 'Phoenix Armor Set',
        'desc': 'Add <font class="inline_shield">1</font> to all hit locations.<br/><b>Charge:</b> Spend <font class="kdm_font">c a</font>, full move in a straight line. At the end of the movement, activate a melee weapon and attack. Add the number of spaces you moved to your strength for the attack.',
    },
    'phoenix_faulds': {
        'type': 'plumery',
        'name': 'Phoenix Faulds',
        'keywords': ['armor','set','feather','metal','flammable'],
        'armor': 4,
        'location': 'waist',
        'desc': 'When you <b>depart</b>, gain +1 insanity.',
    },
    'phoenix_gauntlet': {
        'type': 'plumery',
        'name': 'Phoenix Gauntlet',
        'armor': 4,
        'location': 'arms',
        'keywords': ['armor','set','feather','metal','flammable'],
        'desc': 'When you <b>depart</b>, gain +1 insanity.',
    },
    'phoenix_greaves': {
        'type': 'plumery',
        'name': 'Phoenix Greaves',
        'keywords': ['armor','set','feather','metal','flammable'],
        'affinities': {'right': 'red'},
        'armor': 4,
        'location': 'legs',
        'desc': 'If <b>insane</b>, gain +2 movement.',
    },
    'phoenix_helm': {
        'type': 'plumery',
        'name': 'Phoenix Helm',
        'keywords': ['armor','set','feather','metal','flammable'],
        'armor': 4,
        'location': 'head',
        'affinities': {'bottom': 'blue'},
        'affinity_bonus': {
            'desc': 'If <b>insane</b> at the start of the showdown, gain +1 evasion token.',
            'requires': {
                'puzzle': {'blue':1},
                'complete': {'green': 1, 'red': 1},
            },
        },
    },
    'phoenix_plackart': {
        'type': 'plumery',
        'name': 'Phoenix Plackart',
        'keywords': ['armor','set','feather','metal','flammable'],
        'location': 'body',
        'armor': 4,
        'affinities': {'top': 'blue', 'left': 'green', 'right': 'red'},
        'affinity_bonus':{
            'desc': 'If <b>insane</b>, ignore the first hit each round and suffer 1 brain damage instead.',
            'requires':{
                'puzzle':{'red':1,'blue':1,'green':1},
            },
        },
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
    },

    # rare gear
    'adventure_sword': {
        'type': 'rare_gear',
        'name': 'Adventure Sword',
        'keywords': ['weapon','melee','sword','finesse','other'],
        'rules': ['Unique','Irreplaceable'],
        'desc': "Your courage is added to this weapon's strength.",
        'speed': 3,
        'accuracy': 6,
        'strength': 0,
    },
    'butcher_cleaver': {
        'type': 'rare_gear',
        'name': 'Butcher Cleaver',
        'keywords': ['weapon','melee','axe','other'],
        'rules': ['Paired', 'Sentient', 'Irreplaceable'],
        'speed': 2,
        'accuracy': 5,
        'strength': 5,
        'desc': '<b>Sentient:</b> Must be insane to activate.<br/><b>Irreplaceable:</b> When you die, archive this card.',
    },
    'forsaker_mask': {
        'type': 'rare_gear',
        'name': 'Forsaker Mask',
        'keywords': ['item','mask','metal','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'desc': 'During the Aftermath, you run off into the darkness never to be seen again.<hr/>During the Settlement Phase, you may archive this item to build the <b>Mask Maker</b> location.',
        'armor': 2,
        'location': 'head',
    },
    'lantern_halberd': {
        'type': 'rare_gear',
        'name': 'Lantern Halberd',
        'keywords': ['weapon','melee','two-handed','spear','other'],
        'rules': ['Reach 2','Irreplaceable','Unique'],
        'desc': 'After attacking, if standing, you may move up to 2 spaces directly away from the monster.',
        'speed': 2,
        'accuracy': 4,
        'strength': 7,
    },
    'muramasa': {
        'type': 'rare_gear',
        'name': 'Muramasa',
        'keywords': ['weapon','melee','katana', 'two-handed','other'],
        'rules': ['Frail','Sharp','Sentient','Deadly 2','Unique'],
        'desc': 'When you critically wound with this weapon, gain 2 bleeding tokens.',
        'speed': 6,
        'accuracy': 6,
        'strength': 6,
    },
    'regal_faulds': {
        'type': 'rare_gear',
        'name': 'Regal Faulds',
        'keywords': ['armor','bone','metal'],
        'rules': ['Cursed'],
        'desc': "At the Aftermath, <font class='kdm_font'>g</font> <b>King's Curse</b>.",
        'armor': 4,
        'location': 'waist',
    },
    'regal_gauntlet': {
        'type': 'rare_gear',
        'name': 'Regal Gauntlet',
        'keywords': ['armor','bone','metal'],
        'rules': ['Cursed'],
        'desc': "At the Aftermath, <font class='kdm_font'>g</font> <b>King's Curse</b>.",
        'armor': 4,
        'location': 'arms',
    },
    'regal_greaves': {
        'type': 'rare_gear',
        'name': 'Regal Greaves',
        'keywords': ['armor','bone','metal'],
        'rules': ['Cursed'],
        'desc': "At the Aftermath, <font class='kdm_font'>g</font> <b>King's Curse</b>.",
        'armor': 4,
        'location': 'legs',
    },
    'regal_helm': {
        'type': 'rare_gear',
        'name': 'Regal Helm',
        'keywords': ['armor','bone','metal'],
        'rules': ['Cursed'],
        'desc': "At the Aftermath, <font class='kdm_font'>g</font> <b>King's Curse</b>.",
        'armor': 4,
        'location': 'head',
    },
    'regal_plackart': {
        'type': 'rare_gear',
        'name': 'Regal Plackart',
        'keywords': ['armor','bone','metal'],
        'rules': ['Cursed'],
        'desc': "At the Aftermath, <font class='kdm_font'>g</font> <b>King's Curse</b>.",
        'armor': 4,
        'location': 'body',
    },
    'steel_shield': {
        'type': 'rare_gear',
        'name': 'Steel Shield',
        'keywords': ['weapon','melee','shield','metal','heavy'],
        'rules': ['Irreplaceable',],
        'desc': '-3 movement.<br/>Spend <font class="kdm_font">a</font> or survival to ignore a hit.',
        'speed': 1,
        'accuracy': 6,
        'strength': 6,
    },
    'steel_sword': {
        'type': 'rare_gear',
        'name': 'Steel Sword',
        'keywords': ['weapon','melee','sword','finesse','metal'],
        'rules': ['Irreplaceable','Slow','Sharp'],
        'desc': 'On a <b>Perfect hit</b>, the edge sharpens. Gain +1d10 strength for the rest of the attack.',
        'speed': 1,
        'accuracy': 4,
        'strength': 5,
    },
    'thunder_maul': {
        'type': 'rare_gear',
        'name': 'Thunder Maul',
        'keywords': ['weapon','melee','club','two-handed','other'],
        'rules': ['Irreplaceable', 'Unique','Cursed'],
        'desc': 'On a <b>Perfect hit</b>, the monster is knocked down. Suffer a severe arm injury. All non-deaf survivors suffer 1 brain damage.',
        'speed': 2,
        'accuracy': 6,
        'strength': 10,
    },
    'twilight_sword': {
        'type': 'rare_gear',
        'name': 'Twilight Sword',
        'keywords': ['weapon','melee','two-handed', 'finesse', 'other'],
        'rules': ['Slow','Cursed','Cumbersome','Sentient','Irreplaceable'],
        'desc': 'Gains <b>Devastating 2</b> when fighting the Watcher.<br/>* Accuracy is 9 - Twilight Sword proficiency level.',
        'speed': 1,
        'accuracy': '*',
        'strength': 9,
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
        'desc': '<b>Provoke:</b> When you wound with this weapon, gain the <b>priority target</b> token.',
        'speed': 3,
        'accuracy': 7,
        'strength': 1,
    },

    # starting gear
    'cloth': {
        'type': 'starting_gear',
        'name': 'Cloth',
        'keywords': ['armor'],
        'desc': 'The Cloth protects your waist. Gain 1 armor point at the waist hit location.',
        'armor': 1,
        'location': 'waist',
    },
    'founding_stone': {
        'type': 'starting_gear',
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
        'desc': '<font class="kdm_font">a</font>: Activate weapon gear to the left and right of this card. These are two separate attacks. Cannot be used with two-handed weapons.',
        'affinities': {'left': 'paired', 'right': 'paired'},
        'recipes': [
            {
                'locations': ['stone_circle'], 'resource_handles': {'bladder': 1},
                'resource_types': {'organ': 1}, 'innovations': ['paint'],
            },
        ],
    },
    'blue_charm': {
        'type': 'stone_circle',
        'name': 'Blue Charm',
        'keywords': ['item', 'jewelry', 'fragile'],
        'add_affinity': ['blue'],
        'affinity_bonus': {
            'desc': '<b>Unshakeable:</b> When you draw a <b>Trap</b>, roll 1d10. On a 6+, discard the <b>Trap</b> and reshuffle the deck.',
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
        'desc': 'At the start of the showdown, gain +2 speed and +2 strength tokens if <b>insane</b> and all gear in your gear grid has the <i>bone</i> keyword.',
        'recipes': [
            {'locations': ['stone_circle'], 'resource_handles': {'shank_bone': 1}, 'resource_types': {'bone': 1}, },
        ],
    },
    'boss_mehndi': {
        'type': 'stone_circle',
        'name': 'Boss Mehndi',
        'keywords': ['item','soluble'],
        'desc': 'Boss is brave. While adjacent to you, <b>insane</b> survivors gain +1 speed.',
        'recipes': [
            {'locations': ['stone_circle'], 'resource_handles': {'golden_whiskers': 1}, 'resource_types': {'bone': 1}, },
        ],
    },
    'green_charm': {
        'type': 'stone_circle',
        'name': 'Green Charm',
        'keywords': ['item', 'jewelry', 'fragile'],
        'add_affinity': ['green'],
        'affinity_bonus': {
            'desc': '<b>Undeathable:</b> If you would die, roll 1d10. On a 6+, you inexplicably survive.',
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
        'desc': 'Each showdown, the first time you wound, the monster gains a -1 toughness token.',
        'speed': 2,
        'accuracy': 6,
        'strength': 9,
        'recipes': [
            {'locations': ['stone_circle'], 'resource_handles': {'legendary_horns': 1}, 'resource_types': {'organ': 6}, },
        ],
    },
    'red_charm': {
        'type': 'stone_circle',
        'name': 'Red Charm',
        'keywords': ['item', 'jewelry', 'fragile'],
        'add_affinity': ['red'],
        'affinity_bonus': {
            'desc': '<b>Unstoppable:</b> When you attempt to wound, instead roll 1d10. On a 1-5 fail. On 6-10, wound.',
            'requires': {'complete': {'red': 5}},
        },
        'recipes': [
            {'locations': ['stone_circle'], 'resource_types': {'organ': 3}, },
        ],
    },
    'screaming_armor_set': {
        'type': 'stone_circle',
        'name': 'Screaming Armor Set',
        'desc': 'Add <font class="inline_shield">2</font> to all hit locations.<br/><b>Skewer:</b> After you <b>slam</b>, spend <font class="kdm_font">a</font> to move 1 space and activate a melee weapon with +2 strength. If you wound with a spear, apply that wound roll result to the next selected hit location this attack.',
    },
    'screaming_bracers': {
        'type': 'stone_circle',
        'name': 'Screaming Bracers',
        'armor': 2,
        'keywords': ['armor', 'set', 'fur'],
        'affinities': {'left': 'red', 'top': 'green'},
        'location': 'arms',
        'desc': 'On <b>Arrival</b>, if possible, add an <b>Acanthus Plant</b> terrain card to the showdown. When you activate terrain, you may add +2 to your roll result.',
        'recipes': [
            {'locations': ['stone_circle'], 'resource_handles': {'pelt': 1}, 'resource_types': {'hide': 1}, },
        ],
    },
    'screaming_coat': {
        'type': 'stone_circle',
        'name': 'Screaming Coat',
        'affinities': {'top': 'blue', 'left': 'green', 'right': 'blue', 'bottom': 'green'},
        'armor': 2,
        'location': 'body',
        'keywords': ['armor', 'set', 'fur'],
        'desc': '<b>Slam:</b> Spend <font class="kdm_font">c</font>  to full move forward in a straight line. If you move 4+ spaces and stop adjacent to a monster, it suffers <b>knockback 1</b> and -1 toughness until the end of the round.',
        'recipes': [
            {'locations': ['stone_circle'], 'resource_handles': {'pelt': 1}, 'resource_types': {'bone': 1}, },
        ],
    },
    'screaming_horns': {
        'type': 'stone_circle',
        'name': 'Screaming Horns',
        'armor': 3,
        'location': 'head',
        'keywords': ['armor', 'set', 'bone'],
        'affinities': {'bottom': 'blue'},
        'desc': '<font class="kdm_font">a</font>: Scream. Non-deaf <b>insane</b> survivors gain +1 movement until end of round. All other survivors gain +1 insanity.',
        'recipes': [
            {'locations': ['stone_circle'], 'resource_handles': {'spiral_horn': 1}, 'resource_types': {'scrap': 1}, },
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
        'desc': 'Thick, protective fur protects your parts. Add +1 to severe waist injury roll results.',
        'recipes': [
            {'locations': ['stone_circle'], 'resource_handles': {'pelt': 1}, },
        ],
    },

    # weapon crafter
    'blood_sheath': {
        'type': 'weapon_crafter',
        'name': 'Blood Sheath',
        'keywords': ['item','bone','other'],
        'rules': ['Block 1'],
        'desc': 'When Rainbow Katana is left of Blood Sheath, it loses <b>Frail</b> and gains <b>Sharp</b> (add 1d10 strength to each wound attempt).',
        'affinities': {'left': 'paired'},
        'recipes': [
            {'locations': ['weapon_crafter'], 'resource_handles': {'hollow_wing_bones': 1, 'muculent_droppings': 1}, 'resource_types': {'organ': 5} },
        ],
    },
    'counterweighted_axe': {
        'type': 'weapon_crafter',
        'name': 'Counterweighted Axe',
        'keywords': ['weapon','melee','axe','two-handed'],
        'rules': ['Reach 2'],
        'speed': 2,
        'accuracy': 6,
        'strength': 4,
        'affinities': {'top': 'red', 'right': 'green'},
        'affinity_bonus': {
            'desc': 'Gains <b>Devastating 1</b>: Whenever you wound, inflict 1 additional wound.',
            'requires': {
                'complete': {'green': 1},
                'puzzle': {'red': 1},
            },
        },
        'recipes': [
            {'locations': ['weapon_crafter'], 'resource_types': {'bone': 2, 'hide': 1, 'organ': 1} },
        ],
    },
    'finger_of_god': {
        'type': 'weapon_crafter',
        'name': 'Finger of God',
        'keywords': ['weapon','melee','spear','two-handed'],
        'rules': ['Reach 2'],
        'speed': 2,
        'accuracy': 5,
        'strength': 5,
        'affinities': {'top': 'red'},
        'affinity_bonus': {
            'desc': 'As long as you have 5+ survival, gain +1 accuracy and +1 strength.',
            'requires': {
                'complete': {'red': 1, 'blue': 1, 'green': 1},
            },
        },
        'recipes': [
            {'locations': ['weapon_crafter'], 'resource_handles': {'phoenix_finger': 1}, 'resource_types': {'bone': 4,} },
        ],
    },
    'rainbow_katana': {
        'type': 'weapon_crafter',
        'name': 'Rainbow Katana',
        'keywords': ['weapon','melee','katana','finesse','two-handed'],
        'rules': ['Frail',],
        'speed': 4,
        'accuracy': 4,
        'strength': 4,
        'affinities': {'left': 'red'},
        'affinity_bonus': {
            'desc': 'Gains <b>Deadly</b>.',
            'requires': {
                'complete': {'green': 1, 'blue': 1},
                'puzzle': {'red': 1},
            },
        },
        'recipes': [
            {'locations': ['weapon_crafter'], 'resource_handles': {'bird_beak': 1, 'rainbow_droppings': 1}, 'resource_types': {'iron': 1, 'bone': 6}, 'suffix_text': '<b>Heat</b> Required.'},
        ],
    },
    'scrap_dagger': {
        'type': 'weapon_crafter',
        'name': 'Scrap Dagger',
        'keywords': ['weapon','melee','dagger','metal'],
        'desc': "On a <b>Perfect hit</b>, the edge sharpens. Gain +2 strength for the rest of the attack.",
        'speed': 3,
        'accuracy': 7,
        'strength': 2,
        'affinities': {'top': 'red', 'right': 'red'},
        'recipes': [
            {'locations': ['weapon_crafter'], 'resource_types': {'scrap': 1, 'bone': 1}, 'suffix_text': '<b>Heat</b> Required.'},
        ],
    },
    'scrap_sword': {
        'type': 'weapon_crafter',
        'name': 'Scrap Sword',
        'keywords': ['weapon','melee','sword','metal'],
        'desc': "On a <b>Perfect hit</b>, the edge sharpens. Gain +4 strength for the rest of the attack.",
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
            {'locations': ['weapon_crafter'], 'resource_types': {'scrap': 1, 'bone': 2}, 'suffix_text': '<b>Heat</b> Required.'},
        ],
    },
    'skullcap_hammer': {
        'type': 'weapon_crafter',
        'name': 'Skullcap Hammer',
        'desc': 'On a <b>Perfect Hit</b>, the monster is dazed, and gains -1 speed token until the end of its turn. A monster can be dazed once per round.',
        'keywords': ['weapon','melee','club','bone'],
        'speed': 2,
        'accuracy': 7,
        'strength': 3,
        'affinities': {'bottom': 'green'},
        'recipes': [
            {'locations': ['weapon_crafter'], 'resource_types': {'scrap': 1, 'bone': 2}, },
        ],
    },
    'whistling_mace': {
        'type': 'weapon_crafter',
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
            {'locations': ['weapon_crafter'], 'resource_types': {'organ': 1, 'bone': 2}, },
        ],
    },
    'zanbato': {
        'type': 'weapon_crafter',
        'name': 'Zanbato',
        'keywords': ['weapon','melee','grand weapon','two-handed','bone'],
        'rules': ['Slow','Frail','Deadly'],
        'speed': 1,
        'accuracy': 6,
        'strength': 6,
        'affinities': {'top': 'red', 'right': 'green'},
        'affinity_bonus': {
            'desc': 'Gains <b>Devastating 1:</b> Whenever you wound, inflict 1 additional wound.',
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

    # other/misc./random in the core
    'portcullis_key': {
        'type': 'other',
        'name': 'Portcullis Key',
        'desc': (
            '<i>This is the key to the portcullis. Without it, you will never '
            'get through.</i>'
        ),
    },

}

tenth_anniversary_survivors = {
    'teleric_eye_tac': {
        'name': 'Teleric Eye Tac',
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
        'desc': 'On a <b>Perfect hit</b>, a wound attempt in your attack automatically succeeds.',
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'acid_gland': 1}, 'resource_types': {'bone': 2}},
        ],
    },
    'armor_spikes': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Armor Spikes',
        'keywords': ['item','bone','heavy'],
        'desc': 'If adjacent to the monster when you suffer a severe body injury, the monster suffers a wound. Limit, once per round.',
        'affinities': {'bottom': 'blue'},
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'stout_vertebrae': 1}, 'resource_types': {'scrap': 1}},
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
        'desc': """On a <b>Perfect hit</b>, gain +1 survival. If you are a Sword Master, you understand this weapon's potential. It gains +20 strength.""",
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'gormite': 1, 'handed_skull': 1}, },
        ],
    },
    'gaxe': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Gaxe',
        'keywords': ['weapon','melee','axe','bone'],
        'desc': 'Each showdown, the first time you critically wound the monster, it gains -1 evasion token.',
        'speed': 1,
        'accuracy': 6,
        'strength': 4,
        'affinities': {'top': 'red', 'left': 'red'},
        'affinity_bonus': {
            'desc': 'Gains +1 speed and <b>Savage</b>',
            'requires': {'complete': {'red': 1}},
        },
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'dense_bone': 1, 'stout_hide': 1}, },
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
        'desc': 'Other survivors may move through but not end movement in a space you occupy.',
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'stout_hide': 1}, 'resource_types': {'bone': 1}},
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
            'desc': 'If your courage is higher than &#9733;, ignore intimidate actions.',
            'requires': {'puzzle': {'blue': 1, 'green': 1}},
        },
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'stout_hide': 1, 'handed_skull': 1}, },
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
            {'locations':['gormery'], 'resource_handles': {'stout_hide': 1, }, 'resource_types': {'bone':1} },
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
            'desc': '<b>Guard:</b> At the end of your attack, if you are standing and have a shield in your gear grid, spend 1 survival to move 3 spaces directly away from the monster and <b>Block 1</b> for free.',
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
        'desc': '<font class="kdm_font">a</font>: All non-deaf knocked down survivors stand and gain +<font class="inline_shield">1</font> to all hit locations.<br/>Use once per showdown.',
        'affinities': {'bottom': 'blue'},
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'stout_heart': 1, }, 'resource_types': {'bone':3} },
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
        'rules': ['Deadly','Reach 2'],
        'affinities': {'left':'red'},
        'affinity_bonus': {
            'desc': 'On a <b>Perfect hit</b>, the edge sharpens. Gain +4 strength for the rest of the attack.',
            'requires': {'complete': {'green': 1,'red': 1}},
        },
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'dense_bone': 1, 'jiggling_lard': 1}, },
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
        'desc': 'Once per round, if you wound with this weapon, <b>Block 1</b> for free.',
        'affinities': {'bottom': 'red'},
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'mammoth_hand': 1, }, 'resource_types': {'bone':2} },
        ],
    },
    'pulse_lantern': {
        'expansion': 'gorm',
        'type': 'gormery',
        'name': 'Pulse Lantern',
        'keywords': ['item','lantern','gormskin','fragile'],
        'desc': '<font class="kdm_font">a</font>: Once per showdown, roll 1d10. On a result of 4+, the monster is knocked down and all survivors gain -1 accuracy token.',
        'affinities': {'top': 'red',},
        'recipes': [
            {'locations':['gormery'], 'resource_handles': {'milky_eye': 1, 'active_thyroid': 1}, },
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
        'desc': 'When you critically wound, the next time a monster would draw AI, it performs <b>Basic Action</b> instead.',
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
        'desc': 'When you ignore a hit with <b>Block</b>, gain +1 strength token. When you are knocked down, lose all your +1 strength tokens.',
        'affinities': {'top': 'red'},
    },
    'wisdom_potion': {
        'type': 'gormchymist',
        'expansion': 'gorm',
        'name': 'Wisdom Potion',
        'keywords': ['item','consumable','other'],
        'affinities': {'right': 'blue'},
        'affinity_bonus': {
            'desc': 'Play the showdown with the top card of the hit location deck revealed.',
            'requires': {'complete': {'blue':1}, 'puzzle': {'blue':1}},
        },
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
            'desc': "At the start of your act, you may spend 3 insanity to gain 1 survival or 1 survival to gain 3 insanity.",
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
            'desc': "For every 10 insanity you have, gain +1 speed and +1 strength.",
            'requires': {'complete': {'blue': 2}, 'puzzle': {'red': 1}},
        },
    },
    'death_mehndi': {
        'expansion': 'lion_god',
        'type': 'rare_gear',
        'name': 'Death Mehndi',
        'keywords': ['item','soluble','symbol','other'],
        'rules': ['Cursed'],
        'desc': 'On a <b>Perfect hit</b>, gain 1d10 insanity. -4 to all brain trauma rolls.',
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

sunstalker = {
    'apostle_crown': {
        'expansion': 'sunstalker',
        'type': 'sacred_pool',
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
    'cycloid_scale_armor': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
        'name': 'Cycloid Scale Armor',
        'desc': 'Add <font class="inline_shield">1</font> to all hit locations.<br/><b>Prismatic:</b> Your complete affinities and incomplete affinity halves count as all colors.',
    },
    'cycloid_scale_hood': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
        'name': 'Cycloid Scale Hood',
        'location': 'head',
        'armor': 2,
        'keywords': ['armor','set','scale'],
        'affinities': {'bottom': 'blue'},
        'desc': """Whenever you spend <font class="kdm_font">c</font>, the scales' colors shift. Gain +1 evasion until your next act.""",
        'recipes': [
            {'locations': ['skyreef_sanctuary'], 'resource_handles': {'cycloid_scales': 1, 'prismatic_gills': 1}, 'resource_types': {'hide': 1}},
        ],
    },
    'cycloid_scale_jacket': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
        'name': 'Cycloid Scale Jacket',
        'armor': 2,
        'location': 'body',
        'keywords': ['armor','set','scale'],
        'desc': """When you spend <font class="kdm_font">c</font>, you <b>Shadow Walk</b> and may move through spaces survivors occupy without causing <b>collision</b>.""",
        'affinities': {'left': 'red', 'right': 'red', 'top': 'blue'},
        'affinity_bonus': {
            'desc': '+1 Accuracy', 'requires': {'puzzle': {'blue': 1}, 'complete': {'red': 2}},
        },
    },
    'cycloid_scale_shoes': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
        'name': 'Cycloid Scale Shoes',
        'keywords': ['armor','set','scale'],
        'armor': 2,
        'location': 'legs',
        'affinities': {'top': 'blue', 'left': 'green'},
        'affinity_bonus': {'desc': """<font class="kdm_font">c</font>: You are not a threat until you attack. If you have the <b>priority target</b> token, gain +2 survival and remove it.""", 'requires': {'puzzle': {'blue': 1, 'green':1}}},
    },
    'cycloid_scale_skirt': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
        'name': 'Cycloid Scale Skirt',
        'keywords': ['armor','set','scale'],
        'armor': 2,
        'location': 'waist',
        'affinities': {'top': 'blue', 'bottom': 'green'},
        'affinity_bonus': {
            'desc': """When you <b>depart</b>, gain survival equal to the number of <font class="affinity_blue_text">&#9632;</font> you have.""",
            'requires': {'puzzle': {'green': 1}, 'complete': {'blue': 3}},
        },
    },
    'cycloid_scale_sleeves': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
        'name': 'Cycloid Scale Sleeves',
        'keywords': ['armor','set','scale'],
        'armor': 2,
        'location': 'armos',
        'affinities': {'left': 'blue', 'right': 'blue'},
        'desc': """When you <b>Shadow Walk</b> and attack a monster from its blind spot, your weapon gains +1 accuracy and <b>Sharp</b> for that attack.""",
    },
    'denticle_axe': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
        'name': 'Denticle axe',
        'speed': 2,
        'accuracy': 6,
        'strength': 5,
        'keywords': ['weapon','melee','axe','scale'],
        'affinities': {'right': 'red', 'bottom': 'blue'},
        'affinity_bonus': {
            'desc': """When attacking from the blind spot, the attack gains +2 strength and the first successful wound attempt gains <b>devastating 1</b>.""",
            'requires': {
                'puzzle': {'blue':1},
                'complete': {'blue': 1,'red': 1},
            },
        },
    },
    'eye_patch': {
        'expansion': 'sunstalker',
        'type': 'rare_gear',
        'name': 'Eye Patch',
        'keywords': ['item','leather'],
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
        'keywords': ['item','other'],
        'rules': ['Unique'],
        'desc': (
            "When a bow is below God's string, it gains <b>sharp</b>, and its "
            "range is increased by 1."
        ),
        'affinities': {'bottom': 'paired',},
    },
    'ink_blood_bow': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
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
        'type': 'skyreef_sanctuary',
        'name': 'Ink Sword',
        'keywords': ['weapon','melee','sword','fragile'],
        'speed': 4,
        'strength': 4,
        'accuracy': 4,
        'rules': ['Reach 3','Deadly 3'],
        'desc': 'You may only attack with this while ind arkness.',
        'affinities': {'bottom': 'blue'},
    },
    'prism_mace': {
        'expansion': 'sunstalker',
        'type': 'sacred_pool',
        'name': 'Prism Mace',
        'affinities': {'left': 'red', 'top': 'green', 'right': 'blue', 'bottom': 'green'},
        'recipes': [
            {'locations': [{'handle':'sacred_pool', 'level':3}], 'resource_handles': {'iron': 4, 'shimmering_halo': 1, 'elder_cat_teeth': 2}, },
        ],
        'speed': 3,
        'strength': 6,
        'accuracy': 10,
        'rules': ['Unique','Block 1'],
        'desc': """When you wound with this you may <b>block 1</b> for free and discard 1 mood in play if you have any +1 strength tokens.""",
    },
    'quiver_and_sunstring': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
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
        'type': 'skyreef_sanctuary',
        'name': 'Shadow Saliva Shawl',
        'affinities': {'top': 'green', 'bottom': 'green'},
        'affinity_bonus': {'desc': '+1 Evasion. All weapons gain <b>slow</b>', 'requires': {'puzzle': {'green': 2}, 'complete': {'green': 2}}},
        'keywords': ['item','balm','stinky','other'],
        'rules': ['+2 Evasion'],
        'desc': """Cannot ear if you have heavy, soluble, or shield gear, or any gear with <font class="inline_shield">3</font> or higher printed on it.""",
    },
    'skleaver': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
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
        'type': 'skyreef_sanctuary',
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
        'type': 'skyreef_sanctuary',
        'name': 'Sun Lure and Hook',
        'keywords': ['item','tool'],
        'affinities': {'bottom': 'blue'},
        'desc': 'When you <b>depart</b>, gain +1 survival. After Hunt Phase setup, place the <b>Sky Fishing</b> event on any space.',
    },
    'sun_vestments': {
        'expansion': 'sunstalker',
        'type': 'sacred_pool',
        'name': 'Sun Vestments',
        'affinities': {'right': 'red'},
        'recipes': [
            {'locations': [{'handle':'sacred_pool', 'level':2}], 'resource_handles': {'golden_whiskers': 1, 'pustules': 2}, 'resource_types': {'hide': 6} },
        ],
    },
    'sunring_bow': {
        'expansion': 'sunstalker',
        'type': 'sacred_pool',
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
    'sunshark_arrows': {
        'expansion': 'sunstalker',
        'type': 'skyreef_sanctuary',
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
        'type': 'skyreef_sanctuary',
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
        'type': 'skyreef_sanctuary',
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
        'type': 'skyreef_sanctuary',
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

    # Halloween White Speaker 2019
    'black_ghost_dagger': {
        'name': 'Black Ghost Dagger',
        'expansion': 'halloween_white_speaker_2019',
        'type': 'pattern',
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

    # Halloween Ringtail Vixen 2020
    'vixen_tail': {
        'expansion': 'halloween_ringtail_vixen_2020',
        'name': 'Vixen Tail',
        'type': 'pattern',
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

    'grim_muffler': {
        'expansion': 'winter_solstice_lucy',
        'name': 'Grim Muffler',
        'type': 'pattern',
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

    # any promo stuff can go here; white box expansions are separate

    # rare gear
    'ancient_root': {
        'name': 'Ancient Root',
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


    # allison the twilight knight
    'blue_lantern': {
        'expansion': 'promo',
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
        'expansion': 'promo',
        'type': 'rare_gear',
        'name': 'Dormant Twilight Cloak',
        'keywords': ['item','heavy','order','other'],
        'rules': ['Unique','Irreplaceable','Accessory'],
        'desc': 'Ignore sentient on all gear. You cannot depart with this if you have 3+ understanding.',
        'affinities': {'top': 'blue'},
        'location': 'head',
        'armor': 3,
    },

    # pinup devil satan halloween 2018
    'hope_stealer': {
        'expansion': 'promo',
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
        'expansion': 'promo',
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
        'expansion': 'promo',
        'type': 'rare_gear',
        'name': 'Speaker Cult Knife',
        'keywords': ['weapon','melee','steel','dagger','fist & tooth'],
        'speed': 3,
        'accuracy': 6,
        'strength': 4,
        'rules': ['Deadly','Sharp'],
        'affinities': {'top': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'desc': 'While <b>insane</b>, and not wearing armor or accessories, gain +2 evasion, +2 strength.',
            'requires': {'puzzle': {'red': 2}},
        },
    },


    #
    # promo
    #

    # black friday ninja
    'black_friday_lantern': {
        'desc': (
            'On <b>Arrival</b> (at the start of the showdown), you may archive '
            'this and ambush the monster. limit, once per campaign.'
        ),
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Black Friday Lantern',
        'keywords': ['item', 'lantern', 'other'],
        'rules': ['+1 Evasion'],
    },
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

    # detective twilight knight
    'detective_cap': {
        'expansion': 'promo',
        'type': 'promo',
        'name': 'Detective Cap',
        'armor':2,
        'location': 'head',
        'keywords': ['armor','accessory','other'],
        'affinities': {'left': 'red', 'top': 'blue', 'right': 'red', 'bottom': 'blue'},
        'desc': 'You must <b>investigate</b> if a choice to investigate arises. When you would roll to investigate, pick any result. If you are a returning survivor, you leave your hardboiled life behind and retired.',
    },
    'twilight_revolver': {
        'expansion': 'promo',
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

    # pinup wet nurse
    'nightmare_breast_pump': {
        'expansion': 'promo',
        'type': 'promo',
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
        'expansion': 'promo',
        'name': 'Scoopy Club',
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

dbk = {
    'calcified_digging_claw': {
        'expansion': 'dung_beetle_knight',
        'type': 'black_harvest',
        'name': 'Calcified Digging Claw',
        'affinities': {'left': 'green'},
        'speed': 1,
        'accuracy': 4,
        'strength': 5,
        'keywords': ['weapon', 'melee', 'katar', 'pickaxe'],
        'rules': ['Paired', 'Sharp'],
        'desc': """During the <b>Mineral Gathering</b> story event, you may reroll one of your d10.""",
    },
    'calcified_greaves': {
        'expansion': 'dung_beetle_knight',
        'type': 'black_harvest',
        'name': 'Calcified Greaves',
        'keywords': ['item', 'bone', 'heavy'],
        'affinities': {'left': 'green'},
        'desc': """-1 movement. Add <font class="inline_shield">3</font> to all hit locations.""",
        'affinity_bonus': {
            'requires': {'puzzle': {'green': 1}, 'complete': {'blue': 1}},
            'desc': 'Add +2 to <b>Ripple Pattern</b> roll results.',
        },
    },
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
    'calcified_shoulder_pads': {
        'expansion': 'dung_beetle_knight',
        'type': 'black_harvest',
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
        'type': 'black_harvest',
        'name': 'Calcified Zanbato',
        'keywords': ['weapon','melee','grand','two-handed','bone','heavy'],
        'rules': ['Slow','Deadly'],
        'speed': 1,
        'accuracy': 5,
        'strength': 8,
        'affinities': {'top': 'red', 'right': 'green'},
        'affinity_bonus': {
            'desc': 'Gains <b>Devastating 1:</b> Whenever you wound, inflict 1 additional wound.',
            'requires': {
                'puzzle': {'red': 1},
                'complete': {'green': 1},
            },
        },
    },
    'century_greaves': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'Century Greaves',
        'keywords': ['item', 'bone', 'mineral', 'heavy'],
        'affinities': {'left': 'green'},
        'desc': """-1 movement. Add <font class="inline_shield">1</font> to all hit locations.""",
        'affinity_bonus': {
            'requires': {'puzzle': {'green': 1}, 'complete': {'blue': 1}},
            'desc': 'Add +1 to <b>Ripple Pattern</b> roll results.',
        },
    },
    'century_shoulder_pads': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'Century Shoulder Pads',
        'keywords': ['item', 'bone', 'mineral', 'heavy'],
        'affinities': {'right': 'green'},
        'desc': """Add <font class="inline_shield">1</font> to all hit locations.""",
        'affinity_bonus': {
            'requires': {'puzzle': {'green': 1}, 'complete': {'green': 1}},
            'desc': '<b>Ripple Pattern:</b> When you are attacked, roll 1d10. On a 10+, ignore 1 hit.',
        },
    },
    'dbk_errant_badge': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'DBK Errant Badge',
        'keywords': ['item', 'jewelry', 'knight'],
        'rules': ['Unique'],
        'desc': """Add <font class="inline_shield">1</font> to all hit locations. At the start of the showdown, draw 1 tactics card.""",
    },
    'digging_claw': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'Digging Claw',
        'affinities': {'right': 'green'},
        'speed': 1,
        'accuracy': 4,
        'strength': 5,
        'keywords': ['weapon', 'melee', 'katar', 'pickaxe', 'bone', 'mineral'],
        'rules': ['Paired'],
        'desc': """During the <b>Mineral Gathering</b> story event, you may reroll one of your d10.""",
    },
    'hidden_crimson_jewel': {
        'expansion': 'dung_beetle_knight',
        'type': 'rare_gear',
        'name': 'Hidden Crimson Jewel',
        'keywords': ['item', 'jewelry', 'other'],
        'rules': ['Unique', 'Irreplaceable'],
        'desc': 'Once per game phase, you may reroll one d10.',
        'affinities': {'top': 'red', 'right': 'red', 'left': 'red', 'bottom': 'red'},
    },
    'rainbow_wing_belt': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'Rainbow Wing Belt',
        'keywords': ['item', 'flammable'],
        'affinities': {'top': 'red', 'right': 'green'},
        'affinity_bonus': {
            'requires': {'complete': {'red': 2, 'blue': 1, 'green': 1}},
            'desc': 'When any of your attack rolls are 1, you may reroll them. Limit, once per attack.',
        },
    },
    'regenerating_blade': {
        'expansion': 'dung_beetle_knight',
        'type': 'rare_gear',
        'name': 'Regenerating Blade',
        'keywords': ['item', 'mineral', 'other'],
        'affinities': {'left': 'green', 'right': 'blue'},
        'desc': 'During the Settlement Phase, you may archive this to remove the <b>Dismembered Arm</b> or <b>Dismembered Leg</b> permanent injury from one survivor.',
    },
    'rolling_armor_set': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'Rolling Armor Set',
    },
    'rubber_bone_harness': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'Rubber Bone Harness',
        'keywords': ['item', 'bone', 'leather'],
        'affinities': {'left': 'green', 'top': 'red', 'right': 'green', 'bottom': 'blue'},
        'desc': 'Once per showdown, you may convert all of your negative attribute tokens to positive attribute tokens of the same type.',
    },
    'scarab_circlet': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'Scarab Circlet',
        'keywords': ['item', 'bone', 'jewelry', 'other'],
        'affinities': {'top': 'blue', 'bottom': 'blue'},
        'desc': """Add <font class="inline_shield">1</font> to all hit locations. During the showdown, when your survival is reduced to 0, gain +1 strength token.""",
    },
    'seasoned_monster_meat': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'Seasoned Monster Meat',
        'keywords': ['item', 'consumable'],
        'affinities': {'top': 'green', 'right': 'red'},
        'desc': 'When you <b>depart</b>, gain +3 survival.',
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 1}},
            'desc': """<b><font class="kdm_font">a</font> Consume:</b> Gain +3 survival and +1 strength token. Limit, once per showdown.""",
        },
    },
    'the_beetle_bomb': {
        'expansion': 'dung_beetle_knight',
        'type': 'wet_resin_crafter',
        'name': 'The Beetle Bomb',
        'affinities': {'top': 'blue', 'bottom': 'red'},
        'keywords': ['item', 'thrown', 'fragile'],
        'rules': ['Unique'],
        'desc': """<font class="kdm_font">a</font><b>:</b> If adjacent to the monster, roll 1d10. On a 6+, the monster gains -1 accuracy and -1 evasion tokens. Limit, once per showdown.""",
    },
    'trash_crown': {
        'expansion': 'dung_beetle_knight',
        'type': 'rare_gear',
        'name': 'Trash Crown',
        'armor': 4,
        'location': 'head',
        'keywords': ['item', 'jewelry', 'fragile', 'other'],
        'affinities': {'left': 'blue', 'bottom': 'red'},
        'desc': """<b><font class="kdm_font">a</font>:</b> Reveal the next 4 hit location cards and discard 3 that are not <b>traps</b>. Place remaining cards on top of the deck in any order.""",
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
        'desc': """At the start of your act, gain +1 survival.<br/>Once per campaign, you may fire the gun to automatically hit and inflict a critical wound.""",
    },
    "hunters_heart": {
        'expansion': 'manhunter',
        'type': 'manhunter_gear',
        'name': "Hunter's Heart",
        'keywords': ['item', 'consumable', 'metal', 'heavy'],
        'rules': ['Unique'],
        'desc': """If you die, the heart crawls back to the settlement. Roll 1d10. On a 7+, it regrows you.<br/> During the settlement phase, you may archive this to <font class="kdm_font">g</font> <b>Bleeding Heart</b>.""",
    },
    "manhunters_hat": {
        'expansion': 'manhunter',
        'type': 'manhunter_gear',
        'name': "Manhunter's Hat",
        'affinities': {'top': 'red', 'left': 'red', 'bottom': 'blue'},
        'armor': 2,
        'location': 'head',
        'keywords': ['item', 'rawhide', 'leater'],
        'rules': ['Unique', 'Accessory'],
        'affinity_bonus': {
            'desc': """Ignore the first severe <font class="kdm_font_2">b</font> injury you suffer each showdown.""",
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
        'desc': """At the start of any hunt turn, before an event is revealed, you may <font class="kdm_font">g</font> <b>Sonorous Rest</b>. Limit, once per hunt.""", 
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

green_knight = {
    'fetorsaurus': {
        'expansion': 'green_knight_armor',
        'type': 'green_knight_armor',
        'name': 'Fetorsaurus',
        'keywords': ['weapon','set','melee','shield','metal'],
        'rules': ['Block 2'],
        'desc': 'Add <font class="inline_shield">2</font> to all hit locations.<br/>While you carry this, reduce &#9733; by 1.',
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
        'name': 'Green Boots',
        'armor': 5,
        'location': 'legs',
        'expansion': 'green_knight_armor',
        'type': 'green_knight_armor',
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
        'name': 'Green Faulds',
        'armor': 5,
        'location': 'waist',
        'expansion': 'green_knight_armor',
        'type': 'green_knight_armor',
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
        'name': 'Green Gloves',
        'armor': 5,
        'location': 'arms',
        'expansion': 'green_knight_armor',
        'type': 'green_knight_armor',
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
        'name': 'Green Helm',
        'armor': 5,
        'location': 'head',
        'expansion': 'green_knight_armor',
        'type': 'green_knight_armor',
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
        'name': 'Green Plate',
        'armor': 5,
        'location': 'body',
        'expansion': 'green_knight_armor',
        'type': 'green_knight_armor',
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
        'type': 'green_knight_armor',
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


flower_knight = {
    'flower_knight_badge': {
        'expansion': 'flower_knight',
        'type': 'sense_memory',
        'name': 'Flower Knight Badge',
        'keywords': ['item', 'jewelry', 'badge'],
        'rules': ['Unique'],
        'desc': (
            'At the start of the showdown, draw 1 tactics card and gain +1 '
            'evasion token.'
        ),
        'affinities': {'top': 'blue'},
    },
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
    'satchel': {
        'expansion': 'flower_knight',
        'type': 'sense_memory',
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
        'type': 'sense_memory',
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
        'type': 'sense_memory',
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
        'type': 'sense_memory',
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
        'type': 'sense_memory',
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

slenderman = {
    'dark_water_vial': {
        'expansion': 'slenderman',
        'type': 'light_forging',
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
        'type': 'light_forging',
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
        'type': 'light_forging',
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
        'type': 'light_forging',
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
        'type': 'light_forging',
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
        'type': 'light_forging',
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
        'type': 'light_forging',
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
        'type': 'light_forging',
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
        'type': 'light_forging',
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
        'type': 'light_forging',
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

sword_hunter = {
    'excalibur': {
        'name': 'Excalibur',
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
