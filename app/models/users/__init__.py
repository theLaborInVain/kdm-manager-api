"""

    Basic methods for working with users and authentication live here.

    The whole first half of this module is laziness/convenience methods for
    working with users. There is a TON of stuff here, so check here first before
    rummaging about in utils.

    Starting October 2023, the main class method 'User' lives in a different
    file in this models.users module called '_class_methods.py'

"""

# standard library imports
from copy import copy
from datetime import datetime
from hashlib import md5
import hmac
import io
import os
import json
import pickle
import random
import socket
import string
import urllib

# third party imports
from bson import json_util
from bson.objectid import ObjectId
from dateutil.tz import tzlocal
import flask
import gridfs
import jwt
import pymongo
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

# local imports
from app import API, models, utils
from app.models import user_preferences
from app.models.settlements import Settlement
from app.models.users._class_methods import *

# constants

LOGGER = utils.get_logger()

#
#   JWT helper methods here!
#

def authenticate(username=None, password=None):
    """ Refactored in December 2018 to use Miguel Grinberg's basic method.

    As of the refactor, this supports (legacy) MD5 look-ups: we try them first,
    and, if they fail, then we try to use the Werkzeug helper methods above.

    The 'username' and 'password' kwargs should be non-hashed/plaintext.

    Returns None if the 'username' is bogus or the 'password' check fails.
    """

    # return None immediately if either input is None
    if username is None or password is None:
        return None

    # initialize U as None, i.e. our default/failure return
    user_object = None

    # grab the user's MDB document, but DO NOT initialize the User:
    user = utils.mdb.users.find_one({"login": username})

    # if we have a user dict, do our comparisons and set U to be an
    #   initialized User object if they succeed:
    if user is not None:
        if check_password_hash(user['password'], password):
            user_object = User(_id=user["_id"])
        else:
            try:
#                if safe_str_cmp(
                if hmac.compare_digest(
                    user["password"],
                    md5(password.encode()).hexdigest()
                ):
                    user_object = User(_id=user["_id"])
            except UnicodeEncodeError as exception:
                raise utils.InvalidUsage(exception)

    # timestamp this authentication
    if user_object is not None:
        user_object.set_latest_authentication()

    return user_object


def get_user_id_from_email(email):
    """ Pulls the user from the MDB (or dies trying). Returns its email. """

    record = utils.mdb.users.find_one({'login': email.lower().strip()})
    if record is None:
        raise AttributeError("Could not find user data for %s" % email)
    return record['_id']



def import_user(user_data=None):
    """ Import a user from a pickle to the local mdb.

    The 'user_data' arg can be either a pickle on the file system or a
    string representation of a pickle.

    Used primarily for legacy support and admin jobs, e.g. clone.
    """

    data = None

    # coerce incoming data to dict or die trying.
    if isinstance(user_data, bytes):
        data = pickle.loads(user_data, encoding='bytes')

    if data is None and os.path.isfile(user_data):
        data = pickle.load(open(user_data, 'rb'))

    if data is None:
        raise ValueError("'%s' does not appear to be a pickle!" % user_data)

    # clean up the raw data
    for foreign_attr in ['current_session']:
        if data['user'].get(foreign_attr, False):
            del data['user'][foreign_attr]

    # start the import and check to see if we're doing something stupid
    msg = "Importing user %s [%s]" % (
        data['user']['login'],
        data['user']['_id']
    )
    LOGGER.warning(msg)

    try:
        new_user_oid = utils.mdb.users.save(data['user'])
    except pymongo.errors.DuplicateKeyError as exception:
        err = "User login '%s' exists under a different user ID!"
        LOGGER.error(exception)
        LOGGER.error(err)
        raise pymongo.errors.DuplicateKeyError(err)

    # private method to load individual assets
    def import_user_assets(asset_name):
        """ Helper function to import assets generically.

        The 'asset_name' arg should be something like "settlement_events" or
        "survivors" or "settlements", i.e. one of the keys in the incoming
        'assets_dict' dictionary (called 'data' here). """

        imported_assets = 0
        LOGGER.warning("Importing %s assets...", asset_name)
        try:
            for asset in data[asset_name]:
                imported_assets += 1
                utils.mdb[asset_name].save(asset)
        except KeyError:
            LOGGER.error('No %s assets found in user data!', asset_name)
        LOGGER.warning("%s %s assets imported.", imported_assets, asset_name)

    # load the important user assets to local
    for asset_collection in [
        'settlements',
        'settlement_events',
        'survivors',
        'survivor_notes'
    ]:
        import_user_assets(asset_collection)

    # check for orphan survivors (i.e. ones with no settlement)
    for survivor in utils.mdb.survivors.find():
        if utils.mdb.settlements.find_one(
            {"_id": survivor["settlement"]}
        ) is None:
            err = "Survivor %s belongs to a non-existent settlement (%s)!"
            LOGGER.error(err, survivor['_id'], survivor['settlement'])
            LOGGER.warning("Removing survivor %s from mdb...", survivor["_id"])
            utils.mdb.survivors.remove({"_id": survivor["_id"]})

    # next import avatars
    imported_avatars = 0
    for avatar in data["avatars"]:
        if gridfs.GridFS(utils.mdb).exists(avatar["_id"]):
            gridfs.GridFS(utils.mdb).delete(avatar["_id"])
            LOGGER.info("Removed object %s from local GridFS.", avatar["_id"])
            gridfs.GridFS(utils.mdb).put(
                avatar["blob"],
                _id=avatar["_id"],
                content_type=avatar["content_type"],
                created_by=avatar["created_by"],
                created_on=avatar["created_on"]
            )
            imported_avatars += 1
        LOGGER.info("Imported %s avatars!", imported_avatars)

    # legacy webapp: clean up sessions
    culled = utils.mdb.sessions.remove({"login": data["user"]["login"]})
    if culled['n'] > 0:
        LOGGER.info(
            "Removed %s session(s) belonging to incoming user!", culled['n']
        )

    return new_user_oid


def initiate_password_reset():
    """ Attempts to start the mechanism for resetting a user's password.
    Unlike a lot of methods, this one handles the whole flask.request processing
    and is very...self-contained. """

    # first, validate the post
    incoming_json = flask.request.get_json()
    user_login = incoming_json.get('username', None)
    if user_login is None:
        msg = "A valid email address is required for password reset requests!"
        return flask.Response(response=msg, status=400)

    # normalize emails issue #501
    user_login = user_login.strip().lower()

    # next, validate the user
    user = utils.mdb.users.find_one({"login": user_login})
    if user is None:
        return flask.Response(
            response = "'%s' is not a registered email address." % user_login,
            status = 404
        )

    # if the user looks good, set the code
    user_object = User(_id=user["_id"])
    user_code = user_object.set_recovery_code()

    # support for applications with their own URLs
    incoming_app_url = incoming_json.get('app_url', None)
    if incoming_app_url is not None:
        application_url = incoming_app_url
        parsed = urllib.parse.urlsplit(incoming_app_url)
        netloc = parsed.scheme + "://" + parsed.netloc
    else:
        netloc = utils.get_application_url()
        application_url = utils.get_application_url()

    info = "%s has requested a password reset. Incoming app URL: '%s'!"
    LOGGER.info(info, user_login, incoming_app_url)

    # finally, send the email to the user
    try:
        tmp_file = utils.html_file_to_template('password_recovery.html')
        msg = tmp_file.safe_substitute(
            login=user_login,
            recovery_code=user_code,
            app_url=application_url,
            netloc=netloc
        )
        email_session = utils.mailSession()
        email_session.send(
            recipients=[user_login],
            html_msg=msg,
            subject='KDM-Manager password reset request!'
        )
    except Exception as err:
        LOGGER.error(err)
        raise

    # exit 200
    return utils.http_200


def jwt_identity_handler(payload):
    """ Bounces the authentication request payload off of the user collection.
    Returns a user object if "identity" in the request exists. """

    u_id = payload["identity"]
    user = utils.mdb.users.find_one({"_id": ObjectId(u_id)})

    if user is not None:
        user_object = User(_id=user["_id"])
        return user_object.serialize()

    return utils.http_404


def refresh_authorization(expired_token):
    """ Opens an expired token, gets the login and password hash, and checks
    those against mdb. If they match, we return the user. This is what is
    referred to, in the field, as "meh--good enough" security.

    If you find yourself getting None back from this one, it's because your
    user changed his password.
    """

    user = token_to_identity(expired_token)

    # return MDB record
    login = user["login"]
    pw_hash = user["password"]
    return utils.mdb.users.find_one({"login": login, "password": pw_hash})


def reset_password():
    """ Checks out an incoming recovery code and, if everything looks OK, loads
    up the user, changes its password, removes the code from the user and saves
    it back to the mdb. """

    user_login = flask.request.get_json().get('username', None)
    new_password = flask.request.get_json().get('password', None)
    recovery_code = flask.request.get_json().get('recovery_code', None)

    for var_name, var_desc in [
        (user_login, 'Login'),
        (new_password, 'Password'),
        (recovery_code, 'Recovery code')
    ]:
        if var_name is None:
            err = (
                "Password reset requests require a login, password and a "
                "recovery code. (%s missing.)"
            ) % var_desc
            return flask.Response(response=err, status=400)

    user = utils.mdb.users.find_one(
        {'login': user_login, 'recovery_code': recovery_code}
    )
    if user is None:
        msg = "The password recovery code supplied is not valid for user '%s'."
        return flask.Response(
            response=msg % user_login,
            status=400
        )

    user_object = User(_id=user["_id"])
    del user_object.user['recovery_code']
    user_object.update_password(new_password)
    return utils.http_200


def token_to_identity(token, verify=False, return_type=dict):
    ''' Takes an incoming JWT and converts it to the 'identity' compoenent
    called "sub" in JWT 4.0.0 (previously called "identity").

    Returns a dictionary, if possible; returns a Flask response if it fails.
    '''

    # first, decode it
    try:
        decoded = jwt.decode(
            token,
            API.config['SECRET_KEY'],
            algorithms="HS256",
            options={
                'verify_exp': verify,
                'verify_signature': verify,
            },
        )
    except jwt.exceptions.ExpiredSignatureError:
        return utils.http_401
    except Exception as exception:
        LOGGER.error("JWT decoding failed! Request URL: %s", flask.request.url)
        LOGGER.error("Exception: |%s|", exception)
        LOGGER.error("Token contents: |%s|", token)
        err = "JWT token could not be processed! Exception: %s" % exception
        raise utils.InvalidUsage(err, status_code=401)

    # next, try to get the identity from the decoded token; fail if it's not
    #   where we expect it to be
    identity = {}
    for key in ['sub', 'identity']:
        if decoded.get(key, None) is not None:
            identity = dict(json.loads(decoded[key]))
            break

    # sanity check it for required keys
    for required_key in ['login', 'password', '_id']:
        if identity.get(required_key, None) is None:
            err = (
                "Incoming, decoded JWT does not include %s key/value "
                "and cannot be processed. Decoded token: %s" %
                (required_key, decoded)
            )
            LOGGER.error(err)
            raise utils.InvalidUsage(err, status_code=500)

    # process special returns
    if return_type == 'http':
        return flask.Response(
            response=json.dumps(identity, default=json_util.default),
            status=200,
            mimetype='application/json'
        )

    return identity


def token_to_object(request, strict=True):
    """ Processes the "Authorization" param in the header and returns an http
    response OR a user object. Requires the application's initialized JWT to
    work. """

    # first, get the token or bail
    auth_token = request.headers.get("Authorization", None)
    if auth_token is None:
        msg = "'Authorization' header missing!"
        LOGGER.error(msg)
        raise utils.InvalidUsage(msg, status_code=401)

    # if strict, try to decode the token and return a user object
    if strict:
        user = token_to_identity(auth_token)
        return User(_id=user["_id"]["$oid"])

    # otherwise, return a user object straight from the token
    user = refresh_authorization(auth_token)
    return User(_id=user["_id"])
