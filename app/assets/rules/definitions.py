core = {
    'accessory': {
        'name': 'Accessory',
        'type': 'gear_special_rule',
        'desc': (
            'A gear special rule. Accessory gear may be worn in addition to '
            'armor on a hit location. Each accessory specifies the hit '
            'location it covers.'
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
        'type': 'gear_keyword',
        'desc': (
            "This gear is ammunition for another weapon gear."
        ),
    },
    'archive': {
        'name': 'Archive',
        'type': 'rule',
        'desc': (
            'Remove this card from play and return it to the game box. Unless '
            "it is recorded into settlement storage or the survivor's record "
            "sheet, any archived card is permanently lost."
        ),
    },
    'armor': {
        'name': 'Armor',
        'type': 'gear_keyword',
        'desc': (
            'Gear with this keyword is armor. Protects the survivor from '
            'injury. Each piece of armor will have the hit location symnbol '
            'for the hit location it can be worn on. Each hit location may '
            'only wear one piece of armor.'
        ),
    },
    'arrow': {
        'name': 'Arrow',
        'type': 'gear_keyword',
        'desc': "This gear card is an arrow.",
    },
    'balm': {
        'name': 'Balm',
        'type': 'gear_keyword',
        'desc': (
            "Balm items work by rubbing them on a survivor's "
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
    'block_x': {
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
        'type': 'gear_keyword',
        'desc': (
            'Bone is one of the primary materials used to '
            'craft this gear.'
        ),
    },
    'collision': {
        'name': 'Collision',
        'type': 'special_rule',
        'desc': 'When a survivor suffers collision, they are knocked down.',
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
        'desc': "A keyword. This may be consumed by survivors.",
        'related': ['consume'],
    },
    'cumbersome': {
        'name': 'Cumbersome',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. Survivors must spend both movement and '
            'activation to activate Cumbersome gear. Ignore this if the weapon '
            'is activated indirectly (Pounce. Charge, etc).'
        ),
    },
    'cursed': {
        'name': 'Cursed',
        'type': 'gear_special_rule',
        'desc': (
            'This gear cannot be removed from the gear '
            'grid for any reason. If the survivor dies, archive this gear.'
        ),
        'related': ['archive'],
    },
    'dazed': {
        'name': 'Dazed',
        'type': 'gear_special_rule',
        'desc': (
            'The monster is dazed, and gains -1 '
            'speed token until the end of its turn. A monster can be dazed '
            'once per round.'
        ),
    },
    'deadly': {
        'name': 'Deadly',
        'type': 'gear_special_rule',
        'desc': (
            'Gain +l luck while attacking with this '
            'weapon. This increases the odds of inflicting critical wounds.'
        ),
    },
    'deflect_x': {
        'name': 'Deflect X',
        'type': 'gear_special_rule',
        'related': ['block_x'],
        'desc': (
            'When you Deflect X, gain (or lose) deflect '
            'tokens until you have X of them. When you are hit, if you have '
            'any deflect tokens, you ignore that hit and lose a deflect token. '
            'When you Deflect X, you lose the benefits of Block.'
        ),
    },
    'devastating_x': {
        'name': 'Devastating X',
        'type': 'gear_special_rule',
        'desc': (
            'When a devastating weapon wounds a monster, '
            'it will inflict X additional wounds.'
        ),
    },
    'doomed': {
        'name': 'Doomed',
        'type': 'special_rule',
        'desc': (
            'While a survivor is doomed, they cannot perform any actions or '
            "spend survival. If a survivor is doomed by a monster's AI or "
            'Hit Location card, they are doomed until all actions on the card '
            'are performed and the card is resolved.'
        ),
    },
    'early_iron': {
        'name': 'Early Iron',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. When any of your attack roll results are a '
            '1, cancel your attack.'
        ),
    },
    'ethereal': {
        'name': 'Ethereal',
        'type': 'special_rule',
        'desc': (
            'A survivor must be <b>insane</b> and depart with a Savior to wear '
            'it. When the settlement has no Savior, archive it.'
        ),
    },
    'feather': {
        'name': 'Feather',
        'type': 'gear_keyword',
        'desc': 'This gear is substantively crafted of feathers.',
    },
    'finesse': {
        'name': 'Finesse',
        'type': 'gear_keyword',
        'desc': (
            'This gear requires finesse to use. This keyword does not interact '
            'with the core game in any way and is one of those annoying '
            'keywords for expansions.'
        ),
    },
    'flammable': {
        'name': 'Flammable',
        'type': 'gear_keyword',
        'desc': """Fire can destroy this gear.""",
    },
    'fragile': {
        'name': 'Fragile',
        'type': 'gear_keyword',
        'desc': """This gear is easily broken.""",
    },
    'frail': {
        'name': 'Frail',
        'type': 'gear_special_rule',
        'desc': (
            'Frail weapons are destroyed if a survivor '
            'attempts to wound a Super-dense location with them. Archive the '
            'weapon at the end of the attack.'
        ),
        'related': ['archive'],
    },
    'fur': {
        'name': 'Fur',
        'type': 'gear_keyword',
        'desc': 'This gear is substantively crafted of thick fur.',
    },
    'heavy': {
        'name': 'Heavy',
        'type': 'gear_keyword',
        'desc': "This gear has substantial weight.",
    },
    'herb': {
        'name': 'Hide',
        'type': 'gear_keyword',
        'desc': 'An item primarily made of herbs.',
    },
    'instrument': {
        'name': 'Instrument',
        'type': 'gear_keyword',
        'desc': "This gear can be used to play music.",
    },
    'irreplaceable': {
        'name': 'Irreplaceable',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. If a survivor dies, archive all irreplaceable'
            ' gear in their gear grids.'
        ),
        'related': ['archive'],
    },
    'item': {
        'name': 'Item',
        'type': 'gear_keyword',
        'desc': 'Gear that is neither a weapon nor armor.',
    },
    'jewelry': {
        'name': 'Jewelry',
        'type': 'gear_keyword',
        'desc': 'Decorative and functional!',
    },
    'lantern': {
        'name': 'Lantern',
        'type': 'gear_keyword',
        'desc': """A lantern illuminates the darkness.""",
    },
    'leather': {
        'name': 'Leather',
        'type': 'gear_keyword',
        'desc': """Cured hides are a crucial component of this gear.""",
    },
    'melee': {
        'name': 'Melee',
        'type': 'gear_keyword',
        'related': ['reach_x'],
        'desc': (
            'A weapon gear keyword. To attack with a melee weapon, survivors '
            'must be in a space adjacent to the monster. Melee weapons with '
            'Reach can attack from further away.'
        ),
    },
    'metal': {
        'name': 'Metal',
        'type': 'gear_keyword',
        'desc': """This gear is substantively crafted of metal.""",
    },
    'noisy': {
        'name': 'Noisy',
        'type': 'gear_keyword',
        'desc': """This gear Is hard to keep quiet.""",
    },
    'obstacle': {
        'name': 'Obstacle',
        'type': 'terrain_rule',
        'desc': (
            'This terrain blocks survivor and monster field of '
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
        'type': 'gear_keyword',
        'desc': "The effects of this gear are otherworldly.",
    },
    'outfit': {
        'name': 'Outfit',
        'type': 'special_rule',
        'desc': (
            "This completes an armor set if you're wearing the rest of the set "
            "and it shares a material keyword with the missing armor gear. "
            "For example, if you're wearing an Oxidized Lantern Helm and "
            "Phoenix Armor on every other hit location, you would gain the "
            "Phoenix Armor Set bonus because the Phoenix Helm also has the "
            "metal keyword."
        ),
    },
    'paired': {
        'name': 'Paired',
        'type': 'special_rule',
        'desc': (
            'A gear special rule. Paired weapons are two identical weapons '
            'that can be used as one. Add the speed of the second weapon when '
            'attacking with the first. These weapons must have the same name, '
            'and both must be In your gear grid.'
        ),
    },
    'pickaxe': {
        'name': 'Pickaxe',
        'type': 'gear_keyword',
        'desc': (
            'In certain situations, this can be used to mine '
            'minerals.'
        ),
    },
    'range_x': {
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
        'type': 'gear_keyword',
        'desc': (
            'A ranged weapon, like a bow or dart, allows survivors to attack '
            'from a distance.'
        ),
        'related': ['range'],
    },
    'rawhide': {
        'name': 'Rawhide',
        'type': 'gear_keyword',
        'desc': 'This gear is crafted of uncured hides.',
    },
    'reach_x': {
        'name': 'Reach',
        'type': 'gear_special_rule',
        'desc': (
            'A gear special rule. Reach weapons are long enough to attack '
            'monsters when the survivor is not adjacent. Reach specifies the '
            'maximum number of spaces away that a survivor can attack with '
            'this weapon.'
        ),
    },
    'savage': {
        'name': 'Savage',
        'type': 'gear_special_rule',
        'desc': (
            'A gear special rule. After the first critical wound in an attack, '
            'savage weapons cause 1 additional wound. This rule does not '
            'trigger on Impervious hit locations.'
        ),
    },
    'seed': {
        'name': 'Seed',
        'type': 'gear_keyword',
        'desc': (
            'Gear cards with the seed keyword can be crafted only via their '
            'respective Seed Pattern recipes.'
        ),
    },
    'selfish': {
        'name': 'Selfish',
        'type': 'gear_special_rule',
        'desc': (
            'A gear special rule. A gear with this rule may not be in a same '
            'gear grid with any gear with the "other" keyword.'
        ),
    },
    'sentient': {
        'name': 'Sentient',
        'type': 'gear_special_rule',
        'desc': (
            'A gear special rule. A survivor must be insane to activate '
            'this gear.'
        ),
    },
    'set': {
        'name': 'Set',
        'type': 'gear_keyword',
        'desc': (
            'A gear keyword listed on some armor cards. This means this armor '
            'is part of an armor set.'
        ),
    },
    'sharp': {
        'name': 'Sharp',
        'type': 'gear_special_rule',
        'desc': (
            'Add 1dlO strength to each wound attempt '
            'using this gear. This d1O is not a wound roll, and cannot cause '
            'critical wounds.'
        ),
    },
    'sickle': {
        'name': 'Sickle',
        'type': 'gear_keyword',
        'desc': (
            'In certain situations, this can be used to '
            'harvest herbs.'
        ),
    },
    'slow': {
        'name': 'Slow',
        'type': 'gear_special_rule',
        'desc': (
            'Slow weapons always have an attack speed of '
            '1. Do not add speed modifiers.'
        ),
    },
    'soluble': {
        'name': 'Soluble',
        'type': 'gear_keyword',
        'desc': 'Able to be dissolved in liquid.',
    },
    'stinky': {
        'name': 'Stinky',
        'type': 'gear_keyword',
        'desc': 'This item has a strong odor.',
    },
    'super_dense': {
        'name': 'Super-dense',
        'type': 'hit_location',
        'desc': (
            'A type of hit location. This hit location is unusually hard. '
            'If a survivor attempts to wound one of these locations with a '
            'frail weapon, it is destroyed and archived at the end of the '
            'attack.'
        ),
    },
    'tool': {
        'name': 'Tool',
        'type': 'gear_keyword',
        'desc': (
            'Some tools trigger story events or grant bonuses.'
        ),
    },
    'two-handed': {
        'name': 'Two-handed',
        'type': 'gear_keyword',
        'desc': (
            'This weapon requires two hands to use. Some gear '
            'and rules do not work with two-handed weapons.'
        ),
    },
    'undeathable': {
        'name': 'Undeathable',
        'type': 'gear_special_rule',
        'desc': (
            'If the survivor dies, roll 1d10. On a result of 6+, the '
            'survivor lives. If this roll occurs from the survivor having '
            'a lethal amount of bleeding tokens, the survivor will not die '
            'until they gain another bleeding token.'
        ),
    },
    'unique': {
        'name': 'Unique',
        'type': 'gear_special_rule',
        'desc': (
            'A settlement may only have one copy of this '
            'gear card at a time.'
        ),
    },
    'unwieldy': {
        'name': 'Unwieldy',
        'type': 'gear_special_rule',
        'desc': (
            'If any attack dice roll results are 1, the '
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
    'weapon': {
        'name': 'Weapon',
        'desc': (
            'A type of gear card. Weapon types in the core game include axe, '
            'bow, club, dagger, fist & tooth, grand, katar, shield, spear, '
            'sword, and whip.'
        ),
    },
}
