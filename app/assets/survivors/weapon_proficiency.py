"""

    Weapon proficiency 'asset' definitions live here.

    A weapon proficiency is added to a survivor record as the
    'weapon_proficiency_type' attribute. Using the handle stored as that attrib
    gets you back to these definitions.

"""

weapon_proficiency = {
    "axe": {
        "name":"Axe",
        "specialist_ai": "axe_specialization",
        "master_ai": "mastery_axe",
    },
    "bow": {
        "name": "Bow",
        "specialist_ai": "bow_specialization",
        "master_ai": "mastery_bow",
    },
    "club": {
        "name": "Club",
        "specialist_ai": "club_specialization",
        "master_ai": "mastery_club",
    },
    "dagger": {
        "name": "Dagger",
        "specialist_ai": "dagger_specialization",
        "master_ai": "mastery_dagger",
    },
    "fist_and_tooth": {
        "name": "Fist & Tooth",
        "specialist_ai": "fist_and_tooth_specialization",
        "master_ai": "mastery_fist_and_tooth",
    },
    "grand_weapon": {
        "name": "Grand Weapon",
        "specialist_ai": "grand_weapon_specialization",
        "master_ai": "mastery_grand_weapon",
    },
    "katana": {
        "name": "Katana",
        "expansion": "sunstalker",
        "specialist_ai": "katana_specialization",
        "master_ai": "mastery_katana",
    },
    "katar": {
        "name":"Katar",
        "specialist_ai": "katar_specialization",
        "master_ai": "mastery_katar",
    },
    "scythe": {
        "name": "Scythe",
        "expansion": "dragon_king",
        "specialist_ai": "scythe_specialization",
        "master_ai": "mastery_scythe",
    },
    "sword": {
        "name": "Sword",
        "specialist_ai": "sword_specialization",
        "master_ai": "mastery_sword",
    },
    "shield": {
        "name": "Shield",
        "specialist_ai": "shield_specialization",
        "master_ai": "mastery_shield",
    },
    "spear": {
        "name": "Spear",
        "specialist_ai": "spear_specialization",
        "master_ai": "mastery_spear",
    },
    "twilight_sword": {
        "name": "Twilight Sword",
        "excluded_campaigns": ["people_of_the_stars","people_of_the_sun"],
        "specialist_ai": "twilight_sword_specialization",
        "master_ai": "mastery_twilight_sword",
    },
    "whip": {
        "name": "Whip",
        "specialist_ai": "whip_specialization",
        "master_ai": "mastery_whip",
    },
}
