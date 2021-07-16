"""

    The module for cloning users down from the legacy webapp and >= 1.0.0
    versions of the API.

    The methods here basically get data, pickle it (or similar) and then pass
    it along to the models/users.py module's import_data() method to get it
    loaded into the local mdb.

"""

# standard library imports
import _pickle
from datetime import datetime
import sys
from urllib.parse import urljoin

# second party imports
import email_validator
import requests

# local imports
from app import API, admin, utils
from app.models import users

logger = utils.get_logger()

#
#   import data wrappers: these methods get data and feed it to the import_data
#   method below
#
@utils.metered
def one_user_from_legacy_webapp(url, key, uid):
    """ Clones one user down from the legacy webapp to the local mdb. This
    method is DEPRECATED as of December 2020 and is NOT supported by version
    four of https://kdm-manager.com. """

    print('DEPRECATION WARNING!')

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
@admin.pickle_login
def get_one_user_from_api(prod_api, pickle_auth=False, **kwargs):
    """ Dials 'prod_api' and hits the /admin/user_asset/export endpoint with
    a POST containing a user's login ('u_login'). """

    try:
        email_validator.validate_email(kwargs['u_login']) # raises an exception
    except AttributeError as e:
        raise AttributeError('User email must be a string!')

    api_url = prod_api + "/admin/user_asset/export"
    response = requests.post(
        api_url,
        headers = {'API-Key': API.config['API_KEY']},
        auth=(
            kwargs['admin_login'],
            kwargs['admin_password']
        ),
        data={'login': kwargs['u_login']}
    )

    if response.status_code != 200:
        raise requests.RequestException(response.reason)
    logger.warn(response.content)

    pickle_string = response.content
    try:
        user_oid = users.import_user(pickle_string)
    except _pickle.UnpicklingError as e:
        pickled = _pickle.dumps(pickle_string)
        error_path = kwargs['u_login'] + '_import_error.pickle'
        error_dump = open(error_path, 'wb')
        error_dump.write(pickle_string)
        error_dump.close()
        raise ValueError("Could not import user! See '%s'" % error_path)

    # we can silently reset the user's password if 'force' is in the kwargs
    if kwargs.get('force', False):
        user_object = users.User(_id=user_oid)
        user_object.update_password('password')

    return user_oid


@utils.metered
def get_recent_users_from_api(prod_api, **kwargs):
    """ Dials the prod API, hits the user_data route with no args, returns the
    list of recent production user. This is supported in all releases. """

    # create a URL and do the request
    api_url = prod_api + "/admin/get/user_data"
    response = requests.get(
        api_url,
        headers = {'API-Key': API.config['API_KEY']},
        auth=(
            kwargs['admin_login'],
            kwargs['admin_password']
        ),
    )

    if response.status_code == 200:
        output = response.json()
        return output['user_info']
    else:
        raise requests.RequestException(response.reason)

