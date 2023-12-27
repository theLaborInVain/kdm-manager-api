"""

    This is how we work with collections of monsters as well as individual
    monster objects.

"""

import re

from app import utils

from .._asset import Asset
from .._collection import Collection
from .definitions import *


class Assets(Collection):
    ''' Initializes a collection of monster assets. This collection has a couple
    of custom methods related to being able to get an asset from a name string
    (instead of a handle.'''

    def __init__(self, *args, **kwargs):
        """ Initialize the asset collection object. """
        Collection.__init__(self,  *args, **kwargs)
        self._set_levels()


    def _set_levels(self):
        """ Used while initializing the monsters asset collection to synthesize
        the levels attribute based on key/value pairs that should already be in
        the monster's dict.

        Our logic here is this: if the monster dict already has levels, we pass
        and do nothing; if the dict has 'unique': True, we set levels to 0.

        Otherwise, we set 'levels' = 3 and go about our business.
        """

        for m_handle in self.assets.keys():

            m_dict = self.assets[m_handle]

            if "levels" in m_dict.keys():
                pass
            elif "unique" in m_dict.keys() and m_dict["unique"]:
                self.assets[m_handle]["levels"] = 0
            else:
                self.assets[m_handle]["levels"] = 3


    def get_asset_from_name(self, name=None):
        ''' Tries to return an asset dict based on 'name', a string. '''
        asset_handle = get_handle_from_name(name)
        return self.get_asset(handle=asset_handle)


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

    def __init__(self, *args, **kwargs):
        ''' Normal init followed by special attrib fuckery. '''

        # pop out kwargs that aren't allows by the base class Asset definition
        self.name = kwargs.pop('name', None)
        self.level = kwargs.pop('level', None)

        # This is the last asset we allow to be set from name values and this
        #   is where we support that
        if 'handle' not in kwargs and self.name is not None:
            self.logger = utils.get_logger()    # because we haven't init'd yet
            kwargs['handle'] = get_handle_from_name()
#            self.logger.warn('GOT HANDLE: %s', kwargs['handle'])

        Asset.__init__(self, *args, **kwargs)

        # use name to try to set some attributes
        p_name, p_level, p_comment = split_name_level_comment(self.name)

        # try to use derived values to set level, comment
        for attr in ['level', 'comment']:
            if getattr(self, attr, None) is None:
                setattr(self, attr, 'p_' + attr)
                if getattr(self, attr, None) is None:
                    delattr(self, attr)

        # strip level for uniques
        if self.asset.get('unique', False):
            if hasattr(self, 'level'):
                del self.level



    #
    # object query methods
    #

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




def get_handle_from_name(raw_name=None, decompose=True):
    """ God's mistake. This absolute disasterpiece tries to parse 'name' and
    return a valid handle of a monster asset. """

    # default failure/error msg
    failure_exception = AttributeError(
        "Could not get Monster handle from name '%s'" % raw_name
    )

    # 
    # sanity checks
    #
    if not isinstance(raw_name, str):
        err = "'name' kwarg must be 'str'! Got %s (%s)"
        raise utils.InvalidUsage(err % (type(name), name))

    if "_" in raw_name:
        warn = "Name '%s' contains underscores. Names use whitespace."
        raise utils.InvalidUsage(warn % raw_name)


    # if we're doing this, stage up some stuff:
    # create a dictionary of 'raw' assets (not-initalized) to use later
    raw_assets = {}
    for asset_dict in [quarry, nemesis, core, finale]:
        raw_assets.update(asset_dict)

    # get a name value without level cruft; 'raw_name' no longer used
    name, _, _ = split_name_level_comment(raw_name)
    name_upper = name.strip().upper()

    # method one: see if the incoming name matches a known asset name
    # create a NON-CASE-SENSITIVE look-up dict to search
    name_lookup = {}
    for asset_handle, asset_dict in raw_assets.items():
        asset_dict['handle'] = asset_handle
        name_lookup[asset_dict['name'].upper()] = asset_dict

    # and then search 'name' (which we just made) against it:
    if name_upper in name_lookup.keys():
        return name_lookup[name_upper]['handle']

    # at this point, if optional methods aren't enabled, return None
    if not decompose:
        return None

    # optional method: name string decomposition
    if decompose:
        variations = []
        name_list = name.split(" ")
        for i in range(len(name_list) + 1) :
            variations.append(" ".join(name_list[:i]))
            variations.append(" ".join(name_list[i:]))

        for variation in variations:
            handle = get_handle_from_name(variation, decompose=False)
            if handle is not None:
                return handle

    # optional method: misspellings
    # for this, make a lookup table of misspelled names
    misspelling_lookup = {}
    for asset_handle, asset_dict in raw_assets.items():
        if asset_dict.get('misspellings', None) is not None:
            for incorrect_name in asset_dict["misspellings"]:
                misspelling_lookup[incorrect_name] = asset_handle

    if name_upper in misspelling_lookup:
        return misspelling_lookup[name_upper]


    raise failure_exception



def split_name_level_comment(raw_name):
    """ Private method that takes a 'raw_name' string and tries to return a
    tuple of the name and the level (as an int)."""

    name = None
    level = None

    # go after the comment first
    match = re.search(r'\((.*?)\)', raw_name)
    comment = match.group(1).strip() if match else None

    # now pull out the level stuff
    # not DRY, but if you modify the list while iterating, python gets weird
    name_list = raw_name.split(' ')
    for fragment in name_list:
        if fragment.isdigit():
            name_list.remove(fragment)
            level = int(fragment)

    for fragment in name_list:
        if fragment.upper()[:3] == 'LVL':
            name_list.remove(fragment)

    name = ' '.join(name_list)
    return name, level, comment

