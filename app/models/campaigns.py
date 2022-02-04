'''

    Campaigns as a collection function like a normal asset collection, but this
    module also defines a Campaign object that can be initialized when working
    with campaign assets.

'''

from app import models

class Assets(models.AssetCollection):
    ''' Super class for initializing an AssetCollection of campaign
    definitions. '''

    def __init__(self, *args, **kwargs):
        ''' Vanilla init with a type_override that needs deprecated. '''

        self.type_override = "campaign"
        models.AssetCollection.__init__(self, *args, **kwargs)


class Campaign(models.GameAsset):
    """ This is the base class for all expansions. Private methods exist for
    enabling and disabling expansions (within a campaign/settlement). """

    def __init__(self, *args, **kwargs):

        models.GameAsset.__init__(self, *args, **kwargs)
        self.assets = Assets()
        self.baseline()
        self.initialize()


    def baseline(self):
        """ Campaign objects have a loose data model that we enforce by
        setting attributes manually.

        Theory being that we want to be able to only have to define SOME
        of these attributes in the actual assets/campaigns.py file and
        not have to write a bunch of exception-catching code in the
        methods/modules that work with these types of objects.

        All of the below is subject to overwrite by self.initialize().
        """

        self.default = False
        self.endeavors = []
        self.saviors = False
        self.survivor_special_attributes = []
