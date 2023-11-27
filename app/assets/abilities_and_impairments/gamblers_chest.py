'''

    A&I definitions for expansions included in the Gambler's Chest.

'''

crimson_crocodile = {
    'anemic': {
        'expansion': 'crimson_crocodile',
        'name': 'Anemic',
        'type': 'impairment',
        'desc': (
            'A survivor impairment. It takes one fewer bleeding token to kill '
            'you. This impairment can be gained multiple times. If you gain '
            'Anemic enough times that it takes 0 bleeding tokens to kill you, '
            'you instantly die.'
        ),
        'max_bleeding_tokens': -1,
        'max': False,
    },
    'hemostasis': {
        'expansion': 'crimson_crocodile',
        'name': 'Hemostasis',
        'type': 'ability',
        'desc': (
            'A survivor ability. It takes an additional bleeding token to kill '
            'you. This ability can be gained multiple times. '
        ),
        'max_bleeding_tokens': 1,
        'max': False,
    },

}

smog_singers = {
    'songheart':  {
        'expansion': 'smog_singers',
        'name': 'Songheart',
        'type': 'ability',
        'desc': 'Reduce the cost of performing your Ballads by 1.'
    },
},
