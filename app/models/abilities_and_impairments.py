"""

    The A&I model for the collection is here: we don't support individual A&I
    objects because there is no reason in normal workflow to work with one.

"""

from app import models


class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        """ The init method for the A&I asset collection calls the
        set_default_max_values() methods from the base class. """

        models.AssetCollection.__init__(self,  *args, **kwargs)
        self.set_default_max_values()

