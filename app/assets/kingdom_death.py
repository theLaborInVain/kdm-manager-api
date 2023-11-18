'''

    The magic module. Import * from it and inject all assets into a namespace.

    Do NOT do anything other that imports in this file.

'''

# game assets
from . import (
    abilities_and_impairments,
    campaigns,
    cursed_items,
    disorders,
    endeavors,
    events,
    expansions,
    fighting_arts,
    gear,
    innovations,
    locations,
    monsters,
    names,
    principles,
    resources,
    rules,
    saviors,
    settlements,
    strain_milestones,
    survival_actions,
    survivors,              # these are prefab/vignette survivors
    tags,
    the_constellations,
    versions,
)

# survivor sheet pseudo assets
from .survivors import causes_of_death
from .survivors import color_schemes
from .survivors import once_per_lifetime
from .survivors import special_attributes
from .survivors import status_flags
from .survivors import weapon_proficiency

# settlement sheet pseudo assets
from .settlements import macros
from .settlements import pulse_discoveries
from .settlements import storage
from .campaigns import milestone_story_events
