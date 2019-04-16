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
import glob
import importlib
import os

# third party imports
import flask

# local imports
from app import API, utils
from app.models import settlements, survivors, users


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

    raise utils.InvalidUsage("Collection '%s' does not exist!", status_code=422)


def dump_asset(collection_name, return_type=flask.Response):
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


def list(game_assets=False):
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
            collectionObject = dump_asset(collection_name, return_type=object)
            if not collectionObject.is_game_asset:
                output.remove(collection_name)

    return sorted(output)


