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
import importlib
import json
import os

# second party imports
from bson import json_util
import flask

# local imports
from app import API, utils
from app.models import settlements, survivors, users


LOGGER = utils.get_logger()

#
#	Methods for creating and working with user assets, e.g. survivors,
#		settlements, etc.
#

def new_user_asset(asset_type=None):
    """ Hands off a new asset creation request and returns the result of the
    request. Like all brokerage methods, this method always returns an HTTP
    response.

    The idea is to call this in request-processing workflow when you know that
    you've got an asset creation request.

    This brokerage method expects a few things:

        1.) you've added a logger to the request
        2.) you've also added a models.users.User object to the request
        3.) you're passing in JSON params that can be processed when
            fulfilling your request

    If you are NOT doing all of that, do NOT pass off a request to this method,
    unless you want to throw a 500 back at the user.

    """

    if asset_type == "settlement":
        settlement_obj = settlements.Settlement()
        return settlement_obj.serialize()
    if asset_type == "survivor":
        survivor_object = survivors.Survivor()
        return survivor_object.serialize()
    if asset_type == "survivors":
        output = survivors.create_many_survivors(dict(flask.request.get_json()))
        return flask.Response(
            response=json.dumps(output, default=json_util.default),
            status=200,
            mimetype="application/json"
        )

    err = "Creating '%s' type user assets is not supported!" % asset_type
    return flask.Response(response=err, status=422, mimetype="text/plain")



def get_user_asset(collection=None, asset_id=None):
    """ Tries to initialize a user asset from one of our three user asset
    collections. If any of these fail, they should raise the appropriate
    exception back up (to the user).

    Raises an exception if we get a bogus/bad collection name.
    """

    if collection == "settlement":
        return settlements.Settlement(_id=asset_id)
    if collection == "survivor":
        return survivors.Survivor(_id=asset_id, normalize_on_init=True)
    if collection == "user":
        return users.User(_id=asset_id)

    raise utils.InvalidUsage(
        "Collection '%s' does not exist!" % collection,
        status_code=422
    )



#
#       Methods for working with game assets, e.g. retrieving/dumping an asset
#           collection, a specific game asset, etc.
#

def get_game_asset(collection_name, return_type=flask.Response):
    """ Formerly a part of the (deprecated) request_broker.py module, this
    method imports an asset type, alls its Assets() method and then returns
    its request_response() method."""

    game_asset = importlib.import_module('app.assets.%s' % collection_name)
    asset_object = game_asset.Assets() # initialize a collection object

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

        # ignore non-game assets
        if getattr(collection_object, 'is_game_asset', False):
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
        if getattr(asset_object, 'is_game_asset', False):
            output[asset_collection] = asset_object.get_sorted_assets()

    return json.dumps(output, default=json_util.default)
