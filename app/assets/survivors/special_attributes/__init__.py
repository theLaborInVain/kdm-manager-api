
'''

    This is a pseudo asset used on Survivor records to basicall set random
    flags that aren't part of the Survivor data model.

'''

from app.assets._collection import Collection

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        Collection.__init__(self,  *args, **kwargs)
