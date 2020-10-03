"""

    This is kind of a dumping ground for miscellaneous survivor-related meta
    and webapp assets.

    This module exists so that a.) it is easier to zero in on specific assets
    from the file systems and b.) so that we can do imports in other files more
    legibly, e.g.

        from app.assets.survivors import color_schemes

    That said, please DO NOT add any methods here. Those should still go in
    /app/models/survivors.py under the class object.


"""

defaults = {
    "Movement": 5,
    "max_bleeding_tokens": 5,
}


#
#   these are the 'macro' options used when creating new settlements. See the
#   new_settlement_special() method of the settlements.Settlement model/class
#

specials = {
    "create_first_story_survivors": {
        "name": "First Story",
        "title": 'Four "First Story" Survivors',
        "desc": 'Two male and two female survivors are randomly generated and automatically added to the <i>Departing Survivors</i> group. Starting gear is added to Settlement Storage.',
        "current_quarry": "White Lion (First Story)",
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
            {"ly": 0, "sub_type": "showdown_event", "name": "White Lion (First Story)"},
        ],
    },

    "create_seven_swordsmen": {
        "name": "Seven Swordsmen",
        "title": "Seven Swordsmen",
        "desc": 'Seven survivors with the "Ageless" ability and Sword mastery are randomly generated.',
        "random_survivors": [
            {"sex": "R", 'abilities_and_impairments': ['ageless','mastery_sword']},
            {"sex": "R", 'abilities_and_impairments': ['ageless','mastery_sword']},
            {"sex": "R", 'abilities_and_impairments': ['ageless','mastery_sword']},
            {"sex": "R", 'abilities_and_impairments': ['ageless','mastery_sword']},
            {"sex": "R", 'abilities_and_impairments': ['ageless','mastery_sword']},
            {"sex": "R", 'abilities_and_impairments': ['ageless','mastery_sword']},
            {"sex": "R", 'abilities_and_impairments': ['ageless','mastery_sword']},
        ],
    },

}



#
#   the survivors in the BCS PDF
#

beta_challenge_scenarios = {
    "adam": {
        "name": "Adam",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {
            "name": "Adam",
            "sex": "M",
            "survival": 4,
            "Insanity": 4,
            "Courage": 6,
            "Understanding": 3,
            "Weapon Proficiency": 3,
            "Strength": 1,
            "weapon_proficiency_type": "sword",
            "fighting_arts": ["timeless_eye"],
            "abilities_and_impairments": ["partner", "sword_specialization"],
        },
#        "storage": [
#            "Leather Mask",
#            "Leather Cuirass",
#            "Leather Bracers",
#            "Leather Skirt",
#            "Leather Boots",
#            "Scrap Sword",
#        ],
    },
    "anna": {
        "name": "Anna",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {
            "name": "Anna",
            "sex": "F",
            "survival": 4,
            "Insanity": 4,
            "Courage": 3,
            "Understanding": 6,
            "Weapon Proficiency": 3,
            "Evasion": 1,
            "weapon_proficiency_type": "spear",
            "fighting_arts": ["leader"],
            "abilities_and_impairments": ["partner", "spear_specialization"],
        },
#        "storage": [
#            "Leather Mask",
#            "Leather Cuirass",
#            "Leather Bracers",
#            "Leather Skirt",
#            "Leather Boots",
#            "King Spear",
#        ],
    },
    "paul_the_survivor": {
        "name": "Paul the Survivor",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {
            "name": "Paul",
            "sex": "M",
            "survival": 5,
            "Insanity": 9,
            "Courage": 3,
            "Understanding": 3,
            "fighting_arts": ["thrill_seeker","clutch_fighter","extra_sense"],
            "disorders": ["rageholic","sworn_enemy"],
        },
        "storage": [
#            "Rawhide Pants",
#            "Rawhide Gloves",
#            "Rawhide Vest",
#            "Rawhide Boots",
#            "Bone Dagger",
#            "Scrap Sword",
#            "Piranha Helm",
#            "Petal Lantern",
        ],
    },
    "candy_and_cola":{
        "name": "Candy & Cola",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {"name": "Candy & Cola", "Movement": 6, "disorders": ["hyperactive"], "sex": "F"},
    },
    "kara_black": {
        "name": "Kara Black",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {"name": "Kara Black", "survival": 3, "Strength": 1, "fighting_arts": ["leader","tough"], "sex": "F"},
#        "storage": ["Founding Stone", "Cloth", "Giant Stone Face"],
    },
    "messenger_of_the_first_story": {
        "name": "Messenger of the First Story",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {
            "name": "Messenger of the First Story",
            "sex": "F",
            "survival": 6,
            "Insanity": 6,
            "Courage": 6,
            "Strength": 1,
            "Evasion": 1,
            "Speed": 1,
            "fighting_arts": ["last_man_standing"],
        },
#        "storage": [
#            "Screaming Horns",
#            "Screaming Coat",
#            "Screaming Skirt",
#            "Screaming Bracers",
#            "Screaming Leg Warmers",
#            "Monster Grease",
#            "Cat Eye Circlet",
#            "Dried Acanthus",
#            "Arm of the First Tree",
#        ],
    },
    "messenger_of_courage":{
        "name": "Messenger of Courage",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {
            "name": "Messenger of Courage",
            "sex": "F",
            "survival": 6,
            "Insanity": 9,
            "Courage":  9,
            "Understanding": 5,
            "Strength": 1,
            "Evasion": 2,
            "Speed": 2,
            "hunt_xp": 2,
            "Weapon Proficiency": 5,
            "weapon_proficiency_type": "twilight_sword",
            "fighting_arts": ["last_man_standing"],
            "cursed_items": ["twilight_sword"],
            "abilities_and_impairments": ["twilight_sword_specialization"],
            "epithets": ["twilight_sword"],
        },
#        "storage": [
#            "Scout's Tunic",
#            "Fairy Bottle",
#            "Leather Skirt",
#            "Leather Boots",
#            "Leather Bracers",
#            "Feather Mantle",
#            "Twilight Sword"
#        ],
    },
    "messenger_of_humanity":{
        "name":  "Messenger of Humanity",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {
            "name":  "Messenger of Humanity",
            "sex": "M",
            "survival": 10,
            "abilities_and_impairments": ["bitter_frenzy", "solid", "grand_weapon_specialization"],
            "fighting_arts": ["berserker", "crossarm_block", "unconscious_fighter"],
            "disorders": ["rageholic"],
        },
#        "storage": [
#            "Lantern Helm",
#            "Lantern Cuirass",
#            "Lantern Greaves",
#            "Lantern Mail",
#            "Lantern Gauntlets",
#            "Beacon Shield",
#            "Dragon Slayer"
#            "Stone Arm"
#        ],
    },
    "snow_the_savior":{
        "name": "Snow the Savior",
        'expansion': 'beta_challenge_scenarios',
        "attribs": {
            "name": "Snow",
            "sex": "F",
            "survival": 6,
            "Insanity": 8,
            "Courage": 5,
            "Understanding": 5,
            "fighting_arts": ["unconscious_fighter"],
            "abilities_and_impairments": ["red_glow", "blue_glow", "green_glow"]
        },
    },

}