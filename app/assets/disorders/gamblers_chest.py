'''

    Gambler's Chest disorders are managed here.

'''

gamblers_chest_disorders = {

    'atelophobia': {
        'name': 'Atelophobia',
        'min_version': 'gamblers_chest',
        'flavor_text': 'You have an obsessive fear of imperfection.',
        'survivor_effect': (
            'When there are no <b>Perfect hits</b> in your attack, suffer 1 '
            'brain damage.'
        ),
    },
    'ergophobia': {
        'name': 'Ergophobia',
        'min_version': 'gamblers_chest',
        'flavor_text': (
            'You cannot bear the thought of working. You hide away whenever '
            'you might be needed.'
        ),
        'survivor_effect': (
            'When you are a <b>returning survivor</b>, you do not generate '
            '<font class="kdm_manager_font">E</font>.<br/>'
            'You cannot endeavor.'
        ),
    },
    'photophilia': {
        'name': 'Photophilia',
        'min_version': 'gamblers_chest',
        'flavor_text': 'You cling to light.',
        'survivor_effect': (
            'You cannot <b>depart</b> without a lantern in your gear grid.'
        ),
    },
    'somniphobia': {
        'name': 'Somniphobia',
        'min_version': 'gamblers_chest',
        'flavor_text': (
            'You fear what might happen when you fall asleep away from home.'
        ),
        'survivor_effect': (
            'On <b>Arrival</b>, lose half your survival, rounded down.'
        ),
    },

    #
    #   crimson crocodile
    #

    'bloodlust': {
        'expansion': 'crimson_crocodile',
        'name': 'Bloodlust',
        'flavor_text': 'A single glimpse of red and that is all you can see.',
        'survivor_effect': (
            'Whenever a survivor gains a bleeding token, suffer the '
            '<b>frenzy</b> brain trauma. Limit once per round.'
        ),
    },
    'phobophobia': {
        'expansion': 'crimson_crocodile',
        'name': 'Phobophobia',
        'flavor_text': 'You fear fear.',
        'survivor_effect': (
            'At the start of your act, if you have 0 insanity, gain the '
            '<b>Terrified</b> survivor status card.'
        ),
    },

    #
    #   smog singers
    #

    'pacifist': {
        'expansion': 'smog_singers',
        'name': 'Pacifist',
        'flavor_text': 'You refuse to fight.',
        'survivor_effect': (
            'You cannot activate a weapon to attack. Ignore this if you are '
            '<b>frenzied</b>.'
        ),
    },
    'brain_smog': {
        'expansion': 'smog_singers',
        'name': 'Brain Smog',
        'flavor_text': "You just cannot focus.",
        'survivor_effect': 'You cannot <b>surge</b> or <b>concentrate</b>.',
    },
}
