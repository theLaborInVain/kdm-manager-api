""" The utilities module used by the API. """

# std lib imports
from datetime import datetime, timedelta
import functools
import logging
import os
import platform
import socket
import sys

# third-party imports
from dateutil.relativedelta import relativedelta
import flask
from pymongo import MongoClient

# local imports
from app import api
from app.utils import crossdomain as crossdomain_module
from app.utils import settings

# initialize convenience libraries/methods for lazy importing
crossdomain = crossdomain_module.crossdomain

#   Mongo!
mdb = MongoClient()[settings.get("api","mdb")]


#
#   Application logging is all here. Do not fiddle with logging anywhere else!
#

log_root_dir = os.path.join(
    api.root_path,
    '..',
    settings.get('server','log_root_dir')
)

def get_logger(log_level=None, log_name=None):
    """ Initialize a logger, specifying a new file if necessary. """

    logger = logging.getLogger(__name__)

    if len(logger.handlers):    # if we're initializing a log, kill sother
        logger.handlers = []    # handlers are open, so the latest init wins

    if not len(logger.handlers):    # if it's not already open, open it

        # set the file name or default to the script asking for the logger
        log_file_name = log_name
        if log_name is None:
            log_file_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        log_handler_level = log_level

        # do the same for log level, defaulting to the server's 'log_level'
        if log_handler_level is None:
            logger.setLevel(settings.get("server","log_level"))
        else:
            logger.setLevel(log_handler_level)

        # now check the logging root, create it if it's not there
        if not os.path.isdir(log_root_dir):
            os.mkdir(log_root_dir)

        # create the path and add it to the handler
        log_path = os.path.join(log_root_dir, log_file_name + ".log")
        logger_fh = logging.FileHandler(log_path)

        #   set the formatter and add it via addHandler()
        formatter =  logging.Formatter(
            '[%(asctime)s] %(levelname)s:\t%(message)s',
            ymdhms
        )
        logger_fh.setFormatter(formatter)
        logger.addHandler(logger_fh)

    return logger


#
#   InvalidUsage special exception class
#

class InvalidUsage(Exception):
    """ Raise this type of exception at any point to return an HTTP response to
    the requester. Syntax goes like this:

        raise utils.InvalidUsage("Message", status_code=400)

    Do this whenever the requester's param keys/values are not up to snuff, etc.
    """

    status_code = 400

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.logger = get_logger(log_name='error')
        self.msg = message
        if status_code is not None:
           self.status_code = status_code
           self.payload = payload
        self.alert()

#    def to_dict(self):
#       rv = dict(self.payload or ())
#       rv['msg'] = self.message
#       return Response(rv['msg'], self.status_code)


#
#   performance monitoring/recording
#

def record_response_time(response):
    """ Accepts a request object, uses it to log the request and its response
    time to mdb. Prunes old lines. """

    duration = flask.request.stop_time - flask.request.start_time

    url_list = flask.request.url.split(flask.request.url_root)[1].split("/")
    for i in url_list:
        try:
            ObjectId(i)
            url_list.remove(i)
        except:
            pass
    url = "/".join(url_list)

    mdb.api_response_times.insert({
        "api_key": flask.request.api_key,
        "created_on": datetime.now(),
        "url": url,
        "method": flask.request.method,
        "time": duration.total_seconds()
    })

    if flask.request.log_response_time:
        flask.request.logger = get_logger()
        flask.request.logger.debug('[%s] [%s] [%s] %s ' % (
            flask.request.method,
            response.status_code,
            duration,
            flask.request.url,
            )
        )

    old_record_query = {"created_on": {"$lt": (datetime.now() - timedelta(days=7))}}
    removed_records = mdb.api_response_times.remove(old_record_query)


#
#   misc. helper methods
#

def get_host_ip():
    """ Uses the 8.8.8.8 trick to get the localhost IP address. """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def get_time_elapsed_since(start_time, units=None, round_seconds=True):
    """ Use a datetime object as the first arg and a 'units' kwarg value of
    either 'minutes' or 'hours' to find out how long it has been since that
    time (in your preferred units).

    Use 'age' as the value for 'units' to get a human-readable string
    representing the elapsed time.
    """

    delta = (datetime.now() - start_time)
    days = delta.days
    years = relativedelta(datetime.now(), start_time).years
    offset = delta.total_seconds()

    offset_hours = offset / 3600.0

    if round_seconds:
        offset = int(offset)

    if units == "seconds":
        return offset
    elif units == "hours":
        return int(offset_hours)
    elif units == "minutes":
        return int(delta.seconds / 60)
    elif units == "days":
        return delta.days
    elif units == "years":
        return years
    elif units == "years_and_days":
        for y in range(years):
           days -= 365
        year_word = "year"
        if years >= 2:
           year_word = "years"
        return "%s %s and %s days" % (years, year_word, days)
    elif units == "age":
        if offset == 1:
            return 'one second'
        elif offset < 60:
           return '%s seconds' % offset
        elif offset == 60:
            return 'one minute'
        elif offset < 3600:
           return "%s minutes" % get_time_elapsed_since(start_time, "minutes")
        elif offset == 3600:
            return 'one hour'
        elif offset < 86400:
           return "%s hours" % get_time_elapsed_since(start_time, "hours")
        elif offset < 172800:
           return "one day"
        elif delta.days < 365:
           return "%s days" % get_time_elapsed_since(start_time, "days")
        elif delta.days == 365:
           return "one year"
        elif delta.days > 365:
           return get_time_elapsed_since(start_time, 'years_and_days')

    return delta



#
#  The JUNK DRAWER! Everything past this point is kind of...just random junk
#

ymd = "%Y-%m-%d"
hms = "%H:%M:%S"
ymdhms = "%Y-%m-%d %H:%M:%S"
thirty_days_ago = datetime.now() - timedelta(days=30)


# 	HTTP response objects

# 200s
http_200 = flask.Response(response="OK!", status=200)
http_299 = flask.Response(
    response="Warning! This endpoint is deprecated!",
    status=299
)

# 400s
http_400 = flask.Response(response="Bad Request!", status=400)
http_401 = flask.Response(response="Authorization required", status=401)
http_402 = flask.Response(
    response="This is a subscribers-only endpoint!",
    status=402
)
http_404 = flask.Response(response="Resource not found", status=404)
http_405 = flask.Response(
	response="Method not allowed (did you mean to POST?)",
	status=405
)
http_410 = flask.Response(
    response="Gone. This endpoint is no longer supported! There is no\
    replacement or equivalent for it.",
    status=410
)
http_422 = flask.Response(
	response="Missing argument, parameter or value",
	status=422
)

# 500s
http_500 = flask.Response(response="Server explosion! The server erupts in a\
    shower of gore, killing your request instantly. All other servers are so\
    disturbed that they lose 1 survival.",
    status=500
)
http_501 = flask.Response(response="Not implemented in this release", status=501)




#
#   stub dictionary for creating the meta element of API returns
#

api_meta = {
    "meta": {
        "api": {
            "version": settings.get("api","version"),
            "age": get_time_elapsed_since(
                datetime.strptime('2016-10-13', '%Y-%m-%d'),
                units='age'
            ),
        },
        'server': {
            "hostname": socket.gethostname(),
            "debug": settings.get('server','debug'),
            'log_level': settings.get('server','debug'),
            'os': platform.platform(),
            'ipv4': get_host_ip(),
        },
        "info": {
            "about": "https://github.com/theLaborInVain/kdm-manager-api",
            "copyright": "The Labor in Vain (2015 - %s)" %
                datetime.now().strftime("%Y"),
        },
        "admins": list(
            mdb.users.find({"admin": {"$exists": True}}).sort('login')
        ),
        "object": {},
    },
}
