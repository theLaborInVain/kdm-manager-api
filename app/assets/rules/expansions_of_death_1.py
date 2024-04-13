'''

    The original expansions collection rules are here.

'''

expansions_of_death_1 = {

    # flower knight
    'parry': {
        'expansion': 'flower_knight',
        'type': 'hit_location',
        'name': 'Parry',
        'desc': (
            'A parry hit location represents the monster skillfully deflecting '
            'an attack. <br/> When attempting to would Parry hit locations, '
            'all wound attempts fail unless the wound roll result is critical. '
            'This failure triggers any any Failure reactions as normal.'
        ),
    },
    'perishable': {
        'expansion': 'flower_knight',
        'type': 'special_rule',
        'name': 'Perishable',
        'desc': (
            'This cannot be added to settlement storage. At the end of the '
            'settlement phase, it is lost. Archive it.'
        ),
    },

    # gorm
    'guard': {
        'name': 'Guard',
        'expansion': 'gorm',
        'type': 'special_rule',
        'desc': (
            'At the end of your attack, if you are standing and have a shield '
            'in your gear grid, spend 1 survival to move 3 spaces directly '
            'away from the monster and <b>Block 1</b> for free.'
        ),
        'related': ['block_x'],
    },


    # sunstalker
    'activation_limit_x': {
        'name': 'Activation Limit: N',
        'type': 'special_rule',
        'expansion': 'sunstalker',
        'desc': (
            'May activate this up to N times per showdown (use tokens to '
            'track).'
        ),
    },
    'blind': {
        'name': 'Blind',
        'type': 'special_rule',
        'expansion': 'sunstalker',
        'desc': '-1 Accuracy',
    },
    'prismatic': {
        'expansion': 'sunstalker',
        'type': 'special_rule',
        'name': 'Prismatic',
        'desc': (
            'Your complete affinities and incomplete affinity halves count '
            'as all colors.'
        ),
    },
    'shadow_walk': {
        'expansion': 'sunstalker',
        'type': 'special_rule',
        'name': 'Shadow Walk',
        'desc': None,
    },

}
