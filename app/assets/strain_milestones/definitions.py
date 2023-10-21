"""

    Strain Milestone asset definitions live here. The names of the dictionaries
    are for organizational / reference purposes only and, while they should get
    rolled up into the asset definitions as 'sub_type' values, each asset
    needs to have its 'expansion' key set, just as if they were gear, etc.

"""

tenth_anniversary_white_speaker = {
    'plot_twist': {
        'name': 'Plot Twist',
        'expansion': 'tenth_anniversary_white_speaker',
        'milestone_condition': (
            'If the settlement has remembered all the '
            '<font class="kdm_font">g</font> <b>White Secret</b> stories.'
        ),
        'permanent_effect_flavor_text': (
            'A White Speaker arrives with a new story. She cuts the listener. '
            'Cloudy lymphatic fluid struggles from their wound, forming a '
            'yellow disc. Reaching into it, the White Speaker pulls free a '
            'black lump. Add <b>1 Iron</b> strange resource to the settlement '
            'storage. '
        ),
        'permanent_effect': (
            'The next time a survivor would remember a '
            '<font class="kdm_font">g</font> <b>White Secret</b> story, they '
            'recall the words recited under her breath instead. '
            'Permanently add the <b>Story of Blood</b> fighting art to your '
            'fighting art deck. That survivor gains the <b>Story of Blood</b> '
            'fighting art.'
        ),
    },
}

echoes_of_death = {
    "giants_strain": {
        "name": "Giant's Strain",
        "expansion": "echoes_of_death",
        "milestone_condition": (
            "When a survivor with the <b>Marrow Hunger</b> impairment has a "
            'child from <font class="kdm_font">g</font> <b>Intimacy</b>.'
        ),
        'permanent_effect_flavor_text': (
            "Ardent spliters of bone gnaw into the survivor's brain, halting "
            'their pituitary function. The deviation is passed to their '
            'offspring.'
        ),
        'permanent_effect': (
            "Permanently add the <b>Giant's Blood</b> fighting art to your "
            "fighting art deck. The survivor's newborn child gains the "
            "<b>Giant's Blood</b> fighting art (choose one in case of twins)."
        ),
    },
    "ethereal_culture_strain": {
        "name": "Ethereal Culture Strain",
        "expansion": "echoes_of_death",
        "milestone_condition": (
            "When a survivor consumes a <b>Brain Mint</b> gear while there are "
            "4+ <b>Black Lichen</b> strange resources in settlement storage."
        ),
        'permanent_effect_flavor_text': (
            'Black lichen in storage blooms, blanketing the settlement and its '
            'inhabitants with harmless spores. A bacteria carried in the Brain '
            "Mint forms a symbiotic mass of fungus in the unwitting survivor's "
            'brain. The survivor finds themselves communicating with something '
            'beyond.'
        ),
        'permanent_effect': (
            'Permanently add the <b>Ethereal Pact</b> fighting art to your '
            'fighting art deck. The survivor gains the <b>Ethereal Pact</b> '
            'fighting art.'
        ),
    },
    "trepanning_strain": {
        "name": "Trepanning Strain",
        "expansion": "echoes_of_death",
        "milestone_condition": (
            "When a survivor survives the Trepanning Barber Surgeon endeavor "
            "five times."
        ),
        'permanent_effect_flavor_text': (
            "Slipshod surgery has damaged the survivor's memory. When systems "
            'of the body fail, others rise up to compensate. Without the '
            'burden of triumphs and traumas, the indomitable will to live '
            'thrives.'
        ),
        'permanent_effect': (
            'Permanently add the <b>Infinite Lives</b> fighting art to your '
            'fighting art deck. The survivor gains the <b>Infinite Lives</b> '
            'fighting art.'
        ),
    },
    "opportunists_strain":{
        "name": "Opportunist's Strain",
        "expansion": "echoes_of_death",
        "milestone_condition": (
            "When a survivor with the <b>Prey</b> or <b>Secretive</b> disorder "
            "has 15+ insanity."
        ),
        'permanent_effect_flavor_text': (
            'The survivor eats in secret and forgoes sleep. Their extreme '
            'paranoia liberates a deeply buried genetic memory that has '
            'allowed insignificant people to use their prey instincts to '
            'their advantage.'
        ),
        'permanent_effect': (
            'Permanently add the <b>Backstabber</b> fighting art to your '
            'fighting art deck. The survivor gains the <b>Backstabber</b> '
            'fighting art. They suffer permanent -1 strength and -1 evasion '
            'from lack of sleep!'
        ),
    },
}


echoes_of_death_2 = {
    'hyper_cerebellum': {
        'name': "Hyper Cerebellum",
        'expansion': 'echoes_of_death_2',
        'milestone_condition':
            'When two survivors with the <b>Prey</b> disorder have a newborn.',
        'permanent_effect_flavor_text': (
            'The child is born with an enlarged brain capacity for awareness. '
            'Hyper-alert and raised fearful of the unknown, the child takes up '
            'the shield to protect themselves. Their aptitude for observation '
            'gives them skills with a shield no master could ever dream of.'
        ),
        'permanent_effect': (
            'Permanently add the <b>Shieldarang</b> fighting art to your '
            'fighting art deck. The newborn survivor gains the '
            '<b>Shieldarang</b> fighting art, 3 levels of Shield weapon '
            'proficiency, and the <b>Weak Spot</b> disorder at the body '
            'hit location.'
        ),
    },
    'marrow_transformation': {
        'name': "Marrow Transformation",
        'expansion': 'echoes_of_death_2',
        'milestone_condition': (
            'When the Hand removes a <b>broken leg</b> severe injury from a '
            'survivor with Bow weapon specialization.'
        ),
        'permanent_effect_flavor_text': (
            'Knit together according to unfamiliar anatomical principles, the '
            'mended bones grow new configurations of connective tissue. '
            "Developing an unnaturally smooth gait, the survivor's pounding "
            'steps do not impede their aim.'
        ),
        'permanent_effect': (
            'Permanently add the <b>Rolling Gait</b> fighting art to your '
            'fighting art deck. The survivor gains the <b>Rolling Gait</b> '
            'fighting art.'
        ),
    },
    'memetic_symphony': {
        'name': "Memetic Symphony",
        'expansion': 'echoes_of_death_2',
        'milestone_condition': (
            'During <span class="kd deck_icon" deck="SE">SE</span> '
            '<b>Weird Dream</b>, a storyteller tells a Well Told account that '
            "includes a dreaming survivor hearing the Devil's Symphony."
        ),
        'permanent_effect_flavor_text': (
            'Still possessed by restless sleep, snatches of the malefic '
            'tune spread, humming in every mouth. Under the stone-faced '
            'ground, a massive lodestone vibrates sympathetically, '
            'perpetually attracting a rhythmic spree of frozen lightning. '
            'Its thunder echoes in all directions, the beat throbbing in '
            'every ear.'
        ),
        'permanent_effect': (
            'Permanently add the <b>Infernal Rhythm</b> fighting art to your '
            'fighting art deck. The survivora gains the <b>Infernal Rhythm</b> '
            'fighting art.'
        ),
    },
    'surgical_sight': {
        'name': "Surgical Sight",
        'expansion': 'echoes_of_death_2',
        'milestone_condition': (
            'When a survivor in a settlement with Ocular Parasites gains the '
            '<b>Extra Sense</b> fighting art.'
        ),
        'permanent_effect_flavor_text': (
            'Undetectable creatures in the fluid filter of the eyes transform '
            'perception. Skin cannot hide the pulleys and springs of muscle. '
            'Their workings are as plain as the stone-faced groud. The birth '
            'of ocular symbiosis is turbulent.'
        ),
        'permanent_effect': (
            'The survivor suffers the <b>blind</b> severe head injury. '
            'Permanently add the <b>Convalescer<b/> fighting art to your '
            'fighting arts deck. The survivor gains the <b>Convalescer</b> '
            'fighting art.'
        ),
    },
}

echoes_of_death_3 = {
    'ashen_claw_strain': {
        'name': 'Ashen Claw Strain',
        'expansion': 'echoes_of_death_3',
        'milestone_condition': (
            'The survivors are defeated by the Gold Smoke Knight. '
            '(Check for this at the end of your campaign.)'
        ),
        'permanent_effect_flavor_text': (
            'Departing the smouldering scene, the Gold Smoke Knight '
            'unwittingly crushes the claw of a fleeing crab spider. '
            'Desperate to survive, the crab cauterizes its mangled claw on a '
            'nearby golden ember. It heals anew and much larger than before. '
            'The crab shares the secret with its crab family.'
        ),
        'permanent_effect': (
            'Permanently add <span class="kd deck_icon" deck="FA">FA</span> '
            '<b>Armored Fist</b> to your fighting art deck. Permanently add '
            '<span class="kd deck_icon" deck="V">FA</span> <b>Fiddler Crab '
            'Spider</b> to your vermin deck. '
        ),
    },
    'carnage_worm': {
        'name': 'Carnage Worms',
        'expansion': 'echoes_of_death_3',
        'milestone_condition': (
            'A <b>Crazed</b> survivor witnesses a settlement with '
            '<b>Cannibalize</b> endeavor 8 times at <b>Sacrifice</b> in a '
            'single lantern year.'
        ),
        'permanent_effect_flavor_text' : (
            'The survivor holds a feast at the bloodied site of sacrifice. '
            'Attracted to the carnage, a parasitic worm of other origin is '
            "swept up into the survivor's maw. Now a host, the survivor "
            "spreads the parasite's young everywhere they defecate."
        ),
        'permanent_effect': (
            'Permanently add <span class="kd deck_icon" deck="FA">FA</span> '
            '<b>Dark Manifestation</b> to your fighting art deck. The survivor '
            'gains <span class="kd deck_icon" deck="FA">FA</span> <b>Dark '
            'Manifestation </b>.'
        ),
    },
    'material_feedback_strain': {
        'name': 'Material Feedback Strain',
        'expansion': 'echoes_of_death_3',
        'milestone_condition': (
            'A survivor archives 4 resources from their <b>Hoarder</b> '
            'disorder.'
        ),
        'permanent_effect_flavor_text': (
            'A calm wraps around the anxiously beating heart of the survivor, '
            'steadying their grasping hands. The deeply-felt sense of security '
            'keeps cortical stress levels low. Inheriting the positive '
            'chemical feedback between possession and serenity creates a '
            'powerful ally in the settlement stores.'
        ),
        'permanent_effect': (
            'Permanently add <span class="kd deck_icon" deck="FA">FA</span> '
            '<b>Stockist</b> to your fighting art deck. The survivor gains '
            '<span class="kd deck_icon" deck="FA">FA</span> <b>Stockist</b>.'
        ),
    },
    'sweat_stained_oath': {
        'name': 'Sweat Stained Oath',
        'expansion': 'echoes_of_death_3',
        'milestone_condition': (
            'A survivor gains a sword during the hunt or showdown and '
            'uses it to deliver the killing blow that lantern year.'
        ),
        'permanent_effect_flavor_text': (
            'Lightning splits the sky, illuminating a blade-shaped '
            'castle that was not there before. Gouts of water spray '
            "from the castle. Mingling with the survivor's sweat, "
            'the rain hisses. In the sibilant sound, the survivor hears '
            'a challenge.'
        ),
        'permanent_effect': (
            'Permanently add the '
            '<span class="kd deck_icon" deck="FA">FA</span> '
            '<b>Sword Oath</b> to your fighting art deck. The survivor '
            'gains <span class="kd deck_icon" deck="FA">FA</span> '
            '<b>Sword Oath</b>. '
            'Add <span class="kd deck_icon" deck="SE">SE</span> '
            '<b>Acid Rain<b> to the next lantern year on the timeline.'
        )
    },
}


santa_satan = {
    'atmospheric_change': {
        'name': 'Atmospheric Change',
        'expansion': 'santa_satan',
        'milestone_condition': (
            'When the settlement triggers <font class=kdm_font>g</font> '
            '<b>Necrotoxic Mistletoe</b> or <font class=kdm_font>g</font> '
            '<b>Story in the Snow</b>.'
        ),
        'permanent_effect_flavor_text': (
            "The settlement wakes to find itself transformed. An ever-present "
            "chill pimples the survivor's flesh. Occasionally, evanescent "
            "flakes of snow drift through the sky."
        ),
        'permanent_effect': (
            'Archive <b>Heat Wave</b> from the settlement event deck. Add '
            '<b>Lump of Atnas</b> basic resource to the basic resource deck.'
        ),
    },
}

vignettes_of_death_white_gigalion = {
    'somatotropin_surge': {
        'name': 'Somatotropin Surge',
        'expansion': 'vignettes_of_death_white_gigalion',
        'milestone_condition': (
            'The surviors of Deadrock defeat the White Gigalion in the '
            'vignette.'
        ),
        'permanent_effect_flavor_text': (
            "Enraged, the White Gigalion's pregnant mate overtakes the "
            'exhausted survivors, devouring them. Its guts twist audibly '
            'as the peculiar minerals of the lovelorn rock combine with the '
            "primitive concoction that is the survivors' frenzy drink. "
            'The volatile mixture wreaks havoc on the recessive genes of its '
            'unborn young, ensuring the Gigalion aberration continues.'
        ),
        'permanent_effect': (
            'Campaigns with the White Lion quarry may now also hunt the '
            'White Gigalion quarry.'
        ),
    },
}

