"""

    The asset collection of names has some unusual/atypical methods. Read the
    docs here before fiddling any of this.

"""

# standard library imports
from copy import copy
import random

# third party imports

# local imports
from app.assets import names
from app import models, utils


class Assets(models.AssetCollection):
    """ This asset collection is unlike the others.

    For starts, its the only AssetCollection that is initialized from lists,
    rather than dicts.

    Another major weirdness is how we make list items into dictionaries, which
    involes an odd name-to-handle conversion method and some un-DRY iteration
    for creating dicts out of names.

    On account of that, it sets attribs for all of the assets in its 'assets'
    dict during initialization and, though it supports normal AssetCollection
    methods, it's not recommended to call most of them (given the general non-
    standardness of the 'assets' dict).

    Proceed with caution.
    """

    def __init__(self, *args, **kwargs):

        # set some baseline attribs
        self.is_game_asset = False
        self.type_override = "names"

        # now use private methods to create a self.assets dict

        def name_to_handle(prefix, name):
            """ Turns a name & prefix and turns them into a unique handle."""
            n = name.replace(" ","").lower()
            return "%s_%s" % (prefix, n)

        def load(asset_type, asset_list):
            """ Loads an asset group onto self.assets(). """
            for asset in asset_list:
                self.assets[name_to_handle(asset_type, asset)] = {
                    "name": asset,
                    "sub_type": asset_type
                }

        self.assets = {}

        for asset_type, asset_list in names.__dict__.items():
            if isinstance(asset_list, list) and not asset_type.startswith('_'):
                load(asset_type, asset_list)

        models.AssetCollection.__init__(self,  *args, **kwargs)


    #
    #   Methods for getting random names follow
    #

    def get_random_names(self, count=100):
        """ Returns 'count' random names for each sex. This is meant primarily
        as a front-end helper, so it returns a JSON-like dict. It also raises
        a big, wordy error if you ask it for too many names. """

        m = copy(names.male)
        f = copy(names.female)

        m.extend(copy(names.neuter))
        f.extend(copy(names.neuter))

        male = set()
        female = set()

        for l in m,f:
            if count > len(l):
                raise utils.InvalidUsage('Cannot return more than %s random names!' % len(l))

        for i in [(male, m), (female, f)]:
            l, s = (i)
            while len(l) < count:
                l.add(random.choice(s))

        return {'M': sorted(list(male)), 'F': sorted(list(female))}


    def get_random_surnames(self, count=50):
        """ Returns 'count' random surnames. """

        all_surnames = names.surname
        random_surnames = set()
        while len(random_surnames) < count:
            random_surnames.add(random.choice(all_surnames))
        return list(random_surnames)




    #
    #   private/unique get methods
    #

    def get_names_by_type(self, name_type=None):
        """ Returns a list of names whose 'type' attribute matches the value of
        'name_type'. """

        output = []
        for a in self.assets.keys():
            if self.assets[a]['sub_type'] == name_type:
                output.append(self.assets[a]["name"])
        return output


    def get_random_settlement_name(self):
        """ Returns a random settlement name. What else would it do? """

        settlement_names = self.get_names_by_type('settlement')
        return random.choice(settlement_names)


    def get_random_survivor_name(self, sex="male", include_neuter=True):
        """ Returns a random survivor name. Use the 'include_neuter' bool to
        include/exclude neuter names. """

        if sex.lower() == 'm':
            sex = 'male'
        elif sex.lower() == 'f':
            sex = 'female'
        else:
            raise Exception("Unhandled sex!")

        survivor_names = self.get_names_by_type(sex)
        if include_neuter:
            survivor_names.extend(self.get_names_by_type('neuter'))
        return random.choice(survivor_names)

