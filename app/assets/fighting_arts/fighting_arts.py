fighting_art = {

    #
    #   core fighting arts
    #

    'ambidexterous': {
        'name': 'Ambidexterous',
        'desc': (
            'All melee weapons in your gear grid gain <b>paired</b> '
            '(add the speed of the second weapon when attacking with the '
            'first).<br/> Ambidexterous cannot be used if there are any '
            'shields, two-handed or heavy gear in your gear grid.'
        ),
    },
    'berserker': {
        'desc': (
            'Once per showdown, you may spend <font class="kdm_font">a</font> '
            'to suffer <b>bash</b> and the <b>frenzy</b> brain trauma.'
        ),
        'name': 'Berserker'
    },
    'clutch_fighter': {
        'desc': (
            'While you have 3 or more bleeding tokens, gain +1 strength and +1 '
            'accuracy.'
            ),
        'name': 'Clutch Fighter'
    },
    'combo_master': {
        'desc': 'On a <b>perfect hit</b>, make 1 additional attack roll.',
        'name': 'Combo Master'
    },
    'crazed': {
        'desc': 'On a <b>Perfect hit</b>, gain +1 insanity.',
        'name': 'Crazed'
    },
    'crossarm_block': {
        'desc': 'Whenever you are hit, after hit locations are rolled, you may change 1 result to the arms hit location.',
        'name': 'Crossarm Block'
    },
    'double_dash': {
        'desc': 'During your act, once per round, you may spend <font class="kdm_font">a</font> to gain <font class="kdm_font">c</font>.',
        'name': 'Double Dash'
    },
    'extra_sense': {
        'desc': 'You may <b>dodge</b> 1 additional time per round.',
        'name': 'Extra Sense'
    },
    'last_man_standing': {
        'desc': (
            'While you are the only survivor on the showdown board, you may '
            'not gain bleeding tokens or be knocked down.'
        ),
        'name': 'Last Man Standing',
    },
    'leader': {
        'desc': (
            'Whenever you <b>encourage</b> a survivor, they gain +1 speed '
            'token until the end of the round.<br/>Once per hunt phase, you '
            'may inspire another survivor. They use your understanding and '
            'courage to resolve a hunt or story event. (Example: if you have '
            '3+ courage you can inspire another survivor to walk the path of '
            'the brave during <b>Overwhelming Darkness</b>.)'
        ),
        'name': 'Leader',
    },
    'mighty_strike': {
        'desc': 'On a <b>Perfect hit</b>, gain +2 Strength until the end of the attack.',
        'name': 'Mighty Strike'
    },
    'monster_claw_style': {
        'desc': 'Your <b>Fist & Tooth</b> attacks gain +1 Accuracy, +1 Strength and <b>Savage</b> (after the first critical wound in an attack, savage weapons cause 1 additional wound. This rule does not trigger on Impervious hit locations).',
        'name': 'Monster Claw Style'
    },
    'orator_of_death': {
        'desc': 'Once per showdown, you may spend <font class="kdm_font">a</font> to have all non-deaf survivors gain +2 insanity.<br/>When you die, you <b>encourage</b> all survivors with your last words.',
        'name': 'Orator of Death'
    },
    'rhythm_chaser': {
#        'desc': 'Gain +1 Evasion token the first time you critically wound during a showdown.<br/>Rhythm Chaser cannot be used if there are any shields or <i>heavy</i> gear in your grid.',
        'desc': "On <b>Arrival</b>, gain +1 evasion token. When you are knocked down, if you don't have an instrument in your gear grid, remove all your +1 evasion tokens.<br/>Rhythm Chaser cannot be used if there is any heavy gear in your grid.",
        'name': 'Rhythm Chaser',
    },
    'strategist': {
        'desc': 'During the showdown setup, after placing terrain, you may add a <b>Giant Stone Face</b> or a <b>Toppled Pillar</b> terrain card to the showdown board.',
        'name': 'Strategist'
    },
    'thrill_seeker': {
        'desc': (
            'Whenever you gain survival during the showdown phase, gain 1 '
            'additional survival.'
        ),
        'name': 'Thrill Seeker'
    },
    'timeless_eye': {
        'desc': (
            'Your attack roll is a <b>perfect hit</b> on a result of a 9 or 10.'
            '<br/>You cannot use Timeless Eye if you have the <b>blind</b> '
            'severe head injury.'
        ),
        'name': 'Timeless Eye'
    },
    'tough': {
        'desc': (
            'When rolling on a severe injury table, unless you roll a 1, add '
            '+1 to the result. (This does not include brain trauma. The result '
            'total cannot exceed 10.)'
        ),
        'name': 'Tough'
    },
    'tumble': {
        'desc': (
            "When something would <b>collide</b> with you, roll 1d10. On a "
            "result of 6+, you successfully tumble out of harm's way. Instead, "
            "place your survivor standing on the closest free space outside of "
            "the collision path."
        ),
        'name': 'Tumble'
    },
    'unconscious_fighter': {
        'desc': 'It takes 7 bleeding tokens to kill you.',
        'name': 'Unconscious Fighter',
        '_set_attributes': {
            'max_bleeding_tokens': 7,
        },
    },


    #
    #   expansion fighting arts
    #

    # dragon king
    'acrobatics': {
        'desc': 'When you are adjacent to the monster, you may spend <font class="kdm_font">c</font> to place your survivor on any other space adjacent to the monster.',
        'expansion': 'dragon_king',
        'name': 'Acrobatics'
    },
    "champions_rite": {
        'constellation': {'horizontal': 'Absolute','vertical': 'Reaper'},
        'desc': 'Before making an attack, you may add your understanding to your accuracy attribute for that attack.<br/>Limit, once per showdown.',
        'expansion': 'dragon_king',
        'name': "Champion's Rite"
    },
    'fated_blow': {
        'constellation': {'horizontal': 'Gambler', 'vertical': 'Storm'},
        'desc': 'Once per showdown, you may give your next wound attempt +2 strength and <b>Devastating 1</b>.',
        'expansion': 'dragon_king',
        'name': 'Fated Blow'
    },
    'unbreakable': {
        'constellation': {'horizontal': 'Goblin', 'vertical': 'Rust'},
        'desc': 'Once per lantern year, you may ignore one of your severe injury roll results. If you do, gain a random disorder.',
        'expansion': 'dragon_king',
        'name': 'Unbreakable'
    },


    # DBK
    'carapace_of_will': {
        'desc': (
            'At the start of the showdown, gain the <b>Steadfast</b> survivor '
            'status card.<br/> When you are attacked, if you have 2+ steadfast '
            'tokens, ignore a hit and remove all your steadfast tokens.'
        ),
        'expansion': 'dung_beetle_knight',
        'name': 'Carapace of Will'
    },
    'propulsion_drive': {
        'desc': 'At the start of a showdown, gain the <b>Momentum</b> survivor status card.<br/> When you attack, if you have 5+ momentum tokens, remove them all and roll 1d10. Gain that amount of luck and strength when attempting to wound the first selected hit location for this attack.',
        'expansion': 'dung_beetle_knight',
        'name': 'Propulsion Drive'
    },


    # flower knight
    'otherworldly_luck': {
        'desc': 'During the Hunt and Settlement phase, whenever you roll on a table, you may add +1 to the roll result. This may not exceed the highest possible result of that table.<br/>(This includes Hunt Events, Story Events, Endeavors, Settlement Events, etc.)',
        'expansion': 'flower_knight',
        'name': 'Otherworldly Luck'
    },


    # gorm
    'lure_epilepsy': {
        'desc': 'Once per showdown, you may spend <font class="kdm_font">a</font> to give yourself a seizure. You suffer a random brain trauma and are knocked down.',
        'expansion': 'gorm',
        'name': 'Lure Epilepsy'
    },
    'mammoth_hunting': {
        'desc': "Gain +1 strength when attacking from adjacent spaces outside the monster's facing and blind spot.",
        'expansion': 'gorm',
        'name': 'Mammoth Hunting'
    },


    # lion god
    'burning_focus': {
        'desc': 'If you have 0 survival at the start of your act, gain 1 survival.',
        'expansion': 'lion_god',
        'name': 'Burning Focus'
    },
    'heroic': {
        'desc': 'Once per showdown, if you are standing adjacent to the monster and have 3+ survival, you may spend all of your survival for one automatic hit that inflicts a critical wound.',
        'expansion': 'lion_god',
        'name': 'Heroic'
    },
    'ruthless': {
        'desc': 'Whenever a survivor dies during the showdown, roll 1d10. On a 7+, gain a <b>Skull</b> basic resource.',
        'expansion': 'lion_god',
        'name': 'Ruthless'
    },
    'unrelenting': {
        'desc': 'If all of your attack rolls in an attack miss, you may spend 1 survival to re-roll all attack rolls.',
        'expansion': 'lion_god',
        'name': 'Unrelenting'
    },


    # lion knight
    'headliner': {
        'desc': 'When you become <b>doomed</b> or gain the <b>priority target</b> token, you may choose to gain +1 survival or +1 strength token.',
        'expansion': 'lion_knight',
        'name': 'Headliner'
    },
    'tenacious': {
        'desc': 'When your wound attempt on a hit location is a failure, you may put that hit location back on top of the deck instead of in the discard pile.<br/>Limit, once per round.',
        'expansion': 'lion_knight',
        'name': 'Tenacious'
    },
    'wardrobe_expert': {
        'desc': 'When you suffer a severe injury at a hit location, you may archive a gear worn at that location to ignore it and gain +1 survival.',
        'expansion': 'lion_knight',
        'name': 'Wardrobe Expert'
    },


    # manhunter
    'abyssal_sadist': {
        'desc': 'The first time you wound the monster each attack, gain +1 survival and +1 insanity.<br/>Ignore the effects of the <b>Fear of the Dark</b> and <b>Prey</b> disorders.',
        'epithet': 'sadist',
        'expansion': 'manhunter',
        'name': 'Abyssal Sadist',
    },
    'seasoned_hunter': {
        'desc': 'Whenever a random hunt event result is:<br/>11, 22, 33, 44, 55, 66, 77, 88, 99 or 100,<br/>the event revealer gains +1 understanding and +1 courage.',
        'expansion': 'manhunter',
        'name': 'Seasoned Hunter'
    },
    'trailblazer': {
        'desc': 'The hunting party may start the hunt phase 1 space closer to the monster.<br/>At the start of the showdown, all survivors gain +1 survival and up to +1 insanity.',
        'expansion': 'manhunter',
        'name': 'Trailblazer'
    },
    'transcended_masochist': {
        'desc': 'When you gain a bleeding token, gain +1 survival and +1 insanity.<br/>Ignore the effects of the <b>Aichmophobia</b> and <b>Apathetic</b> disorders.',
        'expansion': 'manhunter',
        'name': 'Transcended Masochist',
        'epithet': 'masochist',
    },

    # slenderman
    'blotted_out': {
        'desc': 'When you suffer a brain trauma, gain a bleeding token.',
        'epithet': 'blotted_out',
        'expansion': 'slenderman',
        'name': 'Blotted Out'
    },
    'phantom_friend': {
        'desc': 'The first time you gain a resource during a showdown, you may feed it to your phantom friend. If you do, archive the resources and gain +1 evasion token.<br/>Lose this token if you are <b>deaf</b> or become <b>deaf</b> during the showdown.',
        'expansion': 'slenderman',
        'name': 'Phantom Friend'
    },

    # spidicules
    'harvestman': {
        'Movement': 3,
        'desc': 'Gain +3 movement. Whenever you are knocked down, gain -1 movement token.<br/>If you have the <b>Tiny Arachnophobia</b> disorder, you are too scared of spiders to imitate them and you cannot use this fighting art.',
        'epithet': 'harvestman',
        'expansion': 'spidicules',
        'name': 'Harvestman',
    },
    'vengeance': {
        'desc': 'When a survivor dies during the showdown, gain +4 survival and +1 strength token.',
        'expansion': 'spidicules',
        'name': 'Vengeance',
        'epithet': 'avenger',
    },

    # sunstalker
    'burning_ambition': {
        'desc': 'When you are instructed to <b>Skip the Next Hunt</b>, ignore it. The "Skip Next Hunt" box on your survivor record sheet cannot be filled in.',
        'expansion': 'sunstalker',
        'name': 'Burning Ambition'
    },
    'defender': {
        'desc': (
            'When a survivor adjacent to you is knocked down, you may spend 1 '
            'survival. If you do, they stand and gain +1 survival from your '
            'words of encouragement.<br/>You cannot use this if you have a '
            '<b>broken jaw</b>.'
        ),
        'expansion': 'sunstalker',
        'name': 'Defender',
        'survival_actions': {
            'enable': ['encourage'],
        },
    },
    'purpose': {
        'desc': 'Your comrades make you strong enough to exceed the limits of death itself.<br/>During the showdown, if you would gain a lethal number of bleeding tokens while there are any other standing survivors, roll 1d10. On a 6+, you live but are knocked down. You will not bleed to death until you gain another bleeding token.',
        'expansion': 'sunstalker',
        'name': 'Purpose'
    },
    'sneak_attack': {
        'desc': 'When you attack a monster from its blind spot, gain +4 strength for that attack.',
        'expansion': 'sunstalker',
        'name': 'Sneak Attack'
    },
    'trick_attack': {
        'name': 'Trick Attack',
        'expansion': 'sunstalker',
        'desc': (
            'Once per showdown, when you wound a monster from its blind spot, '
            'a survivor adjacent to you may gain the <b>priority target</b> '
            'token.'
        ),
    },


    #
    #   Gambler's Chest below!
    #


    # crimson crocodile

    'bloodzerker': {
        'name': 'Bloodzerker',
        'expansion': 'crimson_crocodile',
        'desc': (
            'Gain +1 strength for each of your bleeding tokens.</br>'
            'When you have 3+ bleeding tokens, you lose yourself to the blood '
            'and are <b>guardless</b>!'
        ),
        'related_rules': ['guardless'],
    },
    'glass_mask': {
        'name': 'Glass Mask',
        'expansion': 'crimson_crocodile',
        'desc': (
            'When you <b>depart</b>, you lightly cut your ears, rub blood all '
            'over your face, and wait for it to dry. Gain +3 insanity. <br/>'
            'If you have <b>Face Painting</b>, you create a seal between your '
            'glass mask and your armor. Gain an additional +3 insanity.'
        ),
    },
    'invigorator': {
        'name': 'Invigorator',
        'expansion': 'crimson_crocodile',
        'desc': 'Gain +1 accuracy and +1 speed while you have no insanity.'
    },

}
