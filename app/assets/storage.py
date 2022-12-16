'''

    There are two dictionaries defined here: 'gear' and 'resources'.

    These are used to define Settlement Storage options and are used to create
    the Settlement Storage JSON.

    Keys in these dictionaries should also correspond to an item in
    locations.py.

'''

gear = {

    # core
    'barber_surgeon': {
        'bgcolor': 'E55451', 'color': 'FFF', 'name': 'Barber Surgeon'
    },
    'blacksmith': {'bgcolor': '625D5D', 'color': 'FFF','name': 'Blacksmith'},
    'bone_smith': {'bgcolor': 'e3dac9', 'name': 'Bone Smith'},
    'catarium': {'bgcolor': 'BA8B02', 'name': 'Catarium'},
    'exhausted_lantern_hoard': {
        'bgcolor': 'ddd','name': 'Exhausted Lantern Hoard'
    },
    'leather_worker': {
        'bgcolor': '7F462C', 'color': 'FFF','name': 'Leather Worker'
    },
    'mask_maker': {'bgcolor': 'FFD700','name': 'Mask Maker'},
    'organ_grinder': {'bgcolor': 'B58AA5','name': 'Organ Grinder'},
    'plumery': {'bgcolor': 'FF5EAA', 'name': 'Plumery'},
    'other': {'bgcolor': 'FF00FF', 'color': 'FFF','name': 'Other'},
    'rare_gear': {'bgcolor': '9DC209', 'name': 'Rare Gear'},
    'skinnery': {'bgcolor': 'FFCBA4', 'name': 'Skinnery'},
    'starting_gear': {'bgcolor': 'CCC', 'name': 'Starting Gear'},
    'stone_circle': {
        'bgcolor': '835C3B', 'color': 'FFF', 'name': 'Stone Circle'
    },
    'weapon_crafter': {'bgcolor': 'E1D4C0','name': 'Weapon Crafter'},

    # expansions
    'black_harvest': {
        'expansion': 'dung_beetle_knight', 'name': 'Black Harvest'
    },
    'dragon_armory': {'name': 'Dragon Armory', 'expansion': 'dragon_king'},
    'gormchymist': {'expansion': 'gorm', 'name': 'Gormchymist'},
    'gormery': {'expansion': 'gorm', 'name': 'Gormery'},
    'green_knight_armor': {
        'name': 'Green Knight Armor',
        'expansion': 'green_knight_armor'
    },
    'ivory_carver': {'name': 'Ivory Carver', 'expansion': 'promo'},
    'light_forging': {'name': 'Light-Forging', 'expansion': 'slenderman'},
    'manhunter_gear': {'name': 'Manhunter Gear', 'expansion': 'manhunter'},
    'promo': {'name': 'Promo', 'expansion': 'promo'},
    'sacred_pool': {'expansion': 'sunstalker','name': 'Sacred Pool'},
    'sense_memory': {'expansion': 'flower_knight', 'name': 'Sense Memory'},
    'silk_mill': {'expansion': 'spidicules', 'name': 'Silk Mill', },
    'skyreef_sanctuary': {
        'expansion': 'sunstalker', 'name': 'Skyreef Sanctuary'
    },
    'the_sun': {'expansion': 'sunstalker', 'name': 'The Sun'},
    'wet_resin_crafter': {
        'expansion': 'dung_beetle_knight',
        'name': 'Wet Resin Crafter',
    },

    # multi-expansion/shared
    'beta_gear': {'name': 'Beta Gear', 'bgcolor': '6DB2F5', 'color': 'FFF'},
    'beta_gear_recipe': {
        'name': 'Beta Gear Recipe',
        'bgcolor': '6DB2F5',
        'color': 'FFF'
    },
    'gear_recipe': {'name': 'Gear Recipe'},
    'pattern': {'name': 'Pattern'},
    'seed_pattern': {'name': 'Seed Pattern Gear'},

}

resources = {
    # gear
    'basic_resources': {'bgcolor': 'B1FB17', 'name': 'Basic Resources'},
    'phoenix_resources': {'bgcolor': 'DCD900', 'name': 'Phoenix Resources'},
    'screaming_antelope_resources': {
        'name': 'Screaming Antelope Resources',
        'bgcolor': 'DCD900',
    },
    'strange_resources': {'bgcolor': '9DC209', 'name': 'Strange Resources'},
    'vermin': {'bgcolor': '99CC66', 'name': 'Vermin'},
    'white_lion_resources': {
        'name': 'White Lion Resources',
        'bgcolor': 'DCD900',
    },

    # expansions
    'dragon_king_resources': {
        'expansion': 'dragon_king',
        'name': 'Dragon King Resources',
        'bgcolor': 'DCD900',
        'excluded_campaigns': ['people_of_the_stars']
    },
    'dung_beetle_knight_resources': {
        'name': 'Dung Beetle Knight Resources',
        'bgcolor': 'DCD900',
        'expansion': 'dung_beetle_knight',
    },
    'flower_knight_resources': {
        'bgcolor': 'DCD900',
        'expansion': 'flower_knight',
        'name': 'Flower Knight Resources'
    },
    'gorm_resources': {
        'bgcolor': 'DCD900',
        'expansion': 'gorm',
        'name': 'Gorm Resources'
    },
    'spidicules_resources': {
        'bgcolor': 'DCD900',
        'name': 'Spidicules Resources',
        'expansion': 'spidicules'
    },
    'sunstalker_resources': {
        'bgcolor': 'DCD900',
        'expansion': 'sunstalker',
        'name': 'Sunstalker Resources'
    },
}
