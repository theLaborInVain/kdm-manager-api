'''

    Dictionary names here ultimately cannot be sub_type values because of
    expansion content.

'''

from .gamblers_chest import *

ability = {
    'ageless': {
        'desc': (
            'You may hunt if you are retired. When you gain Hunt XP, you may '
            'decide not to gain it.'
        ),
        'name': 'Ageless',
        'type': 'ability'
    },
    'analyze': {
        'desc': (
            "At the start of the Survivors' turn, if you are adjacent to the "
            "monster, reveal the top AI card, then place back on top of the "
            "deck."
        ),
        'name': 'Analyze',
        'type': 'ability',
        'base_attribute': 'Understanding',
        'excluded': ['explore','tinker'],
    },
    'bitter_frenzy': {
        'desc': (
            'Each showdown, the first time you suffer the frenzy brain trauma, '
            'gain d10 survival. You may spend survival while <b>Frenzied</b>.'
        ),
        'name': 'Bitter Frenzy',
        'type': 'ability'
    },
    'blue_life_exchange': {
        'desc': (
            'In the <b>Aftermath</b>, gain 3 additional Hunt XP. You may not '
            'place <b>other</b> gear in your grid. Gain +1 permanent luck with '
            'each <b>Age</b> milestone. When you retire, you cease to exist.'
        ),
        'selectable': False,
        'name': 'Blue Life Exchange',
        'related': ['dream_of_the_lantern', 'lucernae'],
        'type': 'ability'
    },
    'bone_witch_scarred_eyes':{
        'Accuracy': -4,
        'Strength': 4,
        'desc': 'Suffer -4 permanent Accuracy and gain +4 permanent strength.',
        'name': 'Bone Witch - Scarred Eyes',
        'type': 'impairment'
    },
    'bone_witch_wounds': {
        'Accuracy': -1,
        'Strength': -1,
        'desc': (
            'Suffer -1 permanent strength, -1 permanent accuracy and skip the '
            'next hunt.'
        ),
        'name': 'Bone Witch - Wounds',
        'skip_next_hunt': True,
        'type': 'impairment'
    },
    'burnt_nerves': {
        'name': 'Burnt Nerves',
        'desc': 'You are immune to <b>Bash</b>.',
    },
    'cancerous_illness': {
        'desc': 'You cannot gain survival.',
        'name': 'Cancerous Illness',
        'type': 'impairment',
        'cannot_gain_survival': True,
    },
    'caratosis': {
        'desc': (
            'Before making an attack roll, you may declare "Caratosis X" in a '
            'loud, booming voice. If you do, that attack gains X automatic '
            'hits. X cannot be more than your total red affinities. When the '
            'attack ends, gain +X hunt Xp.<br/>When you trigger Age 2, gain '
            'the <b>Beast of Caratosis</b> secret fighting art.'
        ),
        'selectable': False,
        'name': 'Caratosis',
        'epithet': 'caratosis',
        'related': ['dream_of_the_beast', 'life_exchange'],
        'type': 'ability'
    },
    'crystal_skin': {
        'desc': 'You ignore <b>cursed</b> and cannot wear armor. When you <b>depart</b>, gain <font class="inline_shield">3</font> to all hit locations. Suffer -2 to the result of all severe injury rolls. When you participate in <b>Intimacy</b>, newborns gain <b>Crystal Skin</b> in addition to any other roll results.',
        'name': 'Crystal Skin',
        'type': 'ability',
        'inheritable': True,
        'max': 1,
    },
    'dead_inside': {
        'name': 'Dead Inside',
        'desc': 'You cannot gain survival.',
        'type': 'impairment',
        "cannot_gain_survival": True,
    },
    'dormenatus': {
        'desc': """When you suffer damage, you may declare 'Dormenatus X' in a loud, booming voice. If you do, gain <font class="inline_shield">x</font> to each hit location. X cannot be more than your total green affinities. After the damage is resolved, gain +X hunt XP.<br/>When you trigger Age 2, gain the <b>Grace of Dormenatus</b> secret fighting art.""",
        'selectable': False,
        'name': 'Dormenatus',
        'epithet': 'dormenatus',
        'related': ['dream_of_the_crown', 'life_exchange'],
        'type': 'ability'
    },
    'dream_of_the_beast': {
        'Strength': 1,
        'affinities': {'red': 1},
        'desc': '1 permanent red affinity.',
        'epithet': 'red_savior',
        'selectable': False,
        'name': 'Dream of the Beast',
        'related': ['caratosis', 'life_exchange'],
        'type': 'ability'
    },
    'dream_of_the_crown': {
        'Evasion': 1,
        'affinities': {'green': 1},
        'desc': '1 permanent green affinity.',
        'epithet': 'green_savior',
        'selectable': False,
        'name': 'Dream of the Crown',
        'related': ['dormenatus', 'life_exchange'],
        'type': 'ability'
    },
    'dream_of_the_lantern': {
        'Luck': 1,
        'affinities': {'blue': 1},
        'desc': '1 permanent blue affinity.',
        'epithet': 'blue_savior',
        'selectable': False,
        'name': 'Dream of the Lantern',
        'related': ['lucernae', 'life_exchange'],
        'type': 'ability'
    },
    'endless_babble': {
        'desc': 'When you <b>depart</b>, <b>departing survivors</b> gain +1 insanity. You may not encourage.',
        'name': 'Endless Babble',
        'survival_actions': {
            'disable': ['encourage'],
        },
        'type': 'impairment'
    },
    'explore': {
        'desc': 'When you roll on an investigate table, add +2 to your roll result.',
        'summary': "Add +2 to your investigate roll results.",
        'name': 'Explore',
        'type': 'ability',
        'base_attribute': 'Understanding',
        'excluded': ['analyze','tinker'],
    },
    'fated_battle': {
        'desc': 'At the start of a showdown with the picked monster, gain +1 speed token.',
        'name': 'Fated Battle',
        'type': 'ability'
    },
    'green_life_exchange': {
        'desc': 'In the <b>Aftermath</b>, gain 3 additional Hunt XP. You may not place <b>other</b> gear in your grid. Gain +1 permanent evasion with each <b>Age</b> milestone. When you retire, you cease to exist.',
         'selectable': False,
         'name': 'Green Life Exchange',
         'related': ['dream_of_the_crown', 'dormenatus'],
         'type': 'ability'
    },
    "homing_instinct": {
        "name": "Homing Instinct",
        "type": "ability",
        "desc": "Add +5 to your rolls on the Run Away story event."
    },
    "iron_will": {
        "name": "Iron Will",
        "desc": "You cannot be knocked down. Reduce all knockback you suffer to <b>knockback 1</b>.",
        "type": "ability",
    },
    "kings_curse": {
        'desc': 'At the Aftermath, <font class="kdm_font">g</font> <b>King\'s Curse</b>.',
        'epithet': "kings_curse",
        'name': "King's Curse",
        'type': 'curse'
    },
    'legendcaller': {
        'desc': 'Once a lifetime, on a hunt board space after <b>Overwhelming Darkness</b>, in place of rolling a random hunt event, use "53" as your result.',
        'epithet': 'legendcaller',
        'name': 'Legendcaller',
        'type': 'ability'
    },
    'leprosy': {
        'desc': 'Reduce all damage suffered by 1 to a minimum of 1. Suffer -2 to severe injury rolls.',
        'epithet': 'leper',
        'name': 'Leprosy',
        'type': 'impairment'
    },
    'leyline_walker': {
        'desc': 'While there is no armor or accessory gear in your grid, gain +3 evasion.',
        'epithet': 'leyline_walker',
        'name': 'Leyline Walker',
        'type': 'ability'
    },
    'lovelorn_rock': {
        'desc': 'Forever in love, the straggler loses one gear slot permanently to the rock. This survivor must always leave one gear space empty to hold their rock. The rock can be lost like normal gear.',
        'name': 'Lovelorn Rock',
        'type': 'impairment',
        'epithet': 'lithophile',
    },
    'lucernae': {
        'desc': """Before making a wound attempt, you may declare "Lucernae X" in a loud, booming voice. If you do, that wound attempt gains X luck. X cannot be more than your total blue affinities. When the attack ends, you gain +X hunt XP.<br/> When you trigger Age 2, gain the <b>Lucernae's Lantern</b> secret Fighting Art.""",
        'selectable': False,
        'name': 'Lucernae',
        'epithet': 'lucernae',
        'related': ['dream_of_the_lantern', 'life_exchange'],
        'type': 'ability'
    },
    'mad_oracle': {
        'desc': (
            'Once per showdown, as a monster draws an AI, name a card out '
            'loud. If the AI card drawn is the card you named, gain +1 evasion '
            'token.'
        ),
        'name': 'Mad Oracle',
        'type': 'ability',
    },
    'marrow_hunger': {
        'desc': 'When the Murder or Skull Eater settlement events are drawn, this survivor is nominated.',
        'epithet': 'skull_eater',
        'name': 'Marrow Hunger',
        'type': 'impairment'
    },
    'matchmaker': {
        'desc': 'When you are a returning survivor, once per year you may spend 1 Endeavor to trigger Intimacy (story event).',
        'summary': "Spend 1 endeavor to trigger Intimacy story event.",
        'name': 'Matchmaker',
        'type': 'ability',
        'endeavors': ['matchmaker_trigger_intimacy'],
        'base_attribute': 'Courage',
        'excluded': ['stalwart','prepared'],
    },
    'metal_maw': {
        '4desc': 'Your Fist & Tooth gains <b>Sharp</b>. (Add 1d10 strength to each wound attempt using this gear. This d10 is not a wound roll, and cannot cause critical wounds.)',
        'name': 'Metal Maw',
        'type': 'ability'
    },
    'partner': {
        'desc': 'When you both <b>Arrive</b>, gain survival up to the survival limit. Partners may only nominate each other for <b><font class="kdm_font">g</font> Intimacy</b>. When a partner dies, the remaining partner gains a random disorder and loses this ability.',
        'name': 'Partner',
        'type': 'ability'
    },
    'peerless': {
        'desc': 'When you gain insanity, you may gain an equal amount of survival.',
        'name': 'Peerless',
        'type': 'ability'
    },
    'possessed': {
        'Accuracy': 1,
        'Strength': 2,
        'cannot_use_fighting_arts': True,
        'desc': (
            'Cannot use weapon specialization, weapon mastery, or fighting '
            'arts.'
        ),
        'name': 'Possessed',
        'type': 'ability',
    },
    'prepared': {
        'desc': 'When rolling to determine a straggler, add your hunt experience to your roll result.',
        'summary': "Add Hunt XP to your roll when determining a straggler.",
        'name': 'Prepared',
        'type': 'ability',
        'base_attribute': 'Courage',
        'excluded': ['stalwart','matchmaker'],
    },
    'life_exchange': {
        'desc': 'In the <b>Aftermath</b>, gain 1 additional Hunt XP. You may not wear <b>other</b> gear. If you trigger the White Secret story event, you cease to exist. When you retire, you cease to exist.',
        'name': 'Life Exchange',
    },
    'red_life_exchange': {
        'desc': 'In the <b>Aftermath</b>, gain 3 additional Hunt XP. You may not place <b>other</b> gear in your grid. Gain +1 permanent strength with each <b>Age</b> milestone. When you retire, you cease to exist.',
        'selectable': False,
        'name': 'Red Life Exchange',
        'related': ['caratosis', 'dream_of_the_beast'],
        'type': 'ability'
    },
    'sour_death': {
        'desc': "When you are knocked down, you may encourage yourself (even if you're deaf). If you do, gain +1 strength token.",
        'name': 'Sour Death',
        'type': 'ability'
    },
    'stalwart': {
        'desc': 'Ignore being knocked down by brain trauma and intimidation actions.',
        'summary': "Can't be knocked down by brain trauma or intimidate.",
        'name': 'Stalwart',
        'type': 'ability',
        'base_attribute': 'Courage',
        'excluded': ['prepared','matchmaker'],
    },
    'story_of_the_forsaker': {
        'desc': 'You cannot be knocked down during a showdown with a nemesis monster.',
        'name': 'Story of the Forsaker',
        'type': 'ability'
    },
    'story_of_the_goblin': {
        'desc': 'Once per showdown you may...roll 1d10. On a 3+, gain the priority target token and the monster gains +1 damage token.',
        'name': 'Story of the Goblin',
        'type': 'ability'
    },
    'story_of_the_young_hero': {
        'desc': 'At the start of your act, you may...[g]ain 2 bleeding tokens and +1 survival.',
        'name': 'Story of the Young Hero',
        'type': 'ability'
    },
    'sweet_battle': {
#        'desc': 'You may surge without spending survival. If you do, the Activation must be used to activate a weapon.',
        'desc': 'Once per round, you may <b>surge</b> without spending survival. If you do, the Activation must be used to activate the weapon.',
        'name': 'Sweet Battle',
        'type': 'ability',
        'survival_actions': {
            'enable': ['surge'],
        },
    },
    'thundercaller': {
        'desc': 'Once a lifetime, on a hunt board space after <b>Overwhelming Darkness</b>, in place of rolling a random hunt event, use "100" as your result.',
        'epithet': 'thundercaller',
        'name': 'Thundercaller',
        'type': 'ability'
    },
    'tinker': {
        'desc': 'When you are a returning survivor, gain +1 Endeavor to use this settlement phase.',
        'summary': '+1 endeavor when a returning survivor.',
        'name': 'Tinker',
        'type': 'ability',
        'base_attribute': 'Understanding',
        'excluded': ['analyze','explore'],
    },
    'twilight_sword': {
        'desc': 'You may select <b>Twilight Sword</b> as a weapon proficiency type. This weapon may not be removed from your gear grid for any reason. When you die, archive your <b>Twilight Sword</b> card.',
        'epithet': 'twilight_sword',
        'name': 'Twilight Sword',
        'type': 'curse'
    },
}

severe_injury = {
    'bleeding_kidneys': {
        'desc': 'Gain 2 bleeding tokens.',
        'name': 'Bleeding kidneys',
        'max': False,
        "bleeding_tokens": 2,
    },
    'blind': {
        'Accuracy': -1,
        'desc': 'Lose an eye. Suffer -1 permanent Accuracy. This injury is permanent and can be recorded twice. A survivor with two <b>blind</b> severe injuries suffers -4 permanent accuracy and retires at the end of the next showdown or settlement phase, having lost all sight. Gain 1 bleeding token.',
        'epithet': 'the_blind',
        'max': 2,
        'name': 'Blind',
        "bleeding_tokens": 1,
    },
    'broken_arm': {
        'Accuracy': -1,
        'Strength': -1,
        'desc': 'An ear-shattering crunch. Suffer -1 permanent Accuracy and -1 permanent Strength. This injury is permanent and can be recorded twice. Gain 1 bleeding token.',
        'max': 2,
        'name': 'Broken arm',
        "bleeding_tokens": 1,
    },
    'broken_hip': {
        'Movement': -1,
        'desc': 'Your hip is dislocated. You can no longer <b>dodge</b>. Suffer -1 permanent movement. This injury is permanent and can be recorded once. Gain 1 bleeding token.',
        'name': 'Broken hip',
        'survival_actions': {
            'disable': ['dodge'],
        },
        "bleeding_tokens": 1,
    },
    'broken_leg': {
        'Movement': -1,
        'desc': 'An ear-shattering crunch! Adjacent survivors suffer 1 brain damage. Suffer -1 permanent movement. This injury is permanent, and can be recorded twice. Gain 1 bleeding token.',
        'max': 2,
        'name': 'Broken leg',
        "bleeding_tokens": 1,
    },
    'broken_rib': {
        'Speed': -1,
        'desc': 'It even hurts to breathe. Suffer -1 permanent speed. This injury is permanent, and can be recorded multiple times. Gain 1 bleeding token.',
        'name': 'Broken rib',
        "max": False,
        "bleeding_tokens": 1,
    },
    'bruised_tailbone': {
        'desc': 'The base of your spine is in agony. You cannot <b>dash</b> until showdown ends. You are knocked down. Gain 1 bleeding token.',
        'name': 'Bruised tailbone',
        "max": False,
        "bleeding_tokens": 1,
    },
    'collapsed_lung': {
        'desc': "You can't catch a breath. Gain -1 movement token. Gain 1 bleeding token.",
        'name': 'Collapsed Lung',
        "max": False,
        "attribute_detail": {"Movement": {"tokens": -1}},
        "bleeding_tokens": 1,
    },
    'concussion': {
        'desc': 'Your brain is scrambled like an egg. Gain a random disorder. Gain 1 bleeding token.',
        'name': 'Concussion',
        "max": False,
        "bleeding_tokens": 1,
    },
    'contracture': {
        'Accuracy': -1,
        'desc': 'The arm will never be the same. Suffer -1 permanent Accuracy. This injury is permanent and can be recorded multiple times. Gain 1 bleeding token.',
        'name': 'Contracture',
        "max": False,
        "bleeding_tokens": 1,
    },
    'deaf': {
        'Evasion': -1,
        'desc': 'Suffer -1 permanent Evasion. This injury is permanent and can be recorded once.',
        'name': 'Deaf',
    },
    'destroyed_back': {
        'Movement': -2,
        'desc': 'A sharp cracking noise. Suffer -2 permanent movement. You can no longer activate any gear that has 2+ Strength. This injury is permanent and can be recorded once. Gain 1 bleeding token.',
        'name': 'Destroyed back',
        "bleeding_tokens": 1,
        'cannot_activate_two_plus_str_gear': True,
    },
    'destroyed_genitals': {
        'desc': 'You cannot be nominated for the Intimacy story event. This injury is permanent and can be recorded once. Gain a random disorder. You are knocked down. Gazing upwards, you wonder at the futility of your struggle. Gain +3 insanity. Gain 1 bleeding token.',
        'name': 'Destroyed genitals',
        'cannot_be_nominated_for_intimacy': True,
        "bleeding_tokens": 1,
    },
    'destroyed_tooth': {
        'desc': 'If you have 3+ courage, you boldly spit the tooth out and gain +2 insanity! Otherwise. the blow sends you sprawling and you are knocked down.',
        'name': 'Destroyed tooth',
        'max': False,
    },
    'disemboweled': {
        'desc': 'Your movement is reduced to 1 until the showdown ends. Gain 1 bleeding token. Skip the next hunt. If you suffer <b>disemboweled</b> during a showdown, at least one other survivor must live to the end of the showdown to carry you back to the settlement. Otherwise, at the end of the showdown, you are lost. Dead.',
        'name': 'Disemboweled',
        'skip_next_hunt': True,
        'max': False,
        "bleeding_tokens": 1,
    },
    'dislocated_shoulder': {
        'desc': 'Pop! You cannot activate two-handed or <b>paired</b> weapons or use <b>block</b> until showdown ends. Gain 1 bleeding token.',
        'name': 'Dislocated shoulder',
        'max': False,
        "bleeding_tokens": 1,
    },
    'dismembered_arm': {
        'desc': 'Lose an arm. You can no longer activate two-handed weapons. This injury is permanent, and can be recorded twice. A survivor with two <b>dismembered arm</b> severe injuries cannot activate any weapons. Gain 1 bleeding token.',
        'max': 2,
        'name': 'Dismembered Arm',
        "bleeding_tokens": 1,
        'cannot_activate_two_handed_weapons': True,
    },
    'dismembered_leg': {
        'Movement': -2,
        'desc': 'Lose a leg. You suffer -2 permanent movement, and can no longer <b>dash</b>. This injury is permanent and can be recorded twice. A survivor with two <b>dismembered leg</b> severe injuries has lost both of their legs and must retire at the end of the next showdown or settlement phase. Gain 1 bleeding token.',
        'max': 2,
        'name': 'Dismembered leg',
        'survival_actions': {
            'disable': ['dash'],
        },
        "bleeding_tokens": 1,
    },
    'gaping_chest_wound': {
        'Strength': -1,
        'desc': 'Suffer -1 permanent Strength. This injury is permanent and can be recorded multiple times. Gain 1 bleeding token.',
        'name': 'Gaping chest wound',
        'max': False,
        "bleeding_tokens": 1,
    },
    'hamstrung': {
        'cannot_use_fighting_arts': True,
        'desc': 'A painful rip. The leg is unusable. You can no longer use any fighting arts or abilities. This injury is permanent and can be recorded once. Gain 1 bleeding token.',
        'name': 'Hamstrung',
        "bleeding_tokens": 1,
    },
    'intestinal_prolapse': {
        'desc': 'Your gut is gravely injured. You can no longer equip any gear on your waist, as it is too painful to wear. This injury is permanent, and can be recorded once. Gain 1 bleeding token.',
        'disable_locations': ['Waist'],
        'name': 'Intestinal prolapse',
        "bleeding_tokens": 1,
    },
    "intracranial_hemorrhage": {
        "name": "Intracranial hemorrhage",
        "desc": "You can no longer use or gain any survival. This injury is permanent and can be recorded once. Gain 1 bleeding token.",
        "cannot_gain_survival": True,
        "cannot_spend_survival": True,
        "bleeding_tokens": 1,
    },
    'ruptured_muscle': {
        'cannot_use_fighting_arts': True,
        'desc': 'A painful rip. The arm hangs limp. You can no longer activate fighting arts. This injury is permanent and can be recorded once. Gain 1 bleeding token.',
        'name': 'Ruptured muscle',
        "bleeding_tokens": 1,
    },
    'ruptured_spleen': {
        'desc': 'A vicious body blow. Skip the next hunt. Gain 2 bleeding tokens.',
        'name': 'Ruptured spleen',
        'skip_next_hunt': True,
        'max': False,
        "bleeding_tokens": 2,
    },
    'shattered_jaw': {
        'desc': 'You drink your meat through a straw. You can no longer <b>consume</b> or be affected by events requiring you to <b>consume</b>. You can no longer <b>encourage</b>. This injury is permanent and can be recorded once. Gain 1 bleeding token.',
        'name': 'Shattered jaw',
        'survival_actions': {
            'disable': ['encourage'],
        },
        "bleeding_tokens": 1,
        'cannot_consume': True,
    },
    'slashed_back': {
        'desc': 'Making sudden movement is excruciatingly painful. You cannot <b>surge</b> until showdown ends. Gain 1 bleeding token.',
        'name': 'Slashed back',
        'type': 'severe_injury',
        'max': False,
        "bleeding_tokens": 1,
    },
    'spiral_fracture': {
        'desc': 'Your arm twists unnaturally. Gain -2 strength tokens. Skip the next hunt. Gain 1 bleeding token.',
        'name': 'Spiral fracture',
        'skip_next_hunt': True,
        'max': False,
        "bleeding_tokens": 1,
    },
    'torn_achilles_tendon': {
        'desc': (
            'Your leg cannot bear your weight. Until the end of the showdown, '
            'whenever you suffer light, heavy, or severe injury, you are also '
            'knocked down. Skip the next hunt. Gain 1 bleeding token.'
        ),
        'name': 'Torn Achilles Tendon',
        'skip_next_hunt': True,
        'max': False,
        "bleeding_tokens": 1,
    },
    'torn_muscle': {
        'desc': (
            'Your quadriceps is ripped to shreds. You cannot <b>dash</b> '
            'until he showdown ends. Skip the next hunt. Gain 1 bleeding '
            'token.'
        ),
        'name': 'Torn muscle',
        'skip_next_hunt': True,
        'max': False,
        "bleeding_tokens": 1,
    },
    'warped_pelvis': {
        'max': False,
        'Luck': -1,
        'desc': (
            'Your pelvis is disfigured. Suffer -1 permanent luck. This injury '
            'is permanent and can be recorded multiple times. Gain 1 bleeding '
            'token.'
        ),
        'name': 'Warped Pelvis',
        "bleeding_tokens": 1,
    },


}

expansion_ai = {

    # beta challenge scenarios
    'blue_glow': {
        'desc': '<font class="kdm_font">a</font> Move a Portal terrain tile on the showdown board to Snow\'s space. If there are less than 2 Portals on the board, add one to Snow\'s space instead.',
        'expansion': 'beta_challenge_scenarios',
        'max': 1,
        'name': 'Blue Glow',
        'type': 'ability',
    },
    'green_glow': {
        'desc': '<font class="kdm_font">a</font> Add <font class="inline_shield">1</font> to all hit locations.',
        'expansion': 'beta_challenge_scenarios',
        'max': 1,
        'name': 'Green Glow',
        'type': 'ability'
    },
    'red_glow': {
        'desc': '<font class="kdm_font">a</font> Make a melee attack with speed 3, accuracy 7+, and strength 5.',
        'expansion': 'beta_challenge_scenarios',
        'max': 1,
        'name': 'Red Glow',
        'type': 'ability'
    },
    'solid': {
        'desc': 'If you would be knocked down, roll 1d10. On a 4+, you are not knocked down.',
        'expansion': 'beta_challenge_scenarios',
        'max': 1,
        'name': 'Solid',
        'type': 'ability'
    },
    'twilight_succession': {
        'desc': 'If you die during the showdown and have a Twilight Sword, nominate another survivor on the showdown board to gain the Twilight Sword and this ability.',
        'expansion': 'beta_challenge_scenarios',
        'max': 1,
        'name': 'Twilight Succession',
        'type': 'ability'
    },

    # flower knight
    "sleeping_virus_flower": {
        "name": "Sleeping Virus Flower",
        "expansion": "flower_knight",
        "desc": 'When you die, a flower blooms from your corpse. Add <font class="kdm_font">g</font> <b>A Warm Virus</b> to the timeline next year. You are the guest.',
        "epithet": "host",
        "max": 1,
        "Luck": 1,
    },

    # gorm
    'acid_palms_gorm': {
        'desc': 'Add 1d10 strength to your wound attempts when attacking with Fist & Tooth.',
        'expansion': 'gorm',
        'max': 1,
        'name': 'Acid Palms',
        'type': 'ability'
    },


    # lonely tree
    'nightmare_blood': {
        'desc': 'Whenever you gain a bleeding token, add <font class="inline_shield">1</font> to all hit locations.',
        'expansion': 'lonely_tree',
        'max': 1,
        'name': 'Nightmare Blood',
        'type': 'ability'
    },
    'nightmare_membrane': {
        'desc': 'You may spend <font class="kdm_font">a c</font> to exchange any 1 of your tokens for a +1 strength token.',
        'expansion': 'lonely_tree',
        'max': 1,
        'name': 'Nightmare Membrane',
        'type': 'ability'
    },
    'nightmare_spurs': {
        'desc': 'Once per showdown, you may spend all your survival (at least 1) to lose all your +1 strength tokens and gain that many +1 luck tokens.',
        'expansion': 'lonely_tree',
        'max': 1,
        'name': 'Nightmare Spurs',
        'type': 'ability'
    },
    'super_hair': {
        'desc': (
            'You may spend <font class="kdm_font">a</font> to freely exchange '
            'any tokens with adjacent survivors who have <b>Super Hair</b>.'
        ),
        'expansion': 'lonely_tree',
        'max': 1,
        'name': 'Super Hair',
        'type': 'ability'
    },

    # lion knight
    "hideous_disguise": {
        "name": "Hideous Disguise",
        "expansion": "lion_knight",
        "desc": (
            "At the start of the showdown, if you are fighting the Lion "
            "Knight, choose your Role card."
        ),
        "epithet": "hideous",
        "max": 1,
    },

    # lion god
    'death_mehndi': {
        'desc': (
            'On a <b>Perfect hit</b>, gain 1d10 insanity. -4 to all brain '
            'trauma rolls.'
        ),
        'expansion': 'lion_god',
        'max': 1,
        'name': 'Death Mehndi',
        'type': 'curse'
    },

    # slenderman
    "forgettable": {
        "name": "Forgettable",
        "type": "ability",
        "max": 1,
        "expansion": "slenderman",
        "desc": (
            "Gain +2 permanent evasion. Forgettable survivors cannot be "
            "encouraged."
        ),
        "Evasion": 2,
    },

    # spidicules
    "rivals_scar": {
        "name": "Rival's Scar",
        "type": "ability",
        "expansion": "spidicules",
        "desc":"Gain +1 permanent strength and -1 permanent evasion.",
        "max": 1,
        "epithet": "rivals_scar",
        "Strength": 1,
        "Evasion": -1,
    },

    # sunstalker
    'reflection': {
        'desc': (
            '<ul><li>Your complete affinities and incomplete affinity halves '
            'count as all colors.</li>'
            '<li>You may dodge at any time and as many times as you like '
            'each round.</li>'
            '<li>When you attack from a blind spot, add +1d10 to all wound '
            'attempts for that attack.</li></ul>'
        ),
        'expansion': 'sunstalker',
        'max': 1,
        'name': 'Reflection',
        'type': 'ability'
    },
    'refraction': {
        'desc': (
            '<ul><li>Your complete affinities and incomplete affinity halves '
            'count as all colors.</li><li>During the Showdown, after you '
            'perform a survival action, gain +1 survival.</li></ul>'
        ),
        'expansion': 'sunstalker',
        'max': 1,
        'name': 'Refraction',
        'type': 'ability'
    },

    # vignettes of death: white gigalion
    'gigaslayer': {
        'desc': (
            "Gain +2 strength and +1 luck when attacking a 3x3 or larger "
            "monster. When you participate in <b>Intimacy</b>, newborns with "
            "your surname gain <b>Gigaslayer</b> in addition to any other "
            "benefits."
        ),
        'expansion': 'vignettes_of_death_white_gigalion',
        'max': 1,
        'name': 'Gigaslayer',
        'type': 'ability',
        'inheritable': True,
    },


    # dragon king
    'acid_palms_dk': {
        'desc': (
            'Add 1d10 strength to your wound attempts when attacking with Fist '
            '& Tooth.'
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Acid Palms',
        'type': 'ability'
    },
    'heart_of_the_sword': {
        'desc': (
            'If you gain weapon proficiency during the Aftermath, gain +3 '
            'additional ranks. You cough up a hunk of your own solidified '
            'blood and gain +1 <b>Iron</b> strange resource.'
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Heart of the Sword',
        'type': 'ability'
    },
    'iridescent_hide': {
        'constellation': {'horizontal': 'Absolute', 'vertical': 'Storm'},
        'desc': (
            'Gain +<font class="inline_shield">1</font> to all hit locations '
            'for each different-colored affinity in your gear grid.'
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Iridescent Hide',
        'type': 'ability'
    },
    'limb_maker': {
        'desc': (
            'Once per settlement phase, spend 2 '
            '<font class="kdm_font">d</font> to carve a prosthetic limb. '
            "Remove a survivor's <b>dismembered</b> injury and add 1 bone to "
            "the settlement's storage."
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Limb-maker',
        'type': 'ability',
        'endeavors': ['limb_maker'],
    },
    "oracles_eye": {
        'constellation': {'horizontal': 'Goblin','vertical': 'Witch'},
        'desc': (
            'At the start of the showdown, look through the AI deck then '
            'shuffle.'
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': "Oracle's Eye",
        'type': 'ability'
    },
    'presage': {
        'desc': (
            'Each time you attack, before drawing hit locations, loudly say a '
            'name. You lightly bite the eye in your cheek to see what it sees. '
            'If you draw any hit locations with that name, gain +3 insanity '
            'and +10 strength when attempting to wound them.'
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Presage',
        'type': 'ability'
    },
    'pristine': {
        'constellation': {'horizontal': 'Gambler', 'vertical': 'Reaper'},
        'desc': (
            'When you suffer a <b>dismembered</b> severe injury, ignore it '
            'and gain 1 bleeding token instead.'
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Pristine',
        'type': 'ability'
    },
    'psychovore': {
        'desc': (
            "Once per showdown, you may eat an adjacent survivor's disorder. "
            "If you do, remove the disorder. They gain 1 bleeding token and "
            "you gain +1 permanent strength. At the end of the showdown, if "
            "you haven't eaten a disorder, you die."
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Psychovore',
        'type': 'ability'
    },
    'rooted_to_all': {
        'desc': (
            'If you are standing at the start of your act, reveal the top 2 '
            'cards of the AI deck and put them back in any order.'
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Rooted to All',
        'type': 'ability'
    },
    'twelve_fingers': {
        'desc': (
            'You cannot carry two-handed gear. On a Perfect hit, your right '
            'hand pulses. Gain +5 insanity and +1 luck for the attack. '
            'However, for each natural 1 rolled when attempting to hit, your '
            'left hand shakes. Suffer 5 brain damage and -1 luck for the '
            'attack.'
        ),
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Twelve Fingers',
        'type': 'ability',
        'cannot_activate_two_handed_weapons': True,
    },
    'way_of_the_rust': {
        'desc': 'Your bleeding tokens are also +1 evasion tokens.',
        'expansion': 'dragon_king',
        'max': 1,
        'name': 'Way of the Rust',
        'type': 'ability',
    },

    # white box
    'gender_swap': {
        'desc': (
            'You own the <b>Belt of Gender Swap</b>, it will always take one '
            'space in your gear grid and while it is there, your gender is '
            'reversed.'
        ),
        'epithet': 'gender_swap',
        'expansion': 'promo',
        'max': 1,
        'name': 'Gender Swap',
        'reverse_sex': True,
        'type': 'curse'
    },

    # winter solstice lucy
    'bald': {
        'desc': 'You fidget too much.',
        'name': 'Bald',
    },

}
