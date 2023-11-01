'''

    Gambler's Chest disorders are managed here.

'''

gamblers_chest_disorders = {

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

}
