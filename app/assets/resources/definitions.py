"""

    The baseline assets.resources definitions live here.

    Starting with the October 2023 refactor of the API, expansion definitions
    can live in their own files (see imports below).

    Resources, Indomitable Resources and Strange Resources should all be defined
    in these definitions files.

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
        'flavor_text': 'A mind numbingly perfect bone.',
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
        'copies': 2,
        'flavor_text': 'Shockingly appetizing.',
    },
    'bladder': {
        'type': 'screaming_antelope_resources',
        'name': 'Bladder',
        'keywords': ['organ','consumable'],
        'copies': 1,
        'flavor_text': 'Smells like urine.',
    },
    'large_flat_tooth': {
        'type': 'screaming_antelope_resources',
        'name': 'Large Flat Tooth',
        'keywords': ['bone'],
        'desc': (
            'When you gain this, a survivor of your choice gains +1 '
            'insanity.'
        ),
        'copies': 2,
        'flavor_text': 'Its surface is rough and bumpy.',
    },
    'muscly_gums': {
        'type': 'screaming_antelope_resources',
        'name': 'Muscly Gums',
        'keywords': ['organ','consumable'],
        'copies': 2,
        'flavor_text': 'Difficult to pry apart.',
    },
    'pelt': {
        'type': 'screaming_antelope_resources',
        'name': 'Pelt',
        'keywords': ['hide'],
        'copies': 3,
        'flavor_text': 'Coarse and warm.',
    },
    'screaming_brain': {
        'type': 'screaming_antelope_resources',
        'name': 'Screaming Brain',
        'keywords': ['organ','consumable'],
        'desc': (
            '<b class="special-rule">Consume:</b> Archive this and gain '
            'survival up to the current limit.'
        ),
        'copies': 1,
    },
    'shank_bone': {
        'type': 'screaming_antelope_resources',
        'name': 'Shank Bone',
        'keywords': ['bone'],
        'copies': 4,
        'flavor_text': 'Strangely jointed.',
    },
    'spiral_horn': {
        'type': 'screaming_antelope_resources',
        'name': 'Spiral Horn',
        'keywords': ['bone'],
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


core_vermin = {
    'crab_spider': {
        'type': 'vermin_resources',
        'name': 'Crab Spider',
        'desc': '<b class="special-rule">Consume:</b> Archive this and gain +3 survival.',
        'keywords': ['hide','vermin','consumable'],
        'copies': 3,
    },
    'cyclops_fly': {
        'type': 'vermin_resources',
        'name': 'Cyclops Fly',
        'desc': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.<br/><table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The fly\'s eye explodes, releasing acids that melt your insides. You die.</td></tr><tr><td class="roll">4-5</td><td class="result">Slight citrus flavor. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent accuracy.</td></tr></table>',
        'keywords': ['vermin','consumable'],
        'copies': 1,
    },
    'hissing_cockroach': {
        'type': 'vermin_resources',
        'name': 'Hissing Cockroach',
        'keywords': ['vermin','consumable'],
        'desc': '<b class="special-rule">Consume:</b> Archive this to lose all survival and gain 2d10 insanity.<br/>If you are insane, you must consume this.',
        'copies': 1,
    },
    'lonely_ant': {
        'type': 'vermin_resources',
        'name': 'Lonely Ant',
        'keywords': ['vermin','consumable'],
        'desc': '<b class="special-rule">Consume:</b> Archive this to swap your insanity and survival values.',
        'copies': 1,
    },
    'nightmare_tick': {
        'type': 'vermin_resources',
        'name': 'Nightmare Tick',
        'keywords': ['vermin','consumable'],
        'desc': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.<br/><table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The tick grabs the roof of your mouth and sucks all your blood. You die.</td></tr><tr><td class="roll">4-5</td><td class="result">Tastes like iron. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent evasion.</td></tr></table>',
        'copies': 1,
    },
    'sword_beetle': {
        'type': 'vermin_resources',
        'name': 'Sword Beetle',
        'desc': '<b class="special-rule">Consume:</b> Archive this and roll 1d10.<br/><table class="roll-table"><tr class="zebra"><td class="roll">1-3</td><td class="result">The beetle burrows into your brain. You die instantly.</td></tr><tr><td class="roll">4-5</td><td class="result">Tough and disgusting. No effect.</td></tr><tr class="zebra"><td class="roll">6+</td><td class="result">Gain +1 permanent strength.</td></tr></table>',
        'keywords': ['vermin','consumable'],
        'copies': 1,
    },

}

expansion_version = {

    'gibbering_haremite': {
        'name': 'Gibbering Haremite',
        'type': 'vermin_resources',
        'expansion': 'easter_pinup_twilight_knight',
        'keywords': ['vermin', 'consumable'],
        'desc': (
            'When you gain this, unless you <b>consume</b> it immediately, it '
            'latches on and removes all your head armor points. If this is in '
            'settlement storage when survivors <b>depart</b>, add another to '
            'storage and suffer -1 population.<br/><b>Consume:</b> Archive '
            'this and roll 1d10.'
        ),
    },

    # Echoes of Death 3
    'fiddler_crab_spider' : {
        'name': 'Fiddler Crab Spider',
        'expansion': 'echoes_of_death_3',
        'type': 'vermin_resources',
        'keywords': ['hide', 'vermin', 'consumable'],
        'desc': (
            '<b>Consume:</b> Archive this and gain the <b>Armored Fist</b> '
            'fighting art.'
        ),
    },

    # cockroach queen
    'blind_rocker': {
        'name': 'Blind Rocker',
        'expansion': 'cockroach_queen',
        'type': 'vermin_resources',
        'keywords': ['vermin', 'consumable'],
        'survival_limit': 1,
        'detail_box': {
            'title': 'Survival Limit +1',
            'desc': (
                'Creates a pleasing melody with its limbs while in settlement '
                'storage.'
            ),
        },
        'desc': (
            'When survivors return to the settlement and the Blind Rocker is '
            'in storage, roll 1d10. On a 7+, select a <b>returning '
            'survivor</b> to <b>consume</b> this and roll 1d10. On a 1-2, they '
            'die, otherwise they gain the following ability:</br>'
            '<b>Myopic Fighter:</b> Gain +2 accuracy. You may only attack with '
            'daggers or katars.'
        ),
    },

}


expansion_resources = {

    # vignettes of death: white gigalion
    'hooked_claw': {
        'expansion': 'vignettes_of_death_white_gigalion',
        'type': 'strange_resources',
        'name': 'Hooked Claw',
        'flavor_text':
            'Stained with flecks of ancient dried blood and ossified hair',
        'keywords': ['bone'],
    },

    # santa satan
    'lump_of_atnas': {
        'expansion': 'santa_satan',
        'type': 'basic_resources',
        'name': 'Lump of Atnas',
        'keywords': ['hide','bone','organ'],
        'desc': (
            "Nostrils flare with delight. A pungent, pine scent emanates from "
            "the quivering cube. At the start of the settlement phase, if "
            "there are 5 or more <b>Cubes of Atnas</b> in settlement storage, "
            "their scent draws a survivor, sniffing through the darkness. Gain "
            "+1 population, this survivor has a random disorder."
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

    # death crown inheritor aya
    'undying_heart': {
        'name': 'Undying Heart',
        'expansion': 'death_crown_inheritor_aya',
        'type': 'strange_resources',
        'keywords': ['perfect', 'organ'],
        'desc': (
            'When you gain this, gain '
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            '<b>Heartbow</b> and '
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            '<b>Heartstop Arrows</b>.'
        ),
        'flavor_text': 'Slowly ticks at regular intervals.',
    },

    'overgrown_dewclaw': {
        'name': 'Overgrown Dewclaw',
        'keywords': ['indomitable', 'perfect', 'bone'],
        'desc': (
            'When you gain this, gain '
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            '<b>Longclaw</b>.'
        ),
        'flavor_text': 'A powerful vein runs through its center.',
    },

}
