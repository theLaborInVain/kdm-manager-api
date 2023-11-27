"""

   For purposes of API organization, there are three types of locations in
   Kingdom Death: Monster.

   The first type of location is settlement locations. These are added to the
   settlement locations and function like a normal settlement game asset. The
   'Lantern Hoard' is one of these, as is the Dragon King's 'Throne'.

   The second type of location is a gear location. These are 'pseudo' locations
   that do not get added to options (decks) or to the Settlement Sheet, but
   certain types of gear comes from them. Examples include "Rare Gear" and
   items created in the "Sense Memory" story event.

   The third type of location is resources. Resource type gear comes from these
   bogus 'locations'. The 'Strange Resources' and 'Vermin' type of items belong
   to these locations.

"""


resources = {
    "basic_resources": {
        "name": "Basic Resources",
        "color": "B1FB17",
        "selectable": False,
    },
    "vermin_resources": {
        "name": "Vermin",
        "color": "99CC66",
        "selectable": False,
    },
    "strange_resources": {
        "name": "Strange Resources",
        "color": "9DC209",
        "selectable": False,
    },
    "white_lion_resources": {
        "name": "White Lion Resources",
        "color": "DCD900",
        "selectable": False,
    },
    "screaming_antelope_resources": {
        "name": "Screaming Antelope Resources",
        "color": "DCD900",
        "selectable": False,
    },
    "phoenix_resources": {
        "name": "Phoenix Resources",
        "color": "DCD900",
        "selectable": False,
    },
    "spidicules_resources": {
        "name": "Spidicules Resources",
        "expansion": "spidicules",
        "color": "DCD900",
        "selectable": False,
    },
    "gorm_resources":{
        "name": "Gorm Resources",
        "expansion": "gorm",
        "color": "DCD900",
        "selectable": False,
    },
    "flower_knight_resources":{
        "name": "Flower Knight Resources",
        "expansion": "flower_knight",
        "color": "DCD900",
        "selectable": False,
    },
    "dung_beetle_knight_resources": {
        "name": "Dung Beetle Knight Resources",
        "expansion": "dung_beetle_knight",
        "color": "DCD900",
        "selectable": False,
    },
    "dragon_king_resources":{
        "name": "Dragon King Resources",
        "expansion": "dragon_king",
        "color": "DCD900",
        "selectable": False,
    },
    "sunstalker_resources":{
        "name": "Sunstalker Resources",
        "expansion": "sunstalker",
        "color": "666",
        "selectable": False,
    },

    # gambler's chest
    "crimson_crocodile_resources":{
        "name": "Crimson Crocodile Resources",
        "expansion": "crimson_crocodile",
        "selectable": False,
    },
    "smog_singers_resources":{
        "name": "Smog Singers Resources",
        "expansion": "smog_singers",
        "selectable": False,
    },
}


gear = {
    "beta_gear": {
        "name": "Beta Gear",
        "color": "6DB2F5",
        "font_color": "FFF",
        "selectable": False,
    },
    "beta_gear_recipe": {
        "name": "Beta Gear Recipe",
        "color": "6DB2F5",
        "font_color": "FFF",
        "selectable": False,
    },
    "black_harvest": {
        "name": "Black Harvest",
        "expansion": "dung_beetle_knight",
        "color": "333",
        "font_color": "FFF",
        "selectable": False,
    },
    "gear_recipe": {
        "name": "Gear Recipe",
        "color": "333",
        "font_color": "FFF",
        "selectable": False,
    },
    "light_forging_gear": {
        "name": "Light-Forging",
        "expansion": "slenderman",
        "color": "570A75",
        "font-color": "fff",
        "selectable": False,
    },
    "green_knight_armor_gear": {
        "name": "Green Knight Armor",
        "expansion": "green_knight_armor",
        "color": "42AB59",
        "font_color": "fff",
        "selectable": False,
    },
    "manhunter_gear": {
        "name": "Manhunter Gear",
        "expansion": "manhunter",
        "color": "000",
        "font_color": "F50057",
        "selectable": False,
    },
    "sense_memory_gear": {
        "name": "Sense Memory",
        "expansion": "flower_knight",
        "color": "145314",
        "font_color": "FFF",
        "selectable": False,
    },
    "rare_gear": {
        "name": "Rare Gear",
        "color": "9DC209",
        "selectable": False,
    },
    "promo": {
        "name": "Promo",
        "color": "3BB9FF",
        "selectable": False,
    },
    "ivory_carver": {
        "name": "Ivory Carver",
        "color": "FFFFF0",
        "selectable": False,
    },
    "other": {
        "name": "Other",
        "font_color": "FFF",
        "color": "FF00FF",
        "selectable": False,
    },
    "pattern": {
        "name": "Pattern",
        "font_color": "FFF",
        "color": "9E999C",
        "selectable": False,
    },
    "seed_pattern": {
        "name": "Seed Pattern Gear",
        "font_color": "F1E4D3",
        "color": "E67022",
        "selectable": False,
    },
    "starting_gear": {
        "name": "Starting Gear",
        "color": "CCC",
        "selectable": False,
    },

}

location = {

    #
    #   Core locations! Keep these on top
    #

    "lantern_hoard": {
        "type": "gear",
        'has_no_gear': True,
        "name": "Lantern Hoard",
        "consequences": [
            "bone_smith",
            "skinnery",
            "organ_grinder",
            "catarium",
            "plumery",
            "exhausted_lantern_hoard",
            "mask_maker"
        ],
        "endeavors": [
            'innovate',
            'build_bonesmith',
            'build_skinnery',
            'build_organ_grinder',
            'lantern_hoard_shared_experience',
        ],
    },
    "exhausted_lantern_hoard": {
        "type": "gear",
        "name": "Exhausted Lantern Hoard",
        "color": "9F99A5",
        "special_rules": [
            {
                "name": "Dead Guardian",
                "desc": (
                    "The sleeping predator is gone. Without its protective "
                    'presence, intelligent monsters draw near. '
                    '<ul class="dead_guardian_ul"><li>You may '
                    "only hunt Lvl 3+ monsters</li><li>All departing survivors "
                    "must have 1 gear with the <i>lantern</i> keyword in their "
                    "gear grid.</li><li>If the settlement has the Final "
                    "Lantern, 1 survivor must depart with it in their gear "
                    "grid.</li></ul><br/><b>The light of inspiration is "
                    "extinguished. You cannot innovate.</b>"
                ),
                "bg_color": "9F99A5",
                "font_color": "FFF",
            },
        ],
        'endeavors': [
            'exhausted_lantern_hoard_0_lantern_research',
            'exhausted_lantern_hoard_1_oxidation',
            'exhausted_lantern_hoard_2_survivors_lantern',
            'exhausted_lantern_hoard_3_investigate',
        ],
    },

    "bone_smith": {
        "type": "gear",
        "name": "Bone Smith",
        "color": "e3dac9",
        "consequences": ["Weapon Crafter"],
        "endeavors": ['bone_smith_build_weapon_crafter'],
    },

    "weapon_crafter": {
        "type": "gear",
        "name": "Weapon Crafter",
        "color": "E1D4C0",
        "endeavors": ['weapon_crafter_innovate_scrap_smelting','weapon_crafter_scrap_scavenge'],
    },

    "skinnery": {
        "type": "gear",
        "name": "Skinnery",
        "color": "FFCBA4",
        "consequences": ["leather_worker"],
        "endeavors": ['skinnery_build_leather_worker',],
    },
    "leather_worker": {
        "type": "gear",
        "name": "Leather Worker",
        "color": "7F462C",
        "font_color": "FFF",
        "endeavors": ['leather_worker_leather_making'],
    },

    "organ_grinder": {
        "type": "gear",
        "name": "Organ Grinder",
        "color": "B58AA5",
        "consequences": ["Stone Circle"],
        "endeavors": [
            'organ_grinder_augury',
            'organ_grinder_stone_noses',
            'organ_grinder_build_stone_circle',
        ],
    },

    "stone_circle": {
        "type": "gear",
        "name": "Stone Circle",
        "color": "835C3B",
        "font_color": "FFF",
        "endeavors": ['stone_circle_harvest_ritual'],
    },

    "plumery": {
        "type": "gear",
        "name": "Plumery",
        "color": "FF5EAA",
    },

    "catarium": {
        "type": "gear",
        "name": "Catarium",
        "color": "BA8B02",
    },

    "giga_catarium": {
        "type": "gear",
        'extension': True,
        'expansion': 'vignettes_of_death_white_gigalion',
        "name": "Giga-Catarium",
        "color": "BA8B02",
    },

    "blacksmith": {
        "type": "gear",
        "name": "Blacksmith",
        "requires": ("innovations", "Scrap Smelting"),
        "color": "625D5D",
        "font_color": "FFF",
    },
    "barber_surgeon": {
        "type": "gear",
        "name": "Barber Surgeon",
        "requires": ("innovations", "Pottery"),
        "color": "E55451",
        "font_color": "FFF",
        'endeavors': ['barber_surgeon_trepanning'],
    },
    "mask_maker": {
        "type": "gear",
        "name": "Mask Maker",
        "color": "FFD700",
        'settlement_buff': (
            'A <b>departing survivor</b> with a mask in their gear grid may '
            'lead their hunting party to a legendary monster. Rules for these '
            'monsters are found on the Legendary Monster story event.'
        ),
        "endeavors": ['mask_maker_0', 'mask_maker_1', 'mask_maker_2'],
    },



    # DBK

    "wet_resin_crafter": {
        "type": "gear",
        "name": "Wet Resin Crafter",
        "expansion": "dung_beetle_knight",
        "color": "C9CE62",
    },


    #
    #   Gorm locations!
    #

    "gormchymist": {
        "type": "gear",
        "name": "Gormchymist",
        "expansion": "gorm",
        "color": "8C001A",
        "font_color": "FFF",
        "endeavors": ['gormchymist_special_innovate'],
    },
    "gormery": {
        "type": "gear",
        "name": "Gormery",
        "expansion": "gorm",
        "color": "600313",
        "font_color": "FFF",
    },


    #
    #   Sunstalker Locations
    #

    "the_sun": {
        "type": "gear",
        "name": "The Sun",
        'has_no_gear': True,
        "expansion": "sunstalker",
        "consequences": [
            "bone_smith",
            "skinnery",
            "organ_grinder",
            "catarium",
            "plumery",
            "mask_maker",
            "sacred_pool"
        ],
        "endeavors": [
            'innovate',
            'build_bonesmith',
            'build_organ_grinder',
            'build_skinnery'
        ],
        "special_rules": [
            {
                "name": "Extreme Heat",
                "desc": "Survivors cannot wear heavy gear.",
                "bg_color": "DD3300",
                "font_color": "FFF",
            },
            {
                "name": "Supernova",
                "desc": (
                    'If you suffer defeat against a nemesis monster, the sun '
                    'cleanses the settlement, instantly killing everyone. '
                    '<font class="kdm_font">g</font> <b>Game Over</b>'
                ),
                "bg_color": "990000",
                "font_color": "FFF",
            },
        ],
    },

    "sacred_pool": {
        "type": "gear",
        "name": "Sacred Pool",
        "expansion": "sunstalker",
        "levels": 3,
        "color": "eee541",
        "endeavors": ['sacred_pool_0','sacred_pool_1','sacred_pool_2'],
    },

    "skyreef_sanctuary": {
        "type": "gear",
        "name": "Skyreef Sanctuary",
        "expansion": "sunstalker",
        "color": "FFF541",
    },



    #
    #   Dragon King locations!
    #

    "dragon_armory": {
        "type": "gear",
        "name": "Dragon Armory",
        "expansion": "dragon_king",
        "color": "6A1B9A",
        "font_color": "FFF",
    },
    "throne": {
        "type": "gear",
        'has_no_gear': True,
        "name": "Throne",
        "expansion": "dragon_king",
        "consequences": [
            "Bone Smith",
            "Skinnery",
            "Organ Grinder",
            "Catarium",
            "Plumery",
            "Mask Maker"
        ],
        "endeavors": [
            'innovate',
            'build_bonesmith',
            'build_organ_grinder',
            'build_skinnery',
            'fear_and_trembling'
        ],
    },


    # Spidicules

    "silk_mill": {
        "type": "gear",
        "name": "Silk Mill",
        "expansion": "spidicules",
        "color": "C0CA33",
        "font_color": "000",
    },


    # gambler's chest
    'crimson_crockery': {
        'type': 'gear',
        'name': 'Crimson Crockery',
        'expansion': 'crimson_crocodile',
        'color': '894142',
        'font_color': 'fff',
    },
    'chorusseum': {
        'type': 'gear',
        'name': 'Chorusseum',
        'expansion': 'smog_singers',
        'color': 'A2A291',
        'font_color': 'fff',
    },
}
