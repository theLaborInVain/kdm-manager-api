"""

    Models have a lot of class methods. The basic theory is this:

    - UserAsset is a base class for all user assets, e.g. individual survivors,
        settlements, users.
    - DataModel is a class object that different types of UserAsset objects
        initialize within themselves so that their data model can be treated
        like an object.

"""

# standard lib imports
from bson import json_util
from bson.objectid import ObjectId
from collections import OrderedDict
from copy import copy, deepcopy
from datetime import datetime, timedelta
import functools
import importlib
import inspect
import json
import os
from user_agents import parse as ua_parse
import random

# third party imports
import flask
import werkzeug

# local imports
from app import API, utils
from app.models import settlements, survivors, users
from app.models._decorators import *


#
#   Methods for creating and working with user assets
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
        settlement_record = utils.mdb.settlements.find_one(
            {'_id': ObjectId(flask.request.get_json()['settlement'])}
        )
        survivor_object = survivors.Survivor(
            Settlement = settlements.Settlement(_id=settlement_record['_id'])
        )
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
        survivor_record = utils.mdb.survivors.find_one(
            {'_id': ObjectId(asset_id)}
        )
        return survivors.Survivor(
            _id=asset_id,
            normalize_on_init=True,
            Settlement = settlements.Settlement(
                _id=survivor_record['settlement']
            )
        )
    if collection == "user":
        return users.User(_id=asset_id)

    raise utils.InvalidUsage(
        "Collection '%s' does not exist!" % collection,
        status_code=422
    )




#
#   KillboardAsset starts here
#

class KillboardAsset:
    """ This is where we do work with killboard assets. """

    def __init__(self, _id=None, params={}):
        """ Basic init routine. Use a valid ObjectID as '_id' if you've got an
        edit that you want to do; leave '_id' set to None to create a new
        entry in the killboard."""

        self.logger = utils.get_logger()

        # initialize kwargs as part of the object
        self._id = _id
        self.params = params

        if self._id is None and params == {}:
            err = str(
                "New killboard objects must be initialized with an '_id' value "
                "of None and a non-empty 'params' dict!"
            )
            raise ValueError(err)

        if self._id is None and params != {}:
            self.new()  # defines self._id when it's done inserting

        # now that we've got a self._id defined, add the document as an attrib
        self.document = utils.mdb.killboard.find_one({'_id': self._id})
        if self.document is None:
            err = "Cannot find a killboard entry with _id=%s" % self._id
            raise ValueError(err)

        # set all document keys to be attributes
        for key, value in self.document.items():
            setattr(self, key, value)

        #finally, normalize:
        self.normalize()


    def save(self, verbose=True):
        """ Generic save method. """
        utils.mdb.killboard.save(self.document)
        if verbose:
            self.logger.info('Saved changes to Killboard object: %s' % self._id)


    def normalize(self):
        """ Forces Killboard objects to adhere to our data model. """

        perform_save = False

        # fix the type, if necessary, to be the type in the monsters asset dict
        if self.type == 'monsters':
            self.logger.warn("Correcting Killboard entry 'type' attribute!")
            MonsterAsset = models.monsters.Monster(handle=self.handle)
            self.type = MonsterAsset.sub_type
            self.document['type'] = self.type
            perform_save = True

        if perform_save:
            self.save()




#
#   Exception classes!
#

class AssetMigrationError(Exception):
    """ Handler for asset migration/conversion errors. """

    def __init__(self, message="An error occurred while migrating this asset!"):
        self.logger = utils.get_logger()
        self.logger.exception(message)
        Exception.__init__(self, message)

class AssetInitError(Exception):
    """ Handler for asset-based errors. """

    def __init__(self, message="An error occurred while loading this asset!"):
        self.logger = utils.get_logger()
        self.logger.exception(message)
        Exception.__init__(self, message)

class AssetLoadError(Exception):
    """ Handler for asset-based errors. """

    def __init__(self, message="Asset could not be retrieved from mdb!"):
        self.logger = utils.get_logger()
        self.logger.exception(message)
        Exception.__init__(self, message)

