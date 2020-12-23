"""

    The admin module should only be used for web-based administration stuff.

    CLI admin methods are found in the __main__.py file.

"""

# standard library imports
import getpass
from optparse import OptionParser
import os
import pickle
import sys

# second party imports
import requests

# API imports
from app import admin, utils
from app.admin import notifications, panel, releases


def get_data(resource=None):
    """ Retrieves various types of admin panel data. If the requester wants
	something we don't have, raise a 400. """

    if resource == 'user_data':
        return panel.get_user_data()
    elif resource == 'settlement_data':
        return panel.get_settlement_data()
    elif resource == 'logs':
        return panel.serialize_system_logs()

    raise utils.InvalidUsage(
        "Resource '%s' does not exist!" % resource,
        status_code=400
    )


def get_notifications(method=None):
    """ Creates a new admin asset. Used currently only for webapp alerts. """

    A = notifications.Alert()
    if method == "new":
        return A.serialize()
    elif method == "expire":
        A.expire()
        return A.serialize()
    else:
        return utils.http_501

    return utils.http_501


def pickle_login(func):
    """ This is a wrapper that does two things:
            1.) it attempts to get an admin credential from the admin pickle
                (see the AdminPickle class below) BEFORE 'func' is called:
                if this fails, it will get it from the CLI, so this is a
                CLI-only type of deco;
            2.) it attempts to update the pickle afterwards, if 'func' returns
                anything that evaluates to True.

        Most importantly, it adds the 'admin_login' and 'admin_password kwargs
        to 'func' when it calls it, so anything wrapped in this deco has to
        accept those two.

    """

    def wrapped(*args, **kwargs):
        """ Wraps the incoming function in a start/stop, logs. """

        # determine if the wrapped func wants to do pickle auth
        pickle_auth = kwargs.get('pickle_auth', False)

        if pickle_auth:
            # then, update the kwargs of 'func' to have special kwargs;
            # it's important to do these HERE, in case we're not doing pickle
            # auth and passing the kwargs normally
            kwargs['admin_login'] = None
            kwargs['admin_password'] = None

            # try to get the admin's email from the admin pickle
            admin_login = None
            a_pickle = AdminPickle()
            if a_pickle.data.get('admin_login', None) is not None:
                use_prev = input(
                    '\n Admin login %s? [YES]: ' % a_pickle.data['admin_login']
                )
                if use_prev is not None and len(use_prev) == 0:
                    use_prev = 'Y'
                if use_prev.upper() == 'Y':
                    admin_login = a_pickle.data.get('admin_login')
                    print(' Login: %s' % admin_login)

            # manually key the admin login if we don't have one
            if admin_login is None:
                admin_login = input(' Login: ')

            # always get the password from the CLI
            admin_password = getpass.getpass(' Password: ')
            print()

            kwargs['admin_login'] = admin_login
            kwargs['admin_password'] = admin_password

        result = func(*args, **kwargs)

        if pickle_auth and wrapped != requests.exceptions.RequestException:
            # since we logged in successfully, see if we have an admin email
            # in the pickle and save this login if we do NOT
            if a_pickle.data.get('admin_login', None) is None:
                a_pickle.add_key('admin_login', admin_login)

        return result

    return wrapped


class AdminPickle:
    """ creates an object that gives us easy methods for working with the
    so-called admin pickle, which stashes admin stuff on the local file system
    (which is lame, but using the db for it seemed like overkill. """

    def __init__(self):
        self.working_dir = os.path.dirname(admin.__file__)
        self.abs_path = os.path.join(self.working_dir, 'admin.pickle')

        if not os.path.isfile(self.abs_path):
            self.data = {}
        else:
            self.data = pickle.load(open(self.abs_path, "rb"))

    def add_key(self, key, value):
        """ Adds or overwrites a 'key' in the self.data with 'value'. """

        self.data[key] = value
        pickle.dump(self.data, open(self.abs_path, "wb" ))
