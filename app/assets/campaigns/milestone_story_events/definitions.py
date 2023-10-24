milestone_story_events = {
    "first_child": {
        "sort_order": 0,
        "name": "First child is born",
        "story_event": "Principle: New Life",
        "story_event_handle": "core_new_life",
    },
    "first_death": {
        "sort_order": 1,
        "name": "First time death count is updated",
        "story_event": "Principle: Death",
        "story_event_handle": "core_death",
        "add_to_timeline": 'int(self.settlement["death_count"]) >= 1',
    },
    "pop_15": {
        "sort_order": 2,
        "name": "Population reaches 15",
        "story_event": "Principle: Society",
        "story_event_handle": "core_society",
        "add_to_timeline": 'int(self.settlement["population"]) >= 15',
    },
    "innovations_5": {
        "sort_order": 3,
        "name": "Settlement has 5 innovations",
        "story_event": "Hooded Knight",
        "story_event_handle": "core_hooded_knight",
        "add_to_timeline": 'len(self.settlement["innovations"]) >= 5',
    },
    "innovations_8": {
        "sort_order": 2,
        "name": "Settlement has 8 innovations",
        "story_event": "Edged Tonometry",
        "story_event_handle": "ss_edged_tonometry",
        "add_to_timeline": 'len(self.settlement["innovations"]) >= 8',
    },
    "nemesis_defeat": {
        "sort_order": 6,
        "name": "Not Victorious against Nemesis",
        "story_event_handle": "core_game_over",
        "story_event": "Game Over",
    },
    "game_over": {
        "sort_order": 10,
        "name": "Population reaches 0",
        "story_event": "Game Over",
        "story_event_handle": "core_game_over",
        "add_to_timeline": (
            'int(self.settlement["population"]) == 0 and '
            'int(self.settlement["lantern_year"]) >= 1'
        ),
    },
}
