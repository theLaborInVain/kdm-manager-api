"""

    Basic methods for working with users and authentication live here.

    The whole first half of this module is laziness/convenience methods for
    working with users. There is a TON of stuff here, so check here first before
    rummaging about in utils.

    The class definition for the User object (which is kind of a big deal) lives
    here as well (all the way at the bottom of the file).

"""

# standard library imports
from bson import json_util
from bson.objectid import ObjectId
from copy import copy
from datetime import datetime, timedelta
import gridfs
import os
import pickle
import random
import socket
import string
from urllib.parse import urlparse

# third party imports
from dateutil.relativedelta import relativedelta
from flask import Response, request
from hashlib import md5
import json
import jwt
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash

# local imports
from app import models, utils
from app.models import user_preferences
from app.models.settlements import Settlement


# laaaaaazy
logger = utils.get_logger()
secret_key = utils.settings.get("api","secret_key","private")


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
    U = None

    # grab the user's MDB document, but DO NOT initialize the User:
    user = utils.mdb.users.find_one({"login": username})

    # if we have a user dict, do our comparisons and set U to be an
    #   initialized User object if they succeed:
    if user is not None:
        if check_password_hash(user['password'], password):
            U = User(_id=user["_id"])
        else:
            try:
                if safe_str_cmp(user["password"], md5(password.encode()).hexdigest()):
                    U = User(_id=user["_id"])
            except UnicodeEncodeError as e:
                raise utils.InvalidUsage(e)

    # timestamp this authentication
    if U is not None:
        U.set_latest_authentication()

    return U



def check_authorization(token):
    """ Tries to decode 'token'. Returns an HTTP 200 if it works, returns a 401
    if it doesn't. """

    try:
        jwt.decode(token, secret_key, verify=True)
        return utils.http_200
    except Exception as e:
        decoded = json.loads(jwt.decode(token, secret_key, verify=False)["identity"])
        logger.info("[%s (%s)] authorization check failed: %s!" % (decoded["login"], decoded["_id"]["$oid"], e))
        return utils.http_401


def get_user_id_from_email(email):
    """ Pulls the user from the MDB (or dies trying). Returns its email. """

    u = utils.mdb.users.find_one({'login': email.lower().strip()})
    if u is None:
        raise AttributeError("Could not find user data for %s" % email)
    return u['_id']


def refresh_authorization(expired_token):
    """ Opens an expired token, gets the login and password hash, and checks
    those against mdb. If they match, we return the user. This is what is
    referred to, in the field, as "meh--good enough" security.

    If you find yourself getting None back from thi sone, it's because your
    user changed his password.
    """

    decoded = jwt.decode(expired_token, secret_key, verify=False)
    user = dict(json.loads(decoded["identity"]))
    login = user["login"]
    pw_hash = user["password"]

    return utils.mdb.users.find_one({"login": login, "password": pw_hash})


def reset_password():
    """ Checks out an incoming recovery code and, if everything looks OK, loads
    up the user, changes its password, removes the code from the user and saves
    it back to the mdb. """

    user_login = request.get_json().get('username', None)
    new_password = request.get_json().get('password', None)
    recovery_code = request.get_json().get('recovery_code', None)

    for v in [user_login, new_password, recovery_code]:
        if v is None:
            return Response(response="Password reset requests require a login, password and a recovery code.", status=400)

    user = utils.mdb.users.find_one({'login': user_login, 'recovery_code': recovery_code})
    if user is None:
        return Response(
            response="The password recovery code supplied is not valid for user '%s'." % (user_login),
            status="400"
        )

    U = User(_id = user["_id"])
    del U.user['recovery_code']
    U.update_password(new_password)
    return utils.http_200


def initiate_password_reset():
    """ Attempts to start the mechanism for resetting a user's password.
    Unlike a lot of methods, this one handles the whole request processing and
    is very...self-contained. """

    # first, validate the post
    incoming_json = request.get_json()
    user_login = incoming_json.get('username', None)
    if user_login is None:
        return Response(
            response = "A valid user email address must be included in password reset requests!",
            status = 400
        )

    # normalize emails issue #501
    user_login = user_login.strip().lower()

    # next, validate the user
    user = utils.mdb.users.find_one({"login": user_login})
    if user is None:
        return Response(
            response = "'%s' is not a registered email address." % user_login,
            status = 404
        )

    # if the user looks good, set the code
    U = User(_id=user["_id"])
    user_code = U.set_recovery_code()

    # support for applications with their own URLs
    incoming_app_url = incoming_json.get('app_url', None)
    if incoming_app_url is not None:
        application_url = incoming_app_url
        parsed = urlparse.urlsplit(incoming_app_url)
        netloc = parsed.scheme + "://" + parsed.netloc
    else:
        netloc = utils.get_application_url()
        application_url = utils.get_application_url()

    # finally, send the email to the user
    try:
        tmp_file = os.path.join(utils.settings.get("api","cwd"), "html/password_recovery.html")
        msg = string.Template(file(tmp_file, "rb").read())
        msg = msg.safe_substitute(login=user_login, recovery_code=user_code, app_url=application_url, netloc=netloc)
        e = utils.mailSession()
        e.send(recipients=[user_login], html_msg=msg)
    except Exception as e:
        logger.error(e)
        raise

    # exit 200
    return utils.http_200


def jwt_identity_handler(payload):
    """ Bounces the authentication request payload off of the user collection.
    Returns a user object if "identity" in the request exists. """

    u_id = payload["identity"]
    user = utils.mdb.users.find_one({"_id": ObjectId(u_id)})

    if user is not None:
        U = User(_id=user["_id"])
        return U.serialize()

    return utils.http_404


def token_to_object(request, strict=True):
    """ Processes the "Authorization" param in the header and returns an http
    response OR a user object. Requires the application's initialized JWT to
    work. """

    # first, get the token or bail
    auth_token = request.headers.get("Authorization", None)
    if auth_token is None:
        msg = "'Authorization' header missing!"
        logger.error(msg)
        raise utils.InvalidUsage(msg, status_code=401)

    # now, try to decode the token and get a dict
    try:
        if strict:
            decoded = jwt.decode(auth_token, secret_key, verify=True)
            user_dict = dict(json.loads(decoded["identity"]))
            return User(_id=user_dict["_id"]["$oid"])
        else:
            user_dict = refresh_authorization(auth_token)
            return User(_id=user_dict["_id"])
    except jwt.DecodeError:
        logger.error("Incorrectly formatted token!")
        logger.error("Token contents: |%s|" % auth_token)
    except Exception as e:
        logger.exception(e)

    raise utils.InvalidUsage("Incoming JWT could not be processed!", status_code=422)


#
#   import_user method here! This is mostly called by admin methods, e.g. clone
#

def import_user(user_data=None):
    """ Import a user from a pickle to the local mdb.

    The 'user_data' arg can be either a pickle on the file system or a
    string representation of a pickle.
    """

    # coerce incoming data to dict or die trying.
    if isinstance(user_data, bytes):
        data = pickle.loads(user_data, encoding='bytes')

    if os.path.isfile(user_data):
        data = pickle.load(open(user_data, 'rb'))

    if data is None:
        raise ValueError("'%s' does not appear to be a pickle!" % user_data)

    # clean up the raw data
    for foreign_attr in ['current_session']:
        if data[b'user'].get(foreign_attr, False):
            del data[b'user'][foreign_attr]

    # start the import and check to see if we're doing something stupid
    msg = "Importing user %s [%s]" % (
        data[b'user']['login'],
        data[b'user']['_id']
    )
    logger.warn(msg)

    try:
        new_user_oid = utils.mdb.users.save(data[b'user'])
    except pymongo.errors.DuplicateKeyError:
        err = "User login '%s' exists under a different user ID!"
        raise pymongo.errors.DuplicateKeyError(err)

    # private method to load individual assets
    def import_user_assets(asset_name):
        """ Helper function to import assets generically.

        The 'asset_name' arg should be something like "settlement_events" or
        "survivors" or "settlements", i.e. one of the keys in the incoming
        'assets_dict' dictionary (called 'data' here). """

        imported_assets = 0
        logger.warn("Importing %s assets..." % asset_name)
        for asset in data[bytes(asset_name, 'utf-8')]:
            imported_assets += 1
            utils.mdb[asset_name].save(asset)
        logger.warn("%s %s assets imported." % (imported_assets, asset_name))

    # load the important user assets to local
    import_user_assets("settlements")
    import_user_assets("settlement_events")
    import_user_assets("survivors")

    # check for orphan survivors (i.e. ones with no settlement)
    for survivor in utils.mdb.survivors.find():
        if utils.mdb.settlements.find_one(
            {"_id": survivor["settlement"]}
        ) is None:
            logger.error("Survivor %s belongs to a non-existent settlement (%s)!" % (
                survivor['_id'], survivor['settlement']
                )
            )
            logger.warn("Removing survivor %s from mdb..." % (survivor["_id"]))
            utils.mdb.survivors.remove({"_id": survivor["_id"]})

    # next import avatars
    imported_avatars = 0
    for avatar in data[b"avatars"]:
        if gridfs.GridFS(utils.mdb).exists(avatar[b"_id"]):
            gridfs.GridFS(utils.mdb).delete(avatar[b"_id"])
            logger.info("Removed object %s from local GridFS." % avatar[b"_id"])
            gridfs.GridFS(utils.mdb).put(
                avatar[b"blob"],
                _id=avatar[b"_id"],
                content_type=avatar[b"content_type"],
                created_by=avatar[b"created_by"],
                created_on=avatar[b"created_on"]
            )
            imported_avatars += 1
        logger.info("Imported %s avatars!" % imported_avatars)

    # legacy webapp: clean up sessions
    culled = utils.mdb.sessions.remove({"login": data[b"user"]["login"]})
    if culled['n'] > 0:
        logger.info(
            "Removed %s session(s) belonging to incoming user!" % culled['n']
        )

    return new_user_oid


#
#   The big User object starts here
#

class User(models.UserAsset):
    """ This is the main controller for all user objects. """

    def __repr__(self):
        return "[%s (%s)]" % (self.user["login"], self._id)


    def __init__(self, *args, **kwargs):
        self.collection="users"
        self.object_version=0.24
        models.UserAsset.__init__(self,  *args, **kwargs)

        # JWT needs this
        self.id = str(self.user["_id"])

        # baseline/normalize
        self.perform_save = False
        self.baseline()
        self.bug_fixes()
        self.normalize()

        # check temporary users for expiration
        if self.user['subscriber']['level'] >= 3:
            self.check_subscriber_expiration()

        # random initialization methods
        self.set_current_settlement()

        # assets
        self.Preferences = user_preferences.Assets()


    def new(self):
        """ Creates a new user based on request.json values. Like all UserAsset
        'new()' methods, this one returns the new user's MDB _id when it's done.
        """

        self.logger.info("Creating new user...")
        self.check_request_params(['username','password'])

        # clean up the incoming values so that they conform to our data model
        username = self.params["username"].strip().lower()
        password = self.params["password"].strip()

        # do some minimalistic validation (i.e. rely on front-end for good data)
        #   and barf if it fails #separationOfConcerns

        msg = "The email address '%s' does not appear to be a valid email address!" % username
        if not '@' in username:
            raise utils.InvalidUsage(msg)
        elif not '.' in username:
            raise utils.InvalidUsage(msg)

        # make sure the new user doesn't already exist

        msg = "The email address '%s' is already in use by another user!" % username
        if utils.mdb.users.find_one({'login': username}) is not None:
            raise utils.InvalidUsage(msg)


        # now do it
        self.user = {
            'created_on': datetime.now(),
            'login': username,
#            'password': md5(password).hexdigest(),
            'password': generate_password_hash(password),
            'preferences': {},
            'collection': {"expansions": []},
            'notifications': {},
            'subscriber': {'level': 0},
        }
        self._id = utils.mdb.users.insert(self.user)
        self.load()
        logger.info("New user '%s' created!" % username)

        return self.user["_id"]


    def serialize(self, return_type=None):
        """ Creates a dictionary meant to be converted to JSON that represents
        everything that the front-end might need to know about a user. """

        output = self.get_serialize_meta()

        # check if this is an application admin
        if 'admin' in self.user.keys():
            output['is_application_admin'] = True

        # now create the user dict (analogous to 'sheet' in asset exports)
        output["user"] = self.user

        # basics; all views, generic UI/UX stuff
        output["user"]["age"] = self.get_age()
        output['user']['gravatar_hash'] = md5(self.user['login'].encode('utf-8')).hexdigest()
        output["user"]["settlements_created"] = utils.mdb.settlements.find({'created_by': self.user['_id'], 'removed': {'$exists': False}}).count()
        output["user"]["survivors_created"] = utils.mdb.survivors.find({'created_by': self.user['_id']}).count()
        output['user']['subscriber'] = self.get_subscriber_attributes()

        output['user']['preferences'] = self.get_preferences()

        # items common to dashboard and admin_panel
        if return_type in ['dashboard']:
            output["preferences"] = self.get_preferences('dashboard')
            output["dashboard"] = {}
            output["dashboard"]["friends"] = self.get_friends(return_type=list)
            output["dashboard"]["campaigns"] = self.get_settlements(return_type='list_of_dicts', qualifier='player')
            output["dashboard"]["settlements"] = self.get_settlements(return_type='list_of_dicts')

        # punch the user up if we're returning to the admin panel
        if return_type in ['admin_panel']:
            output['user']["latest_activity_age"] = self.get_latest_activity(return_type='age')
            output["user"]["has_session"] = self.has_session()
            output["user"]["is_active"] = self.is_active()
            output['user']["friend_list"] = self.get_friends(list)
            output['user']["current_session"] = utils.mdb.sessions.find_one({"_id": self._id})
            output["user"]["survivors_created"] = self.get_survivors(return_type=int)
            output["user"]["survivors_owned"] = self.get_survivors(qualifier="owner", return_type=int)
            output["user"]["settlements_administered"] = self.get_settlements(qualifier="admin", return_type=int)
            output["user"]["campaigns_played"] = self.get_settlements(qualifier="player", return_type=int)

        # user assets
#        output["user_assets"] = {}
#        output["user_assets"]["survivors"] = self.get_survivors(return_type=list)


        if return_type in ['admin_panel','create_new',dict]:
            return output

        return json.dumps(output, default=json_util.default)


    def jsonize(self):
        """ Returns JSON of the user's MDB dict. """
        return json.dumps(self.user, default=json_util.default)


    #
    #   set/update/modify methods
    #

    def set_attrib(self):
        """ Parses and processes request JSON and attempts to set user attrib
        key/value pairs. Returns an http response. """

        allowed_keys = ["current_settlement"]
        failed_keys = []
        success_keys = []

        # first, check the keys to see if they're legit; bail if any of them is
        #   bogus, i.e. bail before we attempt to do anything.
        for k in self.params.keys():
            if k not in allowed_keys:
                self.logger.warn("Unknown key '%s' will not be processed!" % k)
                failed_keys.append(k)
            else:
                success_keys.append(k)

        # now, individual value handling for allow keys begins
        for k in success_keys:
            if k == "current_settlement":
                self.user[k] = ObjectId(self.params[k])
            else:
                self.user[k] = self.params[k]
            self.logger.debug("Set {'%s': '%s'} for %s" % (k, self.params[k], self))

        # build the response message
        msg = "OK!"
        if len(success_keys) >= 1:
            msg += " User attributes successfully updated: %s." % (utils.list_to_pretty_string(success_keys, quote_char="'"))
        if len(failed_keys) >= 1:
            msg += " The following user attributes are NOT supported and could not be updated: %s." % (utils.list_to_pretty_string(failed_keys, quote_char="'"))

        # finally, assuming we're still here, go ahead and save/return 200
        self.save()

        return Response(response=msg, status=200)


    def set_current_settlement(self):
        """ This should probably more accurately be called 'default_current_settlement'
        or something along those lines, because it basically tries a series of
        back-offs to set a settlement for a user who hasn't got one set. """

        if "current_settlement" in self.user.keys():
            return True

        settlements = self.get_settlements()
        if len(settlements) != 0:
            self.user["current_settlement"] = settlements[0]["_id"]
            self.logger.warn("Defaulting 'current_settlement' to %s for %s" % (settlements[0]["_id"], self))
        elif len(settlements) == 0:
            self.logger.debug("User %s does not own or administer any settlements!" % self)
            p_settlements = self.get_settlements(qualifier="player")
            if len(p_settlements) != 0:
                self.user["current_settlement"] = p_settlements[0]["_id"]
                self.logger.warn("Defaulting 'current_settlement' to %s for %s" % (p_settlements[0]["_id"], self))
            elif len(p_settlements) == 0:
                self.logger.warn("Unable to default a 'current_settlement' value for %s" % self)
                self.user["current_settlement"] = None

        self.save()


    def set_latest_action(self, activity_string=None, ua_string=None, save=True):
        """ Updates the user's 'latest_activity' string and saves the user back
        to the MDB. Supercedes the BS version of this that went on in the legacy
        webapp (i.e. between session.py and the assets.User.mark_usage() method).
        """

        self.user['latest_action'] = activity_string
        self.user['latest_activity'] = datetime.now()
        self.user['latest_user_agent'] = ua_string
        if save:
            self.save(verbose=False)


    def set_latest_authentication(self, timestamp=None, save=True):
        """ Sets the self.user['latest_authentication'] value to the datetime
        object passed in the 'timestamp' kwarg. If 'timestamp' is none, defaults
        to datetime.now(). """

        self.user['latest_authentication'] = datetime.now()
        if save:
            self.save(verbose=False)




    def set_patron_attributes(self, level=None, beta=None):
        """ Deprecated in release 1.0.0. Remove at 1.0.1 and later. """
        raise RuntimeError('This method is not supported in the 1.0.0 release!')


    def set_preferences(self):
        """ Expects a request context and will not work without one. Iterates
        thru a list of preference handles and sets them. """

        self.check_request_params(['preferences'])
        pref_list = self.params['preferences']
        if type(pref_list) != list:
            raise utils.InvalidUsage("set_preferences() endpoint requires 'preferences' to be a list!")

        for pref_dict in pref_list:
            handle = pref_dict.get('handle',None)
            value = pref_dict.get('value',None)
            for p in [handle, value]:
                if p is None:
                    raise utils.InvalidUsage("Nah, bro: individual preference hashes/dicts should follow this syntax: {handle: 'preference_handle', value: true}")
            self.user['preferences'][handle] = value
#            self.logger.info("%s Set '%s' = %s'" % (request.User.login, handle, value))

        self.save()


    def set_recovery_code(self):
        """ Sets self.user['recovery_code'] to a random value. Returns the code
        when it is called. """

        r_code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(30))
        self.user["recovery_code"] = r_code
        self.logger.info("'%s set recovery code '%s' for their account" % (self, r_code))
        self.save()
        return self.user["recovery_code"]


    def set_subscriber_level(self, level=None):
        """ Supersedes set_patron_attributes() in the 1.0.0 release. Sets the
        subscriber level, i.e. self.user['subscriber']['level'] value, which, in
        turn, sets the self.user['subscriber']['desc'] value using the
        subscribers block of settings.cfg.
        """

        # sanity check first
        if level is None:
            raise TypeError("set_subscriber_level() requires an int!")

        if self.user['subscriber']['level'] == level:
            self.logger.warn(
                '%s Subscriber level is already %s. Ignoring...' % (
                    self,
                    self.user['subscriber']['level'],
                )
            )
            return True

        # now make the change
        if self.user['subscriber'].get('created_on', None) is None:
            self.user['subscriber']['created_on'] = datetime.now()

        self.user['subscriber']['level'] = level
        self.user['subscriber']['desc'] = utils.settings.get(
            'subscribers',
            'level_%s' % level
        )
        self.user['subscriber']['updated_on'] = datetime.now()

        self.logger.info('%s Set subscriber level to %s...' % (self, level))
        self.save()


    def update_password(self, new_password=None):
        """ Changes the user's password. Saves. """

        if new_password is None:
            self.check_request_params(['password'])
            new_password = self.params['password']

        if new_password is None:
            raise Exception("New password cannot be None type!")

        self.user['password'] = generate_password_hash(new_password)
        self.logger.info("%s Changed password!" % self)
        self.save()


    #
    #   toggle methods
    #

    def toggle_admin_status(self, save=True):
        """ Toggles the 'admin' attribute on/off. Use 'kwarg' to save (or not)
        after the toggle is done. """

        if 'admin' in self.user.keys():
            del self.user["admin"]
        else:
            self.user["admin"] = datetime.now()
        self.save()


    #
    #   Collection Management - manage the user's asset collection
    #

    def add_expansion_to_collection(self, handle=None):
        """ Adds an expansion handle to self.user['collection']['expansions']
        list. Logs it. """

        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params['handle']

        if handle in self.user['collection']['expansions']:
            self.logger.warn("%s Expansion handle '%s' is already in the user's collection. Ignoring..." % (self, handle))
            return True

        self.user['collection']['expansions'].append(handle)
        self.save()


    def rm_expansion_from_collection(self, handle=None):
        """ Adds an expansion handle to self.user['collection']['expansions']
        list. Logs it. """

        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params['handle']

        if handle not in self.user['collection']['expansions']:
            self.logger.warn("%s Expansion handle '%s' is not in the user's collection. Ignoring..." % (self, handle))
            return True

        self.user['collection']['expansions'].remove(handle)
        self.save()


    #
    #   query/assess methods
    #

    def has_session(self):
        """ Returns a bool representing whether there is a session in the mdb
        for the user."""

        if utils.mdb.sessions.find_one({"created_by": self.user["_id"]}) is not None:
            return True
        return False


    def is_admin(self):
        """ Returns a bool representing whether the user is an API admin. This
        is NOT THE SAME as being a settlement admin (see below)."""

        return bool(self.user.get('admin', False))


    def is_active(self):
        """ Returns a bool representing whether the user has logged an activity
        within our 'active user' horizon/cutoff window. """

        if not self.has_session():
            return False

        minutes_since_latest = self.get_latest_activity('minutes')
        active_horizon = utils.settings.get("application","active_user_horizon")
        if minutes_since_latest <= active_horizon:
            return True

        return False



    #
    #   get methods
    #

    def get_age(self, return_type="years"):
        """ Returns the user's age. """

        return utils.get_time_elapsed_since(self.user["created_on"], 'age')


    def get_subscriber_attributes(self):
        """ Returns a dictionary of subscriber information. """

        self.user['subscriber'].update(
            {'age': utils.get_time_elapsed_since(
                self.user['subscriber'].get('created_on', datetime.now()),
                'age')
            }
        )
        return self.user['subscriber']


    def get_preference(self, p_key):
        """ Ported from the legacy app: checks the user's MDB document for the
        'preference' key and returns its value (which is a bool).

        If the key is NOT present on the user's MDB document, return the default
        value from utils.settings.cfg. """

        default_value = utils.settings.get("users", p_key)

        if "preferences" not in self.user.keys():
            return default_value

        if p_key not in self.user["preferences"].keys():
            return default_value

        return self.user["preferences"][p_key]


    def get_preferences(self, return_type=None):
        """ Not to be confused with self.get_preference(), which gets a bool for
        a single preference handle, this renders a JSON-ish return meant to be
        included in the self.serialize() call (and ultimately represented on the
        application dashboard. """

        if return_type == 'dashboard':
            groups = set()
            for p_dict in self.Preferences.get_dicts():
                groups.add(p_dict['sub_type'])

            output = []
            for g_name in sorted(groups):
                g_handle = g_name.lower().replace(" ","_")
                g_dict = {'name': g_name, 'handle': g_handle, 'items': []}
                for p_dict in self.Preferences.get_dicts():
                    if p_dict['sub_type'] == g_name:
                        election = self.get_preference(p_dict['handle'])
                        p_dict['value'] = election
                        g_dict['items'].append(p_dict)
                output.append(g_dict)

            return output

        output = copy(self.user['preferences'])
        for p_dict in self.Preferences.get_dicts():
            if self.user['preferences'].get(p_dict['handle']) is None:
                output[p_dict['handle']] = p_dict['default']
        return output


    def get_friends(self, return_type=None):
        """ Returns all of the user's friends (i.e. people he plays in campaigns
        with) as objects. """

        friend_ids      = set()
        friend_emails   = set()

        campaigns = self.get_settlements(qualifier="player")
        if len(campaigns) > 0:
            for s in campaigns:
                friend_ids.add(s["created_by"])
                c_survivors = utils.mdb.survivors.find({"settlement": s["_id"]})
                for survivor in c_survivors:
                    friend_ids.add(survivor["created_by"])
                    friend_emails.add(survivor["email"])

            # you can't be friends with yourself
            if self.user["_id"] in friend_ids:
                friend_ids.remove(self.user["_id"])
            if self.user["login"] in friend_emails:
                friend_emails.remove(self.user["login"])

            # they're only your friend if they're a registered email
            friends = utils.mdb.users.find({"$or":
                [
                    {"_id": {"$in": list(friend_ids)}},
                    {"login": {"$in": list(friend_emails)}},
                ]
            })
        else:
            friends = None

        if return_type == int:
            if friends is not None:
                return friends.count()
            else:
                return 0
        elif return_type == list:
            if friends is None:
                return []
            else:
                return [f["login"] for f in friends]

        return friends


    def get_latest_activity(self, return_type=None):
        """ Returns the user's latest activity in a number of ways. Leave the
        'return_type' kwarg blank for a datetime stamp.
        """

        la = self.user["latest_activity"]

        if return_type is not None:
            return utils.get_time_elapsed_since(la, return_type)

        return la


    def get_settlements(self, qualifier=None, return_type=None):
        """ By default, this returns all settlements created by the user. Use
        the qualifiers thus:

            'player' - returns all settlements where the user is a player or
                admin or whatever. This casts the widest possible net.
            'admin' - returns only the settlements where the user is an admin
                but is NOT the creator of the settlement.

        """

        if qualifier is None:
            settlements = utils.mdb.settlements.find({"$or": [
                {"created_by": self.user["_id"], "removed": {"$exists": False}, },
                {"admins": {"$in": [self.user["login"], ]}, "removed": {"$exists": False}, },
            ]})
        elif qualifier == "player":
            settlement_id_set = set()

            survivors = self.get_survivors(qualifier="player")
            for s in survivors:
                settlement_id_set.add(s["settlement"])

            settlements_owned = self.get_settlements()
            for s in settlements_owned:
                settlement_id_set.add(s["_id"])
            settlements = utils.mdb.settlements.find({"_id": {"$in": list(settlement_id_set)}, "removed": {"$exists": False}})
        elif qualifier == "admin":
            settlements = utils.mdb.settlements.find({
                "admins": {"$in": [self.user["login"]]},
                "created_by": {"$ne": self.user["_id"]},
                "removed": {"$exists": False},
            })
        else:
            raise Exception("'%s' is not a valid qualifier for this method!" % qualifier)


        # change settlements to a list so we can do python post-process
        settlements = list(settlements)


	# settlement age support/freemium wall
        # first, see if we even need to be here
        # MOVE ALL OF THIS OUT OF THIS METHOD ASAP
        sub_level = self.get_subscriber_level()
        if sub_level >= 1:
            pass
        else:
            for s in settlements:
                asset_age = datetime.now() - s['created_on']
                older_than_cutoff = asset_age.days > utils.settings.get(
                    'users','free_user_settlement_age_max'
                )
                if older_than_cutoff and self.user['_id'] == s['created_by']:
                    warn_msg = "%s settlement '%s' is more than %s days old!"
                    self.logger.warn(
                        warn_msg % (
                            self,
                            s['name'],
                            utils.settings.get(
                                'users',
                                'free_user_settlement_age_max'
                                )
                            )
                        )
                    msg = utils.html_file_to_template(
                        'auto_remove_settlement.html'
                    )

                    # in case the admin panel hits it before the actual user
                    if not hasattr(request, 'User'):
                        request.User = utils.noUser()

                    msg = msg.safe_substitute(
                        settlement_name=s['name'],
                        settlement_age = asset_age.days,
                        settlement_dict = s,
                        user_email = request.User.login,
                        user_id = request.User._id,
                    )
                    e = utils.mailSession()
                    e.send(
                        subject="Settlement auto-remove! [%s]" % socket.getfqdn(),
                        recipients=utils.settings.get('server','alert_email').split(','),
                        html_msg=msg
                    )
                    s['removed'] = datetime.now()
                    utils.mdb.settlements.save(s)
                    settlements.remove(s)

        #
        # now start handling returns
        #

        if return_type == int:
            return len(settlements)
        elif return_type == list:
            output = [s["_id"] for s in settlements]
            return output
        elif return_type == 'list_of_dicts':
            return settlements
        elif return_type == "asset_list":
            output = []
            for s in settlements:
                try:
                    S = Settlement(_id=s["_id"], normalize_on_init=False)
                    sheet = json.loads(S.serialize('dashboard'))
                    output.append(sheet)
                except Exception as e:
                    logger.error("Could not serialize %s" % s)
                    logger.exception(e)
                    raise

            return output

        return settlements


    def get_subscriber_level(self):
        """ Returns the user's subscriber level as an int. """
        return self.user['subscriber']['level']


    def get_survivors(self, qualifier=None, return_type=None):
        """ Returns all of the survivors created by the user. """

        if qualifier is None:
            survivors = utils.mdb.survivors.find({"$or": [
                {"created_by": self.user["_id"], "removed": {"$exists": False}},
                {"email": self.user["login"], "removed": {"$exists": False}},
            ]})

        elif qualifier == "player":
            survivors = utils.mdb.survivors.find({"$or": [
                {"created_by": self.user["_id"], "removed": {"$exists": False}},
                {"email": self.user["login"], "removed": {"$exists": False}},
            ]})
        elif qualifier == "owner":
            survivors = utils.mdb.survivors.find({
                "email": self.user["login"],
                "created_by": {"$ne": self.user["_id"]},
                "removed": {"$exists": False},
            })
        else:
            raise Exception("'%s' is not a valid qualifier for this method!" % qualifier)

        if return_type == int:
            return survivors.count()
        elif return_type == list:
            output = [s["_id"] for s in survivors]
            output = list(set(output))
            return output

        return survivors


    #
    #   subscription methods
    #

    def check_subscriber_expiration(self):
        """ This method checks subscribers whose self.user['subscriber']
        'level' key is >= 3 and decides whether to expire them back to a
        zero. """

        # determine how many days old the subscription is, remembering that we
        #   can have re-subscriptions (i.e. use updated_on, rather than the
        #   created_on value for the start date)

        subscription_age = utils.get_time_elapsed_since(
            self.user["subscriber"]['updated_on'], units='days'
        )

        subscription_max = utils.settings.get(
            'subscribers',
            'level_' + str(self.user['subscriber']['level']) + '_expires'
        )

        expires_in = subscription_max - subscription_age

        if expires_in < 0:
            self.logger.warn('%s SUBSCRIPTION EXPIRED' % self)
            self.set_subscriber_level(0)


    #
    #   baseline/normalize
    #

    def baseline(self):
        """ Baseline the user record to our data model. """

        if not 'collection' in self.user.keys():
            self.user['collection'] = {"expansions": [], }
            self.logger.info("%s Baselined 'collection' key into user dict." % self)
            self.perform_save = True

        if not 'notifications' in self.user.keys():
            self.user['notifications'] = {}
            self.logger.info("%s Baselined 'notifications' key into user dict." % self)
            self.perform_save = True



    def bug_fixes(self):
        """ Fix bugs! """
        pass


    def normalize(self):
        """ Force/coerce the user into compliance with our data model for users.
        """

        if not 'preferences' in self.user.keys():
            self.user['preferences'] = {'preserve_sessions': False}
            self.logger.warn("%s has no 'preferences' attrib! Normalizing..." % self)
            self.perform_save = True

        # 'patron' becomes 'subscriber' in the 1.0.0 release
        if 'patron' in self.user.keys():
            self.user['subscriber'] = self.user['patron']
            del self.user['patron']
            self.logger.warn("%s Normalized 'patron' to 'subscriber'!" % self)
            self.perform_save = True

        if not 'subscriber' in self.user.keys():
            self.user['subscriber'] = {'level': 0}
            self.logger.warn("%s Added 'subscriber' dict to user!" % self)
            self.perform_save = True

        if self.perform_save:
            self.save()




    #
    #   Do not write model methods below this one.
    #


    def request_response(self, action=None):
        """ Initializes params from the request and then response to the
        'action' kwarg appropriately. This is the ancestor of the legacy app
        assets.Survivor.modify() method. """

        self.get_request_params()

        if action == "get":
            return Response(response=self.serialize(), status=200, mimetype="application/json")
        elif action == "dashboard":
            return Response(response=self.serialize('dashboard'), status=200, mimetype="application/json")
        elif action == "set":
            return self.set_attrib()

        elif action == "update_password":
            self.update_password()
        elif action == 'set_preferences':
            self.set_preferences()

        # collection management
        elif action == "add_expansion_to_collection":
            self.add_expansion_to_collection()
        elif action == "rm_expansion_from_collection":
            self.rm_expansion_from_collection()


        else:
            # unknown/unsupported action response
            self.logger.warn("Unsupported survivor action '%s' received!" % action)
            return utils.http_400


        # finish successfully
        return Response(response="Completed '%s' action successfully!" % action, status=200)





# ~fin
