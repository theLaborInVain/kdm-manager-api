"""

    This is how we work with collections of monsters as well as individual
    monster objects.

"""

from app import utils

from .._asset import Asset
from .._collection import Collection
from .definitions import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        """ Initialize the asset collection object. """
        Collection.__init__(self,  *args, **kwargs)
        self.set_levels()


    def set_levels(self):
        """ Used while initializing the monsters asset collection to synthesize
        the levels attribute based on key/value pairs that should already be in
        the monster's dict.

        Our logic here is this: if the monster dict already has levels, we pass
        and do nothing; if the dict has 'unique': True, we set levels to 0.

        Otherwise, we set 'levels' = 3 and go about our business.
        """

        for m in self.assets.keys():

            m_dict = self.assets[m]

            if "levels" in m_dict.keys():
                pass
            elif "unique" in m_dict.keys() and m_dict["unique"]:
                self.assets[m]["levels"] = 0
            else:
                self.assets[m]["levels"] = 3


    def get_asset_from_name(self, name=None, decompose=True):
        """ Overwrites the base class method of the same name. """

        # fail if we don't get a str
        if not isinstance(name, str):
            err = "'name' kwarg must be 'str'! Got %s (%s)"
            raise utils.InvalidUsage(err % (type(name), name))

        name_upper = name.strip().upper()

        # now create a NON-CASE-SENSITIVE look-up dict to search
        name_lookup = {}
        for m_dict in self.get_dicts():
            name_lookup[m_dict['name'].upper()] = m_dict

        # now check it against the incoming string
        base_class_result = None
        if name_upper in name_lookup.keys():
            base_class_result = self.get_asset(
                name_lookup[name_upper]['handle']
            )

        # if that worked, return it
        if base_class_result is not None:
            return base_class_result

        # if it didn't and we're not decomposing, return None
        if base_class_result is None and not decompose:
            return base_class_result # i.e. None

        # now try decomposition
        variations = []
        name_list = name.split(" ")
        for i in range(len(name_list) + 1) :
            variations.append(" ".join(name_list[:i]))
            variations.append(" ".join(name_list[i:]))

        for variation in variations:
            asset_dict = self.get_asset_from_name(variation, decompose=False)
            if asset_dict is not None:
                return asset_dict


    def init_asset_from_name(self, name=None):
        ''' Returns an initialized monster object from 'name'. '''

        monster_asset = self.get_asset_from_name(name)

        # try to get level
        monster_level = None
        split_name = name.split(' ')
        for piece in split_name:
            if piece.isdigit():
                monster_level = int(piece)

        return Monster(
            handle = monster_asset['handle'],
            collection_obj=self,
            level = monster_level,
        )


class Monster(Asset):
    """ This is the base class for all monsters. We should NOT have to sub-class
    it with quarry/nemesis type child classes, but that design may change. """

    def __init__(self, *args, level=None, **kwargs):
        ''' Normal init followed by special attrib fuckery. '''

        Asset.__init__(self, *args, **kwargs)

        self.level = level
        if self.level is None:
            del self.level

        # strip level for uniques
        if self.asset.get('unique', False):
            if hasattr(self, 'level'):
                del self.level

        # set attribs (yikes)
        for attr in ['comment', 'type']:
            if self.asset.get(attr, None) is not None:
                setattr(self, attr, self.asset[attr])


    def is_unique(self):
        """ Returns a bool representing whether the monst is unique. Monsters
        are non-unique by default. """
        if self.asset.get('unique', False):
            return self.asset['unique']
        return False


    def is_selectable(self):
        """ Returns a bool representing whether the monst is unique. Monsters
        are selectable by default. """
        if self.asset.get('selectable', False):
            return self.asset['selectable']
        return True




    def initialize_from_name(self, check_asset=True):
        """ Try to initialize a monster object from a string. Lots of craziness
        here to protect the users from themselves.
        """

        # sanity warning
        if "_" in self.name:
            self.logger.warn("Asset name '%s' contains underscores. Names should use whitespace." % self.name)
            self.logger.warn("Attempting to initialize by handle...")
            self.handle = self.name
            self.initialize_from_handle()
            return True

        # first, check for an exact name match (long-shot)
        asset_dict = self.assets.get_asset_from_name(self.name, decompose=False)
        if asset_dict is not None:
            self.initialize_asset(asset_dict)
            return True

        # next, split to a list and try to set asset and level
        name_list = self.name.split(" ")
        for i in name_list:
            if i.isdigit():
                setattr(self, "level", int(i))

        # now iterate through the list and see if we can get a name from it
        for variation in utils.decompose_name_string(self.name):
            asset_dict = self.assets.get_asset_from_name(variation, decompose=False)
            if asset_dict is not None:
                self.initialize_asset(asset_dict)
#                if len(name_list) > i and name_list[i].upper() not in ["LEVEL","LVL","L"]:
#                    setattr(self, "comment", (" ".join(name_list[i:])))
                return True

        # finally, create a list of misspellings and try to get an asset from that
        #   (this is expensive, so it's a last resort)
        m_dict = {}
        for asset_handle in self.assets.get_handles():
            asset_dict = self.assets.get_asset(asset_handle)
            if "misspellings" in asset_dict.keys():
                for m in asset_dict["misspellings"]:
                    m_dict[m] = asset_handle

        for i in range(len((name_list))+1):
            parsed_name = " ".join(name_list[:i]).upper()
            if parsed_name in m_dict.keys():
                asset_handle = m_dict[parsed_name]
                self.initialize_asset(self.assets.get_asset(asset_handle))
                if len(name_list) > i and name_list[i].upper() not in ["LEVEL","LVL","L"]:
                    setattr(self, "comment", (" ".join(name_list[i:])))
                return True


        # if we absolutely cannot guess wtf monster name this is, give up and
        #   throw a utils.Asseterror()
        if self.handle is None:
            raise models.AssetInitError("Asset name '%s' could not be translated to an asset handle!" % self.name)
