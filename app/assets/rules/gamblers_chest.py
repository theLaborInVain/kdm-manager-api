'''

    Gambler's Chest, an unplayably rules- and systems-heavy expansion
    collection, rules live here.

'''


crimson_crocodile = {

    'clobber_x': {
        'expansion': 'crimson_crocodile',
        'name': 'Clobber X',
        'type': 'gear_special_rule',
        'related_rules': ['super_dense'],
        'desc': (
            'Gain +X strength while attempting to wound a <b>Super-dense</b> '
            'hit location.'
        ),
    },
    'disarm': {
        'expansion': 'crimson_crocodile',
        'name': 'Disarm',
        'type': 'special_rule',
        'desc':(
            'When a survivor suffers disarm or is disarmed, end their attack. '
            'Place a disarm tile on the attack weapon and a matching tile 5 '
            'spaces away from that survivor. That survivor may not activate '
            'that weapon until they remove the tile on it or the show down '
            'ends. When a survivor moves over their associated tile, archive '
            'it and remove the tile on your gear grid.'
        ),
    },
    'guardless': {
        'expansion': 'crimson_crocodile',
        'name': 'Guardless',
        'type': 'special_rule',
        'desc': (
            'A guardless survivor may not dodge, block, '
            'deflect, or ignore hits. Attack rolls can still miss guardless '
            'survivors, as they still factor their evasion in.'
        ),
    },
    'heroic': {
        'expansion': 'crimson_crocodile',
        'type': 'weapon_ability',
        'name': 'Heroic',
        'desc': (
            'During your attack with this weapon, reroll '
            'any natural 1s. You must keep the new results.'
        ),
    },
    'honed_x': {
        'expansion': 'crimson_crocodile',
        'name': 'Honed X',
        'type': 'gear_special_rule',
        'desc': (
            'Honed weapons gain +X strength until they strike something '
            'hard (Super-Dense or Parry hit locations), ruining their edge. '
            'Unless something explicitly preserves or restores the edge of a '
            'honed weapon, it loses its additional strength until it is '
            'restored at the settlement.'
        ),
    },
    'locked': {
        'expansion': 'crimson_crocodile',
        'name': 'Locked',
        'type': 'gear_special_rule',
        'desc': 'This cannot be disarmed.',
    },
    'foresight': {
        'expansion': 'crimson_crocodile',
        'name': 'Foresight',
        'type': 'gear_special_rule',
        'desc': (
            'Survivors have Foresight if there are '
            'any revleaed AI or HL cards.'
        )
    },
    'surpass_x': {
        'expansion': 'crimson_crocodile',
        'name': 'Surpass X',
        'type': 'gear_special_rule',
        'desc': (
            'When your successful wound attempt total '
            "surpasses the monster's toughness by X or more, the monster "
            'suffers an additional wound.'
        ),
    },
}

smog_singers = {

    'hushed': {
        'expansion': 'smog_singers',
        'name': 'Hushed',
        'type': 'special_rule',
        'desc': (
            'Hushed survivors are cloaked in silence. They ignore vibration '
            'damage, are considered deaf, and cannot encourage, roar, scream, '
            'perform audible effects, or activate noisy gear.'
        ),
    },

    'pursue': {
	'expansion': 'smog_singers',
        'name': 'Pursue',
        'type': 'special_rule',
        'desc': (
            'Gain <font class="kdm_manager_font">M</font>, which must be '
            'immediately spent to move towards the monster. If you moved and '
            'are now adjacent, draw another '
            '<span class="kd deck_icon" deck="HL">HL</span>.'
        ),
    },

}
