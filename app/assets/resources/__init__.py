"""

    Resources, like gear, are initialized with some mandatory attributes so that
    individual assets that maybe don't have keywords or descriptions get a blank
    attribute of that type when self.assets() is created.

"""

from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        ''' Needs a refactor to remove mandatory_attributes, which is
        deprecated and should be replaced with data model.'''
        self.mandatory_attributes = {'keywords': [], 'desc': ""}
        Collection.__init__(self,  *args, **kwargs)


    def get_all_keywords(self):
        """ Returns a set of all keywords for all assets. """

        keywords = set()
        for a_dict in self.get_dicts():
            keywords = keywords.union(a_dict['keywords'])
        return sorted(keywords)


class Resource(Asset):

    def __init__(self, *args, **kwargs):
        Asset.__init__(self,  *args, **kwargs)
        self.assets = Assets()
        self.initialize()

        self.consumable_keywords = ['fish','consumable','flower']

    def is_consumable(self):
        """ Returns a Boolean representing whether the resource is consumable
        or not. """
        for k in self.keywords:
            if k in self.consumable_keywords:
                return True
        return False

