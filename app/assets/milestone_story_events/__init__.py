"""

    This is a pseudo model that initializes only the _milestone_story_events
    dictionary from the campaigns asset dict (/app/assets/campaigns.py).

    This should probably be refactored so that the milestone story events are
    in their own file.

"""

from .._asset import Asset
from .._collection import Collection

from ..campaigns.definitions import _milestone_story_events

class Assets(Collection):

    def __init__(self, *args, **kwargs):
#        self.type_override = "milestone_story_events"
        self.assets = _milestone_story_events
        Collection.__init__(self,  *args, **kwargs)


class Milestone(Asset):

    def __init__(self, *args, **kwargs):
       Asset.__init__(self,  *args, **kwargs)
       self.assets = Assets()
       self.initialize()
