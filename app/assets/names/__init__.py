"""

    The asset collection of names has some unusual/atypical methods. Read the
    docs here before fiddling any of this.

"""

# standard library imports
from copy import copy
import random

# API imports
from .._collection import Collection
from . import definitions as names    # <-- this one is weird/custom


def get_random_names(count=100):
    """ Returns 'count' random names for each sex. This is meant primarily
    as a front-end helper, so it returns a JSON-like dict. It also raises
    a big, wordy error if you ask it for too many names. """

    male_names = copy(names.male)
    female_names = copy(names.female)

    male_names.extend(copy(names.neuter))
    female_names.extend(copy(names.neuter))

    outbound_male_set = set()
    outbound_female_set = set()

    for name_list in male_names, female_names:
        if count > len(name_list):
            err = 'Cannot return more than %s random names!'
            raise ValueError(err % len(name_list))

    for name_tuple in [
            (outbound_male_set, male_names),
            (outbound_female_set, female_names)
    ]:
        outbound_set, sex_options = (name_tuple)
        while len(outbound_set) < count:
            outbound_set.add(random.choice(sex_options))

    return {
        'M': sorted(list(outbound_male_set)),
        'F': sorted(list(outbound_female_set))
    }


def get_random_surnames(count=50):
    """ Returns 'count' random surnames. """

    all_surnames = names.surname
    random_surnames = set()
    while len(random_surnames) < count:
        random_surnames.add(random.choice(all_surnames))
    return list(random_surnames)


class Assets():
    """ This asset collection DOES NOT take Collection as its base class.

    Rather, it is initialized from lists rather than dicts using custom code
    in the __init__() method below.

    """

    def __init__(self, *args, **kwargs):

        # set some baseline attribs
        self.is_game_asset = False

        # private methods to create a self.assets dict
        def name_to_handle(prefix, name):
            """ Turns a name & prefix and turns them into a unique handle."""
            output = name.replace(" ", "").lower()
            return "%s_%s" % (prefix, output)

        def load(asset_type, asset_list):
            """ Loads an asset group onto self.assets(). """
            for asset in asset_list:
                self.assets[name_to_handle(asset_type, asset)] = {
                    "name": asset,
                    "sub_type": asset_type
                }

        # create assets
        self.assets = {}

        for asset_type, asset_list in names.__dict__.items():
            if isinstance(asset_list, list) and not asset_type.startswith('_'):
                load(asset_type, asset_list)






    #
    #   private/unique get methods
    #

    def get_names_by_type(self, name_type=None):
        """ Returns a list of names whose 'type' attribute matches the value of
        'name_type'. """

        output = []
        for asset in self.assets.keys():
            if self.assets[asset]['sub_type'] == name_type:
                output.append(self.assets[asset]["name"])

        if len(output) == 0:
            raise AttributeError("No names found for type '%s'" % name_type)

        return output


    def get_random_settlement_name(self):
        """ Returns a random settlement name. What else would it do? """

        settlement_names = self.get_names_by_type('settlement')
        return random.choice(settlement_names)


    def get_random_survivor_name(self, sex="male", include_neuter=True):
        """ Returns a random survivor name. Use the 'include_neuter' bool to
        include/exclude neuter names. """

        if sex[0].lower() == 'm':
            sex = 'male'
        elif sex[0].lower() == 'f':
            sex = 'female'
        else:
            raise Exception("Unhandled sex!")

        survivor_names = self.get_names_by_type(sex)
        if include_neuter:
            survivor_names.extend(self.get_names_by_type('neuter'))
        return random.choice(survivor_names)
