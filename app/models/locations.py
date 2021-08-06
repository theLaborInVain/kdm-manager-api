"""

    LOCATIONS!

"""

from app import models

class Assets(models.AssetCollection):
    """ AssetCollection object model for Locations. """

    def __init__(self, *args, **kwargs):
        """ Locations use the base class method to enforce their data model. """

        self.data_model = {
            'selectable': bool,
        }

        models.AssetCollection.__init__(self,  *args, **kwargs)

