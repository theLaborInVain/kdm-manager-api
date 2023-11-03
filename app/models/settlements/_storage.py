'''

    The settlement storage object is a model that has its own class definition
    and does not take Collection as a base class.

    The big idea is that it is initialized by a settlement and uses the
    settlement's already-initialized Gear and Resources collections (attribs)
    to solve the version problem and minimize the number of collections we
    initialize.

    This thing is halfway between an asset and a model. It lives with models
    for now, because it depends on user data and is therefore technically a
    type of user asset.

'''

# standard library imports
from collections import OrderedDict
from copy import copy

# KDM API imports
from app import utils

from app.assets import gear, resources

class Storage():
    ''' The storage class definition. '''

    def __init__(self, gear=None, expansions=None, resources=None):
        ''' This is an object that takes a lot from the settlement object that
        initializes it.

        'gear' is an initialized Gear collection object; same same for the
        'resources' kwarg, but with Resources, etc. '''

        self.logger = utils.get_logger()

        self.gear_collection = gear
        self.expansions_collection = expansions
        self.resources_collection = resources

        for attrib in [
            self.gear_collection,
            self.expansions_collection,
            self.resources_collection
        ]:
            if attrib is None:
                msg = 'Storage objects require Gear and Resources collections!'
                raise AttributeError(msg)

        self.locations = {}


    def add_location(self, location=None):
        ''' The self.locations of the Storage object is a dictionary where the
        keys are handles from assets.locations 'gear' or 'resources' dictionary.

        'location' should be an INITIALIZED assets.storage asset.

        These locations, once added are tuned up to include:
            - 'type': 'gear' or 'resources'
            - 'assets': a list of asset objets from those collections
        '''

        # sanity check the asset by reviewing sub_type
        location_sub_type = location.get('sub_type', None)
        if (
            location_sub_type is None or
            location_sub_type not in ['gear','resources']
        ):
            err = "Storage locations must specify a 'location_type' kwarg."
            raise AttributeError(err)

        # now tune up the location def
        location['collection'] = []
        location['digest'] = OrderedDict()
        location['inventory'] = []

        # add the location to self; work on it
        location_handle = location['handle']
        self.locations[location_handle] = copy(location)
        self._set_location_assets(location_handle)
        self._set_location_flair(location_handle)



    def add_item_to_storage(self, handle=None, quantity=0):
        ''' Add a 'quanity' of 'item_handle' to settlement storage. '''

        item_obj = self._item_handle_to_item_object(handle)
        item_dict = copy(item_obj.serialize(dict))
        item_dict['quantity'] = quantity

        # die informatively if we can't add this because we don't have the loc
        if item_dict['sub_type'] not in self.locations.keys():
            err = "%s asset cannot be added to storage! Missing '%s' location!"
            raise AttributeError(err % (item_obj, item_dict['sub_type']))

        self.locations[item_dict['sub_type']]['collection'].append(
            item_dict
        )



    #
    #   private methods follow
    #

    def _item_handle_to_item_object(self, item_handle=None):
        ''' Returns an item object or dies bloody. '''

        if item_handle in self.gear_collection.get_handles():
            return gear.Gear(
                handle=item_handle,
                collection_obj=self.gear_collection
            )

        if item_handle in self.resources_collection.get_handles():
            return resources.Resource(
                handle=item_handle,
                collection_obj=self.resources_collection
            )

        err = "Item asset handle '%s' could not be initialized!"
        raise AttributeError(err % (item_handle))


    def _set_location_assets(self, location_handle=None):
        ''' Operations on 'location_handle', one of the keys of the
        self.locations dictionary. Creates and populates the 'assets'
        key of the location witha list of initialized item assets. '''

        # set some laziness/legibility stuff
        location = self.locations[location_handle]
        location_sub_type = location.get('sub_type', None)
        location['handles'] = []
        location['assets'] = []

        # get the collection object
        collection_obj = getattr(self, location_sub_type + '_collection')

        # loop through the asset handles matching location_handle
        for item_handle in collection_obj.get_assets_by_sub_type(
            sub_type = location_handle
        ):
            item_object = self._item_handle_to_item_object(item_handle)
            location['handles'].append(item_handle)
            location['assets'].append(item_object)

        # final sanity check
        if (
            len(location['assets']) < 1 and not
            location.get('has_no_gear', False)
        ):
            warn = "No %s assets for storage handle '%s' in collection: %s"
            self.logger.warning(
                warn, location_sub_type, location_handle, collection_obj
            )


    def _set_location_flair(self, location_handle=None):
        ''' Checks a location for expansion flair. If we find any, add it to
        the location keys. '''

        location = self.locations[location_handle]
        expansion_handle = location.get('expansion', None)

        # bail if this isn't expansion content; core content has no flair
        if expansion_handle is None or location['sub_type'] != 'gear':
            return True

        expansion_asset = self.expansions_collection.get_asset(expansion_handle)
        for flair in ['bgcolor', 'color']:
            location[flair] = expansion_asset.get(flair, None)
