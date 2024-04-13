white_box = {

    # promo
    'female_only': {
        'expansion': 'promo',
        'name': 'Female Only',
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
            'proficiency.<br/>'
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
            'Sealed gear has a bonus effect that can only be earned by '
            'training. '
            'A survivor can unseal the gear by declaring it as their weapon '
            'proficiency, forsaking the normal bonuses of selecting a weapon '
            'type. When the survivor reaches the specialization rank, they '
            'earn the effect listed after the gear card.<br/>'
            "A survivor can only earn a gear's <b>Sealed</b> bonus once per "
            'lifetime.<br/>'
            'For example, the <b>Toxicimitar</b> has "<b>Sealed</b> - Gain the '
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
    },

    # novice
    'novice': {
        'expansion': 'novice',
        'name': 'Novice',
        'type': 'special_rule',
        'desc': 'A survivor with 1 or less Hunt XP.',
    },

    #hellebore
    'insulated': {
        'expansion': 'hellebore',
        'name': 'Insulated',
        'type': 'special_rule',
        'desc': (
            'A survivor is insulated if they have 6 or more gear cards '
            'that grant them armor points.'
        ),
    },
    'melting_x': {
        'expansion': 'hellebore',
        'name': 'Melting X',
        'type': 'special_gear_rule',
        'desc': (
            'A gear special rule. On <b>Arrival</b>, place X +1 strength '
            'tokens on this gear. At the end of your act, remove +1 '
            'strength token from this gear.'
        ),
    },

    # death crown inheritor aya
    'campaign_limit_x': {
        'expansion': 'death_crown_inheritor_aya',
        'name': 'Campaign Limit X',
        'type': 'gear_special_rule',
        'desc': (
            'This gear may only be activated X times '
            'per campaign. Track this on your settlement record sheet. '
        ),
    },

    # Vitanvox
    'banshee_dura_x':{
        'expansion': 'vitanvox',
        'name': 'Banshee Dura X',
        'type': 'gear_special_rule',
        'desc': (
            'At the start of your act, gain (or lose) howling tokens until '
            'you have X of them. During your act or a survival opportunity, '
            'you may spend one howling token to: <ul>'
            '<li>Gain <font class="kdm_manager_font">M</font>, which must be '
            'spent immediately. Limit once per round.</li>'
            '<li>Gain <font class="kdm_manager_font">A</font>, which must be '
            'spent immediattely. Limit once per round.</li>'
            '<li>Perform a survival action, using the howling token in place '
            'of survival.</li>'
            '<li>Gain +1 strength token until the end of the round.</li>'
            '</ul>'
        ),
    },

    # gnostin
    'demolish': {
        'expansion': 'gnostin_stonesmasher',
        'name': 'Demolish',
        'type': 'gear_special_rule',
        'desc': (
            'Spend <font class="kdm_manager_font">A</font> to archive an '
            'adjacent <b>Impassable</b> terrain tile. If a monster is standing '
            'on that terrain when its archived, the monster is knocked down.'
        ),
    },


    # gunborg
    'bloodeater': {
        'expansion': 'gunborg',
        'name': 'Bloodeater',
        'type': 'gear_special_rule',
        'desc': (
            'If you are adjacent to another survivor, you may spent '
            '<font class="kdm_manager_font">A</font> to kill them. '
            'Transfer their bleeding tokens to you and it takes an '
            'additional 5 bleeding tokens to kill you this showdown.'
        ),
    },


    # lolowen
    'rush': {
        'expansion': 'lolowen',
        'name': 'Rush',
        'desc': (
            'When a survivor hits 3+ times in a single attack, they Rush for '
            'that attack.'
        ),
    },
#    'surpass_x': {
#        'expansion': 'lolowen',
#        'name': 'Surpass X',
#        'type': 'gear_special_rule',
#        'desc': (
#            "When a survivor's wound attempt total surpasses the monster's "
#            'toughness by X or more, the monster suffers an additional wound.'
#        ),
#    },

    # mist - raikin armor
    'charged_token': {
        'expansion': 'mist_raikin_armor',
        'name': 'Charged token',
        'type': 'gear_special_rule',
        'desc': (
            'If you have a Charged token at the end of your attack with a '
            'metal weapon, if you hit the monster, it is shocked and suffers '
            'an automatic wound. <br/> Archive all Charged tokens at the end '
            'of each round.'
        ),
    },

}
