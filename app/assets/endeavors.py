core = {

    # innovations
    'barber_surgeon_trepanning': {
        'name': 'Trepanning',
        'desc': 'roll 1d10.',
        'cost': 1,
    },
    'bed_rest': {
        'name': 'Rest',
        'cost': 1,
    },
    'black_guard_style': {
        'name': 'Black Guard Style',
        'desc': 'During the settlement phase you may spend <font class="kdm_font">d</font> to train a survivor. They gain the <b>Black Guard Style</b> secret fighting art. You lose it and suffer the <b>broken arm</b> severe injury.',
        'cost': 1,
    },
    'bloodletting_breathing_a_vein': {
        'name': 'Breathing a Vein',
        'cost': 1,
    },
    'build_skinnery': {
        'name': 'Build',
        'desc': 'Skinnery',
        'cost': 1,
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'skinnery',
    },
    'build_organ_grinder': {
        'name': 'Build',
        'desc': 'Organ Grinder',
        'cost': 1,
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'organ_grinder',
    },
    'bone_smith_build_weapon_crafter': {
        'name': 'Build',
        'desc': 'Weapon Crafter',
        'cost': 1,
        'cost_detail': ['3 x bone','1 x hide'],
        'cost_detail_type': 'build',
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'weapon_crafter',
    },
    'cooking_default': {
        'name': 'Cooking',
        'desc': '<font class="kdm_font">g</font> <b>Cooking</b>',
        'cost': 1,
    },
    'cooking_stone_nose_gruel': {
        'name': 'Stone Nose Gruel',
        'desc': (
            'Spend 1 organ and 1 bone to cook stone nose gruel. During the '
            'next Hunt phase, ignore <b>Starvation</b>.'
        ),
        'cost': 1,
    },
    'drums_bone_beats': {
        'name': 'Bone Beats',
        'cost': 1,
    },
    'exhausted_lantern_hoard_0_lantern_research': {
        'name': 'Lantern Research',
        'desc': '<font class="kdm_font">g</font> <b>Lantern Research</b>',
        'cost': 2,
        'requires_gear': ['final_lantern'],
    },
    'exhausted_lantern_hoard_1_oxidation': {
        'name': 'Oxidation',
        'desc': '<font class="kdm_font">g</font> <b>Oxidation</b>',
        'cost': 1,
    },
    'exhausted_lantern_hoard_2_survivors_lantern': {
        'name': "Survivor's Lantern",
        'cost': 1,
        'requires_gear': ['final_lantern'],
    },
    'exhausted_lantern_hoard_3_investigate': {
        'name': 'Investigate',
        'desc': 'roll 1d10.',
        'cost': 1,
    },
    'face_painting_battle_paint': {
        'name': 'Battle Paint',
        'cost': 1,
    },
    'face_painting_founders_eye': {
        'name': "Founder's Eye",
        'cost': 1,
    },
    'forbidden_dance_default':{
        'name': "Forbidden Dance",
        'cost': 1,
    },
    'guidepost_default': {
        'name': 'Lantern Halberd',
        'desc': (
            'The survivor attempts to pull the weapon free from the ground. '
            'Roll 1d10 and add their strength. If the result is 12+, gain the '
            '<b>Lantern Halberd</b> rare gear and lose this innovation '
            '(archive this card).'
        ),
        'cost': 1,
    },
    'heart_flute_devils_melody':{
        'name': "Devil's Melody",
        'cost': 1,
    },
    'build_bonesmith': {
        'name': 'Build',
        'desc': 'Bone Smith',
        'cost': 1,
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'bone_smith',
    },
    'innovate': {
        'name': 'Innovate',
        'desc': 'Once per settlement phase, you may spend the listed resources to draw 2 innovation cards. Keep 1 and return the other to the deck.',
        'cost': 1,
        'cost_detail': ['1 x bone','1 x organ', '1 x hide'],
        'cost_detail_type': 'innovate',
        'class': 'available_endeavors_innovate',
    },
    'lantern_hoard_shared_experience': {
        'name': 'Shared Experience',
        'cost': 1,
        'requires_innovations': ['language'],
    },
    'leather_worker_leather_making': {
        'name': 'Leather-Making',
        'desc': 'Spend any number of hide to add an equal number of leather strange resources to the settlement storage.',
        'cost': 1,
        'requires_innovations': ['ammonia'],
    },
    'limb_maker': {
        'expansion': 'dragon_king',
        'name': 'Limb-maker',
        'cost': 2,
        'desc': """Once per settlement phase, spend 2 <font class="kdm_font">d</font> to carve a prosthetic limb. Remove a survivor's <b>dismembered</b> injury and add 1 bone to the settlement's storage.""",
    },
    'mask_maker_0': {
        'name': 'White Lion Mask',
        'desc': 'White Lion Mask. You may hunt the Great Golden Cat.',
        'cost': 1,
    },
    'mask_maker_1': {
        'name': 'Antelope Mask',
        'desc': 'Antelope Mask. You may hunt the Mad Steed.',
        'cost': 1,
    },
    'mask_maker_2': {
        'name': 'Phoenix Mask',
        'desc': 'Phoenix Mask. You may hunt the Golden Eyed King.',
        'cost': 1,
    },
    'matchmaker_trigger_intimacy': {
        'name': 'Matchmaker',
        'desc': 'Spend 1 endeavor to trigger <font class="kdm_font">g</font> <b>Intimacy</b>.',
        'requires_returning_survivor': True,
        'cost': 1,
    },
    'momento_mori_default': {
        'name': 'Momento Mori',
        'desc': (
            'Nominate a survivor that died in the last showdown and roll id10.'
        ),
        'cost': 1,
    },
    'nightmare_training_train': {
        'name': "Train",
        'desc': 'Lose 3 survival and roll 1d10.',
        'cost': 1,
    },
    'organ_grinder_stone_noses':{
        'name': 'Stone Noses',
        'cost': 1,
    },
    'organ_grinder_augury': {
        'name': 'Augury',
        'desc': 'roll 1d10. The survivor endeavors to glean the meaning of existence. Roll on the table. Add +1 to your roll result if your understanding is 3 or higher.',
        'cost': 1,
    },
    'organ_grinder_build_stone_circle': {
        'name': 'Build',
        'desc': 'Stone Circle',
        'cost': 1,
        'cost_detail': ['3 x organ','3 x hide'],
        'cost_detail_type': 'build',
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'stone_circle',
    },
    'partnership_default': {
        'name': 'Partnership',
        'desc': (
            'Nominate two survivors. They pair off, and each gains the '
            '<b>Partner</b> ability. A survivor may be nominated for '
            'Partnership once per lifetime.'
        ),
        'cost': 2,
    },
    'pottery_fermentation': {
        'name': 'Fermentation',
        'desc': 'Spend 1 organ resource and gain 1 <b>Love Juice</b> basic resource. Limit, once per lantern year.',
        'cost': 1,
    },
    'pottery_ret': {
        'name': 'Ret',
        'desc': 'Spend 1 herb resource and gain 1 hide basic resource. Limit, once per lantern year.',
        'cost': 1,
    },
    'records_0_scholar_of_death': {
        'name': 'Scholar of Death',
        'desc': "You gain the <b>Scholar of Death</b> secret fighting art.",
        'cost': 1,
    },
    'records_1_monster_volume': {
        'name': 'Moster Volume',
        'desc': (
            'You laboriously create a volume about a monster you have '
            'defeated during your lifetime. Add "Monster Name" Vol. X '
            'where X is the level of the defeated monster to the Settlement '
            'Record Sheet. The work is exhausting, you retire. There can be '
            'up to 3 volumes for each monster.'
        ),
        'cost': 1,
    },
    'sacrifice_death_ritual': {
        'name': 'Death Ritual',
        'cost': 1,
    },
    'scarification_initiation': {
        'name': "Initiation",
        'desc': 'Once per lifetime, gain +1 courage and roll the hit location die.',
        'cost': 1,
    },
    'scrap_smelting_purification': {
        'name': 'Purification',
        'cost': 1
    },
    'scrap_smelting_build_blacksmith': {
        'name': 'Build',
        'desc': 'Blacksmith',
        'cost': 1,
        'cost_detail': ['6 x bone','3 x scrap'],
        'cost_detail_type': 'build',
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'blacksmith',
    },
    'sculpture_0': {
        'name': 'Inspirational Statue',
        'desc': (
            'You create an Inspirational Statue. Skip the next hunt and lose '
            'a fighting art. Record this fighting art on the Settlement '
            'Record Sheet. A settlement can only have one Inspirational '
            'Statue. (You cannot make another! Secret fighting arts are not '
            'fighting arts!)'
        ),
        'cost': 1,
        'hide_if_settlement_attribute_exists': 'inspirational_statue',
    },
    'sculpture_1': {
        'name': 'Study the Inspirational Statue',
        'desc': (
            'You study the inspirational statue. Roll 1d10. On a 6+, '
            'gain the recorded fighting art.'
        ),
        'cost': 1,
    },
    'shrine_armor_ritual': {
        'name': 'Armor Ritual',
        'desc': 'May be used once per settlement phase.',
        'cost': 1,
    },
    'skinnery_build_leather_worker': {
        'name': 'Build',
        'desc': 'Leather Worker',
        'cost': 1,
        'cost_detail': ['3 x hide','1 x organ'],
        'cost_detail_type': 'build',
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'leather_worker',
    },
    'stone_circle_harvest_ritual': {
        'name': 'Harvest Ritual',
        'desc': "Spend any number of monster esources to draw an equal number of basic resources.",
        'cost': 1,
        'requires_innovations': ['forbidden_dance'],
    },
    'storytelling_story_time': {
        'name': "Story Time",
        'cost': 1,
    },
    'weapon_crafter_innovate_scrap_smelting': {
        'name': 'Special Innovate',
        'desc': 'Scrap Smelting',
        'cost': 1,
        'cost_detail': ['2 x scrap', '5 x bone', '5 x organ'],
        'cost_detail_type': 'innovate',
        'class': 'available_endeavors_innovate',
        'hide_if_innovation_exists': 'scrap_smelting',
    },
    'weapon_crafter_scrap_scavenge': {
        'name': 'Scrap Scavenge',
        'desc': 'roll 1d10',
        'cost': 1,
    },
}

lingering_effects = {
    'acid_storm_distillation': {
        'name': 'Acid Storm Distillation',
        'cost': 1,
        'desc': 'roll 1d10',
        'requires_innovations': ['cooking'],
    },
    'acid_storm_exercise': {
        'name': 'Acid Storm Exercise',
        'cost': 1,
        'desc': 'roll 1d10',
        'requires_innovations': ['nightmare_training'],
    },
    'automatic_writing': {
        'name': 'Automatic Writing',
        'cost': 1,
        'desc': 'roll 1d10',
        'requires_innovations': ['pictograph'],
    },
    'brave_the_maw': {
        'name': 'Brave the Maw',
        'cost': 1,
    },
    'breathe_fumes': {
        'name': 'Breathe Fumes',
        'cost': 1,
    },
    'deep_listen': {
        'name': 'Deep Listen',
        'cost': 1,
        'desc': 'Spend 2 resources',
    },
    'duel': {
        'name': 'Duel',
        'cost': 2,
    },
    'find_fluid': {
        'name': 'Find Fluid',
        'cost': 1,
    },
    'lights_in_the_sky_01': {
        'name': 'Lights in the Sky: Graves',
        'cost': 1,
        'desc': 'Once per settlement phase',
        'requires_innovations': ['graves'],
    },
    'lights_in_the_sky_02': {
        'name': 'Lights in the Sky: Face Painting',
        'cost': 1,
        'desc': 'Once per settlement phase',
        'requires_innovations': ['face_painting'],
    },
    'lights_in_the_sky_03': {
        'name': 'Lights in the Sky: Inner Lantern',
        'cost': 1,
        'desc': 'Once per settlement phase',
        'requires_innovations': ['inner_lantern'],
    },
    'rename': {
        'name': 'Rename',
        'cost': 1,
        'desc': 'Spend 1 organ, roll id10',
        'requires_innovations': ['pictograph'],
    },
    'silk_diet': {
        'name': 'Silk Diet',
        'cost': 1,
    },
    'talk_to_legless_ball': {
        'name': 'Talk to Legless Ball',
        'cost': 1,
        'requires_innovations': ['legless_ball'],
    },
    'treatment': {
        'name': 'Treatment',
        'cost': 1,
        'requires_innovations': ['ammonia'],
    },
    'vapor_scar': {
        'name': 'Vapor Scar',
        'cost': 1,
        'requires_innovations': ['scarification'],
    },
    'vapor_visions': {
        'name': 'Vapor Visions',
        'cost': 1,
        'requires_innovations': ['shrine'],
    },
}

campaigns = {
    'potskull_skull_ritual': {
        'name': "Skull Ritual",
        "cost": 1,
        "desc": "Cost: 1 skull resource, 1 endeavor. Nominate up to four survivors to consume the skull. They gain a permanent +1 to all their attributes.",
    },
    'bloom_people_forest_run': {
        'name': 'Forest Run',
        'cost': 1,
        'desc': "You may exchange any number of monster resources for that number of random Flower resources.",
    },
}

expansions = {
    'arena_spar': {
        'name': 'Spar',
        'desc': 'Spend 1 iron and roll 1d10.',
        'cost': 1,
    },
    'aquarobics_underwater_train': {
        'name': 'Underwater Train',
        'cost': 1,
    },
    'choreia_spider_dance': {
        'name': 'Spider Dance',
        'desc': (
            'Spider Dance. Nominate a male and a female survivor and roll '
            '1d10.'
        ),
        'cost': 2,
    },
    'crimson_candy_crimson_cannibalism': {
        'name': 'Crimson Cannibalism',
        'cost': 1,
    },
    'dark_water_research_0': {
        'name': 'Light Forging',
        'desc': '<font class="kdm_font">g</font> <b>Light Forging</b>.',
        'cost': 1,
    },
    'dark_water_research_1': {
        'name': 'Dark Water Research',
        'desc': (
            'Spend 2x resources and 2x Dark Water to increase the level of '
            '<b>Dark Water Research</b> by 1, to a maximum of 3. (Update '
            'your settlement record sheet.)'
        ),
        'cost': 1,
    },
    'dbk_horn_ceremony': {
        'name': 'Horn Ceremony',
        'desc': 'Archive and roll 1d10.',
        'cost': 1,
        'requires_innovations': ['scarification'],
    },
    'fear_and_trembling': {
        'name': 'Fear and Trembling',
        'desc': 'Once per settlement phase, a survivor may spend <font class="kdm_font">d</font> to approach the throne and roll 1d10.',
        'cost': 1,
    },
    'filleting_table_advanced_cutting': {
        'name': 'Advanced Cutting',
        'cost': 1,
    },
    'gorm_albedo': {
        'name': 'Albedo',
        'desc': 'Once this lantern year, roll 1d10',
        'cost': 2,
    },
    'gorm_citrinitas': {
        'name': 'Citrinitas',
        'desc': 'Once this lantern year, roll 1d10',
        'cost': 3,
    },
    'gorm_nigredo': {
        'name': 'Nigredo',
        'desc': 'Once this lantern year, roll 1d10',
        'cost': 1,
    },
    'gorm_rubedo': {
        'name': 'Rubedo',
        'desc': 'Once this lantern year, roll 1d10',
        'cost': 4,
    },
    'gormchymist_special_innovate': {
        'name': 'Special Innovate',
        'desc': 'Gain the next Gormchymy innovation.',
        'cost': 1,
        'cost_detail': ['1 x strange resource','1 x gorm brain'],
        'cost_detail_type': 'innovate',
        'class': 'available_endeavors_innovate',
        'hide_if_innovation_exists': 'gorm_rubedo',
    },
    'legless_ball_0': {
        'name': 'Legless Ball',
        'desc': 'Add 1 <b>Web Silk</b> strange resource to settlement storage.',
        'cost': 1,
    },
    'legless_ball_1': {
        'name': 'Legless Ball',
        'desc': (
            'A survivor with 10+ insanity may put the Spidicules out of its '
            'misery. Gain the <b>Grinning Visage</b> rare gear and lose this '
            'innovation. (Archive this card.)'
        ),
        'cost': 1,
    },
    'lion_knight_0_visit_the_retinue': {
        'name': 'Visit the retinue',
        'desc': (
            'Visit the retinue. <font class="kdm_font">g</font> <b>Strange '
            'Caravan</b>'
        ),
        'cost': 1,
    },
    'lion_knight_black_mask_face_the_monster': {
        'name': 'Face the Monster',
        'desc': '<b>Face the Monster.</b> Roll 1d10.',
        'cost': 2,
    },
    'lion_knight_white_mask_leave_the_monster': {
        'name': 'Leave the monster an offering',
        'desc': (
            '<b>Leave the monster an offering.</b> Spend 1 resource and '
            'roll 1d10.'
        ),
        'cost': 1,
    },
    'petal_spiral_trace_petals': {
        'name': 'Trace Petals',
        'cost': 1,
    },
    'round_stone_training_train': {
        'name': 'Train',
        'desc': 'Spend 1 resource and roll 1d10',
        'cost': 1,
    },
    'sacred_pool_0':{
        'name': 'Sacred Water',
        'desc': 'Once per settlement phase, the settlement drinks the oil that builds up on the surface of the pool. <font class="kdm_font">g</font> <b>Intimacy</b>.', 
        'cost': 1,
    },
    'sacred_pool_1':{
        'name': 'Purification Ceremony',
        'desc': 'You may endeavor here once per lifetime. Your body is infused with sacred water and <b>Purified</b> (record this). You cannot <b>depart</b> this year. Gain the <b>Protective</b> disorder and roll 1d10. On 8+ gain +1 permanent attribute of your choice. Otherwise, gain +1 permanent strength or accuracy.',
        'cost': 2,
    },
    'sacred_pool_2':{
        'name': 'Sun Sealing',
        'desc': 'You sit for a year, in the boiling darkness of the Shrine. Gain the <b>Hellfire</b> secret fighting art. You cannot <b>depart</b> this year.',
        'cost': 1,
        'requires_innovations': ['sauna_shrine'],
    },
    'sauna_shrine_tribute': {
        'name': 'Tribute',
        'desc': 'Spend 1 organ and roll 1d10.',
        'cost': 1,
    },
    'settlement_watch_new_recruits': {
        'name': 'New Recruits',
        'cost': 1,
    },
    'serrated_fangs_razor_pushups': {
        'name': 'Razor Push-ups',
        'expansion': 'spidicules',
        'cost': 1,
    },
    'shadow_dancing_final_dance': {
        'name': 'Final Dance',
        'desc': (
            'You may only endeavor here if a survivor died during the last '
            'hunt or showdown. Once per year, roll 1d10.'
        ),
        'cost': 1,
    },
    'silk_refining_0': {
        'name': 'Silk Surgery',
        'desc': '<font class="kdm_font">g</font> <b>Silk Surgery</b>.',
        'cost': 1,
    },
    'silk_refining_1': {
        'name': 'Silk Refining',
        'desc': 'Convert 1 silk resource in 1 hide basic resource.',
        'cost': 1,
    },
    'silk_refining_2': {
        'name': 'Build',
        'desc': 'Spend 2 silk, 1 bone, and 1 organ to build the <b>Silk Mill</b> settlement location.',
        'cost': 1,
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'silk_mill',
    },
    'stoic_statue_worship_the_monster': {
        'name': 'Worship the monster',
        'desc': '<b>Worship the monster.</b> You may not <b>depart</b> or endeavor again this settlement phase. Roll 1d10.',
        'cost': 1,
    },
    'subterranean_agriculture_0': {
        'name': 'Underground Sow',
        'desc': (
            'If <b>Black Harvest</b> is not on the timeline, '
            '<font class="kdm_font">g</font> <b>Underground Sow</b>.'
        ),
        'cost': 1,
    },
    'subterranean_agriculture_1': {
        'name': 'Preserved Caustic Dung',
        'desc': (
            'If <b>Black Harvest</b> is on the timeline you may spend 1 '
            'Preserved Caustic Dung to increase its rank by 1 to a maximum '
            'rank of 3. Limit, once per settlement phase.'
        ),
        'cost': 1,
    },
    'subterranean_agriculture_2_build_wet_resin_crafter': {
        'name': 'Build',
        'desc': 'Wet Resin Crafter (2 x organ, 2 x bone)',
        'cost': 1,
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'wet_resin_crafter',
    },
    'umbilical_bank_umbilical_symbiosis':{
        'name': 'Umbilical Symbiosis',
        'desc': '<font class="kdm_font">g</font> <b>Umbilical Symbiosis</b>.',
        'cost': 1,
    },
    'umbilical_bank_special_innovate_pottery':{
        'name': 'Special Innovate',
        'desc': 'Pottery',
        'cost': 1,
        'cost_detail': ['3 x organ'],
        'cost_detail_type': 'innovate',
        'class': 'available_endeavors_innovate',
        'hide_if_innovation_exists': 'pottery',
    },
    'war_room_default': {
        'name': 'Make a plan',
        'desc': (
            'The hunt team makes a plan. The group may reroll 1 <b>Hunt Event '
            'Table</b> result (d100) this lantern year. They must reroll '
            'before performing the event.'
        ),
        'cost': 1,
    },
}
