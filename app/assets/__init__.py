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
from bson import json_util
from collections import OrderedDict
import glob
import importlib
import json
import os

# third party imports
import flask

# local imports
from app import API, utils
from app.models import settlements, survivors, users



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
        S = settlements.Settlement()
        return S.serialize()
    elif asset_type == "survivor":
        S = survivors.Survivor()
        return S.serialize()
    elif asset_type == "survivors":
        output = survivors.create_many_survivors(dict(flask.request.get_json()))
        return flask.Response(
            response=json.dumps(output, default=json_util.default),
            status=200,
            mimetype="application/json"
        )
    else:
        # unknown user asset types get a 422
        err = "Creating '%s' type user assets is not supported!" % asset_type
        return flask.Response(response=err, status=422, mimetype="text/plain")

    return utils.http_400


def get_user_asset(collection=None, asset_id=None):
    """ Tries to initialize a user asset from one of our three user asset
    collections. If any of these fail, they should raise the appropriate
    exception back up (to the user).

    Raises an exception if we get a bogus/bad collection name.
    """

    if collection == "settlement":
        return settlements.Settlement(_id=asset_id)
    elif collection == "survivor":
        return survivors.Survivor(_id=asset_id)
    elif collection == "user":
        return users.User(_id=asset_id)

    raise utils.InvalidUsage("Collection '%s' does not exist!" % collection, status_code=422)



#
#       Methods for working with game assets, e.g. retrieving/dumping an asset
#           collection, a specific game asset, etc.
#

def get_game_asset(collection_name, return_type=flask.Response):
    """ Formerly a part of the (deprecated) request_broker.py module, this
    method imports an asset type, alls its Assets() method and then returns
    its request_response() method."""

    model = importlib.import_module('app.models.%s' % collection_name)
    A = model.Assets()

    if return_type == dict:
        return A.assets
    elif return_type == object:
        return A

    return A.request_response()


def list_game_assets(game_assets=False):
    """ Returns a list of all available asset dictionaries. The 'game_assets'
    kwarg filters this to only return game assets (i.e. to filter out meta and
    webapp only assets). """

    asset_dir_abs_path = os.path.join(API.root_path, 'assets')
    py_files_in_asset_dir = glob.glob(os.path.join(asset_dir_abs_path, '*.py'))

    output = [
        os.path.splitext(os.path.basename(f))[0]
        for f
        in py_files_in_asset_dir
        if os.path.basename(f) != '__init__.py'
    ]

    if game_assets:
        for collection_name in output:
            collectionObject = get_game_asset(collection_name, return_type=object)
            if not collectionObject.is_game_asset:
                output.remove(collection_name)

    return sorted(output)


@utils.metered
def kingdom_death(return_type=None):
    """ Returns a dictionary of all assets. """

    output = OrderedDict()

    all_assets = list_game_assets()
    for asset_collection in all_assets:
        asset_object = get_game_asset(asset_collection, return_type=object)
        if getattr(asset_object, 'is_game_asset', False):
            output[asset_collection] = asset_object.get_sorted_assets()

    return json.dumps(output, default=json_util.default)
