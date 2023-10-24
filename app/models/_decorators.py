'''

    Model method decorators live here. Best to keep these separates out from the
    helper methods and whatever else that live in __init__.py

    A reason we do this is to make it hard to accidental decorate an asset
    method with a decorator meant for use with model methods/objects.

'''

# standard library imports
import inspect
import functools

# second-party imports
import flask

# API imports
from app import API, utils

def admin_only(func):
    """ Checks the request context to see if the requester is an API admin.
    Returns 401 if they're not. """

    func._admin_only = True

    def wrapped(*args, **kwargs):
        """ checks admin status. runs the func """
        logger = utils.get_logger()

        if flask.has_request_context():
            if API.config['ENVIRONMENT'].get('is_production', False):
                if (
                    hasattr(flask.request, 'User') and not
                    flask.request.User.is_admin()
                ):
                    err = 'Only API admins may access this endpoint!'
                    raise utils.InvalidUsage(err, 401)
            else:
                warn = 'API is non-prod. Skipping admin check for %s()'
                logger.warning(warn, func.__name__)

        return func(*args, **kwargs)

    return wrapped


def deprecated(method):
    """ Decorate object methods with this to log a deprecation warning when
    they're called. """

    logger = utils.get_logger(log_name='deprecated')

    def wrapped(*args, **kwargs):
        """ Logs the deprecated method and its caller. """

        warning = "DEPRECATION WARNING! The %s() method is deprecated!"
        logger.warning(warning, method.__name__)

        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        logger.warning(
            "%s() called by %s()", method.__name__, calframe[1][3]
        )

        return method(*args, **kwargs)

    return wrapped


def log_event_exception_manager(log_event_call):
    """ This is a decorator for model lookups. Do not use this decorator to
    decorate other methods: it will fail.

    The basic idea here is to capture exceptions, log them, email them and NOT
    interrupt the request. This is really the only method where we ever want to
    handle exceptions this way. """

    def wrapper(self, *args, **kwargs):
        """ Wraps the incoming call. """
        try:
            return log_event_call(self, *args, **kwargs)
        except Exception as log_event_call_exception:
            # first, figure out what called log_event()
            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 2)
            caller_function = calframe[1][3]

            # now roll it all up into a really detailed failure message
            err_msg = (
                '%s() call resulted in an unhandled exception in log_event() '
                'method! log_event(args: %s, kwargs: %s)'
            ) % (caller_function, args, kwargs)

            self.logger.exception(err_msg)

            utils.email_exception(log_event_call_exception)

    return wrapper


def paywall(func):
    """ Checks the flask.request.User subscriber status; fails if they're not
    a subscriber. """

    @functools.wraps(func)
    def decorated_function(*args, **kwargs):
        if flask.request.User.get_subscriber_level() < 1:
            msg = "This feature is only available to subscribers!"
            raise utils.InvalidUsage(msg, status_code=402)
        return func(*args, **kwargs)

    return decorated_function


def web_method(func):
    """ Decorate methods that we do not support a request context and thus
    are not meant to be called as part of web-facing API work, etc.

    If use with other decorators, this should be the FIRST decorator, e.g.
    @utils.admin_only should come second and so on.
    """

    func._web_method = True
    return func
