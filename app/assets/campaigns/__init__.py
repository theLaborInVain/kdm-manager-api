'''

    Campaigns as a collection function like a normal asset collection, but this
    module also defines a Campaign object that can be initialized when working
    with campaign assets.

    This needs a refactor. It may not be necessary anymore.

'''

from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):
    ''' Needs a refactor.'''

    def __init__(self, *args, **kwargs):
        ''' Vanilla init with a type_override that needs deprecated. '''

        self.type_override = "campaign"
        Collection.__init__(self, *args, **kwargs)


class Campaign(Asset):
    """ This is the base class for all expansions. Private methods exist for
    enabling and disabling expansions (within a campaign/settlement). """

    def __init__(self, *args, **kwargs):

        Asset.__init__(self, *args, **kwargs)
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
