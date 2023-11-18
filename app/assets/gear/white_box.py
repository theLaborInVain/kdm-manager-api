'''

    Gear from White Box expansions lives here.

'''

white_box_2023 = {

    # helebore a frozen survivor
    'cold_face_dagger': {
        'name': 'Cold Face Dagger',
        'beta': True,
        'type': 'beta_gear_recipe',
        'expansion': 'hellebore',
        'speed': 2,
        'accuracy': 7,
        'strength': 0,
        'keywords': ['weapon', 'melee', 'dagger', 'ice', 'stone'],
        'rules': ['Melting 4'],
        'desc': (
            'If you are <b>Insulated</b>, your warm hands can better clutch '
            'the blade. This gains +1 speed.'
        ),
        'recipes': [
            {
                'endeavor_tokens': 1,
                'gear_handles': {'founding_stone': 1},
            },
        ],
    },

    # deathcrown inheritor aya
    'heartstop_arrows': {
        'name': 'Heartstop Arrows',
        'type': 'pattern',
        'expansion': 'death_crown_inheritor_aya',
        'speed': 1,
        'accuracy': 4,
        'strength': 9,
        'keywords': ['item', 'ammunition', 'arrow', 'fragile', 'other'],
        'rules': ['Ammo - Heartbow, Campaign Limit 5'],
        'desc': (
            'When you wound with this, the monster is knocked down.'
        ),
        'recipes': [
            {
                'resource_handles': [
                    {'leather': 2},
                    {'undying_heart': 1},
                    {'phoenix_eye': 1},
                ],
            },
        ],
    },
    'heartbow': {
        'name': 'Heartbow',
        'type': 'pattern',
        'expansion': 'death_crown_inheritor_aya',
        'speed': 2,
        'accuracy': 7,
        'strength': 7,
        'keywords': ['weapon', 'ranged', 'bow', 'two-handed', 'other'],
        'rules': ['Cumbersome', 'Range: 4'],
        'affinities': {'top': 'red', 'bottom': 'red'},
        'affinity_bonus': {
            'requires': {'puzzle': {'red': 2}},
            'desc': (
                'If you have no non-red affinities, this loses '
                '<b>Cumbersome</b> and gains <b>Sharp</b>.'
            ),
        },
        'recipes': [
            {
                'resource_handles': [
                    {'perfect_bone': 2},
                    {'undying_heart': 1},
                    {'phoenix_whisker': 1},
                ],
            },
        ],
    },

    # lunar twilight knight
    'fish_of_abundance':  {
        'expansion': 'lunar_twilight_knight',
        'type': 'rare_gear',
        'name': 'Fish of Abundance',
        'keywords': ['item', 'consumable'],
        'desc': (
            'On <b>Arrival</b>, gain +1 luck token. Whenever you are knocked '
            'down, flip all your luck tokens.'
        ),
    },

}
