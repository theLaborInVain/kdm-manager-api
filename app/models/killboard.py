"""

    Working with killboard objects (i.e. documents from the 'killboard'
    collection) happens here.

    Since these are NOT user assets, they use their own model object as
    their base class.

"""

from app import models

class Killboard(models.KillboardAsset):
    """ Use this to initialize a killboard entry. It's base class lives in the
    app.models.__init__ module. """

    def __init__(self, *args, **kwargs):
        models.KillboardAsset.__init__(self,  *args, **kwargs)

