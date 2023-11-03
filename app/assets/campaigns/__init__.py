'''

    Campaigns as a collection function like a normal asset collection, but this
    module also defines a Campaign object that can be initialized when working
    with campaign assets.

    This needs a refactor. It may not be necessary anymore.

'''

from .._asset import Asset
from .._collection import Collection
from .definitions import *

from app.assets import expansions

class Assets(Collection):
    ''' Needs a refactor.'''

    def __init__(self, *args, **kwargs):
        ''' Vanilla init with a type_override that needs deprecated. '''

#        self.type_override = "campaign"
        Collection.__init__(self, *args, **kwargs)


class Campaign(Asset):
    ''' A campaign asset needs a little punching up. '''

    def __init__(self, *args, **kwargs):

        self.default = False
        self.endeavors = []
        self.saviors = False
        self.survivor_special_attributes = []

        Asset.__init__(self, *args, **kwargs)


    def get_required_expansions(self):
        ''' Returns a list of required expansions for the campaign.'''

        return self.asset['settlement_sheet_init'].get('expansions', [])


    def get_pillar_value(self):
        ''' Iterates through expansion content and tallying the pillar value of
        a campaign. '''

        # we'll need an initialized expansions collection to do this
        expansions_collection = expansions.Assets()

        pillar_value = 0
        for expansion in self.get_required_expansions():
            expansion_dict = expansions_collection.get_asset(expansion)
            pillar_value += expansion_dict.get('pillar_value', 0)

        return pillar_value
