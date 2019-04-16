"""

    This controls the /app/assets/user_preferences.py assets dictionaries,
    which are named for the client webapps they serve.

    This is...not great decoupling, but hey, we're getting there.

"""


from app.assets import user_preferences
from app import models, utils


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        self.root_module = user_preferences
        models.AssetCollection.__init__(self,  *args, **kwargs)

        # quickly grab the defaults from the settings.cfg and set them
        for p_key in self.assets.keys():
            default = utils.settings.get('users', p_key)
            self.assets[p_key]['default'] = default


class Preference(models.GameAsset):
    """ This is the base class for all expansions. Private methods exist for
        enabling and disabling expansions (within a campaign/settlement). """

    def __init__(self, *args, **kwargs):
        models.GameAsset.__init__(self,  *args, **kwargs)
        self.assets = Assets()
        self.initialize()

