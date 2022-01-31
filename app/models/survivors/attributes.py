"""

    The app/assets/survivors/attribtues.py file is used primarily to manage the
    various lists and dictionaries that are part of the survivor object.

    We shouldn't be initializing these and working with them, generally, but
    we provide support for it just in case.

"""


from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        """ These are emphatically NOT game assets. Otherwise, we initialize
        them using defaults. """

        self.is_game_asset = False
        models.AssetCollection.__init__(self,  *args, **kwargs)
