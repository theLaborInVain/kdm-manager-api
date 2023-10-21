'''

    The old import for this was:
        from app.assets.survivors import weapon_proficiency

'''

from .._collection import Collection

from ..survivors import weapon_proficiency

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.root_module = weapon_proficiency
        Collection.__init__(self,  *args, **kwargs)
