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
    ''' A campaign asset needs a little punching up. '''

    def __init__(self, *args, **kwargs):

        self.default = False
        self.endeavors = []
        self.saviors = False
        self.survivor_special_attributes = []

        Asset.__init__(self, *args, **kwargs)
