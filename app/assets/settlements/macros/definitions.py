"""

    Macros are dictionaries that can be used to operate on settlements.

    Most of them add a group of survivors to a settlement, e.g. the four random
    starting survivors of the 'First Story' event or the four Vignette Survivors
    of the Vignettes of Death expansion, etc.

    This module is an extension of what we used to call 'specials' in the
    survivors pseudo asset.

"""

add_survivors = {

    "create_first_story_survivors": {
        "name": "First Story",
        'new_settlement': True,
        "desc": (
            'Sets the quarry to be a White Lion, creates four new survivors '
            'and adds them to the <i>Departing Survivors</i> group.'
        ),
        "summary": [
            'Two male and two female survivors are randomly generated.',
            'Survivor <i>Waist</i> hit locations are set to 1.',
            (
                'Starting gear is added to settlement storage: 4x Cloth and '
                '4x Founding Stone.'
            ),
            'Survivors are added to the Departing Survivors group.',
            'Quarry is set to <i>White Lion (First Story)</i>.',
            'Timeline is updated.',
        ],
        "current_quarry": "White Lion (First Story)",
        'monsters': ['white_lion'],
        'showdown_type': 'normal',
        "random_survivors": [
            {"sex": "M", "Waist": 1, "departing": True},
            {"sex": "M", "Waist": 1, "departing": True},
            {"sex": "F", "Waist": 1, "departing": True},
            {"sex": "F", "Waist": 1, "departing": True},
        ],
        "storage": [
            {"name": "founding_stone", "quantity": 4},
            {"name": "cloth", "quantity": 4},
        ],
        "timeline_events": [
            {
                "ly": 0,
                "sub_type": "showdown_event",
                "name": "White Lion (First Story)"
            },
        ],
        'warning': (
            'This macro was intended to be applied to new settlements at '
            'creation time! Apply this macro to existing settlements at '
            'your own risk...'
        ),
    },

    "create_devour_the_white_lion_survivors": {
        "name": "Devour the White Lion",
        'new_settlement': True,
        "desc": (
            'Adds the <b>Crimson Crocodile</b> expansion, '
            'sets the quarry to be the <i>Prologue Crimson Crocodile</i>, '
            'creates four new survivors and adds them to the '
            '<i>Departing Survivors</i> group.'
        ),
        'expansions': ['crimson_crocodile'],
        "summary": [
            'Two male and two female survivors are randomly generated.',
            'Survivor <i>Waist</i> hit locations are set to 1.',
            (
                'Starting gear is added to settlement storage: 4x Cloth and '
                '4x Founding Stone.'
            ),
            'Survivors are added to the Departing Survivors group.',
            'Quarry is set to <i>Prologue Crimson Crocodile</i>.',
            'Timeline is updated.',
        ],
        "current_quarry": "Prologue Crimson Crocodile",
        'monsters': ['crimson_crocodile'],
        'showdown_type': 'normal',
        "random_survivors": [
            {"sex": "M", "Waist": 1, "departing": True},
            {"sex": "M", "Waist": 1, "departing": True},
            {"sex": "F", "Waist": 1, "departing": True},
            {"sex": "F", "Waist": 1, "departing": True},
        ],
        "storage": [
            {"name": "founding_stone", "quantity": 4},
            {"name": "cloth", "quantity": 4},
        ],
        "timeline_events": [
            {
                "ly": 0,
                "sub_type": "showdown_event",
                "name": "Prologue Crimson Crocodile"
            },
        ],
        'warning': (
            'This macro was intended to be applied to new settlements at '
            'creation time! Apply this macro to existing settlements at '
            'your own risk...'
        ),
    },

    "create_seven_swordsmen": {
        'new_settlement': True,
        "name": "Seven Swordsmen",
        "desc": (
            'Seven survivors with the "Ageless" ability and Sword mastery are '
            'randomly generated.'
        ),
        "summary": [
            'Seven survivors are randomly generated (sex is randomized).',
            (
                "Each survivor's <i>Abilities and Impairments</i> are updated "
                "to include <i>Ageless</i> and <i>Mastery - Sword</i>."
            ),
        ],
        "random_survivors": [
            {
                "sex": "R",
                'abilities_and_impairments': ['ageless','mastery_sword'],
            },
            {
                "sex": "R",
                'abilities_and_impairments': ['ageless','mastery_sword'],
            },
            {
                "sex": "R",
                'abilities_and_impairments': ['ageless','mastery_sword'],
            },
            {
                "sex": "R",
                'abilities_and_impairments': ['ageless','mastery_sword'],
            },
            {
                "sex": "R",
                'abilities_and_impairments': ['ageless','mastery_sword'],
            },
            {
                "sex": "R",
                'abilities_and_impairments': ['ageless','mastery_sword'],
            },
            {
                "sex": "R",
                'abilities_and_impairments': ['ageless','mastery_sword'],
            },
        ],
    },
}

update_survivors = {
    'reduce_all_survivors_survival_to_0': {
        "name": "Reduce all Survivors' Survival to 0",
        "desc": 'Reduces the Survival of all living survivors to zero.',
        "summary": [
            'Survival is set to zero for all living survivors.',
            "Dead survivors' sheets are not modified.",
            'The event is logged in the settlement event log.'
        ],
        'living_survivors': {
            'set': {
                'survival': 0,
            },
        },
    },
    'increment_all_survivors_survival_by_1': {
        "name": "Increase all Survivors' Survival by 1",
        "desc": 'Increases the Survival of all living survivors by one.',
        "summary": [
            'Survival is increased by one for all living survivors.',
            'Settlement limits are respected.',
            "Dead survivors' sheets are not modified.",
            'The event is logged in the settlement event log.'
        ],
        'living_survivors': {
            'increment': {
                'survival': 1,
            },
        },
    },
}

