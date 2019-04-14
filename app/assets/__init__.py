"""
    This module allows programmatic access to the various asset dictionaries we
    support. Some are game assets, some are "meta" assets used by the webapp(s),
    etc.
"""

# standard lib imports
import glob
import os

# third part imports

# local imports
from app import api

import importlib

def list(game_assets=False):
    """ Returns a list of all available asset dictionaries. The 'game_assets'
    kwarg filters this to only return game assets (i.e. to filter out meta and
    webapp only assets). """

    asset_dir_abs_path = os.path.join(api.root_path, 'assets')
    py_files_in_asset_dir = glob.glob(os.path.join(asset_dir_abs_path, '*.py'))

    output = [
        os.path.splitext(os.path.basename(f))[0]
        for f
        in py_files_in_asset_dir
        if os.path.basename(f) != '__init__.py'
    ]
    return output


def dump_asset(collection_name):
    """ Formerly a part of the (deprecated) request_broker.py module, this
    method imports an asset type, alls its Assets() method and then returns
	its request_response() method."""

    model = importlib.import_module('app.models.%s' % collection_name)
    A = model.Assets()

    return A.request_response()
