"""

    This module allows programmatic access to the various asset dictionaries we
    support. Some are game assets, some are "meta" assets used by the webapp(s),
    etc.

    This module also replaces the deprecated/cancelled 'request_broker.py'
    module (in part), so there are some methods here that return flask Response
    objects.

    YHBW

"""

# standard lib imports
from collections import OrderedDict
import glob
import json
import os

# second party imports
from bson import json_util
import flask

# local imports
from app import API, utils
from app.assets import kingdom_death as KingdomDeath
from app.models import settlements, survivors, users


#
#       Methods for working with game assets, e.g. retrieving/dumping an asset
#           collection, a specific game asset, etc.
#

@utils.metered
def get_game_asset(collection_name, return_type=flask.Response):
    """ Formerly a part of the (deprecated) request_broker.py module, this
    method imports an asset type, calls its Assets() method and then returns
    its request_response() method.

    This could honestly go back into routes.py at this point.
    """

    game_asset = getattr(KingdomDeath, collection_name, None)
    if game_asset is None:
        return utils.HTTP_404

    try:
        asset_object = game_asset.Assets() # initialize a collection object
    except AttributeError as error:
        return None    # if it doesn't have an Assets() method, keep going

    if return_type == dict:
        return asset_object.assets
    if return_type == object:
        return asset_object

    return asset_object.request_response()


def list_game_assets():
    ''' Returns a list of packages from the assets module if the package
    is a game asset. '''

    # set the path to the assets directory
    module_abs_path = os.path.join(API.root_path, 'assets/')

    # get folders (i.e. modules); exclude anything starting with an underscore
    dir_contents = os.listdir(module_abs_path)
    packages = [
        folder for folder in dir_contents if (
            os.path.isdir(os.path.join(module_abs_path, folder)) and
            not folder.startswith('_')
        )
    ]

    # initialize each package (as a Collection object) and check it
    output = []
    for package in packages:
        collection_object = get_game_asset(package, return_type=object)

        # ignore non-game assets or ones that aren't collections
        if (
            collection_object is not None and
            getattr(collection_object, 'is_game_asset', False)
        ):
            output.append(package)

    return sorted(output)


@utils.metered
def kingdom_death():
    ''' Returns a dictionary of all game assets by using methods in this module.

    The basic workflow is:
        1. list_game_assets(), which is basically a fancy glob of the assets mod
        2. For each asset package in the assets module, get_game_asset()
        3. return it all in an ordered dict.
    '''

    output = OrderedDict()

    all_assets = list_game_assets()
    for asset_collection in all_assets:
        asset_object = get_game_asset(asset_collection, return_type=object)
        if (
            asset_object is not None and
            getattr(asset_object, 'is_game_asset', False)
        ):
            output[asset_collection] = asset_object.get_sorted_assets()

    return json.dumps(output, default=json_util.default)
