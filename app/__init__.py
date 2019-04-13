"""
    Welcome to the app!

    This extremely un-Pythonic __init__.py file sets up our primary Flask object
    for use by the other elements of the API.

    Keep in mind that order of imports is critical here, since Flask is subject
    to so-called circular imports/mutual import references.

"""

# import flask
import flask
import flask_jwt_extended


# create the app
api = flask.Flask(__name__)

# import the settings module and add it
from app.utils import settings
api.settings = settings

# update the config items used by flask
api.config.update(
    DEBUG = api.settings.get("server","DEBUG"),
    TESTING = api.settings.get("server","DEBUG"),
)

#app.logger.addHandler(utils.get_logger(log_name="server"))
#app.config['SECRET_KEY'] = utils.settings.get(
#    "api",
#    "secret_key",
#    "private"
#)

#   Javascript Web Token! DO NOT import jwt (i.e. pyjwt) here!
jwt = flask_jwt_extended.JWTManager(api)


#   HTTP basic auth, which we use for the admin panel:
from flask_httpauth import HTTPBasicAuth
api.basicAuth = HTTPBasicAuth()


# Finally, import the routes and start the riot!
from app import routes
