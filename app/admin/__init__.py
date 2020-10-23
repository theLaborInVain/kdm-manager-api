"""

    The admin module should only be used for web-based administration stuff.

    CLI admin methods are found in the __main__.py file.

"""

# standard library imports
from optparse import OptionParser
import os
import pickle
import sys

# local imports
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
