core = {
    'accessory': {
        'name': 'Accessory',
        'type': 'keyword',
        'desc': (
            'A gear special rule. Accessory gear may be worn in addition to '
            'armor on a hit location. Each accessory specifies the hit '
            'location it covers.'
        ),
    },
    'activation_limit': {
        'name': 'Activation Limit: N',
        'type': 'special_rule',
        'expansion': 'sunstalker',
        'desc': (
            'May activate this up to N times per showdown (use tokens to '
            'track).'
        ),
    },
    'ammo_bow': {
        'name': 'Ammo - Bow',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. You must have a bow in your gear grid '
            'to activate this card. Ammo has the range of a bow in your '
            'gear grid.'
        ),
    },
    'ammuntion': {
        'name': 'Ammunition',
        'type': 'keyword',
        'desc': (
            "A gear keyword. This gear is ammunition for another weapon gear."
        ),
    },
    'archive': {
        'name': 'Archive',
        'type': 'keyword',
        'desc': (
            'Remove this card from play and return it to the game box. Unless '
            "it is recorded into settlement storage or the survivor's record "
            "sheet, any archived card is permanently lost."
        ),
    },
    'arrow': {
        'name': 'Arrow',
        'type': 'keyword',
        'desc': "A gear keyword. This gear card is an arrow.",
    },
    'balm': {
        'name': 'Balm',
        'type': 'keyword',
        'desc': (
            "A gear keyword. Balm items work by rubbing them on a survivor's "
            "skin."
        ),
    },
    'barbed': {
        'name': 'Barbed N',
        'type': 'special_rule',
        'min_version': 'core_1_6',
        'desc': (
            'On a <b>Perfect hit</b>, gain +N strength for the rest of the '
            'attack.'
        ),
    },
    'blind': {
        'name': 'Blind',
        'type': 'special_rule',
        'expansion': 'sunstalker',
        'desc': '-1 Accuracy',
    },
    'block': {
        'name': 'Block N',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. Spend activation to ignore N hits the next '
            'time you are attacked. Lasts until your next act. A survivor may '
            'not use block more than once per attack.'
        ),
    },
    'bone': {
        'name': 'Bone',
        'type': 'keyword',
        'desc': (
            'A gear keyword. Bone is one of the primary materials used to '
            'craft this gear.'
        ),
    },
    'consume': {
        'name': 'Consume',
        'type': 'special_rule',
        'desc': (
            'A special rule. This consumable gear or resources may be ingested '
            'by survivors for a listed result. Some are archived after use.'
        ),
        'related': ['consumable','archive'],
    },
    'consumable': {
        'name': 'Consumable',
        'type': 'keyword',
        'desc': """A keyword. This may be consumed by survivors.""",
        'related': ['consume'],
    },
    'cumbersome': {
        'name': 'Cumbersome',
        'type': 'special_rule',
        'desc': """A gear special rule. Survivors must spend both movement and activation to activate Cumbersome gear. Ignore this if the weapon is activated indirectly (Pounce. Charge, etc).""",
    },
    'cursed': {
        'name': 'Cursed',
        'type': 'special_rule',
        'desc': """A gear special rule. This gear cannot be removed from the gear grid for any reason. If the survivor dies, archive this gear.""",
        'related': ['archive'],
    },
    'deadly': {
        'name': 'Deadly',
        'type': 'special_rule',
        'desc': """A gear special rule. Gain +l luck while attacking with this weapon. This increases the odds of inflicting critical wounds.""",
    },
    'deflect': {
        'name': 'Deflect X',
        'type': 'special_rule',
        'desc': """A gear special rule, when you Deflect X, gain (or lose) deflect tokens until you have X of them. When you are hit, if you have any deflect tokens, you ignore that hit and lose a deflect token. When you Deflect X, you lose the benefits of Block.""",
    },
    'devastating': {
        'name': 'Devastating X',
        'type': 'special_rule',
        'desc': """A gear special rule. When a devastating weapon wounds a monster, it will inflict X additional wounds.""",
    },
    'early_iron': {
        'name': 'Early Iron',
        'type': 'special_rule',
        'desc': """A gear special rule. When any of your attack roll results are a l, cancel your attack.""",
    },
    'ethereal': {
        'name': 'Ethereal',
        'type': 'special_rule',
        'desc': """A survivor must be <b>insane</b> and depart with a Savior to wear it. When the settlement has no Savior, archive it.""",
    },
    'feather': {
        'name': 'Feather',
        'type': 'keyword',
        'desc': """A gear keyword. This gear is substantively crafted of feathers.""",
    },
    'finesse': {
        'name': 'Finesse',
        'type': 'keyword',
        'desc': """A gear keyword. This gear requires finesse to use. This keyword does not interact with the core game in any way and is one of those annoying keywords for expansions.""",
    },
    'flammable': {
        'name': 'Flammable',
        'type': 'keyword',
        'desc': """A gear keyword. Fire can destroy this gear.""",
    },
    'fragile': {
        'name': 'Fragile',
        'type': 'keyword',
        'desc': """A gear keyword. This gear is easily broken.""",
    },
    'frail': {
        'name': 'Frail',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. Frail weapons are destroyed if a survivor '
            'attempts to wound a Super-dense location with them. Archive the '
            'weapon at the end of the attack.'
        ),
        'related': ['archive'],
    },
    'fur': {
        'name': 'Fur',
        'type': 'keyword',
        'desc': (
            'A gear keyword. This gear is substantively crafted of thick fur.'
        ),
    },
    'guard': {
        'name': 'Guard',
        'expansion': 'gorm',
        'type': 'special_rule',
        'desc': (
            'At the end of your attack, if you are standing and have a shield '
            'in your gear grid, spend 1 survival to move 3 spaces directly '
            'away from the monster and <b>Block 1</b> for free.'
        ),
        'related': ['block'],
    },
    'heavy': {
        'name': 'Heavy',
        'type': 'keyword',
        'desc': """A gear keyword. This gear has substantial weight.""",
    },
    'herb': {
        'name': 'Hide',
        'type': 'keyword',
        'desc': """A gear keyword. An item primarily made of herbs.""",
    },
    'instrument': {
        'name': 'Instrument',
        'type': 'keyword',
        'desc': """A gear keyword. This gear can be used to play music.""",
    },
    'irreplaceable': {
        'name': 'Irreplaceable',
        'type': 'special_rule',
        'desc': """A gear special rule. If a survivor dies, archive all irreplaceable gear in their gear grids.""",
        'related': ['archive'],
    },
    'jewelry': {
        'name': 'Jewelry',
        'type': 'keyword',
        'desc': """A gear keyword. Decorative and functional!""",
    },
    'lantern': {
        'name': 'Lantern',
        'type': 'keyword',
        'desc': """A gear keyword. A lantern illuminates the darkness.""",
    },
    'leather': {
        'name': 'Leather',
        'type': 'keyword',
        'desc': """A gear keyword. Cured hides are a crucial component of this gear.""",
    },
    'melee': {
        'name': 'Melee',
        'type': 'keyword',
        'desc': """ A weapon gear keyword. To attack with a melee weapon, survivors must be in a space adjacent to the monster. Melee weapons with Reach can attack from further away.""",
    },
    'metal': {
        'name': 'Metal',
        'type': 'keyword',
        'desc': """A gear keyword. This gear is substantively crafted of metal.""",
    },
    'noisy': {
        'name': 'Noisy',
        'type': 'keyword',
        'desc': """A gear keyword. This gear Is hard to keep quiet.""",
    },
    'obstacle': {
        'name': 'Obstacle',
        'type': 'keyword',
        'desc': (
            'A terrain rule. This terrain blocks survivor and monster field of '
            'view. Interrupting ranged weapon attacks and monster targeting. '
            'To check if field of view is blocked, draw an imaginary line from '
            "the center of the miniature's base to the center of the intended "
            "target's base. If the line comes in contact with a space occupied "
            "by an obstacle, the field of view is blocked and the target is "
            'not In field of view.'
        ),
    },
    'other': {
        'name': 'Other',
        'type': 'keyword',
        'desc': "A gear keyword. The effects of this gear are otherworldly.",
    },
    'outfit': {
        'name': 'Outfit',
        'type': 'special_rule',
        'desc': """This completes an armor set if you're wearing the rest of the set and it shares a material keyword with the missing armor gear. For example, if you're wearing an Oxidized Lantern Helm and Phoenix Armor on every other hit location, you would gain the Phoenix Armor Set bonus because the Phoenix Helm also has the metal keyword.""",
    },
    'paired': {
        'name': 'Paired',
        'type': 'special_rule',
        'desc': """A gear special rule. Paired weapons are two Identical weapons that can be used as one. Add the speed of the second weapon when attacking with the first. These weapons must have the same name, and both must be In your gear grid.""",
    },
    'pickaxe': {
        'name': 'Pickaxe',
        'type': 'keyword',
        'desc': """A gear keyword, in certain situations, this can be used to mine minerals.""",
    },
    'prismatic': {
        'name': 'Prismatic',
        'type': 'special_rule',
        'expansion': 'sunstalker',
        'desc': (
            'Your complete affinities and incomplete affinity halves count as '
            'all colors.'
        ),
    },
    'range': {
        'name': 'Range: N',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. Survivors this many or fewer spaces away '
            'from a monster may attack with this weapon. Ranged weapons cannot '
            'be used If field of view to the monster is blocked (by terrain '
            'with the Obtsacle rule).'
        ),
        'related': ['ranged','obstacle'],
    },
    'ranged': {
        'name': 'Ranged',
        'type': 'keyword',
        'desc': """A gear keyword. A ranged weapon, like a bow or dart, allows survivors to attack from a distance.""",
        'related': ['range'],
    },
    'rawhide': {
        'name': 'Rawhide',
        'type': 'keyword',
        'desc': """A gear keyword. This gear is crafted of uncured hides.""",
    },
    'reach': {
        'name': 'Reach',
        'type': 'special_rule',
        'desc': """A gear special rule. Reach weapons are long enough to attack monsters when the survivor Is not adjacent. Reach specifies the maximum number of spaces away that a survivor can attack with this weapon."""
    },
    'savage': {
        'name': 'Savage',
        'type': 'special_rule',
        'desc': """A gear special rule. After the first critical wound in an attack, savage weapons cause 1 additional wound. This rule does not trigger on Impervious hit locations.""",
    },
    'selfish': {
        'name': 'Selfish',
        'type': 'special_rule',
        'desc': """A gear special rule. A gear with this rule may not be in a same gear grid with any gear with the "other" keyword.""",
    },
    'sentient': {
        'name': 'Sentient',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. A survivor must be insane to activate '
            'this gear.'
        ),
    },
    'set': {
        'name': 'Set',
        'type': 'keyword',
        'desc': (
            'A gear keyword listed on some armor cards. This means this armor '
            'is part of an armor set.'
        ),
    },
    'sharp': {
        'name': 'Sharp',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. Add 1dlO strength to each wound attempt '
            'using this gear. This d1O is not a wound roll, and cannot cause '
            'critical wounds.'
        ),
    },
    'sickle': {
        'name': 'Sickle',
        'type': 'keyword',
        'desc': (
            'A gear keyword. In certain situations, this can be used to '
            'harvest herbs.'
        ),
    },
    'slow': {
        'name': 'Slow',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. Slow weapons always have an attack speed of '
            '1. Do not add speed modifiers.'
        ),
    },
    'soluble': {
        'name': 'Soluble',
        'type': 'keyword',
        'desc': 'A gear keyword. Able to be dissolved in liquid.',
    },
    'stinky': {
        'name': 'Stinky',
        'type': 'keyword',
        'desc': 'A gear keyword. This item has a strong odor.',
    },
    'tool': {
        'name': 'Tool',
        'type': 'keyword',
        'desc': (
            'A gear keyword. Some tools trigger story events or grant bonuses.'
        ),
    },
    'two_handed': {
        'name': 'Two-handed',
        'type': 'keyword',
        'desc': (
            'A gear keyword. This weapon requires two hands to use. Some gear '
            'and rules do not work with two-handed weapons.'
        ),
    },
    'unique': {
        'name': 'Unique',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. A settlement may only have one copy of this '
            'gear card at a time.'
        ),
    },
    'unwieldy': {
        'name': 'Unwieldy',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. If any attack dice roll results are 1, the '
            'weapon causes 1 random damage to the survivor for each 1 roiled. '
            'Continue the attack as normal.'
        ),
    },
    'vital': {
        'name': 'Vital',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. If the settlement has any gear with this '
            'rule, the survivors cannot depart without this gear. If the '
            'survivor holding Vital gear perishes before the showdown, '
            'another survivor must pick up the Vital gear (discarding gear '
            'to make room in their grid if needed).'
        ),
    },
}

expansion = {

    # promo
    'female_only': {
        'expansion': 'promo',
        'name': 'Female Only',
        'desc': None,
    },

    # sunstalker
    'prismatic': {
        'expansion': 'sunstalker',
        'type': 'special_rule',
        'name': 'Prismatic',
        'desc': (
            'Your complete affinities and incomplete affinity halves count '
            'as all colors.'
        ),
    },
    'shadow_walk': {
        'expansion': 'sunstalker',
        'type': 'special_rule',
        'name': 'Shadow Walk',
        'desc': None,
    },

    # grimmory
    'consecutive_spaces': {
        'name': 'Consecutive Spaces',
        'desc': (
            'When a survivor is instructed to move consecutive spaces, they '
            'must move without occupying the same space more than once.<br/>'
            'A survivor could not, for example, move back and forth between '
            'two spaces to fulfill consecutive space movement. They could, '
            'however, move around a monster or move in a straight line.'
        ),
    },

    # Pascha
    'cleavage_x': {
        'name': 'Cleavage X',
        'type': 'special_rule',
        'expansion': 'pascha',
        'desc': (
            'A gear special rule. When you attempt to wound a hit location '
            'with a persistent injury, gain +X luck for that wound attempt.'
        ),
    },

    # willow
    'novel_proficiency': {
        'name': 'Novel Proficiency',
        'type': 'special_rule',
        'expansion': 'willow',
        'desc': (
            "When a survivor's proficiency level reaches specialization and "
            'they have at least 3 courage, they can develop something new.'
            'They may select a novel weapon proficiency that matches their '
            'weapon type, instead of continuing with normal weapon '
            'proficiency<br/>.'
            'When a survivor with a novel proficency reaches mastery, it '
            'becomes an innovation and all survivors gain the benefit of its '
            'specialization rules. A campaign can have both types of weapon '
            'proficiencies, so it is possible for a settlement to have sword '
            'mastery and a novel sword mastery.'
        ),
    },
    'refined': {
        'name': 'Refined',
        'type': 'special_rule',
        'expansion': 'willow',
        'desc': (
            'When this fails to wound, you may reroll the '
            'wound attempt. Limit, once per attack.'
        ),
    },

    # badar
    'cleave': {
        'expansion': 'badar',
        'name': 'Cleave',
        'desc': (
            'You may spend '
            '<font class="kdm_font">c</font><font class="kdm_font">a</font>'
            'to activate and attack with this weapon. If you do, it gains the '
            'two-handed keyword, +4 strength, and <b>slow</b> for the attack.'
            '<br/>'
            'You cannot use <b>Cleave</b> if an injury or or other effect is '
            'preventing you from activating gear with the two-handed keyword.'
        ),
    },
    'sealed': {
        'expansion': 'badar',
        'name': 'Sealed',
        'desc': (
            'Seal gear has a bonus effect that can only be earned by training. '
            'A survivor can unseal the gear by declaring it as their weapon '
            'proficiency, forsaking the normal bonuses of selecting a weapon '
            'type. When the survivor reaches the specialization rank, they '
            'earn the effect listed after the gear card.<br/>'
            "A survivor can only earn a gear's <b>Sealed</b> bonus once per "
            'lifetime.<br/>'
            'For example, the <b>Toxicimitar</b> has "<b>Sealed - Gain the '
            '<b>Crescent Step</b> <span class="kd deck_icon" deck="SF">'
            'SF</span>." When a survivor with '
            '<b>Toxicimitar</b> proficiency reaches rank 3 (specialization), '
            'they gain the <b>Crescent Step</b> <span class="kd deck_icon" '
            'deck="SF">SF</span>.'
        ),
    },

    # doll
    'center': {
        'name': 'Center',
        'type': 'special_gear_rule',
        'expansion': 'doll',
        'desc': (
            'This gear must be placed in the center of your gear grid.<br/>'
            'If you gain this and already have a gear in the center of your '
            'grid archive it and place this in the center of your grid instead.'
        ),
    },

    # erza of dedheim
    'doombound': {
        'expansion': 'erza_of_dedheim',
        'name': 'Doombound',
        'type': 'special_gear_rule',
        'desc': (
            '<b>Doombound:</b> When you become <b>doomed</b>, place a doom '
            'token on this. You must archive a doom token to activate this. '
        ),
    }
}
