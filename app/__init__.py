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

# third party imports
import flask
import flask_jwt_extended


# create the app
api = flask.Flask(__name__)

# import the settings module and add it
from app.utils import settings
from app.utils import crossdomain

api.settings = settings
api.default_methods = settings.get('api','default_methods').split(',')

# update the config items used by flask
api.config.update(
    DEBUG = api.settings.get("server","DEBUG"),
    TESTING = api.settings.get("server","DEBUG"),
)

api.logger.addHandler(utils.get_logger(log_name="server"))
api.config['SECRET_KEY'] = api.settings.get(
    "api",
    "secret_key",
    "private"
)

#   Javascript Web Token! DO NOT import jwt (i.e. pyjwt) here!
jwt = flask_jwt_extended.JWTManager(api)


#   HTTP basic auth, which we use for the admin panel:
from flask_httpauth import HTTPBasicAuth
api.basicAuth = HTTPBasicAuth()


#
#   pre- and post-request methods, exception handling, etc.
#

@api.before_request
def before_request():
    """ Updates the request with the 'start_time' attrib, which is used for
    performance monitoring. """
    flask.request.start_time = datetime.now()
    flask.request.log_response_time = False

    # get the API key from the incoming request
    flask.request.api_key = flask.request.headers.get('API-Key', None)

    if socket.getfqdn() != api.settings.get('server','prod_fqdn'):
        flask.request.log_response_time = True


@api.after_request
def after_request(response):
    """ Logs the response times of all requests for metering purposes. """
    flask.request.stop_time = datetime.now()
    utils.record_response_time(response)
    if response.status == 500:
        api.logger.error("fail")
    return response


# error handling

@api.errorhandler(Exception)
@crossdomain(origin=['*'])
def general_exception(exception):
    """ This is how we do automatic email alerts on arbitrary API failures.

    In production, we send an alert email out and then return a 500 to the user
    for reference/debugging purposes.

    In non-production environments, we just raise it to the Flask debugger."""

    if socket.getfqdn() != api.settings.get('server','prod_fqdn'):
        raise(exception)

    utils.email_exception(exception)
    try:
        return flask.Response(response=exception.msg, status=500)
    except:
        return flask.Response(response=str(exception), status=500)


@api.errorhandler(utils.InvalidUsage)
@crossdomain(origin=['*'])
def return_exception(exception):
    """ This is how we fail user error (i.e. back) to the requester. """
    return flask.Response(response=exception.msg, status=error.status_code)



# Finally, import the routes and start the riot!
from app import routes
