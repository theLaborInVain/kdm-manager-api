"""
    Welcome to the app!

    This extremely un-Pythonic __init__.py file sets up our primary Flask object
    for use by the other elements of the API.

    Keep in mind that order of imports is critical here, since Flask is subject
    to so-called circular imports/mutual import references.

"""

# standard library imports
from datetime import datetime, timedelta
import socket

# second party imports
import flask
from flask_httpauth import HTTPBasicAuth
import flask_jwt_extended
import pymongo
import werkzeug

# app imports
import config

# create the app
API = flask.Flask(__name__, instance_relative_config=True)
API.config.from_object(config.Config)
API.config.from_pyfile('secret.py')

# import the settings module and add it
from app import assets, utils
from app.utils import settings
from app.utils import crossdomain

# fiddle the loggers; remove the default to avoid handle conflicts
API.logger.removeHandler(flask.logging.default_handler)
API.logger = utils.get_logger(log_name="server")

API.settings = settings

#   Javascript Web Token! DO NOT import jwt (i.e. pyjwt) here!
JWT = flask_jwt_extended.JWTManager(API)


#   HTTP basic auth, which we use for the admin panel:
API.basicAuth = HTTPBasicAuth()
@API.basicAuth.verify_password
def verify_password(username, password):
    """ cf. the methods in routes.py that use the @basicAuth decorator. This is
    what happens when those routes try to verify their user. """

    flask.request.User = assets.users.authenticate(username, password)

    if flask.request.User is None:
        return False
    elif flask.request.User.user.get("admin", None) is None:
        msg = "Non-admin user %s attempted to access the admin panel!" % (
            flask.request.User.user["login"])
        application.logger.warn(msg)
        return False

    return True


#
#   pre- and post-request methods, exception handling, etc.
#

@API.before_request
def before_request():
    """ Updates the request with the 'start_time' attrib, which is used for
    performance monitoring. """
    flask.request.start_time = datetime.now()
    flask.request.log_response_time = False

    # get the API key from the incoming request
    flask.request.api_key = flask.request.headers.get('API-Key', None)

    # set a flag on the request if it's a good key
    flask.request.api_key_valid = False
    if API.config['KEYS'].get(flask.request.api_key, None) is not None:
        flask.request.api_key_valid = True

    if socket.getfqdn() != API.settings.get('server', 'prod_fqdn'):
        flask.request.log_response_time = True


@API.after_request
def after_request(response):
    """ Logs the response times of all requests for metering purposes. """
    flask.request.stop_time = datetime.now()
    utils.record_response_time(response)
    if response.status == 500:
        API.logger.error("fail")
    return response


#
#   error handling/errorhandlers
#

@API.errorhandler(404)
def four_oh_four(e):
    """ Default 404 for the API, which gets a lot of bogus endpoint spam. """

    return utils.http_404


@API.errorhandler(werkzeug.exceptions.MethodNotAllowed)
def method_not_allowed(e):
    """ We don't want to be emailed about requests where we don't support
    the method. """

    err = "%s endpoint does not support the '%s' method!"
    return flask.Response(
        response = err % (flask.request.path, flask.request.method),
        status = e.code
    )


@API.errorhandler(Exception)
@crossdomain(origin=['*'])
def general_exception(exception):
    """ This is how we do automatic email alerts on arbitrary API failures.

    In production, we send an alert email out and then return a 500 to the user
    for reference/debugging purposes.

    In non-production environments, we just raise it to the Flask debugger."""

    logger = utils.get_logger(log_name='error')
    logger.error('Flask caught an unhandled exception!')

    # in the criminal justice system, database failure is especially heinous
    if isinstance(exception, pymongo.errors.ServerSelectionTimeoutError):
        logger.error('The database is unavailable!')
        utils.email_exception(exception)

    if socket.getfqdn() != API.settings.get('server', 'prod_fqdn'):
        err = "'%s' is not production! Raising exception..." % socket.getfqdn()
        logger.warn(err)
        raise exception

    try:
        utils.email_exception(exception)
    except Exception as e:
        logger.error('An exception occurred while sending the alert email!')
        logger.exception(e)

    try:
        return flask.Response(response=exception.msg, status=500)
    except AttributeError:
        return flask.Response(response=str(exception), status=500)


@API.errorhandler(utils.InvalidUsage)
@crossdomain(origin=['*'])
def return_exception(exception):
    """ This is how we fail user error (i.e. back) to the requester. """
    return flask.Response(response=exception.msg, status=exception.status_code)



# Finally, import the routes and start the riot!
from app import routes
