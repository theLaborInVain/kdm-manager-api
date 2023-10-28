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
        'type': 'crimson_crocodile_resources',
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
        'type': 'crimson_crocodile_resources',
        'copies': 3,
        'keywords': ['bone'],
        'flavor_text': 'The twisted bone of a twisted monster.'
    },
    'crimson_fin': {
        'name': 'Crimson Fin',
        'expansion': 'crimson_crocodile',
        'type': 'crimson_crocodile_resources',
        'copies': 1,
        'keywords': ['hide', 'organ'],
        'flavor_text': 'Bloodless, yet always wet.'
    },
    'eye_of_immortal': {
        'name': 'Eye of Immortal',
        'expansion': 'crimson_crocodile',
        'type': 'crimson_crocodile_resources',
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
        'type': 'crimson_crocodile_resources',
        'copies': 3,
        'keywords': ['organ'],
        'flavor_text': 'Makes a flatulent sound when blown into.',
    },
    'groomed_nails': {
        'name': 'Groomed Nails',
        'expansion': 'crimson_crocodile',
        'type': 'crimson_crocodile_resources',
        'copies': 1,
        'keywords': ['bone'],
        'flavor_text': 'Impressively stone-ground.'
    },
    'immortal_tongue': {
        'name': 'Immortal Tongue',
        'expansion': 'crimson_crocodile',
        'type': 'crimson_crocodile_resources',
        'copies': 1,
        'keywords': ['bone', 'organ'],
        'flavor_text': (
            'A strange organ supported by a skeleton of pliable bones.'
        ),
    },
    'pale_fingers': {
        'name': 'Pale Fingers',
        'expansion': 'crimson_crocodile',
        'type': 'crimson_crocodile_resources',
        'copies': 2,
        'keywords': ['bone', 'hide'],
        'flavor_text': 'Slender digits taken from its back.',
    },
    'pale_flesh': {
        'name': 'Pale Flesh',
        'expansion': 'crimson_crocodile',
        'type': 'crimson_crocodile_resources',
        'copies': 3,
        'keywords': ['hide'],
        'flavor_text': 'A hunk of foul-smelling flesh.',
    },
    'tiny_ear': {
        'name': 'Tiny Ear',
        'expansion': 'crimson_crocodile',
        'type': 'crimson_crocodile_resources',
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
        'type': 'crimson_crocodile_resources',
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
        'type': 'crimson_crocodile_resources',
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
        'type': 'crimson_crocodile_resources',
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
        'type': 'crimson_crocodile_resources',
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
        'type': 'crimson_crocodile_resources',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'organ'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Immortal Arm</b>. <br/>"
            'You may spend <font class="kdm_manager_font">e</font> to archive '
            'this and suck an artery. Gain'
            '<span class="kd deck_icon deck="FA">FA</span> <b>Bloodzerker</b>.'
        ),
    },
    'secret_stone': {
        'name': 'Secret Stone',
        'expansion': 'crimson_crocodile',
        'type': 'crimson_crocodile_resources',
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
        'type': 'crimson_crocodile_resources',
        'copies': 1,
        'keywords': ['indomitable', 'perfect', 'bone'],
        'desc': (
            "When you gain this, gain "
            '<span class="kd deck_icon kdm_manager_font" deck="p">XX</span> '
            "<b>Blood Drinker</b>. <br/>"
            '<b>Consume:</b> Archive this to gain '
            '<span class="kd deck_icon deck="SF">SF</span> <b>Aerial '
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
