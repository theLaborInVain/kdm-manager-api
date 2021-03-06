kdm_manager = {
    "beta": {
        "type": "General",
        "desc": "Enable Beta (&beta;) features of the Manager?",
        "name": "Enable Beta (&beta;) features of the Manager?",
        "affirmative": "Enable",
        "negative": "Disable",
        "patron_level": 2,
    },
    "preserve_sessions": {
        "type": "General",
        "desc": "Preserve Sessions?",
        "name": "Preserve Sessions?",
        "affirmative": "Keep me logged in",
        "negative": "Remove sessions after 24 hours",
        "patron_level": 1,
    },

    "random_names_for_unnamed_assets": {
        "type": "New Asset Creation",
        "desc": "Let the Manager choose random names for Settlements/Survivors without names?",
        "name": "Let the Manager choose random names for Settlements/Survivors without names?",
        "affirmative": "Choose randomly",
        "negative": "Use 'Unknown' and 'Anonymous'",
        "patron_level": 0,
    },
    "apply_new_survivor_buffs": {
        "type": "New Survivor Creation",
        "desc": "Automatically apply settlement bonuses to new, newborn and current survivors where appropriate?",
        "name": "Automatically apply settlement bonuses to new, newborn and current survivors where appropriate?",
        "affirmative": "Automatically apply",
        "negative": "Do not apply",
        "patron_level": 0,
    },
    "apply_weapon_specialization": {
        "type": "New Survivor Creation",
        "desc": "Automatically add weapon specialization ability to living survivors if settlement Innovations list includes that weapon mastery?",
        "name": "Automatically add weapon specialization ability to living survivors if settlement Innovations list includes that weapon mastery?",
        "affirmative": "Add",
        "negative": "Do Not Add",
        "patron_level": 0,
    },
    "show_endeavor_token_controls": {
        "type": "Interface - Campaign Summary",
        "desc": "Show Endeavor Token controls on Campaign Summary view?",
        "name": "Show Endeavor Token controls on Campaign Summary view?",
        "affirmative": "Show controls",
        "negative": "Hide controls",
        "patron_level": 0,
    },
    "show_epithet_controls": {
        "type": "Interface - Survivor Sheet",
        "desc": "Use survivor epithets (tags)?",
        "name": "Use survivor epithets (tags)?",
        "affirmative": "Show controls on Survivor Sheets",
        "negative": "Hide controls and tags on Survivor Sheets",
        "patron_level": 0,
    },

    # Interface
    "night_mode": {
        "type": "Interface",
        "desc": "UI Color Theme:",
        "name": "UI Color Theme:",
        "affirmative": "Dead Guardian (high contrast)",
        "negative": "Glowing Center (default)",
        "patron_level": 2,
    },
    "show_remove_button": {
        "type": "Interface",
        "desc": "Show controls for removing Settlements and Survivors?",
        "name": "Show controls for removing Settlements and Survivors?",
        "affirmative": "Show the Delete button",
        "negative": "Hide the Delete button",
        "patron_level": 0,
    },
    "show_ui_tips": {
        "type": "Interface",
        "desc": "Display in-line help and user interface tips?",
        "name": "Display in-line help and user interface tips?",
        "affirmative": "Show UI tips",
        "negative": "Hide UI tips",
        "patron_level": 2,
    },
    "show_dashboard_alerts": {
        "type": "Interface",
        "desc": "Display webapp alerts on the Dashboard?",
        "name": "Display webapp alerts on the Dashboard?",
        "affirmative": "Show alerts",
        "negative": "Hide alerts",
        "patron_level": 2,
    },
}
