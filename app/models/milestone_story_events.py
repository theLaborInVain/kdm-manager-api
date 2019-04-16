"""

    This is a pseudo model that initializes only the _milestone_story_events
    dictionary from the campaigns asset dict (/app/assets/campaigns.py).

    This should probably be refactored so that the milestone story events are
    in their own file.

"""

from app.assets import campaigns
from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.type_override = "milestone_story_events"
        self.assets = campaigns._milestone_story_events
        models.AssetCollection.__init__(self,  *args, **kwargs)


class Milestone(models.GameAsset):

    def __init__(self, *args, **kwargs):
       models.GameAsset.__init__(self,  *args, **kwargs)
       self.assets = Assets()
       self.initialize()
