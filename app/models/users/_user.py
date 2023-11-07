"""

    The class definition for the User object (which is kind of a big deal) lives
    here.

    Over time, this needs to get way simpler and/or have some methods moved into
    other files in the models.users module, etc.

"""

# standard library imports
from datetime import datetime
from hashlib import md5
import io
import json
import pickle
import random
import socket
import string

# second-party imports
from bson import json_util
from bson.objectid import ObjectId
from dateutil.tz import tzlocal
import flask
import gridfs
from werkzeug.security import (
    generate_password_hash,
)

# local imports
from app import API, utils

from .._decorators import admin_only, web_method
from .._data_model import DataModel
from .._user_asset import UserAsset


class User(UserAsset):
    """ This is the main controller for all user objects. """

    DATA_MODEL = DataModel('user')
    DATA_MODEL.add('login', str)
    DATA_MODEL.add('password', str)
    DATA_MODEL.add('preferences', dict)
    DATA_MODEL.add('collection', dict, {"expansions": []})
    DATA_MODEL.add('notifications', dict)
    DATA_MODEL.add('subscriber', dict, {'level': 0})
    DATA_MODEL.add('verified_email', bool)
    DATA_MODEL.add('email_verification_code', str)
    DATA_MODEL.add('favorite_survivors', str)


    def __repr__(self):
        """ Custom repr for User objects. """
        try:
            return "[%s (%s)]" % (self.user["login"], self._id)
        except Exception as exception:
            self.logger.debug(exception)
            return super().__repr__()


    def __init__(self, *args, **kwargs):
        self.collection="users"
        UserAsset.__init__(self,  *args, **kwargs)

        # JWT needs this
        self.id = str(self.user["_id"])

        # baseline/normalize
        self.perform_save = False
        self.baseline()
        self.bug_fixes()
        self.normalize()

        # check temporary users for expiration
        if (
            int(self.user['subscriber']['level']) > 2 and
            int(self.user['subscriber']['level']) < 6
        ):
            self.check_subscriber_expiration()

        # random initialization methods
        self.set_current_settlement()

        # finally, if it's actually them, record that the user is using the API
        if (
            flask.request and
            hasattr(flask.request, 'User') and
            self.user.get('login', None) is not None and
            flask.request.User.user['login'] == self.user.get('login', None)
        ):
            self.set_latest_action(
                activity_string = flask.request.path,
                ua_string = flask.request.user_agent.string
            )


    def load(self):
        """ Calls the base class load() method and then sets self.login. """

        super().load()
        self.login = self.user['login']


    def new(self):
        """ Creates a new user based on request.json values. Like all UserAsset
        'new()' methods, this one returns the new user's MDB _id when it's done.
        """

        self.logger.info("Creating new user...")
        self.check_request_params(['username', 'password'])

        # clean up the incoming values so that they conform to our data model
        username = self.params["username"].strip().lower()
        password = self.params["password"].strip()

        # do some minimalistic validation (i.e. rely on front-end for good data)
        #   and barf if it fails #separationOfConcerns
        msg = "The email address '%s' is not a valid email address!" % username
        if not '@' in username:
            raise utils.InvalidUsage(msg)
        if not '.' in username:
            raise utils.InvalidUsage(msg)

        # make sure the new user doesn't already exist
        msg = "The email address '%s' is in use by another user!" % username
        if utils.mdb.users.find_one({'login': username}) is not None:
            raise utils.InvalidUsage(msg)

        # now do it
        self.user = self.DATA_MODEL.new()
        self.user.update({
            'created_on': datetime.now(tzlocal()),
            'login': username,
            'password': generate_password_hash(password),
        })
        self._id = utils.mdb.users.insert(self.user)

        self.load() # call load to set self.login, etc.

        self.logger.info("New user '%s' created!", username)

        return self.user["_id"]


    @web_method
    @admin_only
    def export(self, return_type=None):
        """ This supercedes everything that happens in the legacy webapp's
        'get_user' CGI and facilitates "cloning" users from one environment
        to another.

        All returns should be flask responses.

        THIS CODE WAS ALL PORTED FROM THE LEGACY WEBAPP ON 2020-12-09 AND
        IS IN NEED OF A REFACTOR. PLEASE REFACTOR IT.
        """

        created_by = {'created_by': self.user['_id']}
        assets_dict = {
            "user": self.user,
            "settlements": list(utils.mdb.settlements.find(created_by)),
            "settlement_events": list(
                utils.mdb.settlement_events.find(created_by)
            ),
            "survivor_notes": list(utils.mdb.survivor_notes.find(created_by)),
            "survivors": [],
            "avatars": [],
        }

        # get all survivors (including those created by other users) for the
        #   user's settlements; then get all survivors created by the user.
        for settlement_rec in assets_dict["settlements"]:
            assets_dict["settlement_events"].extend(
                utils.mdb.settlement_events.find(
                    {"settlement_id": settlement_rec["_id"]}
                )
            )
            survivors = utils.mdb.survivors.find(
                {"settlement": settlement_rec["_id"]}
            )
            assets_dict["survivors"].extend(survivors)

        other_survivors = utils.mdb.survivors.find(created_by)
        for survivor_rec in other_survivors:
            if survivor_rec not in assets_dict["survivors"]:
                assets_dict["survivors"].append(survivor_rec)

        msg = "%s Exported %s survivors!"
#        self.logger.debug(msg % (self, len(assets_dict["survivors"])))

        # now we have to go to GridFS to get avatars
        for s in assets_dict["survivors"]:
            if "avatar" in s.keys():
                try:
                    img = gridfs.GridFS(utils.mdb).get(ObjectId(s["avatar"]))
                    img_dict = {
                        "blob": img.read(),
                        "_id": ObjectId(s["avatar"]),
                        "content_type": img.content_type,
                        "created_by": img.created_by,
                        "created_on": img.created_on,
                    }
                    assets_dict["avatars"].append(img_dict)
                except gridfs.errors.NoFile:
                    err = "Could not retrieve avatar for survivor %s"
                    self.logger.error(err, s["_id"])

        for key in assets_dict:
            msg = "%s Added %s '%s' assets to user export..."
            self.logger.debug(msg, self, len(assets_dict[key]), key)

        # now we (finally) do returns:
        if return_type in ['pickle', None]:
            dump = io.BytesIO()
            pickle.dump(assets_dict, dump)
            dump.seek(0)
            return flask.send_file(
                dump,
                as_attachment=True,
                attachment_filename='export.pickle',
                mimetype='application/octet-stream'
            )

        return assets_dict


    def tokenize(self):
        ''' Returns a version of the User object that DOES NOT include the
        user's recent history, so as not to hit the 4k limit on cookie size
        in most browsers. '''

        slim_record = {}
        for key in ['_id', 'login', 'password']:
            slim_record[key] = self.get_record()[key]

        return json.dumps(slim_record, default=json_util.default)


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

        # gravatar hash, which is determined programmatically
        output['user']['gravatar_hash'] = md5(
            self.user['login'].encode('utf-8')
        ).hexdigest()

        # count user assets created by the user
        output["user"]["settlements_created"] = utils.mdb.settlements.find(
            {'created_by': self.user['_id'], 'removed': {'$exists': False}}
        ).count()
        output["user"]["survivors_created"] = utils.mdb.survivors.find(
            {'created_by': self.user['_id']}
        ).count()

        output['user']['subscriber'] = self.get_subscriber_attributes()

        output['user']['preferences'] = self.user['preferences']

        # items common to dashboard and admin_panel
        if return_type in ['dashboard']:
            output["dashboard"] = {}
            output["dashboard"]["friends"] = self.get_friends(return_type=list)
            output["dashboard"]["campaigns"] = self.get_settlements(
                return_type='list_of_dicts', qualifier='player'
            )
            output["dashboard"]["settlements"] = self.get_settlements(
                return_type='list_of_dicts', qualifier='player'
            )

        # punch the user up if we're returning to the admin panel
        if return_type in ['admin_panel']:
            output['user']["latest_activity_age"] = self.get_latest_activity(
                return_type='age'
            )
            output["user"]["is_active"] = self.is_active()
            output['user']["friend_list"] = self.get_friends(list)
            output['user']["current_session"] = utils.mdb.sessions.find_one(
                {"_id": self._id}
            )
            output["user"]["survivors_created"] = self.get_survivors(
                return_type=int
            )
            output["user"]["survivors_owned"] = self.get_survivors(
                qualifier="owner", return_type=int
            )
            output["user"]["settlements_administered"] = self.get_settlements(
                qualifier="admin", return_type=int
            )
            output["user"]["campaigns_played"] = self.get_settlements(
                qualifier="player", return_type=int
            )

        if return_type in ['admin_panel','create_new',dict]:
            return output

        return json.dumps(output, default=json_util.default)


    # email verification

    @web_method
    def set_verified_email(self, new_value=None, save=True):
        """ Sets the verified email value. Expects a request context, but can
        be called directly. Fails if the authenticated user is not a.) the user
        being modified or b.) an API admin. """

        if not (
            flask.request.User.is_admin() or
            flask.request.User.user['login'] == self.user['login']
        ):
            err = "Only API administrators may verify other users' email!"
            raise utils.InvalidUsage(err)

        if new_value is None:
            self.check_request_params(['value'])
            new_value = self.params['value']

        self.user['verified_email'] = bool(new_value)
        self.logger.info('%s Set verified email to %s', self, new_value)

        if save:
            self.save()


    @web_method
    def send_verification_email(self):
        """ Sets a verification code; sends a verification email."""

        self.user['email_verification_code'] = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=23)
        )

        # figure out where the API target is
        api_destination = utils.get_application_url()
        if not API.config['ENVIRONMENT'].get('is_production', False):
            api_destination += ':%s' % API.config['PORT']

        msg = utils.html_file_to_template('verify_email_email.html')
        email_body = msg.safe_substitute(
            login=self.user['login'],
            netloc = utils.get_application_url(),
            apiloc = api_destination,
            verification_code = self.user['email_verification_code']
        )
        mail_sesh = utils.mailSession()
        mail_sesh.send(
            subject="KD:M API - email verification request",
            recipients=[self.user['login']],
            html_msg=email_body,
        )
        self.logger.info('Email verification request sent!')
        self.save()


    def verify_email_from_code(self, code):
        """ Non-web method; returns a bool if 'code' matches the user record's
        'email_verification_code' attribute. """

        if code == self.user.get('email_verification_code', None):
            del self.user['email_verification_code']
            self.set_verified_email(new_value=True) # saves by default
            return True

        return False


    #
    #   set/update/modify methods
    #

    @web_method
    def set_favorite_survivors(self, save=True):
        '''
        Requires a request context. Updates the user's favorite survivors list.

        We very intentionally DO NOT initialize survivors or settlements here,
        since we want to avoid expanding the footprint of this method to involve
        janitorial work around removed settlements/survivors, etc.
        '''

        self.check_request_params(['favorite_survivors'])
        new_favorites = self.params['favorite_survivors']

        add_list, rm_list = utils.list_compare(
            self.user['favorite_survivors'],
            new_favorites
        )

        if add_list != []:
            [self.user['favorite_survivors'].append(s_id) for s_id in add_list]
        if rm_list != []:
            [self.user['favorite_survivors'].remove(s_id) for s_id in rm_list]

        if save:
            self.save()


    def set_current_settlement(self):
        """
        This should probably more accurately be called
        'default_current_settlement' or something along those lines, because it
        basically tries a series of back-offs to set a settlement for a user
        who hasn't got one set.
        """

        if "current_settlement" in self.user.keys():
            return True

        settlements = self.get_settlements()
        if len(settlements) != 0:
            self.user["current_settlement"] = settlements[0]["_id"]
            msg = "Defaulting 'current_settlement' to %s for %s" % (
                settlements[0]["_id"], self
            )
            self.logger.warning(msg)
        elif len(settlements) == 0:
            p_settlements = self.get_settlements(qualifier="player")
            if len(p_settlements) != 0:
                self.user["current_settlement"] = p_settlements[0]["_id"]
                msg = "Defaulting 'current_settlement' to %s for %s" % (
                    p_settlements[0]["_id"], self
                )
                self.logger.warning(msg)
            elif len(p_settlements) == 0:
                msg = "Cannot set 'current_settlement' value for %s" % self
                self.logger.warning(msg)
                self.user["current_settlement"] = None

        self.save()


    def set_latest_action(self, activity_string=None, ua_string=None,
                            save=True):
        """ Updates the user's 'latest_activity' string and saves the user back
        to the MDB.

        Also saves the last 10 operations in self.user['activity_log'].
        """

        self.user['latest_action'] = activity_string
        self.user['latest_activity'] = datetime.now(tzlocal())
        self.user['latest_user_agent'] = ua_string

        if utils.get_api_client() is not None:
            self.user['latest_api_client'] = utils.get_api_client()

        # save the most recent 10 actions in the 'activity_log' list
        activity_tuple = (
            datetime.now(tzlocal()), utils.get_api_client(), activity_string
        )

        if self.user.get('activity_log', None) is None:
            self.user['activity_log'] = [activity_tuple]
        else:
            self.user['activity_log'].insert(0, activity_tuple)
            self.user['activity_log'] = self.user['activity_log'][:10]

        if save:
            self.save(verbose=True)


    def set_latest_authentication(self, save=True):
        """ Sets the self.user['latest_authentication'] value to datetime.now().
        Saves, optionally. """

        self.user['latest_authentication'] = datetime.now(tzlocal())
        if save:
            self.save(verbose=False)


    @web_method
    def set_notifications(self):
        """ Sets a notification handle to datetime.now(). POST the handle value
        'RESET' to reset the list. """

        self.check_request_params(['notifications'])
        notification_list = self.params['notifications']

        if not isinstance(notification_list, list):
            raise utils.InvalidUsage("This method requires a list of handles!")

        for n_handle in sorted(notification_list):
            if n_handle == 'RESET':
                self.user['notifications'] = {}
            else:
                self.user['notifications'][n_handle] = datetime.now(tzlocal())

        self.save()


    @web_method
    def set_preferences(self):
        """ Expects a request context and will not work without one. Iterates
        thru a list of preference handles and sets them. """

        self.check_request_params(['preferences'])
        pref_list = self.params['preferences']

        if not isinstance(pref_list, list):
            raise utils.InvalidUsage("'preferences' must be a list type!")

        for pref_dict in pref_list:
            handle = pref_dict.get('handle',None)
            value = pref_dict.get('value',None)
            for pref in [handle, value]:
                if pref is None:
                    err = (
                        "Invalid dict: {handle: %s, value: %s} "
                        "Preference hashes/dicts should follow this syntax: "
                        "{handle: 'preference_handle', value: true}"
                    ) % (handle, value)
                    raise utils.InvalidUsage(err)
            self.user['preferences'][handle] = value

        self.save()


    def set_recovery_code(self):
        """ Sets self.user['recovery_code'] to a random value. Returns the code
        when it is called. """

        r_code = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase + string.digits) for _ in range(30)
        )
        self.user["recovery_code"] = r_code

        msg = "'%s set recovery code '%s' for their account"
        self.logger.info(msg, self, r_code)

        self.save()

        return self.user["recovery_code"]


    @web_method
    @admin_only
    def set_subscriber_level(self, level=None):
        """ Supersedes set_patron_attributes() in the 1.0.0 release. Sets the
        subscriber level, i.e. self.user['subscriber']['level'] value, which, in
        turn, sets the self.user['subscriber']['desc'] value using the
        subscribers block of settings.cfg.
        """

        # support updates from params, but check if we're an admin
        if hasattr(self, 'params') and 'level' in self.params:
            level = self.params['level']
            if flask.request.User.user.get('admin', None) is None:
                raise utils.InvalidUsage('Only API admins can do this!')

        # sanity check first
        if level is None:
            raise TypeError("set_subscriber_level() requires an int!")

        if self.user['subscriber']['level'] == level:
            self.logger.warning(
                '%s Subscriber level is already %s. Ignoring...',
                self,
                self.user['subscriber']['level'],
            )
            return True

        # now make the change
        if self.user['subscriber'].get('created_on', None) is None:
            self.user['subscriber']['created_on'] = datetime.now(tzlocal())

        self.user['subscriber']['level'] = level
        self.user['subscriber']['desc'] = utils.settings.get(
            'subscribers',
            'level_%s' % level
        )
        self.user['subscriber']['updated_on'] = datetime.now(tzlocal())

        info = '%s subscriber level set to %s (admin: %s)'

        # September 2021: automatically set email to verified
#        self.set_verified_email(new_value=True, save=False)

        # log and save
        self.logger.info(info, self, level, self.user['login'])
        self.save()



    @web_method
    def update_password(self, new_password=None):
        """ Changes the user's password. Saves. """

        if new_password is None:
            self.check_request_params(['password'])
            new_password = self.params['password']

        if new_password is None:
            raise Exception("New password cannot be None type!")

        self.user['password'] = generate_password_hash(new_password)
        self.logger.info("%s Changed password!", self)
        self.save()


    #
    #   toggle methods
    #

    @admin_only
    def toggle_admin_status(self, save=True):
        """ Toggles the 'admin' attribute on/off. Use 'kwarg' to save (or not)
        after the toggle is done. """

        if 'admin' in self.user.keys():
            del self.user["admin"]
        else:
            self.user["admin"] = datetime.now(tzlocal())

        if save:
            self.save()


    #
    #   Collection Management - manage the user's asset collection
    #

    @web_method
    def set_collection(self):
        """ Expects/requires a request context. Evaluates the incoming request
        and hands off add/rm jobs to private/non-request methods. """

        self.check_request_params(['collection'])
        collection = self.params['collection']

        for collection_type in collection.keys():
            if collection_type not in ['expansions']:
                err = "Collection type '%s' is not implemented!"
                raise utils.InvalidUsage(err % collection_type, 501)

            add_list, rm_list = utils.list_compare(
                self.user['collection'][collection_type],
                collection[collection_type]
            )

            if add_list != []:
                [self.add_expansion_to_collection(exp) for exp in add_list]
            if rm_list != []:
                [self.rm_expansion_from_collection(exp) for exp in add_list]



    @web_method
    def add_expansion_to_collection(self, handle=None):
        """ Adds an expansion handle to self.user['collection']['expansions']
        list. Logs it.

        DEPRECATION WARNING: This is going to be an internal-only method soon!
        """

        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params['handle']

        if handle in self.user['collection']['expansions']:
            err = "%s Expansion '%s' already added to collection. Ignoring..."
            self.logger.warning(err, self, handle)
            return True

        self.user['collection']['expansions'].append(handle)

        self.save()


    @web_method
    def rm_expansion_from_collection(self, handle=None):
        """ Adds an expansion handle to self.user['collection']['expansions']
        list. Logs it.

        DEPRECATION WARNING: This is going to be an internal-only method soon!
        """

        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params['handle']

        if handle not in self.user['collection']['expansions']:
            err = "%s Expansion '%s' not found in collection. Ignoring..."
            self.logger.warning(err, self, handle)
            return True

        self.user['collection']['expansions'].remove(handle)
        self.save()


    #
    #   query/assess methods
    #

    def is_active(self):
        """ Refactored in February 2021 to no longer reference the legacy
        webapp's 'sessions' collection in MDB. Now, we use activity in the API
        to determine if a user is active. """

        if (
            self.get_latest_activity('minutes') <=
            API.config['ACTIVE_USER_HORIZON']
        ):
            return True

        return False


    def is_admin(self):
        """ Returns a bool representing whether the user is an API admin. This
        is NOT THE SAME as being a settlement admin (see below)."""

        return bool(self.user.get('admin', False))




    #
    #   get methods
    #

    def get_age(self):
        """ Returns the user's age. """
        return utils.get_time_elapsed_since(self.user["created_on"], 'age')


    def get_friends(self, return_type=None):
        """ Returns all of the user's friends (i.e. people he plays in campaigns
        with) as objects. """

        friend_ids      = set()
        friend_emails   = set()

        campaigns = self.get_settlements(qualifier="player")

        friends = None
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

        if return_type == int:
            if friends is not None:
                return friends.count()
            return 0

        if return_type == list:
            if friends is None:
                return []
            return [f["login"] for f in friends]

        if return_type == 'JSON':
            return json.dumps(list(friends), default=json_util.default)

        return friends


    def get_latest_activity(self, return_type=None):
        """ Returns the user's latest activity in a number of ways. Leave the
        'return_type' kwarg blank for a datetime stamp.
        """

        latest = self.user["latest_activity"]

        if return_type is not None:
            return utils.get_time_elapsed_since(latest, return_type)

        return latest


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
        elif qualifier == 'created_by':
            settlements = utils.mdb.settlements.find(
                {
                    'created_by': self.user['_id'],
                    'removed': {'$exists': False}
                }
            )
        elif qualifier == "player":
            settlement_id_set = set()

            survivors = self.get_survivors(qualifier="player")
            for s in survivors:
                settlement_id_set.add(s["settlement"])

            settlements_owned = self.get_settlements()
            for s in settlements_owned:
                settlement_id_set.add(s["_id"])
            settlements = utils.mdb.settlements.find(
                {
                    "_id": {"$in": list(settlement_id_set)},
                    "removed": {"$exists": False}
                }
            )
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
        if self.get_subscriber_level() < 1:
            for s in settlements:

                # get asset age
                created_on = API.config['TIMEZONE'].localize(s['created_on'])
                asset_age = datetime.now(tzlocal()) - created_on

                max_age = API.config['FREE_USER_SETTLEMENT_AGE_MAX']

                older_than_cutoff = (asset_age.days > max_age)
                if older_than_cutoff and self.user['_id'] == s['created_by']:
                    warn = "%s settlement '%s' is more than %s days old!"
                    self.logger.warning(warn, self, s['name'], max_age)
                    msg = utils.html_file_to_template(
                        'auto_remove_settlement.html'
                    )

                    # in case the admin panel hits it before the actual user
                    if not hasattr(flask.request, 'User'):
                        flask.request.User = utils.noUser()

                    msg = msg.safe_substitute(
                        settlement_name=s['name'],
                        settlement_age = asset_age.days,
                        settlement_dict = s,
                        user_email = flask.request.User.login,
                        user_id = flask.request.User._id,
                    )
                    e = utils.mailSession()
                    e.send(
                        subject="Settlement auto-remove! [%s]" % socket.getfqdn(),
                        html_msg=msg
                    )
                    s['removed'] = datetime.now(tzlocal())
                    utils.mdb.settlements.save(s)
                    settlements.remove(s)

        #
        # now start handling returns
        #

        if return_type == int:
            return len(settlements)

        if return_type == list:
            output = [s["_id"] for s in settlements]
            return output

        if return_type == 'list_of_dicts':
            return settlements

        if return_type == "asset_list":
            output = []
            for s in settlements:
                try:
                    S = Settlement(_id=s["_id"], normalize_on_init=False)
                    sheet = json.loads(S.serialize('dashboard'))
                    output.append(sheet)
                except Exception as e:
                    self.logger.error("Could not serialize %s", s)
                    self.logger.exception(e)
                    raise

            return output

        return settlements


    def get_subscriber_attributes(self):
        """ Returns a dictionary of subscriber information. """

        self.user['subscriber'].update(
            {
                'age': utils.get_time_elapsed_since(
                    self.user['subscriber'].get(
                        'created_on',
                        datetime.now(tzlocal())
                    ),
                'age'
                )
            }
        )

        self.user['subscriber'].update(
            {'level_handle': 'level_%s' % self.user['subscriber']['level']}
        )

        return self.user['subscriber']


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
            err = "'%s' is not a valid qualifier for this method!" % qualifier
            raise AttributeError(err)

        # returns
        if return_type == int:
            return survivors.count()

        if return_type == list:
            output = [s["_id"] for s in survivors]
            output = list(set(output))
            return output

        return survivors


    @web_method
    def can_create_settlement(self, raise_on_false=False):
        """ Checks a free user's settlement count versus the limit we define
        in config.py; returns False if they're at their limit.

        Use the 'raise_on_false' kwarg to have this raise and return a 405.
        """

        if self.user['subscriber']['level'] > 0:
            return True

        free_user_max = API.config['NONSUBSCRIBER_SETTLEMENT_LIMIT']
        user_created = self.get_settlements(
            qualifier = 'created_by',
            return_type=int
        )

        if user_created >= free_user_max:
            if raise_on_false:
                msg = 'Non-subscribers may only create %s settlements!'
                raise utils.InvalidUsage(msg % free_user_max, status_code=405)

        return False


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
            self.logger.warning('%s SUBSCRIPTION EXPIRED', self)
            self.set_subscriber_level(0)


    #
    #   baseline/normalize
    #       these appear here in order. When we initialize a user, we go
    #           1. baseline()
    #           2. bug_Fixes()
    #           3. normalize()
    #

    def baseline(self):
        """ Baseline the user record to our data model. """

        if 'collection' not in self.user.keys():
            self.user['collection'] = {"expansions": [], }
            self.logger.info(
                "%s Baselined 'collection' key into user dict.", self
            )
            self.perform_save = True

        if 'notifications' not in self.user.keys():
            self.user['notifications'] = {}
            self.logger.info(
                "%s Baselined 'notifications' key into user dict.", self
            )
            self.perform_save = True

        # create 'favorite_survivors' if it doesn't exist
        if not isinstance(self.user.get('favorite_survivors', None), list):
            self.user['favorite_survivors'] = []
            self.perform_save = True


    def bug_fixes(self):
        """ Fix bugs! """


    def normalize(self):
        """ Force/coerce the user into compliance with our data model for users.
        """

        if 'preferences' not in self.user.keys():
            self.user['preferences'] = {'preserve_sessions': False}
            self.logger.warning(
                "%s has no 'preferences' attrib! Normalizing...", self
            )
            self.perform_save = True

        # 'patron' becomes 'subscriber' in the 1.0.0 release
        if 'patron' in self.user.keys():
            self.user['subscriber'] = self.user['patron']
            del self.user['patron']
            self.logger.warning("%s Normalized 'patron' to 'subscriber'!", self)
            self.perform_save = True

        if 'subscriber' not in self.user.keys():
            self.user['subscriber'] = {'level': 0}
            self.logger.warning("%s Added 'subscriber' dict to user!", self)
            self.perform_save = True

        if isinstance(self.user['subscriber']['level'], str):
            warn = "%s Subscriber 'level' is str type! Normalizing to int..."
            self.logger.warning(warn, self)
            self.user['subscriber']['level'] = int(
                self.user['subscriber']['level']
            )
            self.perform_save = True

        if self.perform_save:
            self.save()


    def request_response(self, action=None):
        """ Initializes params from the request and then responds to the
        'action' kwarg. If 'action' is NOT a web method, do a custom return;
        otherwise, super() the base class request_response() method to handle
        web methods. """

        if action == 'get':
            return self.json_response()
        if action == "dashboard":
            return flask.Response(
                response=self.serialize('dashboard'),
                status=200,
                mimetype="application/json"
            )
        if action == "get_friends":
            return flask.Response(
                response=self.get_friends('JSON'),
                status=200,
                mimetype="application/json"
            )

        return super().request_response(action)

# ~fin
