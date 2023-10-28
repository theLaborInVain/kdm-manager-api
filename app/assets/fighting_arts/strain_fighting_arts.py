'''

    As of the October 2023 API refactor, Strain FA's live in this module and
    nowhere else.

    The root dictionary here must remain 'strain' in order to avoid having to
    define the FA 'type' variables manually.

'''


strain = {

    #
    # 10th anniversary
    #

    'story_of_blood_1': {
        'name': 'Story of Blood 1',
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


    #
    # echoes of death
    #

    'backstabber': {
        'name': 'Backstabber',
        'expansion': 'echoes_of_death',
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

    #
    # echoes of death 2 - 2019
    #
    'convalescer': {
        'name': 'Convalescer',
        'expansion': 'echoes_of_death_2',
        'strain_milestone': 'surgical_sight',
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
        'desc': (
            "You are impervious behind your shield. IF you have a shield in "
            "your gear grid, ignore the first severe injury you suffer each "
            "showdown.<br/> If you have Shield Specialization, shields in your "
            "gear grid gain <b>Reach 3</b> and +1 strength for each level of "
            "Shield weapon proficiency you have beyond 3."
        ),
    },

    #
    # echoes of death 3 - Black Friday 2020
    #
    'armored_fist': {
        'name': 'Armored Fist',
        'expansion': 'echoes_of_death_3',
        'strain_milestone': 'ashen_claw_strain',
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
