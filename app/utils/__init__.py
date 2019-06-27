""" The utilities module used by the API. """

# std lib imports
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import functools
from html.parser import HTMLParser
from io import BytesIO
import logging
import os
import platform
import socket
from string import Template
import sys
import time
import traceback

# third-party imports
from dateutil.relativedelta import relativedelta
import flask
import gridfs
from pymongo import MongoClient

# local imports
from app import API
from app.utils import crossdomain as crossdomain_module
from app.utils import settings

# initialize convenience libraries/methods for lazy importing
crossdomain = crossdomain_module.crossdomain

#   Mongo!
mdb = MongoClient()[settings.get("api", "mdb")]


#
#   Application logging is all here. Do not fiddle with logging anywhere else!
#

log_root_dir = os.path.join(
    API.root_path,
    '..',
    settings.get('server', 'log_root_dir')
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
            logger.setLevel(settings.get("server", "log_level"))
        else:
            logger.setLevel(log_handler_level)

        # now check the logging root, create it if it's not there
        if not os.path.isdir(log_root_dir):
            os.mkdir(log_root_dir)

        # create the path and add it to the handler
        log_path = os.path.join(log_root_dir, log_file_name + ".log")
        logger_fh = logging.FileHandler(log_path)

        #   set the formatter and add it via addHandler()
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s:\t%(message)s',
            ymdhms
        )
        logger_fh.setFormatter(formatter)
        logger.addHandler(logger_fh)

    return logger


#
#   special exception class definitions
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
        self.logger.exception("[%s] %s" % (self.status_code, self.msg))


class WorldQueryError(Exception):
    """ Handler for asset-based errors. """

    def __init__(self, query=None, message="World query produced no results!"):
        self.logger = get_logger()
        self.logger.exception(message)
        self.logger.error("Query was: %s" % query)
        Exception.__init__(self, message)


#
#	Generic exception auto-mailer
#

def email_exception(exception):
    """ This is called by the main Flask errorhandler() decorator in api.py
    when we have an unhandled exception at any point of responding to a request.

    This prevents user-facing (or Khoa-facing) failures from being silently
    swallowed. """

    # first, log it
    e_logger = get_logger(log_name='error')
    e_logger.exception(exception)

    if not hasattr(flask.request, 'User'):
        flask.request.User = noUser()

    # finally, prepare the message template and the traceback for emailing
    msg = html_file_to_template("exception_alert.html")
    tb = traceback.format_exc().replace("    ", "&ensp;").replace("\n", "<br/>")

    # do it
    s = msg.safe_substitute(
        traceback=tb,
        user_login=flask.request.User.login,
        user_oid=flask.request.User._id,
        datetime=datetime.now(),
        r_method=flask.request.method,
        r_url=flask.request.url,
        r_json=flask.request.json
    )
    e = mailSession()
    e.send(
        subject="API Error! [%s]" % socket.getfqdn(),
        recipients=API.settings.get('server', 'alert_email').split(','),
        html_msg=s
    )




#
#   performance monitoring/recording
#

def metered(method):
    """ A decorator for logging the time a method takes to execute. Note that
    this is hardcoded to only work in dev! We don't want to spam the prod logs,
    since we rent disc there.
    """

    def not_timed(*args, **kwargs):
        """ Just does the function. """
        return method(*args, **kwargs)

    def timed(*args, **kwargs):
        """ Wraps the incoming function in a start/stop, logs. """
        start = datetime.now()
        result = method(*args, **kwargs)
        stop = datetime.now()
        duration = stop - start
        logger = get_logger()
        logger.info('[%s.%s] %s(%s, %s)' % (
            duration.seconds,
            duration.microseconds,
            method.__name__,
            ", ".join(args[1:]),
            " ".join(["%s: %s" % (k, v) for k,v in kwargs.items()])
            )
        )
        return result

    # we only meter in the dev environment
    if socket.gethostname() in ['mona']:
        return timed
    return not_timed


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
        flask.request.logger = get_logger(log_name='server')
        flask.request.logger.debug(
            '[%s] [%s] [%s] /%s ' % (
                flask.request.method,
                response.status_code,
                duration,
                flask.request.url.split(flask.request.url_root)[1],
            )
        )

    old_record_query = {
        "created_on": {
            "$lt": (datetime.now() - timedelta(days=7))
        }
    }
    removed_records = mdb.api_response_times.remove(old_record_query)


#
#   Settlement event log helpers!
#

def action_keyword(kw):
    """ converts an action keyword 'kw' to a past-tense version of that
    keyword and its preposition. """

    kw = kw.lower()
    if kw in ['add', 'added', 'adds', 'adding']:
        output = ("added", "to")
    elif kw in ['dec', 'decrease', 'subtract', 'subtracts', 'decreases']:
        output = ("subtracted", "from")
    elif kw in ['rm', 'removed', 'remove', 'removes', 'removing']:
        output = ("removed", "from")
    elif kw in ["set", "update"]:
        output = ("set", "to")
    elif kw in ["unset",]:
        output = ("unset", "from")
    elif kw in ["inherited", "inherit"]:
        output = ("inherited", "from")
    elif kw in ["birth", "born"]:
        output = ("born", "to")
    elif kw in ['apply', 'applied', 'applies']:
        output = ('applied', 'to')
    elif kw in ["enforce"]:             # automate
        output = ("automatically set", "to")
    elif kw in ["toggle"]:
        output = ("toggled", "to")
    elif kw in ["create", "created", 'creating']:
        output = ("created", None)
    elif kw in ["abandon", 'abandoned']:
        output = ("abandoned", None)
    else:
        output = (kw, "to")

    return output


#
#   GridFS Image object definition
#

class GridfsImage(object):
    """ Initialize this with a string of an mdb Object ID, and use
    the render_response() method to create an http response of the
    image. Fuck a file system: props to the immortal rschulz. """

    def __init__(self, img_id):
        try:
            img_oid = ObjectId(img_id)
        except:
            err_msg = 'Image OIDs must be 12-byte input or 24-character hex!'
            raise InvalidUsage(err_msg, status_code=400)
        try:
            self.img = gridfs.GridFS(mdb).get(img_oid)
        except gridfs.errors.NoFile:
            self.img = None

    def render_response(self):
        """ Renders an http response. """
        if self.img is None:
            return Response(response="Image not found!", status=404)
        image_file = BytesIO(self.img.read())
        return flask.send_file(image_file, mimetype="image/png")



#
#   misc. helper methods
#

def decompose_name_string(name):
    """ Accepts a name string and returns a list of possible versions of it. """

    output = []

    name_list = name.split(" ")
    for i in range(len(name_list) + 1) :
        output.append(" ".join(name_list[:i]))

    return output


def get_host_ip():
    """ Uses the 8.8.8.8 trick to get the localhost IP address. """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def get_percentage(part, whole):
    """ Input a part, then the whole. Returns percent as a float. """
    if whole == 0:
        return 0
    else:
        return 100 * round(float(part)/float(whole), 2)


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


def html_file_to_template(rel_path):
    """ Turns an HTML file into a string.Template object.

    Important! The files have to live in application.root_path/html/
    """
    tmp_file = os.path.join(
        API.root_path,
        API.settings.get('api','templates_dir'),
        rel_path
    )
    return Template(open(tmp_file, "rb").read())


def html_stripper(s):
    """ Takes a string, 's', that might contain HTML and removes all
    tags, entities, etc. """

    class MLStripper(HTMLParser):
        def __init__(self):
            self.reset()
            self.strict = False
            self.convert_charrefs = True
            self.fed = []
        def handle_data(self, d):
            self.fed.append(d)
        def get_data(self):
            return ''.join(self.fed)

    S = MLStripper()
    S.feed(s)
    return S.get_data()


def list_to_pretty_string(l, quote_char=False):
    """ Takes a list of strings and makes it into a single, pretty string
    with commas, the word 'and' and that type of shit. """

    l = list(l)

    if len(l) == 0:
        return None
    elif len(l) == 1:
        if quote_char:
            return "%s%s%s" % (quote_char, l[0], quote_char)
        else:
            return l[0]

    if quote_char:
        l = [str("%s%s%s" % (quote_char, i, quote_char)) for i in l]
    else:
        try:
            l = [i.encode('ascii', 'ignore') for i in l]
        except:
            l = [str(i) for i in l]

    return " and ".join([", ".join(str(l)[:-1]), str(l)[-1]])



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
http_500 = flask.Response(
    response=("Server explosion! The server erupts in a "
        "shower of gore, killing your request instantly. All other servers are "
        "so disturbed that they lose 1 survival."),
    status=500
)
http_501 = flask.Response(
    response="Not implemented in this release",
    status=501
)




#
#   stub dictionary for creating the meta element of API returns
#

api_meta = {
    "meta": {
        "api": {
            "version": settings.get("api", "version"),
            "age": get_time_elapsed_since(
                datetime.strptime('2016-10-13', '%Y-%m-%d'),
                units='age'
            ),
        },
        'server': {
            "hostname": socket.gethostname(),
            "debug": settings.get('server', 'debug'),
            'log_level': settings.get('server', 'debug'),
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
