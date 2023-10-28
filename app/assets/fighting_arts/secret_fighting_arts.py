'''

    Important! These get their sub_type set by their module, which we use for
    lots of business logic in the API and the various webapps.

'''


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
        'expansion': 'sunstalker',
        'name': 'Suppressed Shadow',
        'desc': (
            'You no longer cast a shadow and you never hesitate. Ignore First '
            'Strike.<br/>On a <b>Perfect Hit</b>, your first wound attempt of '
            'the attack automatically succeeds and inflicts a critical '
            'wound.<br/>If you die during the showdown, place a Shade minion '
            'in the space you occupied.'
        ),
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

    # badar
    'crescent_step_beta': {
        'beta': True,
        'expansion': 'badar',
        'name': 'Crescent Step',
        'desc': (
            'During your act, when your attack ends, gain '
            '<font class="kdm_font">c</font>.'
            'Limit, once per round.'
        ),
    },

    # elgnirk
    'joyous': {
        'expansion': 'elgnirk_the_chaos_elf',
        'name': 'Joyous',
        'desc': (
            'Whenever you would suffer brain damage, gain that much insanity '
            'instead.</br/>'
            'When you have 100 insanity, you die.'
        ),
    },

}
