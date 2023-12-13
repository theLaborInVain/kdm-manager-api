"""

    Working with killboard objects (i.e. documents from the 'killboard'
    collection) happens here.

    Since these are NOT user assets, they use their own model object as
    their base class.

"""

from ._killboard_asset import KillboardAsset

class Killboard(KillboardAsset):
    """ Use this to initialize a killboard entry. It's base class lives in the
    app.models.killboard module/folder. """

    def __init__(self, *args, **kwargs):
        KillboardAsset.__init__(self,  *args, **kwargs)

