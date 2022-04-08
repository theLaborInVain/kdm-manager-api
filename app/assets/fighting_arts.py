fighting_art = {
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
        'desc': 'Once per showdown, you may spend <font class="kdm_font">a</font> to suffer <b>bash</b> and the <b>frenzy</b> brain trauma.',
        'name': 'Berserker'
    },
    'clutch_fighter': {
        'desc': 'While you have 3 or more bleeding tokens, gain +1 strength and +1 accuracy.',
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
        'desc': 'Whenever you <b>encourage</b> a survivor, they gain +1 speed token until the end of the round.<br/>Once per hunt phase, you may inspire another survivor. They use your understanding and courage to resolve a hunt or story event. (Example: if you have 3+ courage you can inspire another survivor to walk the path of the brave during <b>Overwhelming Darkness</b>.)',
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
        'desc': 'Whenever you gain survival during the showdown phase, gain 1 additional survival.',
        'name': 'Thrill Seeker'
    },
    'timeless_eye': {
        'desc': 'Your attack roll is a <b>perfect hit</b> on a result of a 9 or 10.<br/>You cannot use Timeless Eye if you have the <b>blind</b> severe head injury.',
        'name': 'Timeless Eye'
    },
    'tough': {
        'desc': 'When rolling on a severe injury table, unless you roll a 1, add +1 to the result. (This does not include brain trauma. The result total cannot exceed 10.)',
        'name': 'Tough'
    },
    'tumble': {
        'desc': "When something would <b>collide</b> with you, roll 1d10. On a result of 6+, you successfully tumble out of harm's way. Instead, place your survivor standing on the closest free space outside of the collision path.",
        'name': 'Tumble'
    },
    'unconscious_fighter': {
        'desc': 'It takes 7 bleeding tokens to kill you.',
        'name': 'Unconscious Fighter',
        'max_bleeding_tokens': 7,
    },


    #
    #   Expansions!
    #

    # 10th anniversary 

    'story_of_blood_1': {
        'name': 'Story of Blood 1',
        'type': 'strain',
        'strain_milestone': 'plot_twist',
        'desc': (
            'At some point in your life, you learned a miraculous thing! '
            'You cannot recall who taught you or what it was. For a moment, '
            'you see a spectrum of colors in your blood. The first time you '
            'gain a bleeding token during the showdown, gain +1 survival.'
            '<br/><br/>'
            '<b>Observation:</b> When <font class="kdm_font">d</font> is spent '
            'at <b>Bloodletting</b> or <b>Sacrifice</b>, gain +1 '
            '<span class="strain_block"></span>.'
        ),
        'strain_threshold': {
            'blocks': 4,
            'desc': 'Advance <b>Story of Blood 2</b>',
        },
    },
    'story_of_blood_2': {
        'name': 'Story of Blood 2',
        'type': 'strain',
        'strain_milestone': 'plot_twist',
        'desc': (
            'You dream of your skin hardening and turning deep red. '
            'Your own image turns your stomach. Spend '
            '<font class="kdm_font">a</font> to convert a bleeding token '
            'into scab armor. Add <font class="inline_shield">1</font> to any '
            'hit location and suffer 1 brain damage.'
            '<br/><br/>'
            '<b>Observation:</b> When you use this while you have 4+ bleeding '
            'tokens, gain +1 <span class="strain_block"></span>.'
        ),
        'strain_threshold': {
            'blocks': 4,
            'desc': 'Advance <b>Story of Blood 3</b>',
        },
    },
    'story_of_blood_3': {
        'name': 'Story of Blood 3',
        'type': 'strain',
        'strain_milestone': 'plot_twist',
        'desc': (
            'The red creature of your nightmares wears your skin and speaks of '
            'unending torment and eternal life. Spend '
            '<font class="kdm_font">a</font> to convert a bleeding token '
            'into scab armor. Add <font class="inline_shield">1</font> to any '
            'hit location.'
            '<br/><br/>'
            '<b>Observation:</b> When another survivor dies from bleeding '
            'tokens, gain +1 <span class="strain_block"></span>.'
        ),
        'strain_threshold': {
            'blocks': 3,
            'desc': 'Advance <b>Story of Blood 4</b>',
        },
    },
    'story_of_blood_4': {
        'name': 'Story of Blood 4',
        'type': 'strain',
        'strain_milestone': 'plot_twist',
        'desc': (
            "You peel back the monster's skin to reveal a mass of blood with "
            'your likenesss. It hangs in the air briefly before collapsing and '
            'washing the wasteland red. Spend '
            '<font class="kdm_font">a</font> to convert a bleeding token '
            'into scab armor. Add <font class="inline_shield">1</font> to all '
            'hit locations. You may spend your bleeding tokens in place of '
            'survival.'
            '<br/><br/>'
            '<b>Observation:</b> When you use this, gain +1 '
            '<span class="strain_block"></span>.'
        ),
        'strain_threshold': {
            'blocks': 7,
            'desc': (
                'You stress your heart. Roll 1d10. On a 6+, lose 1 '
                '<span class="strain_block"></span>. Otherwise, you have a '
                'heart attack and die.'
            ),
            'final': True,
        },
    },

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
        'desc': 'When a survivor adjacent to you is knocked down, you may spend 1 survival. If you do, they stand and gain +1 survival from your words of encouragement.<br/>You cannot use this if you have a <b>broken jaw</b>.',
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
        'desc': 'Once per showdown, when you wound a monster from its blind spot, a survivor adjacent to you may gain the <b>priority target</b> token.',
        'expansion': 'sunstalker',
        'name': 'Trick Attack'
    },

}


secret_fighting_art = {

    "beast_of_caratosis": {
        'desc': "You may <b>Concentrate</b>. If you do, perform <b>Beast of Caratosis</b> at the start of your next act.<br/><b>Beast of Caratosis:</b> You reach into the dream and disappear in a shimmer of heat.<br/>Place your survivor adjacent to the monster. For this attack, your attack speed is equal to your red affinities, you hit automatically, and you gain strength equal to double your red affinities. Then, gain +6 Hunt XP.",
        'name': "Beast of Caratosis",
    },
    "bone_whisperer": {
        'name': "Bone Whisperer",
        'desc': (
            'When another survivor dies on the showdown board, place a token '
            'where they died. If you pass over it, remove the token and eat '
            'their skull. <b>Heal</b> your survivor and roll 1d10 + your '
            'Hunt XP:<br/>'
            '<table>'
                '<tr class="zebra">'
                '<td class="roll">1-3</td><td class="result">You feel amazing! '
                'Gain +1 permanent movement, speed and evasion.</td></tr>'
                '<tr><td class="roll">4-8</td><td class="result">Gain +1 '
                'permanent strength.</td></tr>'
                '<tr class="zebra"><td class="roll">9-18</td><td '
                'class="result">You gain a fighting art and +5 survival.</td>'
                '</tr><tr><td class="roll">19+</td><td class="result">You run '
                'away into exile. At the end of the showdown, you are gone '
                'forever.</td></tr>'
            '</table>'
        ),
    },
    "lucernaes_lantern": {
        'desc': "You may <b>Concentrate</b>. If you do, perform <b>Lucernae's Lantern</b> at the start of your next act.<br/><b>Lucernae's Lantern:</b> You reach into the dream and excise a screeching skull, darker than darkness. It hurtles at the monster.<br/>Reveal hit locations equal to half your blue affinities (rounded down) one at a time. The mosnter suffers a critical wound at any locations with critical wound effects. (Ignore the effects of trap.) Then reshuffle the hit location deck. Gain +6 Hunt XP.",
        'name': "Lucernae's Lantern",
    },
    "grace_of_dormenatus": {
        'name': "Grace of Dormenatus",
        'desc': "You may <b>Concentrate</b>. If you do, perform <b>Grace of Dormenatus</b> at the start of your next act.<br/><b>Grace of Dormenatus:</b> You reach into the dream and remove a twisting green crown. The crown explodes. A glittering rain of shards coats the survivors.<br/>All survivors gain armor at all hit locations equal to your green affinities. They may remove up to the same number of tokens. Them, gain +6 Hunt XP. If you still exist, gain the priority target token. ",
    },
    "kings_step": {
        'desc': 'Whenever you attack, you may discard any number of Battle Pressure hit locations drawn and draw an equal number of new hit locations. Whenever you attack, after drawing hit locations, but before rolling to wound, you may choose one hit location drawn and discard it to draw a new hit location. Traps will cancel these effects.',
        'name': "King's Step",
    },
    'king_of_a_thousand_battles': {
        'desc': 'Gain +2 Accuracy, +2 Strength, +2 Evasion. You may dodge any number of times in a round. Only 1 survivor may have this Secret Fighting Art.',
        'name': 'King of a Thousand Battles',
    },
    'legendary_lungs': {
        'desc': 'Once per attack, for each successful hit, make an additional attack roll.',
        'name': 'Legendary Lungs',
    },
    'red_fist': {
        'desc': 'At the start of each showdown, each survivor gains +1 Strength token. Survivors may spend +1 Strength tokens in place of survival.',
        'name': 'Red Fist',
    },
    "scholar_of_death": {
        'desc': "On <b>Arrival</b>, gain reroll tokens equal to the number of volumes recorded about your quarry. (e.g. if your settlement has White Lion Volumes 1, 2, and 3 when you fight a White Lion, gain 3 reroll tokens.)<br/>Discard a reroll token to reroll one of your roll results during the showdown. This includes monster roll results when you are the monster controller.",
        'name': "Scholar of Death",
    },
    "swordsmans_promise": {
        'desc': "At the start of each showdown, gain survival up to your settlement's survival limit if you have a sword in your gear grid.",
        'name': "Swordsman's Promise",
    },
    "synchronized_strike": {
        'desc': """With flawless coordination, you strike as one. When <font class="kd_blue_font">you're adjacent</font> to a monster, attack with a melee weapon, and have an <font class="kd_pink_font">Attack Assist</font>, your attack gains +1 Accuracy, +1 Strength. Limit, once per round.<br/><font class="kd_pink_font">Attack Assist:</font> A survivor who also has <b>Synchronized Strike</b> and is in the right spot. They are standing adjacent to the monster, on its opposite side, and parallel to you.""",
        'name': "Synchronized Strike",
    },
    'zero_presence': {
        'desc': 'Gain +1 Strength when attacking a monster from its blind spot. Whenever you attack a monster, you are always considered to be in its blind spot.',
        'name': 'Zero Presence',
    },



    #
    #   Expansion SFAs only past this point!
    #

    # DBK
    'beetle_strength': {
        'desc': 'Once per showdown, you may spend <font class="kdm_font">a</font> to shove an adjacent obstacle terrain. If you do, move the train directly away from you in a straight line until it encounters a board edge or another obstacle terrain. Any monsters the train passes over suffer a wound, and any survivors it <b>collides</b> with suffer <b>knockback 7</b>.<br/>The display of strength is so exhausting it ages you. You are knocked down and gain +1 Hunt XP.',
        'expansion': 'dung_beetle_knight',
        'name': 'Beetle Strength',
    },


    # dragon king
    'altered_destiny': {
        'desc': 'If you would gain a negative attribute token, gain a positive attribute token of that type instead.',
        'expansion': 'dragon_king',
        'name': 'Altered Destiny',
    },
    'frozen_star': {
        'constellation': {'horizontal': 'Absolute', 'vertical': 'Rust'},
        'desc': "Once per round, you may spend 1 survival to freeze a monster's brain. They gain -2 accuracy until the end of the round.<br/>Once per round, you may spend 1 survival to freeze a survivor's brain, killing them instantly. They die.",
        'expansion': 'dragon_king',
        'name': 'Frozen Star',
    },

    # flower knight
    'acanthus_doctor': {
        'desc': (
            'You may wear up to 3 <b>Satchel</b> gear cards.<br/>When you '
            '<b>depart</b>, if you are not wearing any armor, for each '
            '<font id="Dormenatus">&#x02588;</font> you have, gain +1 '
            'strength token and add <font class="inline_shield">1</font> '
            'to all hit locations.<br/>Spend <font class="kdm_font">a</font> '
            'and a Flower or <b>Fresh Acanthus</b> resource to heal a '
            'permanent injury you or an adjacent survivor suffered this '
            'showdown.'
        ),
        'expansion': 'flower_knight',
        'name': 'Acanthus Doctor',
    },
    'fencing': {
        'desc': 'Ignore <b>Parry</b> when attempting to wound hit locations. (Attempt to wound these locations normally.)<br/>When a monster attacks you, roll 1d10. On a 6+, ignore 1 hit. Limit, once per round.',
        'expansion': 'flower_knight',
        'name': 'Fencing',
    },
    'true_blade': {
        'desc': 'All swords in your gear grid gain <b>deadly</b>.<br/>Gain +3 luck when attacking with a sword if you have the <b>Ghostly Beauty</b> and <b>Narcissistic</b> disorders.',
        'expansion': 'flower_knight',
        'name': 'True Blade',
    },


    # gorm
    'immovable_object': {
        'desc': 'If you are on an unoccupied space, you stand firm in the face of any force. You cannot be knocked down and may ignore <b>knockback</b>. (If you occupy the same space as a monster, impassable terrain tile, or another survivor, you are knocked down and suffer <b>knockback</b>.)',
        'expansion': 'gorm',
        'name': 'Immovable Object',
    },


    # lion god
    'necromancer': {
        'desc': 'When you <b>depart</b>, gain <font class="inline_shield">1</font> to all hit locations for each gear card in your grid with the <i>symbol</i> keyword.<br/>If you would roll on the severe injury table, roll on the <b>Worm Trauma</b> table on the other side of this card instead.<br/>When you die or forget this, the settlement gains the <b>Knowledge Worm</b> innovation.',
        'epithet': 'necromancer',
        'expansion': 'lion_god',
        'name': 'Necromancer',
    },


    # lion knight
    'ageless_apprentice': {
        'desc': 'When you gain Hunt XP, you may decide not to gain it.<br/>When you <b>depart</b>, you may rotate up to 3 gear cards in your gear grid. This changes the location of their affinities and arrows. Otherwise, the gear functions normally.',
        'expansion': 'lion_knight',
        'name': 'Ageless Apprentice',
    },
    'courtly_screenwriter': {
        'desc': "At the start of the showdown, secretly write down on a scrap of paper which survivors will live and who will deal the killing blow. During the aftermath, if your predictions were correct, raise the settlement's Survival Limit by 1.",
        'expansion': 'lion_knight',
        'name': 'Courtly Screenwriter',
    },


    # manhunter
    'eternal_will': {
        'desc': 'Gain +1 accuracy and +1 strength for each permanent injury you have.<br/>You may always <b>depart</b>, even when retired.',
        'expansion': 'manhunter',
        'name': 'Eternal Will',
    },


    # slenderman
    'clarity_of_darkness': {
        'desc': 'At the start of the showdown, gain the <b>Path of Gloom</b> survivor status card.<br/>There is a deadly, otherworldly presence about you. Other survivors cannot voluntarily end their movement adjacent to you.',
        'expansion': 'slenderman',
        'name': 'Clarity of Darkness',
    },


    # spid
    'death_touch': {
        'desc': (
            'Gain +1 accuracy when attacking with Fist & Tooth.<br/>When you '
            'wound a monster, it gains -1 toughness until the end of your '
            'attack.<br/>You cannot use this if you are male.'
        ),
        'epithet': 'black_widow',
        'expansion': 'spidicules',
        'name': 'Death Touch',
    },
    'silk_surgeon': {
        'name': 'Silk Surgeon',
        'epithet': 'silk_surgeon',
        'expansion': 'spidicules',
        'desc': '',
        'levels': {
            0: '',
            1: (
                'You may spend <font class="kdm_font">a</font> while adjacent '
                'to another survivor to add <font class="inline_shield">2'
                '</font> to one of their hit locations.'
            ),
            2: (
                'While all armor in your gear grid is silk and all jewelry is '
                'amber, gain +2 evasion.'
            ),
            3: (
                'During the aftermath, roll 1d10 for each other survivor that '
                'died during the showdown. On a 7+, revive them.'
            ),
        },
    },


    # sunstalker
    'hellfire': {
        'desc': 'You cannot lose or remove this fighting art.<br/>Gain +1 strength for each <font id="Caratosis">&#x02588;</font> you have. You cannot be nominated for <b>Intimacy</b>. You ignore <b>Extreme Heat</b>.<br/>At the start of your act, lose 1 survival. At the end of your act, if your survival is 0 or you have any +1 strength tokens, your organs cook themselves and you die.',
        'expansion': 'sunstalker',
        'name': 'Hellfire',
        'epithet': "hellion",
    },
    'sun_eater': {
        'desc': "Your body mysteriously absorbs light. At the start of the showdown, gain survival up to the settlement's Survival Limit.<br/>If you have any +1 strength tokens, you may spend them all to perform the <b>Surge</b> survival action (following all of its normal rules and restrictions).",
        'expansion': 'sunstalker',
        'name': 'Sun Eater',
        'survival_actions': {
            'enable': ['surge'],
        },
    },
    'suppressed_shadow': {
        'desc': 'You no longer cast a shadow and you never hesitate. Ignore First Strike.<br/>On a <b>Perfect Hit</b>, your first wound attempt of the attack automatically succeeds and inflicts a critical wound.<br/>If you die during the showdown, place a Shade minion in the space you occupied.',
        'expansion': 'sunstalker',
        'name': 'Suppressed Shadow',
    },


    # Percival
    'black_guard_style': {
        'desc': (
            'Swords in your gear grid gain <b>Block 1</b>.<br/>When you block '
            'a hit with a sword, your next attack that round with a sword '
            'gains +2 accuracy, +2 strength, +2 speed. Limit, once per '
            'round.<br/> During the settlement phase you may spend '
            '<font class="kdm_font">d</font> to train a survivor. They gain '
            'the <b>Black Guard Style</b> secret fighting art. You lose it '
            'and suffer the <b>broken arm</b> severe injury.'
        ),
        'expansion': 'percival',
        'epithet': 'black_guard',
        'name': 'Black Guard Style',
        'endeavors': ['black_guard_style'],
    },

}


strain_fighting_art = {

    # echoes of death
    'backstabber': {
        'name': 'Backstabber',
        'expansion': 'echoes_of_death',
        'type': 'strain',
        'strain_milestone': 'opportunists_strain',
        'desc': (
            "On a <b>Perfect Hit</b> with a dagger, your first wound attempt "
            "in that attack gains <b>Devastating 1</b>.<br/> When you attack a "
            "monster with a dagger from its blind spot, if you have the "
            "<b>Hoarder</b> or <b>Secretive</b> disorder, increase the range "
            "of your <b>Perfect hits<b> by 1."
        ),
    },
    'ethereal_pact': {
        'name': 'Ethereal Pact',
        'expansion': 'echoes_of_death',
        'strain_milestone': 'ethereal_culture_strain',
        'type': 'strain',
        'desc': (
            "Add +3 to your brain trauma rolls.<br/>When you suffer the "
            "<b>Impossible!</b> brain trauma, the fungus in your head "
            'connects to the dreaming. <font class="kdm_font">g</font> '
            "<b>Birth of a Savior</b> and choose a dream. (If you've already "
            "reached Age 2, you cannot gain your dream's secret fighting "
            "art.)<br/>If you are a Savior, this Fighting Art has no effect."
        ),
        'epithet': 'ethereal',
    },
    'giants_blood': {
        'name': "Giant's Blood",
        'expansion': 'echoes_of_death',
        'strain_milestone': 'giants_strain',
        'type': 'strain',
        'desc': (
            "You overproduce growth hormones! When you gain this "
            "fighting art, gain +1 strength, -1 evasion permanently.<br/> You "
            "may <b>consume</b> skulls. If you do, gain the <b>Marrow "
            "Hunger</b> impairment."
        ),
        'epithet': 'giants_blood',
    },
    'infinite_lives': {
        'name': 'Infinite Lives',
        'expansion': 'echoes_of_death',
        'strain_milestone': 'trepanning_strain',
        'type': 'strain',
        'desc': (
            "You can't create new memories.<br/>You cannot gain new fighting "
            "arts or disorders. When you would gain one, instead gain a new "
            "lifetime! Give yourself a new name and a once per lifetime "
            "reroll. (Gain +1 survival for naming. Gain the reroll regardless "
            "of principle. Only 1 once per lifetime reroll at a time.)"
        ),
    },

    # echoes of death 2 - 2019
    'convalescer': {
        'name': 'Convalescer',
        'expansion': 'echoes_of_death_2',
        'strain_milestone': 'surgical_sight',
        'type': 'strain',
        'desc': (
            "Sympathy and tenderness elevate your care. Whenever you remove "
            "bleeding tokens, gain survival, or add armor points, increase "
            "this benefit by 1.<br/> (e.g., if you use Bandages on another "
            "survivor, they remove up to 3 bleeding tokens.)<br/> "
            "In contrast to your care, your attacks become more crude. They "
            "gain the club keyword."
        ),
    },
    'infernal_rhythm': {
        'name': 'Infernal Rhythm',
        'expansion': 'echoes_of_death_2',
        'strain_milestone': 'memetic_symphony',
        'type': 'strain',
        'desc': (
            'You may spend <font class="kdm_font">a</font> to play an '
            'instrument in your gear grid. Reveal the next 3 monster hit '
            'locations, then put them back in any order.<br/> '
            'Whenever you activate an instrument, gain a lantern token. At '
            "the start of another survivor's act, you may spend 5 lantern "
            'tokens to stir their blood. They gain <font class="kdm_font">'
            'c</font> and <font class="kdm_font">a</font>.'
        ),
    },
    'rolling_gait': {
        'name': 'Rolling Gait',
        'expansion': 'echoes_of_death_2',
        'strain_milestone': 'marrow_transformation',
        'type': 'strain',
        'desc': (
            'Spend <font class="kdm_font">a</font> to notch an arrow. Your '
            "next attack with a bow ignores <b>cumbersome</b>.<br/> At the end "
            "of your attack with a bow or arrow, if you hit the monster from "
            "outside its facing, it gains a <b>flinch token</b>.<br/> "
            "<b>Flinch token:</b> When a monster with a flinch token attempts "
            'to perform <font class="kdm_font">e</font>, cancel'
            '<font class="kdm_font">e</font> and discard this token. '
        ),
    },
    'shielderang': {
        'name': 'Shielderang',
        'expansion': 'echoes_of_death_2',
        'strain_milestone': 'hyper_cerebellum',
        'type': 'strain',
        'desc': (
            "You are impervious behind your shield. IF you have a shield in "
            "your gear grid, ignore the first severe injury you suffer each "
            "showdown.<br/> If you have Shield Specialization, shields in your "
            "gear grid gain <b>Reach 3</b> and +1 strength for each level of "
            "Shield weapon proficiency you have beyond 3."
        ),
    },

    # echoes of death 3 - Black Friday 2020
    'armored_fist': {
        'name': 'Armored Fist',
        'expansion': 'echoes_of_death_3',
        'strain_milestone': 'ashen_claw_strain',
        'type': 'strain',
        'desc': (
            '<b>Requires Fist & Tooth Proficiency.</b><br/>'
            'Your <b>Fist & Tooth</b> attacks gain strength equal to the '
            'current armor value of your arms hit location.'
        ),
    },
    'dark_manifestation': {
        'name': 'Dark Manifestation',
        'expansion': 'echoes_of_death_3',
        'strain_milestone': 'carnage_worms',
        'type': 'strain',
        'desc': (
            'Once per round, at the start of your act, you may spend the '
            'requisite <font class="kd pink_text">insanity</font> to '
            'perform one of the following abilities:'
            '<table>'
                '<tr><td class="roll kd pink_text">3</td><td class="result">'
                'Gain +2 strength until the end of the round.</td></tr>'
                '<tr><td class="roll kd pink_text">6</td><td class="result">'
                'Perform <b>Block 1</b>.</td></tr>'
                '<tr><td class="roll kd pink_text">13</td><td class="result">'
                'If adjacent to the monster, roll 1d10. On a 6+, you touch the'
                'monster, it suffers 1 wound.</td></tr>'
            '</table>'
        ),
    },
    'stockist': {
        'name': 'Stockist',
        'expansion': 'echoes_of_death_3',
        'strain_milestone': 'material_feedback_strain',
        'type': 'strain',
        'desc': (
            'You may <b>Concentrate</b>. If you do, perform <b>Stock Shot</b> '
            'at the start of your next act. <br/>'
            '<b>Stock Shot:</b> Activate a bow in your gear grid and attack '
            "the monster. For this attack, your bow's <b>Range</b> and "
            'strength are equal to the number of resources in the settlement '
            'storage. Limit once per showdown phase.'
        ),
    },
    'sword_oath': {
        'name': 'Sword Oath',
        'expansion': 'echoes_of_death_3',
        'strain_milestone': 'sweat_stained_oath',
        'type': 'strain',
        'desc': (
            'When you gain this, write the name of any sword gear on your '
            'record sheet.  Note each time you wound with the named sword. '
            '<br/> If you have wounded 18+ times with this sword, it gains '
            '<b>Devastating 1</b> and <b>Sentient</b> while you have it '
            'equipped. When you suffer the <b>flee</b> brain trauma, lose '
            'this fighting art.'
        ),
    },
}
