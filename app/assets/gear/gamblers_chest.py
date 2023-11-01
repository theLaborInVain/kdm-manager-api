'''

    Includes gear from all Gambler's Chest expansions.

'''

crimson_crockery = {

    'blood_compass_lantern': {
        'expansion': 'crimson_crocodile',
        'name': 'Blood Compass Lantern',
        'keywords': ['item', 'lantern', 'other'],
        'affinities': {'right': 'blue', 'bottom': 'blue'},
        'desc': (
            'Before making a wound attempt, you may gain 1 bleeding token to '
            'discard all hit locations from your attack and draw that many to '
            'replace them. Limit once per round.'
        ),
        'recipes': [
            {
                'resource_handles': {'groomed_nails': 1, 'skull': 1},
                'resource_types': {'scrap': 1},
            },
        ],
    },

    'bloodglass_cleaver': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodglass Cleaver',
        'keywords': ['weapon', 'melee', 'axe', 'bone'],
        'speed': 3,
        'accuracy': 6,
        'strength': 0,
        'affinities': {'right': 'red', 'bottom': 'red'},
        'rules': ['Honed 5'],
        'related_rules': ['guardless', 'honed_x'],
        'desc': (
            'While this is equipped, you are <b>guardless</b>. <br/>'
            '<b>Guardless:</b> You cannot dodge or ignore hits.'
        ),
        'recipes': [
            {
                'resource_handles': {'flat_vein': 1, 'veined_glass': 1},
                'resource_types': {'organ': 1},
            },
        ],
    },

    'bloodglass_dagger': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodglass Dagger',
        'keywords': ['weapon', 'melee', 'dagger', 'bone'],
        'speed': 3,
        'accuracy': 6,
        'strength': 0,
        'affinities': {'right': 'red'},
        'rules': ['Honed 3'],
        'related_rules': ['honed_x', 'parry', 'super_dense'],
        'desc': (
            '<b>Honed 3:</b> This has +3 strength until its edge is ruined '
            'after wounding a <b>Parry</b> or <b>Super-dense</b> hit location. '
        ),
        'recipes': [
            {
                'resource_handles': {'veined_glass': 1},
            },
        ],
    },

    'bloodglass_katar': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodglass Katar',
        'keywords': ['weapon', 'melee', 'katar', 'bone'],
        'speed': 2,
        'accuracy': 6,
        'strength': 0,
        'affinities': {'bottom': 'green'},
        'rules': ['Honed 4', 'Paired'],
        'related_rules': ['guardless', 'honed_x', 'paired'],
        'desc': (
            'While you have 3+ bleeding tokens, you gain +2 evasion and '
            'are <b>guardless</b>.'
        ),
        'recipes': [
            {
                'resource_handles': {'pale_fingers': 1, 'veined_glass': 1},
            },
        ],
    },

}
