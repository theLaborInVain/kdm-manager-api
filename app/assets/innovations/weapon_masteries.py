'''

    This module does not have a Collection() or Asset() method.

    Instead, it is just the definitions for weapon masteries, which are
    (according to the Core rules p.84) an innovation as well as an A&I
    (according to the website).

'''

mastery = {
    "mastery_club": {
        "name": "Mastery - Club",
        "desc": (
            "When a Club Master attacks with a club, if a successful wound "
            "attempt total is greater than or equal to twice the monster's "
            "toughness, inflict an additional wound."
        ),
        "weapon_proficiency": "club",
        "weapon_name": "club",
        "current_survivor": {
            "abilities_and_impairments": ["club_specialization"]
        },
        "new_survivor": {
            "abilities_and_impairments": ["club_specialization"]
        },
        'epithet': 'club_master',
    },
    "mastery_scythe": {
        "name": "Mastery - Scythe",
        "desc": (
            "When you critically wound with a scythe, roll 1d10. On a 6+, "
            "shuffle the hit location deck (do not shuffle unresolved hit "
            "locations).<br/>Limit, once per round."
        ),
        "expansion": "dragon_king",
        "weapon_proficiency": "scythe",
        "weapon_name": "scythe",
        "current_survivor": {"abilities_and_impairments": ["scythe_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["scythe_specialization"]},
        'epithet': 'scythe_master',
    },
    "mastery_katana": {
        "name": "Mastery - Katana",
        "desc": "When a survivor reaches Katana Mastery, they leave the settlement forever, heeding the call of the storm to hone their art.<br/>Before the master leaves, you may nominate a survivor. Set that survivor's weapon type to Katana and their weapon proficiency level to 1.",
        "expansion": "sunstalker",
        "add_to_innovations": False,
        "weapon_proficiency": "katana",
        "weapon_name": "katana",
        'epithet': 'katana_master',
    },
    "mastery_katar": {
        "name": "Mastery - Katar",
        "desc": "If you are a Katar Master, gain a <i>+1 evasion</i> token on a <b>perfect hit</b> with a katar. When you are knocked down, remove all +1 evasion tokens.",
        "weapon_proficiency": "katar",
        "weapon_name": "katar",
        "current_survivor": {"abilities_and_impairments": ["katar_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["katar_specialization"]},
        'epithet': 'katar_master',
    },
    "mastery_bow": {
        "name": "Mastery - Bow",
        "desc": "If you are a Bow Master, all bows in your gear grid gain <b>Deadly 2</b>. In addition, ignore <b>cumbersome</b> on all Bows.",
        "weapon_proficiency": "bow",
        "weapon_name": "bow",
        "current_survivor": {"abilities_and_impairments": ["bow_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["bow_specialization"]},
        'epithet': 'bow_master',
    },
    "mastery_twilight_sword": {
        "name": "Mastery - Twilight Sword",
        "desc": "Any Survivor who attains Twilight Sword Mastery leaves the settlement forever in pursuit of a higher purpose. Remove them from the settlement's population. You may place the master's Twilight Sword in another survivor's gear grid or archive it.",
        "excluded_campaigns": ["people_of_the_stars","people_of_the_sun"],
        "weapon_proficiency": "twilight_sword",
        "weapon_name": "Twilight Sword",
        "current_survivor": {"abilities_and_impairments": ["twilight_sword_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["twilight_sword_specialization"]},
        'epithet': 'twilight_sword_master',
    },
    "mastery_axe": {
        "name": "Mastery - Axe",
        "desc": "When an Axe Master wounds a monster with an axe at a location with a persistent injury, that wound becomes a critical wound.",
        "weapon_proficiency": "axe",
        "weapon_name": "axe",
        "current_survivor": {"abilities_and_impairments": ["axe_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["axe_specialization"]},
        'epithet': 'axe_master',
    },
    "mastery_spear": {
        "name": "Mastery - Spear",
        "desc": "Whenever a Spear Master hits a monster with a Separ, they may spend 1 survival to gain the Priority Target token. If they made the hit from directly behind another survivor, that survivor gains the Priority Target token instead.",
        "weapon_proficiency": "spear",
        "weapon_name": "spear",
        "current_survivor": {"abilities_and_impairments": ["spear_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["spear_specialization"]},
        'epithet': 'spear_master',
    },
    "mastery_fist_and_tooth": {
        "name": "Mastery - Fist & Tooth",
        "desc": "While a survivor is a Fist & Tooth Master, they gain <i>+2 permanent accuracy</i> and <i>+2 permanent strength</i> (they receive this bonus even when not attacking with Fist and Tooth).",
        "weapon_proficiency": "fist_and_tooth",
        "weapon_name": "fist & tooth",
        "current_survivor": {"abilities_and_impairments": ["fist_and_tooth_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["fist_and_tooth_specialization"]},
        'epithet': 'fist_and_tooth_master',
    },
    "mastery_grand_weapon": {
        "name": "Mastery - Grand Weapon",
        "desc": "When a Grand Weapon Master perfectly hits with a grand weapon, cancel all reactions for that attack.",
        "weapon_proficiency": "grand_weapon",
        "weapon_name": "grand weapon",
        "current_survivor": {"abilities_and_impairments": ["grand_weapon_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["grand_weapon_specialization"]},
        'epithet': 'grand_weapon_master',
    },
    "mastery_whip": {
        "name": "Mastery - Whip",
        "desc": "Whip Masters gain <i>+5 strength</i> when attacking with a Whip.",
        "weapon_proficiency": "whip",
        "weapon_name": "whip",
        "current_survivor": {"abilities_and_impairments": ["whip_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["whip_specialization"]},
        'epithet': 'whip_master',
    },
    "mastery_shield": {
        "name": "Mastery - Shield",
        "desc": (
            "When a Shield Master is adjacent to a survivor that is targeted "
            "by a monster, they may swap spaces on the board with the survivor "
            "and become the target instead. The master must have a shield to "
            "perform this."
        ),
        "weapon_proficiency": "shield",
        "weapon_name": "shield",
        "current_survivor": {
            "abilities_and_impairments": ["shield_specialization"]
        },
        "new_survivor": {
            "abilities_and_impairments": ["shield_specialization"]
        },
        'epithet': 'shield_master',
    },
    "mastery_dagger": {
        "name": "Mastery - Dagger",
        "desc": "After a wounded hit location is discarded, a Dagger Master who is adjacent to the attacker and the wounded monster may spend 1 survival to re-draw the wounded hit location and attempt to wound with a dagger. Treat monster reactions on the re-drawn hit location card normally.",
        "weapon_proficiency": "dagger",
        "weapon_name": "dagger",
        "current_survivor": {"abilities_and_impairments": ["dagger_specialization"]},
        "new_survivor": {"abilities_and_impairments": ["dagger_specialization"]},
        'epithet': 'dagger_master',
    },

    # sword
    "mastery_sword": {
        "name": "Mastery - Sword",
        "desc": (
            'A Sword master gains +1 accuracy, +1 strength, and +1 speed when '
            'attacking with a Sword.'
        ),
        "weapon_proficiency": "sword",
        "weapon_name": "sword",
        "current_survivor": {
            "abilities_and_impairments": ["sword_specialization"]
        },
        "new_survivor": {
            "abilities_and_impairments": ["sword_specialization"]
        },
        'epithet': 'sword_master',
    },
    "novel_sword_mastery": {
        "name": "Novel Sword Mastery",
        "desc": (
            '<font class="kdm_font">c</font> <font class="kdm_font">a</font>: '
            'For the rest of the showdown, all your swords gain the two-handed '
            'keyword and <b>Deflect 1</b>. When attacking with them, double '
            'your strength attribute.<br/>'
            'All survivors gain novel sword specialization in addition to '
            'their other weapon proficiencies.'
        ),
        "weapon_proficiency": "sword",
        "weapon_name": "sword",
        "current_survivor": {
            "abilities_and_impairments": ["novel_sword_specialization"]
        },
        "new_survivor": {
            "abilities_and_impairments": ["novel_sword_specialization"]
        },
        'epithet': 'sword_master',
    },
}

specialization = {
    "club_specialization": {
        "name": "Specialization - Club",
        "desc": (
            "When attacking with a club, on a <b>perfect hit</b>, double your "
            "wound attempt total on the first selected hit location.<br/>"
            "Limit, once per attack."
        ),
    },
    "twilight_sword_specialization": {
        "name": "Specialization - Twilight Sword",
        "desc": "This sentient sword improves as it's used. Gain the effect as proficiency rank increases. Rank 2: Ignore <b>Cumbersome</b> on Twilight Sword. Rank 4: When attacking with the Twilight Sword, ignore <b>slow</b> and gain +2 speed. Rank 6: Twilight Sword gains <b>Deadly</b>.",
        "excluded_campaigns": ["people_of_the_stars","people_of_the_sun"],
    },
    "axe_specialization": {
        "name": "Specialization - Axe",
        "desc":  "When attacking with an axe, if your wound attempt fails, you may ignore it and attempt to wound the selected hit location again. Limit, once per attack.",
    },
    "fist_and_tooth_specialization": {
        "name": "Specialization - Fist & Tooth",
        "desc":  "You may stand (if knocked down) at the start of the monster's turn or the survivor's turn. Limit once per round.",
    },
    "grand_weapon_specialization": {
        "name": "Specialization - Grand Weapon",
        "desc": "When attacking with a grand weapon, gain <i>+1 accuracy</i>.<br/>When attacking with a Grand Weapon during your act, if you critically wound, the monster is knocked down.",
    },
    "whip_specialization": {
        "name": "Specialization - Whip",
        "desc": "When you wound with a whip, instead of moving the top card of the AI deck into the wound stack, you may move the top card of the AI discard pile. Limit once per attack.",
    },
    "shield_specialization": {
        "name": "Specialization - Shield",
        "desc": 'While a shield is in your gear grid, you are no longer knocked down after <b>collision</b> with a monster. While a shield is in your gear grid, add <font class="inline_shield">1</font> to all hit locations.',
    },

    "dagger_specialization": {
        "name": "Specialization - Dagger",
        "desc": "When attacking with a Dagger, if a wound attempt fails, after performing any reactions, you may discard another drawn hit location card to attempt to wound that hit location again. Limit, once per attack.",
    },
    "katana_specialization": {
        "name": "Specialization - Katana",
        "desc": (
            "You may not select this as your weapon type.<br/>If you are "
            "<b>blind</b> and have 4+ levels of Katana proficiency, gain the "
            "following:<br/>On your first <b>Perfect Hit</b> each attack with "
            "a Katana, do not draw a hit location. The monster suffers 1 "
            "wound."
        ),
        "expansion": "sunstalker",
     },
    "scythe_specialization": {
        "name": "Specialization - Scythe",
        "desc": (
            "When you critically wound with a scythe, roll 1d10. On a 6+, "
            "shuffle the hit location deck (do not shuffle unresolved hit "
            "locations).<br/>Limit, once per round."
        ),
        "expansion": "dragon_king",
     },
    "bow_specialization": {
        "name": "Specialization - Bow",
        "desc": (
            "When attacking with a bow, you may reroll any misses once. "
            "Limit, once per attack."
        ),
    },
    "katar_specialization": {
        "name": "Specialization - Katar",
        "desc": (
            "When attacking with a Katar, cancel reactions on the first "
            "selected hit location."
        ),
    },

    "spear_specialization": {
        "name": "Specialization - Spear",
        "desc": (
            'When attacking with a spear, if you draw a <b>trap</b>, roll '
            '1d10. On a 7+, cancel the <b>trap</b>. Discard it, then reshuffle '
            'the hit location discard into the hit location deck and draw a '
            'new card. Limit, once per round.'
        ),
    },

    # sword
    "sword_specialization": {
        "name": "Specialization - Sword",
        "desc": (
            'When attacking with a sword, after drawing hit locations, make a '
            'wound attempt and then select a hit location to resolve with that '
            'result. Limit, once per attack.'
        ),
    },
    'novel_sword_specialization': {
        'name': 'Novel Sword Specialization',
        'expansion': 'pascha',
        'desc': (
            'After resolving a monsters action, if you ignored a hit from it '
            'with <b>block</b> or <b>deflect</b>, you may activate a sword and '
            'attack.'
        ),
    },
}
