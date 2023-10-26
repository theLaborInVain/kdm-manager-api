"""

    All known expansions are defined here.

"""

from datetime import datetime
from app import API
TIMEZONE = API.config['TIMEZONE']

echoes_of_death = {

    # Echoes of Death

    "echoes_of_death": {
        "released": datetime(2018, 7, 1, 12, tzinfo=TIMEZONE), # Gencon 2018
        "name": "Echoes of Death",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "333",
            "bgcolor": "fafafa",
        },
        'strain_milestones': [
            'giants_strain',
            'ethereal_culture_strain',
            'trepanning_strain',
            'opportunist_strain'
        ],
    },

    "echoes_of_death_2": {
        "released": datetime(2019, 8, 1, 12, tzinfo=TIMEZONE), # Gencon 2019
        "name": "Echoes of Death 2",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "333",
            "bgcolor": "fafafa",
        },
        'strain_milestones': [
            'memetic_symphony',
            'marrow_transformation',
            'surgical_sight',
            'hyper_cerebellum',
        ],
    },

    "echoes_of_death_3": {
        "released": datetime(2020, 11, 27, 12, tzinfo=TIMEZONE), # BF2020
        "name": "Echoes of Death 3",
        "ui": {"pretty_category": "Enhancement"},
        "flair": {
            "color": "333",
            "bgcolor": "fafafa",
        },
        'strain_milestones': [
            'ashen_claw_strain',
            'carnage_worms',
            'material_feedback_strain',
            'sweat_stained_oath',
        ],
        'help': [
            {
                'type': 'gear',
                'tip': (
                    'The <b>Twilight Sword</b> cannot be named by survivors '
                    'with the <b>Sword Oath</b> Fighting Art because it does '
                    'not have the <i>sword</i> keyword.'
                ),
            },
        ],
    },

    # echoes four is Gencon 2023
}
