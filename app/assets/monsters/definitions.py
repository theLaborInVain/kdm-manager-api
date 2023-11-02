'''

    Monster asset definitions all live here together, regardless of whether
    they're core or expansion.

'''


quarry = {

    # quarry node 1
    "white_lion": {
        "name": "White Lion",
        "sort_order": 0,
        "node": 1,
    },
    "first_story_white_lion": {
        "name": "First Story White Lion",
        "sort_order": 0,
        "node": 1,
    },
    "gorm": {
        "name": "Gorm",
        "expansion": "gorm",
        "sort_order": 1,
        "node": 1,
    },
    'crimson_crocodile': {
        'name': 'Crimson Crocodile',
        'expansion': 'crimson_crocodile',
        'sort_order': 2,
        'node': 1,
    },
    'prologue_crimson_crocodile': {
        'name': 'Prolofue Crimson Crocodile',
        'expansion': 'crimson_crocodile',
        'sort_order': 2,
        'node': 1,
    },


    # quarry node 2
    "screaming_antelope": {
        "name": "Screaming Antelope",
        "sort_order": 5,
        "misspellings": ["XCREAMING ANTALOPE","SCREAMING ANTALOPE"],
        "node": 2,
    },
    "spidicules": {
        "name": "Spidicules",
        "expansion": "spidicules",
        "sort_order": 6,
        "node": 2,
    },
    "flower_knight": {
        "name": "Flower Knight",
        "expansion": "flower_knight",
        "sort_order": 7,
        "node": 2,
    },

    # quarry node 3
    "phoenix": {
        "name": "Phoenix",
        "sort_order": 10,
        "misspellings": ["PHONIEX"],
        "node": 3,
    },
    "dragon_king": {
        "name": "Dragon King",
        "expansion": "dragon_king",
        "sort_order": 11,
        "node": 3,
    },
    "sunstalker": {
        "name": "Sunstalker",
        "expansion": "sunstalker",
        "sort_order": 12,
        "node": 3,
    },

    # quarry node 4
    "dung_beetle_knight": {
        "name": "Dung Beetle Knight",
        "expansion": "dung_beetle_knight",
        "sort_order": 15,
        "node": 4,
    },
    "lion_god": {
        "name": "Lion God",
        "expansion": "lion_god",
        "sort_order": 16,
        "node": 4,
    },


    # no node / undefined
    "white_gigalion": {
        "name": "White Gigalion",
        'expansion': 'vignettes_of_death_white_gigalion',
        'levels': [2, 3],
        "sort_order": 20,
    },


    #
    #   unique quarries
    #

    "beast_of_sorrow": {
        "unique": True,
        "name": "Beast of Sorrow",
        "sort_order": 30,
    },
    "great_golden_cat": {
        "unique": True,
        "name": "Great Golden Cat",
        "sort_order": 31,
    },
    "mad_steed": {
        "unique": True,
        "name": "Mad Steed",
        "sort_order": 32,
    },
    "golden_eyed_king": {
        "unique": True,
        "name": "Golden Eyed King",
        "sort_order": 33,
    },
    "old_master": {
        "unique": True,
        "name": "Old Master",
        "expansion": "dung_beetle_knight",
        "sort_order": 34,
    },
}

nemesis = {

    # nemesis node 1
    "butcher": {
        "name": "Butcher",
        "sort_order": 100,
        "misspellings": ["THE BUTCHER", "BUTCHEE"],
        "node": 1,
    },
    "manhunter": {
        "name": "Manhunter",
        "sort_order": 101,
        "selectable": False,
        "levels": 4,
        "misspellings": ["THE MANHUNTER", "MAN HUNTER"],
        "node": 1,
    },



    # Nemesis node 2
    "kings_man": {
        "name": "King's Man",
        "sort_order": 105,
        "misspellings": ["KINGSMAN", "KINGMAN", "THE KING'S MAN", "THE KINGSMAN"],
        "node": 2,
    },
    "lion_knight": {
        "name": "Lion Knight",
        "selectable": False,
        "expansion": "lion_knight",
        "sort_order": 106,
        "misspellings": ["LIONKNIGHT", "THE LION KNIGHT", "THE LIONKNIGHT"],
        "node": 2,
    },
    "slenderman": {
        "name": "Slenderman",
        "sort_order": 107,
        "misspellings": ["SLENDER MAN",],
        "node": 2,
    },

    # nemesis node 3
    "the_hand": {
        "name": "The Hand",
        "sort_order": 110,
        "misspellings": ["HAND"],
        'node': 3,
    },


    # core monsters (no levels)
    "ancient_sunstalker": {
        "unique": True,
        "name": "Ancient Sunstalker",
        "expansion": "sunstalker",
        "sort_order": 200,
        "selectable": False,
        "final_boss": True,
    },
    "dragon_king_lv3": {
        "unique": True,
        "name": "The Dragon King",
        "sort_order": 201,
        "selectable": False,
        "final_boss": True,
    },
    "watcher": {
        "unique": True,
        "name": "Watcher",
        "sort_order": 202,
        "misspellings": ["THE WATCHER"],
        "selectable": True,
        "final_boss": False,
    },

    # finale 
    "gold_smoke_knight": {
        "unique": True,
        "name": "Gold Smoke Knight",
        "sort_order": 203,
        "selectable": False,
        "final_boss": True,
    },

    # Special nemesis
    "lonely_tree": {
        "name": "Lonely Tree",
        "sort_order": 150,
        "selectable": False,
    },

    # no node
    "the_tyrant": {
        "name": "The Tyrant",
        "sort_order": 151,
        "selectable": False,
        "misspellings": ["DRAGON KING HUMAN","TYRANT"],
    },
}


#
#   helpers and shorthands below
#

base_game_quarries = [
    "white_lion",
    "screaming_antelope",
    "phoenix",
    "beast_of_sorrow",
    "great_golden_cat",
    "mad_steed",
    "golden_eyed_king",
]
