'''

    Pulse Discovery asset definitions.

'''

pulse_discoveries = {
    'lr_1': {
        "level": 1,
        "bgcolor": "#E1F3FD",
        "name": "Aggression Overload",
        "subtitle": "Add an attack roll to an attack.",
        "desc": (
            "During your attack, after making your attack rolls but "
            "before drawing hit locations, you may roll the Death Die "
            "as an additional attack roll."
        ),
    },
    'lr_2': {
        "level": 2,
        "bgcolor": "#D8F2FF",
        "name": "Acceleration",
        "subtitle": "Add +1d10 movement to a move action.",
        "desc": (
            "Before moving, you may roll the Death Die and add the "
            "result to your movement for one move action this round."
        ),
    },
    'lr_3': {
        "level": 3,
        "bgcolor": "#CEEDFE",
        "name": "Uninhibited Rage",
        "subtitle": "Add +1d10 strength to a wound attempt.",
        "desc": (
            "After a wound attempt is rolled you may roll the Death "
            "Die and add the result to the strength of your wound "
            "attempt."
        ),
    },
    'lr_4': {
        "level": 4,
        "bgcolor": "#C4E8FF",
        "name": "Legs Locked",
        "desc": (
            "When you gian the Death Die, you you stand. While you "
            "have the Death Die, you cannot be knocked down for any "
            "reason."
        )
    },
    'lr_5': {
        "level": 5,
        "bgcolor": "#AFDCFD",
        "name": "Metabolic Surrender",
        "desc": (
            "Any time during the showdown, you may roll the Death Die. "
            "Gain twice that much survival. This round, ignore the "
            "negative effects of permanent injuries, impairments, "
            "disorders and negative attributes (including tokens). "
            "At the end of the round, you die."
        )
    },
}
