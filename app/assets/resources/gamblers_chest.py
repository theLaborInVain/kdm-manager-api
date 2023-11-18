'''

    All Crimson Crocodile resources live here. This is a good template/example
    resources file for how we want to do things in 2024 and beyond in terms of
    the typography, attributes, organization, etc. of expansion resource files.

'''

crimson_crocodile_resources = {

    #
    # resources
    #

    'blood_stool': {
        'name': 'Blood Stool',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['organ', 'consumable'],
        'desc': (
            '<b>Consume:</b> Archive this to roll 1d10. On a 1-3, you become '
            'ill from the fetid mass. Gain the <b>Anemic</b> impairment. On a '
            '9+, it goes down with relative ease. Gain the <b>Hemostasis</b> '
            'ability.'
        ),
    },
    'crimson_bone': {
        'name': 'Crimson Bone',
        'expansion': 'crimson_crocodile',
        'copies': 3,
        'keywords': ['bone'],
        'flavor_text': 'The twisted bone of a twisted monster.'
    },
    'crimson_fin': {
        'name': 'Crimson Fin',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['hide', 'organ'],
        'flavor_text': 'Bloodless, yet always wet.'
    },
    'eye_of_immortal': {
        'name': 'Eye of Immortal',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['organ', 'consumable', 'other'],
        'desc': (
            'When you gain this, gain the <b>Phobophobia</b> disorder.<br/>'
            '<b>Consume:</b> Archive this and roll 1d10. On a 6+, gain the '
            '<b>Immortal</b> disorder.'
        )
    },
    'flat_vein': {
        'name': 'Flat Vein',
        'expansion': 'crimson_crocodile',
        'copies': 3,
        'keywords': ['organ'],
        'flavor_text': 'Makes a flatulent sound when blown into.',
    },
    'groomed_nails': {
        'name': 'Groomed Nails',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['bone'],
        'flavor_text': 'Impressively stone-ground.'
    },
    'immortal_tongue': {
        'name': 'Immortal Tongue',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['bone', 'organ'],
        'flavor_text': (
            'A strange organ supported by a skeleton of pliable bones.'
        ),
    },
    'pale_fingers': {
        'name': 'Pale Fingers',
        'expansion': 'crimson_crocodile',
        'copies': 2,
        'keywords': ['bone', 'hide'],
        'flavor_text': 'Slender digits taken from its back.',
    },
    'pale_flesh': {
        'name': 'Pale Flesh',
        'expansion': 'crimson_crocodile',
        'copies': 3,
        'keywords': ['hide'],
        'flavor_text': 'A hunk of foul-smelling flesh.',
    },
    'tiny_ear': {
        'name': 'Tiny Ear',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['bone', 'hide'],
        'flavor_text': (
            'When squeezed, a funny noise emerges, followed by a tantalizing'
            'aroma.'
        ),
    },
    'psuedopenis': {
        'name': 'Pseudopenis',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['organ', 'consumable'],
        'desc': (
            '<b>Consume:</b> Archive this to gain +3 survival and the '
            '<b>Invigorator</b> fighting art.'
        ),
    },
    'veined_glass': {
        'name': 'Veined Glass',
        'expansion': 'crimson_crocodile',
        'copies': 3,
        'keywords': ['bone', 'glass'],
        'flavor_text': 'Tiny veins throb to an invisible pulse',
    },


    #
    # indomitable resources
    #

    'crimson_gland': {
        'name': 'Crimson Gland',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'organ'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Fear Spear</b>."
        ),
        'flavor_text': "Pulses with light similar to your lantern's.",
    },
    'diamond_scabs': {
        'name': 'Diamond Scabs',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'hide'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Diamond Scab Katar</b>."
        ),
        'flavor_text': (
            'When you shine lantern light into it, you hear a faint scraping '
            'sound.'
        ),
    },
    'diffuser_heart': {
        'name': 'Diffuser Heart',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'organ'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Immortal Arm</b>. <br/>"
            'You may spend <font class="kdm_manager_font">E</font> to archive '
            'this and suck an artery. Gain'
            '<span class="kd deck_icon" deck="FA">FA</span> <b>Bloodzerker</b>.'
        ),
    },
    'secret_stone': {
        'name': 'Secret Stone',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'stone'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Dome Buster</b>."
        ),
        'flavor_text': (
            'No matter the angle, the eyes always seem to be looking away from '
            'you.'
        ),
    },
    'vampire_fang': {
        'name': 'Vampire Fang',
        'expansion': 'crimson_crocodile',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'bone'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Blood Drinker</b>. <br/>"
            '<b>Consume:</b> Archive this to gain '
            '<span class="kd deck_icon" deck="SF">SF</span> <b>Aerial '
            'Transfusion</b>.'
        ),
    },

    #
    # strange resources
    #

    'blood_diamond_tear': {
        'name': 'Blood Diamond Tear',
        'expansion': 'crimson_crocodile',
        'type': 'strange_resources',
        'copies': 1,
        'keywords': ['organ', 'diamond'],
        'desc': 'When you gain this, gain the <b>Phobophobia</b> disorder.',
    },
    'lustrous_tooth': {
        'name': 'Lustrous Tooth',
        'expansion': 'crimson_crocodile',
        'type': 'strange_resources',
        'copies': 1,
        'keywords': ['perfect', 'bone'],
        'flavor_text': 'Eons of tongue-polishing have made the perfect tooth!',
    },
    'irregular_optic_nerve': {
        'name': 'Blood Diamond Tear',
        'expansion': 'crimson_crocodile',
        'type': 'strange_resources',
        'copies': 1,
        'keywords': ['organ',],
        'desc': (
            'If the settlement has a <b>Barber Surgeon</b>, you may undergo a '
            'procedure there! Archive this and roll 1d10. Add +4 to your roll '
            'if there is a <b>Silk Surgeon</b>. On a 6+ the surgeon swaps your '
            'optic nerve. Cure the <b>blind</b> severe head injury. Otherwise, '
            'suffer it from a terrible accident.'
        ),
    },

}


smog_singers_resources = {
    'delicate_hand': {
        'name': 'Delicate Hand',
        'expansion': 'smog_singers',
        'copies': 2,
        'keywords': ['hide'],
        'flavor_text': 'Wants to be held.'
    },
    'fluted_bone': {
        'name': 'Fluted Bone',
        'expansion': 'smog_singers',
        'copies': 3,
        'keywords': ['bone'],
        'desc': (
            'You may archive this to play a tune. If you do, roll 1d10. On an '
            "8+, gain any music innovation from from the settlement's "
            'deck.'
        ),
    },
    'fluted_severed_head': {
        'name': 'Fluted Severed Head',
        'expansion': 'smog_singers',
        'copies': 1,
        'keywords': ['bone', 'skull'],
        'desc': (
            'When you gain this, a survivor of your choice gains +1 insanity.'
        ),
    },
    'gaseous_belly': {
        'name': 'Gaseous Belly',
        'expansion': 'smog_singers',
        'copies': 2,
        'keywords': ['organ'],
        'flavor_text': 'Incredibly elastic.'
    },
    'pink_flesh': {
        'name': 'Pink Flesh',
        'expansion': 'smog_singers',
        'copies': 4,
        'keywords': ['hide'],
        'flavor_text': 'Turns a deeper pink when air-dried.'
    },
    'singing_tongue': {
        'name': 'Singing Tongue',
        'expansion': 'smog_singers',
        'copies': 2,
        'keywords': ['organ'],
        'flavor_text': (
            'A long, elastic tongue capable of folding into many shapes.'
        )
    },
    'tail_fat': {
        'name': 'Tail Fat',
        'expansion': 'smog_singers',
        'copies': 1,
        'keywords': ['organ'],
        'desc': (
            '<b>Consume:</b> Archive this to gain +1d5 survival. If the '
            'settlement has <b>Cannibalize</b>, the taste is familiar. Gain +1 '
            'understanding. Limit once per lifetime.'
        ),
    },
    'vocal_chords': {
        'name': 'Vocal Chords',
        'expansion': 'smog_singers',
        'copies': 1,
        'keywords': ['organ'],
        'flavor_text': 'The silence is heartbreaking.'
    },
    'whistle_tooth': {
        'name': 'Whistle Tooth',
        'expansion': 'smog_singers',
        'copies': 3,
        'keywords': ['bone', 'scrap'],
        'flavor_text': 'Finger-size holes adorn these teeth.'
    },

    #
    #   indomitable resources
    #

    'belly_steel': {
        'name': 'Belly Steel',
        'expansion': 'smog_singers',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'iron', 'organ'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Drum of Hope</b>."
        ),
        'flavor_text': 'Makes a booming sound when beaten.'
    },
    'crystallized_song': {
        'name': 'Crystallized Song',
        'expansion': 'smog_singers',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'hide'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Saxe</b>."
        ),
        'flavor_text': 'The physical form of a melody.'
    },
    'foreskin_hood': {
        'name': 'Foreskin Hood',
        'expansion': 'smog_singers',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'organ', 'hide'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Discordian</b>."
        ),
        'flavor_text': 'Shrieks when stretched.'
    },
    'fused_feet': {
        'name': 'Fused Feet',
        'expansion': 'smog_singers',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'hide'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Curse Hammer</b>."
        ),
        'flavor_text': 'A set of cursed appendages.'
    },
    'milky_milk_tooth': {
        'name': 'Milky Milk Tooth',
        'expansion': 'smog_singers',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'bone'],
        'desc': 'Archive this to remove <b>shattered jaw</b>.',
        'flavor_text': "A tooth that fits nicely in a survivor's jaw."
    },

    #
    #   strange resources
    #

    'crystal_ember': {
        'name': 'Crystal Ember',
        'expansion': 'smog_singers',
        'type': 'strange_resources',
        'copies': 1,
        'keywords': ['bone'],
        'desc': (
            'You may huff this. Archive it to remove all your disorders and '
            'gain one disorder of your choice.'
        ),
    },

}
