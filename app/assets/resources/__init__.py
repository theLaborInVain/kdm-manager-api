"""

    Resources, like gear, are initialized with some mandatory attributes so that
    individual assets that maybe don't have keywords or descriptions get a blank
    attribute of that type when self.assets() is created.

"""

import math

from .._asset import Asset
from .._collection import Collection
from .definitions import *

# constants
_CONSUMABLE_KEYWORDS = ['fish', 'consumable', 'flower']
_RARITY_RATING = {
    0.01: 'very rare',
    0.05: 'rare',
    0.10: 'uncommon',
    0.20: 'common',
    0.30: 'typical',
}

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        ''' Needs a refactor to remove mandatory_attributes, which is
        deprecated and should be replaced with data model.'''
        self.mandatory_attributes = {'keywords': [], 'desc': ""}
        Collection.__init__(self,  *args, **kwargs)
        self.set_rarity()

    def get_all_keywords(self):
        """ Returns a set of all keywords for all assets. """

        keywords = set()
        for a_dict in self.get_dicts():
            keywords = keywords.union(a_dict['keywords'])
        return sorted(keywords)


    def set_rarity(self):
        ''' Counts the cards in the deck; gives each one a rarity dict. '''

        for resource_location in self.get_sub_types():
            total_cards_in_deck = 0

            # get total cards
            for r_handle in self.get_assets_by_sub_type(resource_location):
                resource = self.get_asset(r_handle)
                total_cards_in_deck += resource.get('copies', 1)

            # calculate rarity
            for r_handle in self.get_assets_by_sub_type(resource_location):
                resource = self.get_asset(r_handle)
                copies = resource.get('copies', 1)
                gcd = math.gcd(copies, total_cards_in_deck)
                rarity_dict = {
                    'probability': '%s in %s' % (
                        copies // gcd, total_cards_in_deck // gcd
                    ),
                    'score': round(copies / total_cards_in_deck, 2),
                }
                rarity_dict['percent'] = int(rarity_dict['score'] * 100)
                for score in _RARITY_RATING:
                    if rarity_dict['score'] >= score:
                        rarity_dict['rating'] = _RARITY_RATING[score]
                self.assets[r_handle]['rarity'] = rarity_dict



class Resource(Asset):

    def __init__(self, *args, **kwargs):
        self.assets = Assets()
        Asset.__init__(self,  *args, **kwargs)

    def is_consumable(self):
        """ Returns a Boolean representing whether the resource is consumable
        or not. """
        for k in self.keywords:
            if k in _CONSUMABLE_KEYWORDS:
                return True
        return False

