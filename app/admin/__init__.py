"""

    The admin module should only be used for web-based administration stuff.

    CLI admin methods are found in the __main__.py file.

"""

# standard library imports
from optparse import OptionParser
import sys

# local imports
from app import utils
from app.admin import notifications, panel


def get_data(resource=None):
    """ Retrieves various types of admin panel data. If the requester wants
	something we don't have, raise a 422 """

    if resource == 'user_data':
        return panel.get_user_data()
    elif resource == 'settlement_data':
        return panel.get_settlement_data()
    elif resource == 'logs':
        return panel.serialize_system_logs()

    raise utils.InvalidUsage("Resource '%s' does not exist!", status_code=400)


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



