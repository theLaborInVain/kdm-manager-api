"""

    The module for cloning users down from the legacy webapp and >= 1.0.0
    versions of the API.

    The methods here basically get data, pickle it (or similar) and then pass
    it along to the models/users.py module's import_data() method to get it
    loaded into the local mdb.

"""

# standard library imports
from datetime import datetime
import sys
from urllib.parse import urljoin

# third party imports
import requests

# local imports
from app import utils
from app.models import users


#
#   import data wrappers: these methods get data and feed it to the import_data
#   method below
#
@utils.metered
def one_user_from_legacy_webapp(url, key, uid):
    """ Clones one user down from the legacy webapp to the local mdb. """

    # do the request
    req_url = urljoin(url, "get_user")
    r = requests.get(req_url, params={"admin_key": key, "u_id": uid})

    # exit if the request failed
    if r.status_code != 200:
        print(" Request failed!\n Status: %s\n Reason: %s" % (
            r.status_code, r.reason
            )
        )
        sys.exit(1)

    # assuming we're still here, load the data; return an OID
    pickle_string = r.text.strip().encode()
    return users.import_user(pickle_string)


@utils.metered
def get_recent_users_from_api(prod_api):
    """ Dials the prod API, hits the user_data route with no args, returns the
    list of recent production user. This is supported in all releases. """

    # create a URL and do the request
    api_url = prod_api + "/admin/get/user_data"
    response = requests.get(api_url)

    if response.status_code == 200:
        output = response.json()
        return output['user_info']
    else:
        raise requests.RequestException(r.reason)

