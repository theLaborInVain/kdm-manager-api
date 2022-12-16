"""

    All resources (including vermin, strange, etc.) are recorded here.

    Expansions follow in their own, separate dictionary.

    WARNING: this file was ported from v2 of kdm-manager and is a MESS.
    It needs PEP8 clean-up at a minimum, and features a bunch of placeholder
    and to-do and deprecated stuff. YHBW.

"""

core_resources = {

    # basic resources
    '_question_marks': {
        'type': 'basic_resources',
        'name': '???',
        'keywords': ['organ', 'hide', 'bone','consumable'],
        'desc': (
            'You have no idea what monster bit this is. Can be used as a bone, '
            'organ, or hide!'
        ),
        'copies': 2,
    },
    'broken_lantern': {
        'type': 'basic_resources',
        'name': 'Broken Lantern',
        'keywords': ['scrap'],
        'copies': 2,
        'flavor_text': 'Remains of an extinguished lantern.'
    },
    'love_juice': {
       'type': 'basic_resources',
       'name': 'Love Juice',
       'keywords': ['organ', 'consumable'],
       'copies': 2,
       'desc': (
           'During the settlement phase, you may archive this to '
           '<b class="story-event"><font class="kdm_font">g</font> '
           'intimacy</b>. Nominated survivors must be able to '
           '<b class="special-rule">consume</b>'
        ),
    },
    'monster_bone': {
        'type': 'basic_resources',
        'name': 'Monster Bone',
        'keywords': ['bone'],
        'copies': 4,
        'flavor_text': 'A bone suitable for crafting'
    },
    'monster_hide': {
        'type': 'basic_resources',
        'name': 'Monster Hide',
        'keywords': ['hide'],
        'copies': 7,
        'flavor_text': 'The skin of a beast.'
    },
    'monster_organ': {
        'type': 'basic_resources',
        'name': 'Monster Organ',
        'copies': 3,
        'keywords': ['organ'],
        'desc': (
            'If you <b class="special-rule">consume</b> this, archive this '
            'card. Roll 1d10. On a result of 6+, you contract a parasite. '
            'Archive all <b class="keyword">consumable</b> gear in your gear '
            'grid now.'
        ),
    },
    'perfect_bone': {
        'type': 'basic_resources',
        'name': 'Perfect Bone',
        'min_version': 'core_1_6',
        'keywords': ['perfect', 'bone'],
        'desc': '<i class="flavor-text">A mind numbingly perfect bone.</i>',
    },
    'perfect_hide': {
        'type': 'basic_resources',
        'name': 'Perfect Hide',
        'min_version': 'core_1_6',
        'keywords': ['perfect', 'hide'],
        'desc': '<i class="flavor-text">Supreme texture.</i>',
    },
    'perfect_organ': {
        'type': 'basic_resources',
        'name': 'Perfect Organ',
        'min_version': 'core_1_6',
        'keywords': ['perfect', 'organ', 'consumable'],
        'desc': (
            'If you <b>consume</b> this, archive this card. Roll 1d10. On '
            'a result of 6+, you contract a millennium parasite and gain +10 '
            'Hunt XP.'
        ),
    },
    'skull': {
        'type': 'basic_resources',
        'name': 'Skull',
        'keywords': ['bone'],
        'desc': (
            'When you gain this, a survivor of your choice gains +1 insanity.'
        ),
        'copies': 1,
    },
    'scrap': {
        'type': 'basic_resources',
        'name': 'Scrap',
        'keywords': ['scrap'],
        'copies': 0
    },

    # strange resources
    'black_lichen': {
        'name': 'Black Lichen',
        'copies': 1,
        'type': 'strange_resources',
        'desc': (
            'Malleable, pungent and attractive.<br/>'
            'You may <b class="special-rule">consume</b> this. If you do, your '
            'lips turn grey, your hair whitens, and you become infertile. Gain '
            '+1 courage, +1 understanding and suffer the '
            '<b class="severe-injury waist">destroyed genitals</b> severe '
            'waist injury.'
        ),
        'keywords': ['bone','organ','hide','consumable','other'],
    },
    'cocoon_membrane': {
        'name': 'Cocoon Membrane',
        'copies': 1,
        'desc': (
            'Thin copper hairs permeate this jellylike substance. <br/>'
            'Lanterns are repelled by the copper hairs, their light bending to '
            'avoid them.'
        ),
        'keywords': ['organ', 'other'],
        'type': 'strange_resources',
    },
    'elder_cat_teeth': {
        'type': 'strange_resources',
        'name': 'Elder Cat Teeth',
        'keywords': ['bone'],
        'copies': 1,
        'desc': 'As sharp as they are strange.'
    },
    'fresh_acanthus': {
        'type': 'strange_resources',
        'name': 'Fresh Acanthus',
        'keywords': ['herb'],
        'desc': (
            'Archive this to fully heal 1 hit location, including injury '
            'levels and armor points.'
        ),
        'copies': 4,
    },
    'iron': {
        'type': 'strange_resources',
        'name': 'Iron',
        'keywords': ['scrap'],
        'copies': 8,
        'flavor_text': 'Harder than bone.'
    },
    'lantern_tube': {
        'name': 'Lantern Tube',
        'copies': 1,
        'desc': (
            'A fleshy, muscle-lined tube.<br/>'
            'When you gain this, roll 1d10. On a 6+ you find something stuck '
            'inside! Add 1 <b class="resource basic-resource">Broken '
            "Lantern</b> basic resource to the settlement\'s storage."
        ),
        'type': 'strange_resources',
        'keywords': ['organ', 'scrap'],
    },
    'leather': {
        'type': 'strange_resources',
        'name': 'Leather',
        'keywords': ['hide'],
        'copies': 4,
        'flavor_text': 'Never goes out of style.'
    },
    'legendary_horns': {
        'type': 'strange_resources',
        'name': 'Legendary Horns',
        'keywords': ['bone', 'scrap'],
        'copies': 1,
        'flavor_text': 'Holding them fills you with power.'
    },
    'perfect_crucible': {
        'type': 'strange_resources',
        'name': 'Perfect Crucible',
        'keywords': ['iron'],
        'desc': (
            'When you craft with Perfect Crucible, an ancient bacteria is '
            'released into the air. Suffer -1d10 population and archive this '
            'card.'
        ),
        'copies': 1,
    },
    'phoenix_crest': {
        'type': 'strange_resources',
        'name': 'Phoenix Crest',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'Firm and supple.'
    },
    'second_heart': {
        'type': 'strange_resources',
        'name': 'Second Heart',
        'keywords': ['organ', 'bone'],
        'copies': 1,
        'flavor_text': 'It still tries to bite you.'
    },

    # screaming antelope
    'beast_steak': {
        'type': 'screaming_antelope_resources',
        'name': 'Beast Steak',
        'keywords': ['organ','consumable'],
        'desc': '<i class="flavor-text">Shockingly appetizing.</i>',
        'copies': 2,
        'flavor_text': 'Shockingly appetizing.',
    },
    'bladder': {
        'type': 'screaming_antelope_resources',
        'name': 'Bladder',
        'keywords': ['organ','consumable'],
        'desc': '<i class="flavor-text">Smells like urine.</i>',
        'copies': 1,
        'flavor_text': 'Smells like urine.',
    },
    'large_flat_tooth': {
        'type': 'screaming_antelope_resources',
        'name': 'Large Flat Tooth',
        'keywords': ['bone'],
        'desc': 'When you gain this, a survivor of your choice gains +1 insanity.<br/><i class="flavor-text">Its surface is rough and bumpy.</i>',
        'copies': 2,
        'rules_text': 'When you gain this, a survivor of your choice gains +1 insanity.',
        'flavor_text': 'Its surface is rough and bumpy.',
    },
    'muscly_gums': {
        'type': 'screaming_antelope_resources',
        'name': 'Muscly Gums',
        'keywords': ['organ','consumable'],
        'desc': '<i class="flavor-text">Difficult to pry apart.</i>',
        'copies': 2,
        'flavor_text': 'Difficult to pry apart.',
    },
    'pelt': {
        'type': 'screaming_antelope_resources',
        'name': 'Pelt',
        'keywords': ['hide'],
        'desc': '<i class="flavor-text">Coarse and warm.</i>',
        'copies': 3,
        'flavor_text': 'Coarse and warm.',
    },
    'screaming_brain': {
        'type': 'screaming_antelope_resources',
        'name': 'Screaming Brain',
        'keywords': ['organ','consumable'],
        'desc': '<b class="special-rule">Consume:</b> Archive this and gain survival up to the current limit.',
        'copies': 1,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this and gain survival up to the current limit.',
    },
    'shank_bone': {
        'type': 'screaming_antelope_resources',
        'name': 'Shank Bone',
        'keywords': ['bone'],
        'desc': '<i class="flavor-text">Strangely jointed.</i>',
        'copies': 4,
        'flavor_text': 'Strangely jointed.',
    },
    'spiral_horn': {
        'type': 'screaming_antelope_resources',
        'name': 'Spiral Horn',
        'keywords': ['bone'],
        'desc': '<i class="flavor-text">Moans balefully when blown.</i>',
        'copies': 1,
        'flavor_text': 'Moans balefully when blown.',
    },

    # phoenix
    'bird_beak': {
        'type': 'phoenix_resources',
        'name': 'Bird Beak',
        'keywords': ['bone'],
        'copies': 1,
        'flavor_text': 'Surprisingly toothy.',
    },
    'black_skull': {
        'type': 'phoenix_resources',
        'name': 'Black Skull',
        'keywords': ['iron', 'skull', 'bone'],
        'copies': 1,
        'flavor_text': 'Aged to perfection.',
    },
    'hollow_wing_bones': {
        'type': 'phoenix_resources',
        'name': 'Hollow Wing Bones',
        'keywords': ['bone'],
        'copies': 3,
        'flavor_text': 'Delicate and finely balanced.',
    },
    'muculent_droppings': {
        'type': 'phoenix_resources',
        'name': 'Muculent Droppings',
        'keywords': ['organ'],
        'copies': 3,
        'flavor_text': 'Delicately scented, papery husk',
    },
    'phoenix_eye': {
        'type': 'phoenix_resources',
        'name': 'Phoenix Eye',
        'keywords': ['organ', 'scrap'],
        'copies': 1,
        'flavor_text': 'Filled with a thick, metallic liquid.',
    },
    'phoenix_finger': {
        'type': 'phoenix_resources',
        'name': 'Phoenix Finger',
        'keywords': ['bone'],
        'desc': 'When you gain this, a survivor of your choice gains +3 insanity.',
        'copies': 2,
    },
    'phoenix_whisker': {
        'type': 'phoenix_resources',
        'name': 'Phoenix Whisker',
        'keywords': ['hide'],
        'copies': 1,
        'flavor_text': 'Silky, yet robust.',
    },
    'pustules': {
        'type': 'phoenix_resources',
        'name': 'Pustules',
        'keywords': ['organ','consumable'],
        'copies': 2,
        'flavor_text': 'The aroma is tempting.',
    },
    'rainbow_droppings': {
        'type': 'phoenix_resources',
        'name': 'Rainbow Droppings',
        'keywords': ['organ','consumable'],
        'desc': (
            '<b class="special-rule">Consume:</b> Archive this and roll 1d10. '
            'On 7+, gain +1 permanent speed. Otherwise, your heart explodes, '
            'killing you instantly.'
        ),
        'copies': 1,
    },
    'shimmering_halo': {
        'type': 'phoenix_resources',
        'name': 'Shimmering Halo',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'Curiously heavy.',
    },
    'small_feathers': {
        'type': 'phoenix_resources',
        'name': 'Small Feathers',
        'keywords': ['hide'],
        'copies': 3,
        'flavor_text': 'Soft interior with razor sharp edges.',
    },
    'small_hand_parasites': {
        'type': 'phoenix_resources',
        'name': 'Small Hand Parasites',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'Still wriggling.',
    },
    'tail_feathers': {
        'type': 'phoenix_resources',
        'name': 'Tail Feathers',
        'keywords': ['hide'],
        'copies': 3,
        'flavor_text': 'Lighter than air.',
    },
    'wishbone': {
        'type': 'phoenix_resources',
        'name': 'Wishbone',
        'keywords': ['bone'],
        'copies': 1,
        'flavor_text': 'A delicate bone with a strange aura.',
    },

    # white lion
    'curious_hand': {
        'type': 'white_lion_resources',
        'name': 'Curious Hand',
        'keywords': ['hide'],
        'desc': 'When you gain this, a random survivor gains +1 insanity.',
        'copies': 1,
        'flavor_text': 'Holding this fills you with sadness.',
    },
    'eye_of_cat': {
        'type': 'white_lion_resources',
        'name': 'Eye of Cat',
        'keywords': ['organ','consumable'],
        'copies': 1,
        'flavor_text': 'A perfectly preserved eye.',
    },
    'golden_whiskers': {
        'type': 'white_lion_resources',
        'name': 'Golden Whiskers',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'These whiskers are tough!',
    },
    'great_cat_bones': {
        'type': 'white_lion_resources',
        'name': 'Great Cat Bones',
        'keywords': ['bone'],
        'copies': 4,
        'flavor_text': 'Strong and surprisingly light.',
    },
    'lion_claw': {
        'type': 'white_lion_resources',
        'name': 'Lion Claw',
        'keywords': ['bone'],
        'copies': 3,
        'flavor_text': 'A razor-sharp, retractable claw.',
    },
    'lion_tail': {
        'type': 'white_lion_resources',
        'name': 'Lion Tail',
        'keywords': ['hide'],
        'copies': 1,
        'flavor_text': "It's surprisingly heavy.",
    },
    'lion_testes': {
        'type': 'white_lion_resources',
        'name': 'Lion Testes',
        'keywords': ['organ','consumable'],
        'copies': 1,
        'flavor_text': 'A hefty pair of nuts.',
    },
    'shimmering_mane': {
        'type': 'white_lion_resources',
        'name': 'Shimmering Mane',
        'keywords': ['hide'],
        'desc': 'Archive this to gain 2 basic hide resources.',
        'copies': 1,
        'flavor_text': 'It shimmers in the lantern light.',
    },
    'sinew': {
        'type': 'white_lion_resources',
        'name': 'Sinew',
        'keywords': ['organ'],
        'copies': 2,
        'flavor_text': 'These stringy guts are quite useful.',
    },
    'white_fur': {
        'type': 'white_lion_resources',
        'name': 'White Fur',
        'keywords': ['hide'],
        'copies': 4,
        'flavor_text': 'Luxurious and soft to the touch.',
    },
}


vermin = {
    'crab_spider': {
        'type': 'vermin',
        'name': 'Crab Spider',
        'desc': '<b class="special-rule">Consume:</b> Archive this and gain +3 survival.',
        'keywords': ['hide','vermin','consumable'],
        'copies': 3,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this and gain +3 survival.',
    },
    'cyclops_fly': {
        'type': 'vermin',
        'name': 'Cyclops Fly',
        'desc': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.<br/><table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The fly\'s eye explodes, releasing acids that melt your insides. You die.</td></tr><tr><td class="roll">4-5</td><td class="result">Slight citrus flavor. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent accuracy.</td></tr></table>',
        'keywords': ['vermin','consumable'],
        'copies': 1,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.',
        'rules_table': '<table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The fly\'s eye explodes, releasing acids that melt your insides. You die.</td></tr><tr><td class="roll">4-5</td><td class="result">Slight citrus flavor. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent accuracy.</td></tr></table>'
    },
    'hissing_cockroach': {
        'type': 'vermin',
        'name': 'Hissing Cockroach',
        'keywords': ['vermin','consumable'],
        'desc': '<b class="special-rule">Consume:</b> Archive this to lose all survival and gain 2d10 insanity.<br/>If you are insane, you must consume this.',
        'copies': 1,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this to lose all survival and gain 2d10 insanity.<br/>If you are insane, you must consume this.',
    },
    'lonely_ant': {
        'type': 'vermin',
        'name': 'Lonely Ant',
        'keywords': ['vermin','consumable'],
        'desc': '<b class="special-rule">Consume:</b> Archive this to swap your insanity and survival values.',
        'copies': 1,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this to swap your insanity and survival values.',
    },
    'nightmare_tick': {
        'type': 'vermin',
        'name': 'Nightmare Tick',
        'keywords': ['vermin','consumable'],
        'desc': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.<br/><table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The tick grabs the roof of your mouth and sucks all your blood. You die.</td></tr><tr><td class="roll">4-5</td><td class="result">Tastes like iron. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent evasion.</td></tr></table>',
        'copies': 1,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.',
        'rules_table': '<table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The tick grabs the roof of your mouth and sucks all your blood. You die.</td></tr><tr><td class="roll">4-5</td><td class="result">Tastes like iron. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent evasion.</td></tr></table>'
    },
    'sword_beetle': {
        'type': 'vermin',
        'name': 'Sword Beetle',
        'desc': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.<br/><table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The beetle burrows into your brain. You die instantly.</td></tr><tr><td class="roll">4-5</td><td class="result">Tough and disgusting. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent strength.</td></tr></table>',
        'keywords': ['vermin','consumable'],
        'copies': 1,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.',
        'rules_table': '<table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The beetle burrows into your brain. You die instantly.</td></tr><tr><td class="roll">4-5</td><td class="result">Tough and disgusting. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent strength.</td></tr></table>'
    },


    # expansion vermin!

    'gibbering_haremite': {
        'name': 'Gibbering Haremite',
        'type': 'vermin',
        'expansion': 'promo',
        'keywords': ['vermin', 'consumable'],
        'desc': (
            'When you gain this, unless you <b>consume</b> it immediately, it '
            'latches on and removes all your head armor points. If this is in '
            'settlement storage when survivors <b>depart</b>, add another to '
            'storage and suffer -1 population.<br/><b>Consume:</b> Archive '
            'this and roll 1d10.'
        ),
    },
}


expansions = {

    #gorm strange resources
    'active_thyroid': {
        'expansion': 'gorm',
        'type': 'strange_resources',
        'name': 'Active Thyroid',
        'copies': 1,
        'keywords': ['organ', 'consumable'],
        'desc': (
            '<b class="special-rule">Consume:</b> archive this and roll 1d10. '
            'On a 7+, gain +1 permanent speed. Otherwise, your heart explodes, '
            'killing you instantly.'
        ),
    },
    'gormite': {
        'expansion': 'gorm',
        'type': 'strange_resources',
        'name': 'Gormite',
        'keywords': ['scrap', 'iron'],
        'copies': 1,
        'flavor_text': 'The toughest stuff known to man.',
    },
    'pure_bulb': {
        'expansion': 'gorm',
        'type': 'strange_resources',
        'name': 'Pure Bulb',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': "Don't stare at it.",
    },
    'stomach_lining': {
        'expansion': 'gorm',
        'type': 'strange_resources',
        'name': 'Stomach Lining',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'Steadily expands and contracts.',
    },

    # gorm resources
    'acid_gland': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Acid Gland',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'Melts skin.',
    },
    'dense_bone': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Dense Bone',
        'keywords': ['bone'],
        'copies': 2,
        'flavor_text': 'Sturdy.',
    },
    'gorm_brain': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Gorm Brain',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'Shockingly small.',
    },
    'handed_skull': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Handed Skull',
        'keywords': ['bone'],
        'copies': 1,
        'flavor_text': 'Incomparably dense.',
    },
    'jiggling_lard': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Jiggling Lard',
        'keywords': ['organ','hide'],
        'copies': 2,
        'flavor_text': 'Thick, quivering mass.',
    },
    'mammoth_hand': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Mammoth Hand',
        'keywords': ['bone', 'hide', 'organ'],
        'copies': 2,
        'flavor_text': 'An enormous, leathery glove.',
    },
    'meaty_rib': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Meaty Rib',
        'keywords': ['bone', 'organ'],
        'copies': 2,
        'flavor_text': 'Useful and delicious.',
    },
    'milky_eye': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Milky Eye',
        'keywords': ['organ'],
        'desc': (
            'When this resource is gained, select a survivor to gain +3 '
            'insanity.'
        ),
        'copies': 1,
    },
    'stout_heart': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Stout Heart',
        'keywords': ['organ'],
        'copies': 2,
        'flavor_text': 'A titanic pump.',
    },
    'stout_hide': {'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Stout Hide',
        'keywords': ['hide'],
        'copies': 4,
        'flavor_text': 'Tough, wrinkly skin.',
    },
    'stout_kidney': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Stout Kidney',
        'keywords': ['organ'],
        'desc': (
            '<b class="special-rule">Consume:</b> archive this and roll 1d10. '
            'On a result of 6+, gain 10 survival. Otherwise, reduce your '
            'survival to 0.'
        ),
        'copies': 2,
    },
    'stout_vertebrae': {
        'expansion': 'gorm',
        'type': 'gorm_resources',
        'name': 'Stout Vertebrae',
        'keywords': ['bone'],
        'copies': 2,
        'desc': 'Hefty and intricately jointed.',
    },


    # spidicules strange resources
    'silken_nervous_system': {
        'expansion': 'spidicules',
        'type': 'strange_resources',
        'name': 'Silken Nervous System',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'Separates into tiny golden threads.'
    },
    'web_silk': {
        'expansion': 'spidicules',
        'type': 'strange_resources',
        'name': 'Web Silk',
        'keywords': ['silk'],
        'copies': 6,
        'flavor_text': 'Impossible to tear.'
    },

    # spidicules resources
    'arachnid_heart': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Arachnid Heart',
        'keywords': ['organ'],
        'desc': '<i class="flavor-text">Cold to the touch, even when freshly removed.</i>',
        'copies': 1,
        'flavor_text': 'Cold to the touch, even when freshly removed.',
    },
    'chitin': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Chitin',
        'keywords': ['hide'],
        'desc': '<i class="flavor-text">A flaky, bitter-smelling husk.</i>',
        'copies': 1,
        'flavor_text': 'A flaky, bitter-smelling husk.',
    },
    'exoskeleton': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Exoskeleton',
        'keywords': ['hide'],
        'desc': '<i class="flavor-text">Malleable, interlocking plates.</i>',
        'copies': 1,
        'flavor_text': 'Malleable, interlocking plates.',
    },
    'eyeballs': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Eyeballs',
        'keywords': ['organ'],
        'desc': '<i class="flavor-text">Each points in a different direction.</i>',
        'copies': 1,
        'flavor_text': 'Each points in a different direction.',
    },
    'large_appendage': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Large Appendage',
        'keywords': ['bone'],
        'desc': '<i class="flavor-text">Could come in handy.</i>',
        'copies': 2,
        'flavor_text': '<i>Could come in handy.</i>',
    },
    'serrated_fangs': {
        'endeavors': ['serrated_fangs_razor_pushups'],
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Serrated Fangs',
        'keywords': ['bone'],
        'copies': 1,
        'desc': '<div class="kdm-table endevour-table"><div class="table-requirement">Requires <b class="fighting-art">Nightmare Training</b></div><div class="table-header"><div class="table-cost"><font class="kdm_font">d</font></div><h3 class="table-title"><b class="table-name">Razor Push-ups</b> - roll 1d10</div></div><table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">Gain a random disorder</td></tr><tr><td class="roll">4+</td><td class="result">Gain +1 permanent strength. The fangs are crushed; archive this card.</td></tr></table></div>',
        'rules_table': '<div class="kdm-table endevour-table"><div class="table-requirement">Requires <b class="fighting-art">Nightmare Training</b></div><div class="table-header"><div class="table-cost"><font class="kdm_font">d</font></div><h3 class="table-title"><b class="table-name">Razor Push-ups</b> - roll 1d10</div></div><table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">Gain a random disorder</td></tr><tr><td class="roll">4+</td><td class="result">Gain +1 permanent strength. The fangs are crushed; archive this card.</td></tr></table></div>',
        'table': {
            'type': 'endeavor_table',
            'requirements': ['nightmare_training'], #TODO: should we call out the fighting art type? 
            'cost': '1 Endevour',
            'title': 'Razor Push-ups',
            'dice': '1d10',
            'rolls': [
                {
                    'roll': '1 - 3',
                    'roll_low': 1, #TODO: maybe?
                    'roll_high': 3, #TODO: maybe?
                    'effect': 'Gain a random disorder.'
                },
                {
                    'roll': '4+',
                    'roll_low': 4, #TODO: maybe?
                    'roll_high': 9999, #TODO: maybe?
                    'effect': 'Gain a random disorder.'
                },
            ]
        }
    },
    'small_appendages': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Small Appendages',
        'keywords': ['hide'],
        'desc': '<i class="flavor-text">The inner hands look surprisingly human.</i>',
        'copies': 2,
        'flavor_text': '<i>The inner hands look surprisingly human.</i>',
    },
    'spinnerets': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Spinnerets',
        'keywords': ['organ', 'scrap'],
        'desc': '<i class="flavor-text">More complex than any device.</i>',
        'copies': 1,
        'flavor_text': 'More complex than any device.'
    },
    'stomach': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Stomach',
        'keywords': ['organ'], #KDM_ERROR: doesn't have consumable keyword on card.
        'desc': '<b class="special-rule">Consume:</b> Archive this card to gain +1 Hunt XP.',
        'copies': 1,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this card to gain +1 Hunt XP.'
    },
    'thick_web_silk': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Thick Web Silk',
        'keywords': ['silk','hide'],
        'desc': '<i class="flavor-text">Impossible to pierce.</i>',
        'copies': 1,
        'desc': 'Impossible to pierce.',
    },
    'unlaid_eggs': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Unlaid Eggs',
        'keywords': ['organ','consumable'],
        'desc': (
            'During the settlement phase, you may '
            '<b class="special-rule">consume</b> and archive these '
            'delicious little eggs to gain 10 survival.'
        ),
        'copies': 1,
    },
    'venom_sac': {
        'expansion': 'spidicules',
        'type': 'spidicules_resources',
        'name': 'Venom Sac',
        'keywords': ['organ', 'consumable'],
        'desc': (
                '<b class="special-rule">Consume:</b> Archive this card and '
                'roll 1d10. On a 1-5, you die instantly. On a 6+, gain the '
                '<b class="fighting-art secret-fighting-art">Death Touch</b> '
                'Secret Fighting Art.'
        ),
        'copies': 1,
    },


    # dbk DBK dung_beetle_knight strange resources
    'preserved_caustic_dung': {
        'expansion': 'dung_beetle_knight',
        'type': 'strange_resources',
        'name': 'Preserved Caustic Dung',
        'keywords': ['organ', 'consumable', 'dung'],
        'desc': (
            'The live cultures in this exotic mixture of matured dung have '
            'been preserved within a delicate, airtight jelly casing.'
        ),
        'copies': 4,
    },
    'scell': {
        'expansion': 'dung_beetle_knight',
        'type': 'strange_resources',
        'name': 'Scell',
        'keywords': ['organ','consumable'],
        'desc': (
            'As the monster ages, this sticky and corrosive material builds '
            'between the thin layers of its scarab shells. It breaks down '
            "fecal product, preventing the knight\'s joints from locking up."
            '<br/>During <b class="">Black Harvest</b>, a Restorer can make '
            'excellent use of a Scell, using it to nearly perfect the final '
            'step of the calcification process.'
        ),
        'copies': 1,
    },

    # dung_beetle_knight resources 
    'beetle_horn': {
        'expansion': 'dung_beetle_knight',
        'type': 'dung_beetle_knight_resources',
        'name': 'Beetle Horn',
        'keywords': ['bone'],
        'endeavors': ['dbk_horn_ceremony'],
        'desc': (
            'Requires <b class="innovation">Scarification</b> <br/>'
            '<font class="kdm_font">d</font> <b>Horn Ceremony</b> - Archive '
            'and roll 1d10 <table class="roll-table"> <tr class="zebra"> '
            '<td class="roll">1-4</td><td class="result">Your brain is '
            'punctured and you die.</td></tr><tr> <td class="roll">5+</td>'
            '<td class="result">Brain Stimulation. Gain the benefits of '
            '<b class="story-event">Age 1</b> and <b class="story-event">'
            'Age 2</b> without gaining Hunt XP. Brain stimulation ignores '
            'the "once a lifetime" rule on the <b class="story-event">Age</b> '
            'story event.</td></tr></table>',
        ),
        'copies': 1,
    },
    'century_fingernails': {
        'expansion': 'dung_beetle_knight',
        'type': 'dung_beetle_knight_resources',
        'name': 'Century Fingernails',
        'keywords': ['bone'],
        'desc': (
            'These nails are never clipped. Instead, they are folded and '
            'hammered hundreds of times into an impossibly fine edge.'
        ),
        'copies': 2,
    },
    'century_shell': {
        'expansion': 'dung_beetle_knight',
        'type': 'dung_beetle_knight_resources',
        'name': 'Century Shell',
        'keywords': ['hide', 'iron'],
        'desc': (
            'This ancient and mineral-rich armor plate is covered with razor '
            'wind scratches.<br/>You may spend this as if it were a '
            '<b class="resource">Scarab Shell</b> resource.'
        ),
        'copies': 1,
    },
    'compound_eye': {
        'expansion': 'dung_beetle_knight',
        'type': 'dung_beetle_knight_resources',
        'name': 'Compound Eye',
        'keywords': ['organ','consumable'],
        'desc': (
            'A cluster of differently colored eyes, each filled with a creamy, '
            'tangy syrup.<br/>If you have 3+ courage, you may '
            '<b class="special-rule">consume</b> and archive this to gain '
            '+3d10 insanity.'
        ),
        'copies': 1,
    },
    'elytra': {
        'expansion': 'dung_beetle_knight',
        'type': 'dung_beetle_knight_resources',
        'name': 'Elytra',
        'keywords': ['bone', 'hide', 'organ'],
        'desc': (
            'The ribbed underside of these large shells makes an ideal surface '
            'to grind weapons.</i> <br />A survivor may archive this to give '
            'all of their attacks in the next showdown <b class="">Sharp</b>.'
        ),
        'copies': 1,
    },
    'scarab_shell': {
        'expansion': 'dung_beetle_knight',
        'type': 'dung_beetle_knight_resources',
        'name': 'Scarab Shell',
        'keywords': ['hide'],
        'copies': 3,
        'desc': (
            'Cool and oily to the touch. Lantern light reveals a brilliant '
            'band of color dancing on its surface.'
        ),
    },
    'scarab_wing': {
        'expansion': 'dung_beetle_knight',
        'type': 'dung_beetle_knight_resources',
        'name': 'Scarab Wing',
        'keywords': ['organ'],
        'desc': (
            'When soaked in water, these vein-filled wings gain some '
            'elasticity.'
        ),
        'copies': 1,
    },
    'underplate_fungus': {
        'expansion': 'dung_beetle_knight',
        'type': 'dung_beetle_knight_resources',
        'name': 'Underplate Fungus',
        'keywords': ['herb', 'hide', 'consumable'],
        'copies': 1,
        'desc': (
            'A corkscrew-shaped fungus that grows in the empty channels '
            "between the Dung Beetle Knight's armor plating."
        ),
    },


    # sunstalker strange resources
    '1000_year_sunspot': {
        'expansion': 'sunstalker',
        'type': 'strange_resources',
        'name': '1,000 Year Sunspot',
        'keywords': ['bone', 'organ'],
        'desc': (
            'When you craft with this, nominate a survivor. They suffer the '
            '<b class="severe-injury">blind</b> severe injury from working '
            'with this resource.'
        ),
        'copies': 1,
    },
    '3000_year_sunspot': {
        'expansion': 'sunstalker',
        'type': 'strange_resources',
        'name': '3,000 Year Sunspot',
        'keywords': ['bone', 'organ', 'scrap'],
        'desc': (
            'When you craft with this, nominate a survivor and roll 1d10. On a '
            '5+ they get a terrible headache and die.'
        ),
        'copies': 1,
    },
    'bugfish': {
        'expansion': 'sunstalker',
        'type': 'strange_resources',
        'name': 'Bugfish',
        'copies': 1,
        'keywords': ['fish','organ'],
        'desc': (
            '<b class="special-rule">Consume:</b> Gain +2 survival. There is '
            'something in its belly! Gain 1 random vermin and '
            '<b class="special-rule">consume</b> it immediately. Archive this '
            'card.'
        ),
    },
    'salt': {
        'expansion': 'sunstalker',
        'type': 'strange_resources',
        'name': 'Salt',
        'copies': 2,
        'desc': (
            'You may add this to any cooking recipe to gain +1 permanent '
            "strength in addition to the recipe's listed benefits."
        ),
        'flavor_text': (
            'When exposed to lantern light it evaporates, forming a crust.'
        ),
    },
    'sunstones': {
        'expansion': 'sunstalker',
        'type': 'strange_resources',
        'name': 'Sunstones',
        'misspellings': ['Sun Stones'],
        'keywords': ['bone'],
        'copies': 1,
        'flavor_text': 'Small and warm.',
    },
    'hagfish': {
        'expansion': 'sunstalker',
        'type': 'strange_resources',
        'name': 'Hagfish',
        'keywords': ['bone', 'hide'],
        'desc': (
            '<b class="special-rule">Consume:</b> Your hair turns gray and you '
            'gain +1 Hunt XP. Archive this card.'
        ),
        'copies': 1,
    },
    'jowls': {
        'expansion': 'sunstalker',
        'type': 'strange_resources',
        'name': 'Jowls',
        'keywords': ['fish','iron'],
        'desc': (
            'When you gain Jowls, it bites off your nose! If you have no nose, '
            'you die.<br/> If you have <b class="vermin">Jowls</b>, '
            '<b class="vermin">Hagfish</b>, and <b class="vermin">Bugfish</b>, '
            'you are inspired! You may archive all 3 to gain the '
            '<b class="innovation">Filleting Table</b> innovation.'
        ),
        'copies': 1,
    },
    'life_string': {
        'expansion': 'sunstalker',
        'type': 'strange_resources',
        'min_version': 'core_1_6',
        'name': 'Life String',
        'keywords': ['organ'],
        'desc': '<i>A thread of history.</i>',
    },

    # sunstalker resources
    'black_lens': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Black Lens',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'These eyes are filled with a savory, gluey substance that dries when exposed to air.',
    },
    'brain_root': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Brain Root',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'The strands of the root are strong and elastic. The meat on top is useless.',
    },
    'cycloid_scales': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Cycloid Scales',
        'keywords': ['hide'],
        'copies': 5,
        'flavor_text': 'Extremely reflective and colorful.',
    },
    'fertility_tentacle': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Fertility Tentacle',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'This tube-like appendage has a cavity at the base that stores eggs.',
    },
    'huge_sunteeth': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Huge Sunteeth',
        'keywords': ['bone'],
        'copies': 3,
        'flavor_text': 'These tough but light teeth are made of hundreds of thin layers of bone, separated by rows of dicot stems.',
    },
    'inner_shadow_skin': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Inner Shadow Skin',
        'keywords': ['hide'],
        'copies': 1,
        'flavor_text': 'This soft, yet rubbery material blocks light.',
    },
    'prismatic_gills': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Prismatic Gills',
        'keywords': ['organ'],
        'desc': 'When you gain this, gain the <b class="disorder">Emotionless</b> disorder.',
        'copies': 1,
        'flavor_text': 'The gills emit a fuzzy color trail.',
    },
    'shadow_ink_gland': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Shadow Ink Gland',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'The ink can be used to paint shadows that vanish in lantern light.',
    },
    'shadow_tentacles': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Shadow Tentacles',
        'keywords': ['organ', 'hide'],
        'desc': (
            'When you gain this during the hunt or showdown, return it to the '
            'resource deck and draw again if any survivors are '
            '<b class="severe-injury">blind</b>.'
        ),
        'copies': 2,
    },
    'shark_tongue': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Shark Tongue',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'So slippery that its hard to hold!',
    },
    'small_sunteeth': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Small Sunteeth',
        'keywords': ['bone'],
        'copies': 3,
        'flavor_text': 'Unlike the large sunteeth, these are extremely sharp and clean.',
    },
    'stink_lung': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Stink Lung',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'When squeezed, a funny noise emerges followed by a tantalizing aroma.',
    },
    'sunshark_blubber': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Sunshark Blubber',
        'keywords': ['organ'],
        'copies': 1,
        'flavor_text': 'When inflated with air, this blubber gently floats.',
    },
    'sunshark_bone': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Sunshark Bone',
        'keywords': ['bone'],
        'copies': 1,
        'flavor_text': 'The center is filled with water.',
    },
    'sunshark_fin': {
        'expansion': 'sunstalker',
        'type': 'sunstalker_resources',
        'name': 'Sunshark Fin',
        'keywords': ['bone', 'hide'],
        'copies': 1,
        'flavor_text': 'Removing the slimy hands reveals a curable, viscous substance.',
    },

    # vignettes of death: white gigalion
    'hooked_claw': {
        'expansion': 'vignettes_of_death_white_gigalion',
        'type': 'strange_resources',
        'name': 'Hooked Claw',
        'flavor_text':
            'Stained with flecks of ancient dried blood and ossified hair',
        'keywords': ['bone'],
    },


    # lonely_tree
    'blistering_plasma_fruit': {
        'expansion': 'lonely_tree',
        'type': 'strange_resources',
        'name': 'Blistering Plasma Fruit',
        'keywords': ['organ','consumable'],
        'desc': 'You may <b class="special-rule">consume</b> and archive this to gain the following ability: <br/><b class="ability">Nightmare Blood:</b> Whenever you gain a bleeding token, add <font class="kdm_font_2 inline_shield">1</font> to all hit locations.',
        'copies': 1,
        'rules_text': 'You may <b class="special-rule">consume</b> and archive this to gain the following ability: <br/><b class="ability">Nightmare Blood:</b> Whenever you gain a bleeding token, add <font class="kdm_font_2 inline_shield">1</font> to all hit locations.',
        #'abilities': ['nightmare_blood'] TODO: should this ability be called out for easy reference / lookup?
    },
    'drifting_dream_fruit': {
        'expansion': 'lonely_tree',
        'type': 'strange_resources',
        'name': 'Drifting Dream Fruit',
        'keywords': ['consumable'],
        'desc': 'You may <b class="special-rule">consume</b> and archive this to select a Dream on the <b class="story-event">Birth of a Savior</b> story event and gain all associated abilities.',
        'copies': 1,
        'rules_text': 'You may <b class="special-rule">consume</b> and archive this to select a Dream on the <b class="story-event">Birth of a Savior</b> story event and gain all associated abilities.',
        #'story_events': ['birth_of_a_savior'] TODO: should this story event be called out for easy reference / lookup?
    },
    'jagged_marrow_fruit': {
        'expansion': 'lonely_tree',
        'type': 'strange_resources',
        'name': 'Jagged Marrow Fruit',
        'keywords': ['bone', 'scrap','consumable'],
        'desc': 'You may <b class="special-rule">consume</b> and archive this to gain the following ability: <br /><b class="ability">Nightmare Spurs:</b> Once per showdown, you may spend all your survival (at least 1) to lose all your +1 strength tokens and gain that many +1luck tokens.',
        'copies': 1,
        'rules_text': 'You may <b class="special-rule">consume</b> and archive this to gain the following ability: <br /><b class="ability">Nightmare Spurs:</b> Once per showdown, you may spend all your survival (at least 1) to lose all your +1 strength tokens and gain that many +1luck tokens.',
        #'abilities': ['nightmare_spurs'] TODO: should this ability be called out for easy reference / lookup?
    },
    'lonely_fruit': {
        'expansion': 'lonely_tree',
        'type': 'strange_resources',
        'name': 'Lonely Fruit',
        'keywords': ['consumable'],
        'desc': 'During the settlement phase, you may <b class="special-rule">consume</b> and archive this to <b class="story-event"><font class="kdm_font_expansions">a</font><font class="kdm_font">g</font> Lonely Lady</b>.',
        'copies': 1,
        'rules_text': 'During the settlement phase, you may <b class="special-rule">consume</b> and archive this to <b class="story-event"><font class="kdm_font_expansions">a</font> <font class="kdm_font">g</font> Lonely Lady</b>.',
        #'story_events': ['lonely_lady'] TODO: should this story event be called out for easy reference / lookup -- does it need to specify expansion?
    },
    'porous_flesh_fruit': {
        'expansion': 'lonely_tree',
        'type': 'strange_resources',
        'name': 'Porous Flesh Fruit',
        'keywords': ['hide','consumable'],
        'desc': 'You may <b class="special-rule">consume</b> and archive this to gain the following ability: <br/><b class="ability">Nightmare Membrane: </b> You may spend <font class="kdm_font">a</font> <font class="kdm_font">c</font> to exchange any 1 of your tokens for a +1 strength token.',
        'copies': 1,
        'rules_text': 'You may <b class="special-rule">consume</b> and archive this to gain the following ability: <br/><b class="ability">Nightmare Membrane: </b> You may spend <font class="kdm_font">a</font> <font class="kdm_font">c</font> to exchange any 1 of your tokens for a +1 strength token.',
        #'abilities': ['nightmare_membrane'] TODO: should this ability be called out for easy reference / lookup?
    },


    #dragon king strange resources
    'pituitary_gland': {
        'expansion': 'dragon_king',
        'type': 'strange_resources',
        'name': 'Pituitary Gland',
        'keywords': ['organ','consumable'],
        'desc': '<b class="special-rule">Consume:</b> Archive this and roll 1d10. On a 4+, gain +1 permanent strength. Otherwise, you grow to giant size and die.',
        'copies': 1,
        'rules_text': '<b class="special-rule">Consume:</b> Archive this and roll 1d10. On a 4+, gain +1 permanent strength. Otherwise, you grow to giant size and die.',
    },
    'radiant_heart': {
        'expansion': 'dragon_king',
        'type': 'strange_resources',
        'name': 'Radiant Heart',
        'keywords': ['organ'],
        'desc': 'When you gain this resource, roll 1d10. On a 3+ you burst into flames and die.',
        'copies': 1,
        'rules_text': 'When you gain this resource, roll 1d10. On a 3+ you burst into flames and die.',
    },
    'shining_liver': {
        'expansion': 'dragon_king',
        'type': 'strange_resources',
        'name': 'Shining Liver',
        'keywords': ['organ'],
        'desc': '<i class="flavor-text">When exposed to light, it filters it into heat and become darker.</i>',
        'copies': 1,
        'flavor_text': 'When exposed to light, it filters it into heat and become darker.',
    },

    # dragon king resources
    'cabled_vein': {
        'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': 'Cabled Vein',
        'keywords': ['organ'],
        'desc': '<i class="flavor-text">A dense bundle of bloody tubes.</i>',
        'copies': 2,
        'flavor_text': 'A dense bundle of bloody tubes.'

    },
    'dragon_iron': {
        'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': 'Dragon Iron',
        'keywords': ['iron'],
        'desc': '<i class="flavor-text">It feels heavy, but when dropped, falls as slowly as a feather.</i>',
        'copies': 1,
        'flavor_text': 'It feels heavy, but when dropped, falls as slowly as a feather.',
    },
    'hardened_ribs': {
        'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': 'Hardened Ribs',
        'keywords': ['bone'],
        'desc': '<i class="flavor-text">Strong, flexible, and hollow.</i>',
        'copies': 1,
        'flavor_text': 'Strong, flexible, and hollow.',
    },
    'horn_fragment': {
        'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': 'Horn Fragment',
        'keywords': ['bone'],
        'desc': '<i class="flavor-text">Nearby speech causes them to resonate.</i>',
        'copies': 4,
        'flavor_text': 'Nearby speech causes them to resonate.',
    },
    'husk': {
        'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': 'Husk',
        'keywords': ['hide'],
        'desc': '<i class="flavor-text">A decaying layer of former skin.</i>',
        'copies': 3,
        'flavor_text': 'A decaying layer of former skin.',
    },
    "kings_claws": {'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': "King's Claws",
        'keywords': ['bone'],
        'desc': '<i class="flavor-text">Disturbingly warm, and sharp enough to draw blood with a touch.</i>',
        'copies': 4,
        'flavor_text': 'Disturbingly warm, and sharp enough to draw blood with a touch.',
    },
    "kings_tongue": {
        'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': "King's Tongue",
        'keywords': ['hide'],
        'desc': '<i class="flavor-text">Smooth, dry, and sharp.</i>',
        'copies': 1,
        'flavor_text': 'Smooth, dry, and sharp.',
    },
    'radioactive_dung': {
        'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': 'Radioactive Dung',
        'keywords': ['organ', 'scrap'],
        'desc': '<i class="flavor-text">Gives off smoke with an acrid odor.</i>',
        'copies': 2,
        'flavor_text': 'Gives off smoke with an acrid odor.',
    },
    'veined_wing': {
        'expansion': 'dragon_king',
        'type': 'dragon_king_resources',
        'name': 'Veined Wing',
        'keywords': ['hide'],
        'desc': '<i class="flavor-text">Blood drips from it at a constant rate.</i>',
        'copies': 3,
        'flavor_text': 'Blood drips from it at a constant rate.',
    },

    # lion_god #TODO expansion icon
    'canopic_jar': {
        'expansion': 'lion_god',
        'type': 'strange_resources',
        'name': 'Canopic Jar',
        'keywords': ['organ', 'scrap'],
        'copies': 1,
        'desc': 'When you gain this, remove 2 bleeding tokens. <br />During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        'rules_text': 'When you gain this, remove 2 bleeding tokens. <br />During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        #'story_events': ['lonely_lady'] TODO: should this story event be called out for easy reference / lookup -- does it need to specify expansion?
    },
    'old_blue_box': {
        'expansion': 'lion_god',
        'type': 'strange_resources',
        'name': 'Old Blue Box',
        'keywords': ['scrap'],
        'copies': 1,
        'desc': 'During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        'rules_text': 'During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        #'story_events': ['lonely_lady'] TODO: should this story event be called out for easy reference / lookup -- does it need to specify expansion?
    },
    'sarcophagus': {
        'expansion': 'lion_god',
        'type': 'strange_resources',
        'name': 'Sarcophagus',
        'keywords': ['iron'],
        'copies': 1,
        'desc': '-2 movement while you have this. <br />During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        'rules_text': '-2 movement while you have this. <br />During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        #'story_events': ['lonely_lady'] TODO: should this story event be called out for easy reference / lookup -- does it need to specify expansion?
    },
    'silver_urn': {
        'expansion': 'lion_god',
        'type': 'strange_resources',
        'name': 'Silver urn',
        'keywords': ['bone', 'scrap'],
        'copies': 1,
        'desc': 'During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        'rules_text': 'During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        #'story_events': ['lonely_lady'] TODO: should this story event be called out for easy reference / lookup -- does it need to specify expansion?
    },
    'triptych': {
        'expansion': 'lion_god',
        'type': 'strange_resources',
        'name': 'Triptych',
        'keywords': ['hide', 'scrap'],
        'copies': 1,
        'desc': 'When you gain this, gain +3 insanity. <br />During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        'rules_text': 'When you gain this, gain +3 insanity. <br />During the settlement phase, you may archive this to <b class="story-event"><font class="kdm_font">g</font> Death Reading</b>',
        #'story_events': ['lonely_lady'] TODO: should this story event be called out for easy reference / lookup -- does it need to specify expansion?
    },


    # manhunter
    'crimson_vial': {
        'expansion': 'manhunter',
        'type': 'strange_resources',
        'name': 'Crimson Vial',
        'copies': 1,
        'keywords': ['iron', 'consumable'],
        'desc': (
            'You may <b class="special-rule">consume</b> and archive this to '
            'remove all bleeding tokens and any severe injury of your choice.'
        ),
    },
    'red_vial': {
        'expansion': 'manhunter',
        'type': 'strange_resources',
        'name': 'Red Vial',
        'copies': 4,
        'keywords': ['consumable'],
        'desc': (
            'You may <b class="special-rule">consume</b> and archive this to '
            'remove 2 bleeding tokens and gain +1 survival.'
        ),
    },

    # santa satan
    'lump_of_atnas': {
        'expansion': 'santa_satan',
        'type': 'basic_resources',
        'name': 'Lump of Atnas',
        'keywords': ['hide','bone','organ'],
        'desc': """Nostrils flare with delight. A pungent, pine scene emanates from the quivering cube. At the start of the settlement phase, if there are 5 or more <b>Cubes of Atnas</b> in settlement storage, their scent draws a survivor, sniffing through the darkness. Gain +1 population, this survivor has a random disorder."""
    },

    # slenderman
    'crystal_sword_mold': {
        'expansion': 'slenderman',
        'type': 'strange_resources',
        'name': 'Crystal Sword Mold',
        'keywords': ['scrap','iron'],
        'desc': '<i class="flavor-text">This strange crystal refracts light, concentrating it within a natural, sword-shaped chamber.</i>',
        'copies': 1,
        'flavor_text': 'This strange crystal refracts light, concentrating it within a natural, sword-shaped chamber.'
    },
    'dark_water': {
        'expansion': 'slenderman',
        'type': 'strange_resources',
        'name': 'Dark Water',
        'keywords': ['other','consumable'],
        'desc': 'You may <b class="special-rule">consume</b> and archive this to remove all your disorders, then gain a random disorder.',
        'copies': 5,
        'rules_text': 'You may <b class="special-rule">consume</b> and archive this to remove all your disorders, then gain a random disorder.',
    },

    # flower knight
    'lantern_bloom': {
        'expansion': 'flower_knight',
        'type': 'flower_knight_resources',
        'name': 'Lantern Bloom',
        'keywords': ['flower','hide'],
        'rules': ['Perishable'],
        'desc': (
            'You may <b class="special-rule">consume</b> and archive this '
            'during the showdown to gain +3 luck tokens, -1 permanent luck, '
            'and the <b class="disorder">Flower Addiction</b> disorder.'
        ),
        'copies': 3,
    },
    'lantern_bud': {
        'expansion': 'flower_knight',
        'type': 'flower_knight_resources',
        'name': 'Lantern Bud',
        'keywords': ['flower','scrap',],
        'rules': ['Perishable'],
        'desc': (
            'You may <b class="special-rule">consume</b> and archive this '
            'during the settlement phase to gain +3 '
            '<font class="kdm_font">d</font>, skip the next hunt, and gain '
            'the <b class="disorder">Flower Addiction</b> disorder.'
        ),
        'copies': 1,
    },
    'osseous_bloom': {
        'expansion': 'flower_knight',
        'type': 'flower_knight_resources',
        'name': 'Osseous Bloom',
        'keywords': ['flower','bone'],
        'rules': ['Perishable'],
        'desc': (
            'You may <b '
            'class="special-rule">consume</b> and archive this during the '
            'showdown to remove all your bleeding and negative attribute '
            'tokens and gain the <b class="disorder">Flower Addiction</b> '
            'disorder.'
        ),
        'copies': 5,
    },
    'sighing_bloom': {
        'expansion': 'flower_knight',
        'type': 'flower_knight_resources',
        'name': 'Sighing Bloom',
        'keywords': ['flower','organ',],
        'rules': ['Perishable'],
        'desc': (
            'You may '
            '<b class="special-rule">consume</b> and archive this during the '
            'showdown to gain 3 survival, 3 insanity, and the '
            '<b class="disorder">Flower Addiction</b> disorder.'
        ),
        'copies': 3,
    },
    'warbling_bloom': {
        'expansion': 'flower_knight',
        'type': 'flower_knight_resources',
        'name': 'Warbling Bloom',
        'keywords': ['flower','hide'],
        'rules': ['Perishable'],
        'desc': (
            'You may plant this '
            'during the settlement phase to archive it and gain +1 population. '
            'The survivor is born with the <b class="disorder">Flower '
            "Addiction</b> disorder and a face just like the Warbling Bloom's."
        ),
        'copies': 2,
    },


    # Echoes of Death 3
    'fiddler_crab_spider' : {
        'name': 'Fiddler Crab Spider',
        'expansion': 'echoes_of_death_3',
        'type': 'vermin',
        'keywords': ['hide', 'vermin', 'consumable'],
        'desc': (
            '<b>Consume:</b> Archive this and gain the <b>Armored Fist</b> '
            'fighting art.'
        ),
    },

    # Summer Aya
    'fresh_kill': {
        'name': 'Fresh Kill',
        'expansion': 'summer_aya',
        'type': 'strange_resources',
        'keywords': ['bone', 'hide', 'organ', 'consumable'],
        'desc': (
            '<font class="kdm_manager_font">A</font> <b>consume:</b> Archive '
            'this and set your survival equal to half of your survival limit, '
            'rounded up.'
        ),
    },

    # white sunlion armor
    'bleeding_corpse_lily': {
        'name': 'Bleeding Corpse Lily',
        'expansion': 'white_sunlion_armor',
        'type': 'strange_resources',
        'keywords': ['perfect', 'flower', 'organ'],
        'desc': (
            'When you gain this, gain the <b>White Sunlion Mask</b> and '
            '<b>Beast Kunai</b> pattern cards.'
        ),
        'flavor_text': 'Smells of rust and rot.',
    },

}


