'''
   This package def is more complicated than others, since a lot of it drives
   the business logic of campaigns, i.e. the rules and things that affect or
   interact with lesser game assets.

'''

from app.assets import monsters as monster_assets


_default_timeline = [
    {"year": 0, },
    {"year": 1,
        "story_event":          [{"handle": "core_returning_survivors"}],
        'settlement_event':     [{'handle': 'core_first_day'}],
    },
    {"year": 2,  "story_event":         [{"handle": "core_endless_screams"}]},
    {"year": 3,  },
    {"year": 4,
        "nemesis_encounter":   [{"name": "Nemesis Encounter: Butcher"}]
    },
    {"year": 5,  "story_event":         [{"handle": "core_hands_of_heat"}]},
    {"year": 6,  "story_event":         [{"handle": "core_armored_strangers"}]},
    {"year": 7,  "story_event":         [{"handle": "core_phoenix_feather"}]},
    {"year": 8,  },
    {"year": 9,
        "nemesis_encounter":   [{"name": "Nemesis Encounter: King's Man Lvl 1"}]
    },
    {"year": 10, },
    {"year": 11, "story_event":         [{"handle": "core_regal_visit"}]},
    {"year": 12, "story_event":         [{"handle": "core_conviction"}]},
    {"year": 13,
        "nemesis_encounter":   [{'name': 'Nemesis Encounter: The Hand Lvl 1'}]
    },
    {"year": 14, }, {"year": 15, },
    {"year": 16,
        "nemesis_encounter":   [{"name": "Nemesis Encounter: Butcher Lvl 2"}]
    },
    {"year": 17, }, {"year": 18, },
    {"year": 19,
        "nemesis_encounter":   [{"name": "Nemesis Encounter: King's Man Lvl 2"}]
    },
    {"year": 20, "story_event":         [{"handle": "core_watched"}]},
    {"year": 21, }, {"year": 22, },
    {"year": 23,
        "nemesis_encounter":   [{"name": "Nemesis Encounter: Butcher Level 3"}]
    },
    {"year": 24, },
    {"year": 25,
        "nemesis_encounter":   [{"name": "Nemesis Encounter: Watcher"}]
    },
    {"year": 26  }, {"year": 27, },
    {"year": 28,
        "nemesis_encounter": [{'name': "Nemesis Encounter: - King's Man Lvl 3"}]
    },
    {"year": 29,},
    {"year": 30,
        "nemesis_encounter": [{'name': "Nemesis Encounter: Gold Smoke Knight"}]
    },
]


_default_survivor_attribute_milestones = {
    "hunt_xp": [
        {"values": [2,6,10,15], "handle": "core_age", 'event': 'story_events'},
        {'values': [16], 'handle': 'retired', 'event': 'ui_prompts'},
    ],
    "Courage": [
        {"values": [3], 'boxes': 1, "handle": "core_bold", 'event': 'story_events'},
        {"values": [9], 'boxes': 2, "handle": "core_see_the_truth", 'event': 'story_events'},
        {"values": [9], "handle": "max_courage", 'event': 'ui_prompts'},
    ],
    "Understanding": [
        {"values": [3], 'boxes': 1, "handle": "core_insight", 'event': 'story_events'},
        {"values": [9], 'boxes': 2, "handle": "core_white_secret", 'event': 'story_events'},
        {"values": [9], "handle": "max_understanding", 'event': 'ui_prompts'},
    ],
    "Weapon Proficiency": [
        {"values": [8], "handle": "max_weapon_proficiency", 'event': 'ui_prompts'},
    ],
}

_default_milestones = [
    "first_child",
    "first_death",
    "pop_15",
    "innovations_5",
    "game_over"
]

core_campaign = {
    "people_of_the_lantern": {
        "default": True,
        'saviors': True,
        "name": "People of the Lantern",
        "survival_actions": ["dodge","encourage","dash","surge",'endure'],
        "forbidden": {
            "locations": ["the_sun","throne"],
            "innovations": ["sun_language","dragon_speech","radiating_orb"],
        },
        "principles": ["new_life","death","society","conviction"],
        "milestones": _default_milestones,
        "special_showdowns": ['kings_man','the_hand'],
        "nemesis_monsters": ["butcher","kings_man","the_hand",'watcher'],
        'final_boss': 'gold_smoke_knight',
        "survivor_attribute_milestones": _default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "timeline": _default_timeline,
        "settlement_sheet_init": {
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
        },
        'help': [
            {
                'type': 'timeline',
                'tip': (
                    "As of <i>Monster</i> version 1.5, the <b>Watcher</b> is "
                    "no longer automatically included in settlement Timelines. "
                    "You must first add the <b>Watcher</b> to your "
                    "settlement's Nemesis Monsters list before you may add an "
                    "encounter with it to your Timeline."
                ),
            },
        ],
    },
    "people_of_the_skull": {
        "name": "People of the Skull",
        'saviors': True,
        "subtitle": (
            "Always displays the alternate rules and endeavors on p.213 of the "
            "core game manual on the Campaign Summary view."
        ),
        "survival_actions": ["dodge","encourage","dash","surge",'endure'],
        "always_available": {
            "location": ["Lantern Hoard"],
            "innovation": ["Language"],
        },
        "special_rules": [
            {
                "name": "People of the Skull",
                "desc": (
                    "Survivors can only place weapons and armor with the "
                    "<b>bone</b> keyword in their gear grid. The people of the "
                    "skull ignore the <b>Frail</b> rule."
                ),
                 "bg_color": "E3DAC9",
                 "font_color": "333"},
            {
                "name": "People of the Skull",
                "desc": (
                    "When you name a survivor, if they have the word bone or "
                    "skull in their name, in addition to +1 survival, players "
                    "choose to gain +1 permanent accuracy, evasion, strength, "
                    "luck or speed."
                ),
                 "bg_color": "E3DAC9",
                 "font_color": "333"},
            {
                "name": "Black Skull",
                "desc": (
                    "If a weapon or armor is made with the Black Skull "
                    "resource, a survivor may place it in their gear grid "
                    "despite being iron."
                ),
                 "bg_color": "333",
                 "font_color": "efefef"
            },
        ],
        "endeavors": ['potskull_skull_ritual'],
        "principles": ["new_life","death","society","conviction"],
        "milestones": _default_milestones,
        "nemesis_monsters": ["butcher","kings_man","the_hand","watcher"],
        "special_showdowns": ["kings_man",'the_hand'],
        'final_boss': 'gold_smoke_knight',
        "survivor_attribute_milestones": _default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "timeline": _default_timeline,
        "settlement_sheet_init": {
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
        },
    },

}

expansion_campaign = {
    "the_green_knight": {
        "name": "The Green Knight",
        'saviors': True,
        "subtitle": (
            "A campaign following the 'People of the Lantern' timeline that "
            "includes all content required by the <b>Green Knight Armor</b> "
            "expansion."
        ),
        "survival_actions": ["dodge","encourage","dash","surge",'endure'],
        "always_available": {
            "location": ["Lantern Hoard"],
            "innovation": ["Language"],
        },
        "forbidden": {
            "location": ["the_sun","throne"],
            "innovation": ["sun_language","dragon_speech","radiating_orb"],
        },
        "principles": ["new_life","death","society","conviction"],
        "milestones": _default_milestones,
        "nemesis_monsters": ["butcher","kings_man","the_hand","watcher"],
        "special_showdowns": ["kings_man",'the_hand'],
        'final_boss': 'gold_smoke_knight',
        "survivor_attribute_milestones": _default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "timeline": _default_timeline,
        "settlement_sheet_init": {
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
            "expansions": [
                "green_knight_armor",
                "dung_beetle_knight",
                "flower_knight",
                "lion_knight",
                "gorm"
            ],
        },
    },

    "the_bloom_people": {
        "name": "The Bloom People",
        'saviors': True,
        "survival_actions": ["dodge","encourage","dash","surge",'endure'],
        "forbidden": {
            "disorders": ["flower_addiction"],
            "quarries": ["flower_knight"],
            'events': ['fk_crones_tale'],
        },
        "principles": ["new_life","death","society","conviction"],
        "milestones": _default_milestones,
        "endeavors": ['bloom_people_forest_run'],
        "settlement_buff": (
            "All survivors are born with +1 permanent luck, +1 permanent green "
            "affinity and -2 permanent red affinities."
        ),
        "newborn_survivor": {
            "affinities": {"red": -2, "green": 1,},
            "Luck": 1,
        },
        "timeline": _default_timeline,
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        "special_showdowns": ["kings_man",'the_hand'],
        'final_boss': 'gold_smoke_knight',
        "survivor_attribute_milestones": _default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "settlement_sheet_init": {
            "storage": ["sleeping_virus_flower"],
            "expansions": ["flower_knight"],
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
        },
        'help': [
            {
                'type': 'rules',
                'tip': (
                    'When starting a new "The Bloom People" campaign, any '
                    'survivors who are not created with parents, including the '
                    'first generation of survivors, whether added manually or '
                    'via the "First Story" macro during settlement creation, '
                    "do not benefit from the campaign's intrinsic settlement "
                    'bonus.<br/> &nbsp; The rule states that "All survivors '
                    'are born with +1 permanent luck, +1 permanent green '
                    'affinity and -2 permanent red affinities," and founding'
                    'survivors are not born.'
                ),
            }
        ]
    },

    "people_of_the_sun": {
        "name": "People of the Sun",
        "survivor_special_attributes": [
            'potsun_purified',
            'potsun_sun_eater',
            'potsun_child_of_the_sun'
        ],
        "survival_actions": ["dodge","overcharge","embolden","dash"],
        "forbidden": {
            "locations": ["lantern_hoard","exhausted_lantern_hoard"],
            "innovations": ["leader", "language"],
            "events": ["ss_promise_under_the_sun"],
        },
        "principles": ["potsun_new_life","death","society","conviction"],
        "milestones": [
            "first_child",
            "first_death",
            "pop_15",
            "innovations_8",
            "nemesis_defeat",
            "game_over"
        ],
        "timeline": [
            {"year": 0,  },
            {"year": 1,
                "story_event":          [{"handle": "ss_pool_and_sun"}],
                'settlement_event':     [{'handle': 'core_first_day'}],
            },
            {"year": 2,  "story_event":         [{"handle": "core_endless_screams"}]},
            {"year": 3,  },
            {"year": 4,  "story_event":         [{"handle": "ss_sun_dipping"}]},
            {"year": 5,  "story_event":         [{"handle": "ss_great_sky_gift"}]},
            {"year": 6,  },
            {"year": 7,  "story_event":         [{"handle": "core_phoenix_feather"}]},
            {"year": 8,  }, {"year": 9, },
            {"year": 10, "story_event":         [{"handle": "ss_birth_of_color"}]},
            {"year": 11, "story_event":         [{"handle": "core_conviction"}]},
            {"year": 12, "story_event":         [{"handle": "ss_sun_dipping"}]},
            {"year": 13, "story_event":         [{"handle": "ss_great_sky_gift"}]},
            {"year": 14, }, {"year": 15, }, {"year": 16, }, {"year": 17, }, {"year": 18, },
            {"year": 19, "story_event":         [{"handle": "ss_sun_dipping"}]},
            {"year": 20, "story_event":         [{"handle": "ss_final_gift"}]},
            {"year": 21, "nemesis_encounter":   [{"name": "Nemesis Encounter: Kings Man Level 2"}]},
            {"year": 22, "nemesis_encounter":   [{"name": "Nemesis Encounter: Butcher Level 3"}]},
            {"year": 23, "nemesis_encounter":   [{"name": "Nemesis Encounter: Kings Man Level 3"}]},
            {"year": 24, "nemesis_encounter":   [{"name": "Nemesis Encounter: The Hand Level 3"}]},
            {"year": 25, "story_event":         [{"handle": "ss_great_devourer"}]},
        ],
        "final_boss": "ancient_sunstalker",
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        "survivor_attribute_milestones": _default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "settlement_sheet_init": {
            "expansions": ["sunstalker"],
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
        },
    },

    "people_of_the_stars": {
        "name": "People of the Stars",
        "dragon_traits": "1.3.1",
        "survival_actions": ["dodge","encourage","dash","surge"],
        'survivor_special_attributes': [
            'potstars_scar',
            'potstars_noble_surname',
            'potstars_reincarnated_surname'
        ],
        "forbidden": {
            "locations": [
                "lantern_hoard",
                "dragon_armory",
                "exhausted_lantern_hoard"
            ],
            "innovations": ["language","lantern_oven","clan_of_death","family"],
            'events': ['dk_glowing_crater'],
        },
        "founder_epithet": "foundling",
        "replaced_story_events": {
            "Bold": "Awake",
            "Insight": "Awake",
        },
        'courage_ai_radio_raft': False,
        'understanding_ai_radio_raft': False,
        "special_rules": [
            {
                "name": "Removed Story Events",
                "desc": (
                    "If an event or card would cause you to add/trigger "
                    "<b>Hands of Heat</b>, <b>Regal Visit</b>, <b>Armored "
                    "Strangers</b>, <b>Watched</b>, or <b>Nemesis Encounter - "
                    "Watcher</b>, do nothing instead."
                ),
                "bg_color": "673AB7",
                "font_color": "FFF"
            },
        ],
        "principles": ["new_life","death","society","conviction"],
        "milestones": ["first_child","first_death","pop_15","game_over"],
        "timeline": [
            {"year": 0,  },
            {"year": 1,
                "story_event":          [{"handle": "dk_foundlings"}],
                'settlement_event':     [{'handle': 'core_first_day'}],
            },
            {"year": 2,  "story_event":         [{"handle": "core_endless_screams"}]        },
            {"year": 3,  },
            {"year": 4,  "nemesis_encounter":   [{"name": "Nemesis Encounter - Dragon King Human Lvl 1"}]   },
            {"year": 5,  "story_event":         [{"handle": "dk_midnights_children"}]     },
            {"year": 6,  },
            {"year": 7,  "story_event":         [{"handle": "core_phoenix_feather"}]        },
            {"year": 8,  },
            {"year": 9,  "nemesis_encounter":   [{"name": "Nemesis Encounter - Dragon King Human Lvl 2"}]   },
            {"year": 10, "story_event":         [{"handle": "dk_unveil_the_sky"}]           },
            {"year": 11, },
            {"year": 12, "story_event":         [{"handle": "core_conviction"}]             },
            {"year": 13, "nemesis_encounter":   [{"name": "Nemesis Encounter - Butcher Lvl 2"}] },
            {"year": 14, }, {"year": 15, },
            {"year": 16, "nemesis_encounter":   [{"name": "Nemesis Encounter - Lvl 2"}]     },
            {"year": 17, }, {"year": 18, },
            {"year": 19, "nemesis_encounter":   [{"name": "Nemesis Encounter - Dragon King Human Lvl 3"}]   },
            {"year": 20, "story_event":         [{"handle": "dk_tomb"}]                     },
            {"year": 21, }, {"year": 22, },
            {"year": 23, "nemesis_encounter":   [{"name": "Nemesis Encounter - Lvl 3"}]     },
            {"year": 24, },
            {"year": 25, "nemesis_encounter":   [{"handle": "dk_death_of_the_dragon_king"}] },
        ],
        "survivor_attribute_milestones": {
            "hunt_xp": [
                {"values": [2,6,10,15], "handle": "core_age", 'event': 'story_events'},
                {'values': [16], 'handle': 'retired', 'event': 'ui_prompts'},
            ],
            "Courage": [
                {"values": [3], 'boxes': 1, "handle": "dk_awake", 'event': 'story_events'},
                {"values": [9], 'boxes': 2, "handle": "core_see_the_truth", 'event': 'story_events'},
                {"values": [9], "handle": "max_courage", 'event': 'ui_prompts'},
            ],
            "Understanding": [
                {"values": [3], 'boxes': 1, "handle": "dk_awake", 'event': 'story_events'},
                {"values": [9], 'boxes': 2, "handle": "core_white_secret", 'event': 'story_events'},
                {"values": [9], "handle": "max_understanding", 'event': 'ui_prompts'},
            ],
            "Weapon Proficiency": [
                {"values": [8], "handle": "max_weapon_proficiency", 'event': 'ui_prompts'},
            ],
        },
        "quarries": monster_assets.base_game_quarries,
        "special_showdowns": ["the_tyrant"],
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        'final_boss': 'dragon_king_lv3',
        "settlement_sheet_init": {
            "expansions": ["dragon_king"],
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher","kings_man","the_hand"],
            "nemesis_encounters": {
                "butcher":[1], "kings_man":[1], "the_hand":[1]
            },
        },
    },

    # people of the dream keeper
    # arc people of the sun
    # arc people of the stars

}
