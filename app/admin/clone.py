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
from app.models import users


#
#   import data wrappers: these methods get data and feed it to the import_data
#   method below
#

def one_user_from_legacy_webapp(url, key, uid):
    """ Clones one user down from the legacy webapp to the local mdb. """

    # meter this
    start = datetime.now()

    # do the request
    sys.stderr.write(" Initiating request...")
    req_url = urljoin(url, "get_user")
    r = requests.get(req_url, params={"admin_key": key, "u_id": uid})

    # exit if the request failed
    if r.status_code != 200:
        print(" Request failed!\n Status: %s\n Reason: %s" % (
            r.status_code, r.reason
            )
        )
        sys.exit(1)

    # stop the meter
    stop = datetime.now()
    dur = stop - start
    sys.stderr.write("user data pickle retrieved in %s.%s seconds!\n" % (
        dur.seconds, dur.microseconds
        )
    )

    # assuming we're still here, load the data; return an OID
    pickle_string = r.text.strip().encode()
    return users.import_user(pickle_string)


#
#   Big, lumpy, procedural code for loading misc. data into the local mdb
#


