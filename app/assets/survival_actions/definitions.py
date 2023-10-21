"""

       Define all survival actions here, regardless of campaign or
       expansion.

       Remember: survival actions are defined by the campaign, but whether
       they're avalable is determined by settlement innovations as well as
       survivor impairments, so there is no need to define expansion
       or other SA attributes here.

"""

survival_action = {
    "dodge": {
        "name": "Dodge",
        "available": True,
        "sort_order": 0,
        "title_tip": "'Dodge' is available by default.",
    },
    "encourage": {
        "name": "Encourage",
        "sort_order": 1,
    },
    "surge":{
        "name": "Surge",
        "sort_order": 3,
    },
    "dash": {
        "name": "Dash",
        "sort_order": 4,
    },
    "overcharge": {
        "name": "Overcharge",
        "sort_order": 5,
    },
    "embolden": {               # resolve on the 1.3 sheet
        "name": "Embolden",
        "sort_order": 2,
    },
    "endure": {
        "name": "Endure",
        "sort_order": 6,
    },
}
