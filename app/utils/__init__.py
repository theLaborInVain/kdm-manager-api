""" The utilities module used by the API. """

# std lib imports
from bson import json_util
from bson.objectid import ObjectId
import configparser
from datetime import datetime, timedelta
from dateutil.tz import tzlocal
import email
from email.header import Header as email_Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import functools
from html.parser import HTMLParser
from io import BytesIO
import json
import logging
import os
import platform
import pytz
import smtplib
import socket
from string import Template
import sys
import time
import traceback
from urllib.parse import urlparse

# third-party imports
from dateutil.relativedelta import relativedelta
import flask
import gridfs
from pymongo import MongoClient

# local imports
from app import API
from app.assets import versions
from app.utils import crossdomain as crossdomain_module
from app.utils import settings, web


USCENTRAL = pytz.timezone('US/Central')

# initialize convenience libraries/methods for lazy importing
crossdomain = crossdomain_module.crossdomain

#   Mongo!
mdb = MongoClient()[API.config['MDB']]

# the noUser class is used when emailing errors where we don't have an
# authenticated user. This was missing from the 1.0.0 release and broke the
# alert email feature...which buried a lot of errors. 
class noUser:
    def __init__(self):
        self.login="admin@kdm-manager.com"
        self._id = "666"
        self.user = None

# CONSTANTS
YMD = "%Y-%m-%d"
YMDHMS = "%Y-%m-%d %H:%M:%S"

#
#   Application logging is all here. Do not fiddle with logging anywhere else!
#

def get_logger(log_level=None, log_name=None):
    """ Initialize a logger, specifying a new file if necessary. """

    # defaults
    log_root_dir = os.path.join(API.root_path, '..', 'logs')
    if log_level is None:
        if API.config['DEBUG']:
            log_level = 'DEBUG'
        else:
            log_level = 'INFO'
    if log_name is None:
        log_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    if log_name == '':
        log_name = 'default'

    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)

    if len(logger.handlers):    # if we're initializing a log, kill other
        logger.handlers = []    # open handles, so the latest init wins

    if not len(logger.handlers):    # if it's not already open, open it

        # now check the logging root, create it if it's not there
        if not os.path.isdir(log_root_dir):
            os.mkdir(log_root_dir)

        # create the path and add it to the handler
        log_path = os.path.join(log_root_dir, log_name + ".log")
        logger_fh = logging.FileHandler(log_path)

        #   set the formatter and add it via addHandler()
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s:\t%(message)s', YMDHMS
        )
        logger_fh.setFormatter(formatter)
        logger.addHandler(logger_fh)

    return logger




def check_api_key():
    """ Checks the API key on the request; bombs the whole request out if
    it wants to. """

    logger = get_logger()
    if not flask.request.api_key_valid:
        msg = "Incoming request '%s' from '%s' has invalid API key (%s)!"
        logger.warn(msg % (
            flask.request.url,
            flask.request.referrer,
            flask.request.api_key
            )
        )
        return None

    return True


def get_api_client():
    """ Checks the request's api_key, tries to return a string representing the
    webapp making the request. Returns None if it can't come up with a string
    for the requesting source. """

    # default value
    requester_netloc = urlparse(str(flask.request.referrer)).netloc

    if flask.has_request_context():
        if hasattr(flask.request, 'api_key'):
            api_key_owner = API.config['KEYS'].get(
                flask.request.api_key,
                requester_netloc,
            )
            if isinstance(api_key_owner, dict):
                return api_key_owner['owner']

            return api_key_owner

        return requester_netloc

    return None


#
#   special exception class definitions
#
class ConversionException(Exception):
    ''' Takes no arguments. Returns a 410 ("Gone.") and a standard blurb of text
    that we want to return to let users know their data is  too old. '''

    def __init__(self):
        Exception.__init__(self)
        self.logger = get_logger(log_name='error')
        self.msg = (
            'User data created prior to January 2019 that has was not '
            'ported to the KD:M API prior to October 2023 can no longer be '
            'converted. This data is stored in the API, but can no longer be '
            'accessed by external consumers. '
        )
        self.status_code = 410
        self.logger.exception("[%s] %s" % (self.status_code, self.msg))


class InvalidUsage(Exception):
    """ Raise this type of exception at any point to return an HTTP response to
    the requester. Syntax goes like this:

        raise utils.InvalidUsage("Message", status_code=400)

    Do this whenever the requester's param keys/values are not up to snuff, etc.
    """

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.logger = get_logger(log_name='error')
        self.msg = message
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
#       Mail!
#

class mailSession:
    """ Initialize one of these to authenticate via SMTP and send emails. This
    is a port from the legacy app."""

    def __init__(self):
        self.logger = get_logger()
        p_settings = settings.Settings('private')
        self.smtp_host = p_settings.get("smtp","host")
        self.smtp_user = p_settings.get("smtp","name")
        self.smtp_pass = p_settings.get("smtp","pass")
        self.sender_name = p_settings.get("smtp","name_pretty")
        self.no_reply = p_settings.get("smtp","no-reply")
        self.connect()

    def connect(self):
        self.server = smtplib.SMTP(self.smtp_host, 587)
        self.server.starttls()
        self.server.login(self.smtp_user, self.smtp_pass)
        self.logger.debug("SMTP Authentication successful for %s (%s)." % (
            self.smtp_user,
            self.smtp_host
            )
        )
        time.sleep(0.75)


    def send(self, reply_to=None, subject="KD:M API",
        recipients=API.config['ADMIN_EMAIL_ADDRESSES'],
        html_msg='This is a <b>test</b> message!'):

        """ Generic Emailer. Accepts a list of 'recipients', a 'msg' string and
        a sender name (leave undefinied to use admin@kdm-manager.com). """

        author = email.utils.formataddr(
            (
            str(email_Header(self.sender_name, 'utf-8')),
            self.no_reply
            )
        )
        msg = MIMEMultipart('alternative')
        msg['From'] = author
        msg['Subject'] = subject
        msg['To'] = recipients[0]

        if reply_to is not None:
            msg.add_header('reply-to', reply_to)

#        msg.attach(MIMEText(html_msg.encode('ascii','ignore'),'html'))
        msg.attach(MIMEText(html_msg,'html'))

        self.server.sendmail(self.no_reply, recipients, msg.as_string())
        self.server.quit()
        self.logger.debug("Email sent successfully!")


#
#	Generic exception auto-mailer
#

def email_exception(exception):
    """ This is called by the main Flask errorhandler() decorator in api.py
    when we have an unhandled exception at any point of responding to a request.

    This prevents user-facing failures from being silently swallowed. """

    # first, log it
    e_logger = get_logger(log_name='error')
    e_logger.warn('Preparing to email exception!')
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
        html_msg=s
    )
    e_logger.warn('Exception email sent!')


def email_error_report(report):
    """This assumes an authenticated user, since it's behind the login-required
    decorator in routes.py. It takes 'report' and uses a template to format it
    and then emails it out to the sysadmin address. """

    # finally, prepare the message template and the traceback for emailing
    msg = html_file_to_template("error_report.html")

    # do it
    s = msg.safe_substitute(
        user_login=flask.request.User.login,
        user_oid=flask.request.User._id,
        body=report,
    )
    e = mailSession()
    e.send(
        subject="KDM-Manager Error Report! [%s]" % socket.getfqdn(),
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
            ", ".join(["%s: %s" % (k, v) for k,v in kwargs.items()])
            )
        )
        return result

    # we only meter in the dev environment
    if socket.gethostname() in ['mona']:
        return timed
    return not_timed


def record_collection_use():
    ''' Logs a blurb about collection use during the request.'''

    logger = get_logger()
    for module in flask.request.kd_collections_initialized:
        if flask.request.kd_collections_initialized[module] > 1:
            msg = (
                'The %s collection was initialized %s times while processing '
                'this request!'
            )
            logger.warning(
                msg,
                module,
                flask.request.kd_collections_initialized[module]
            )


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
        'api_key_owner': get_api_client(),
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
            return flask.Response(response="Image not found!", status=404)
        image_file = BytesIO(self.img.read())
        return flask.send_file(image_file, mimetype="image/png")



#
#   misc. helper methods
#

def snake_to_camel_case(string):
    ''' Converts 'string' to a snake-case string. '''
    string = string.split('_')
    return "".join([part.capitalize() for part in string])


def deserialize_json(d):
    """ accepts a dict 'd' that we think might be JSON. Turns it into a normal
    python dict with python types, etc. """

    str_d = json.dumps(d)
    dict_d = json.loads(str_d, object_hook=json_util.object_hook)
    return(dict_d)


def get_application_url(strip_http=False):
    """ Determines the URL to use for API operations based on some socket
    operations and settings from the settings.cfg. Defaults to using localhost
    on the default API port defined in settings.cfg. """

    fqdn = socket.getfqdn()
    if fqdn == API.config['PRODUCTION']['app_fqdn']:
        output = API.config['PRODUCTION']['url']
    else:
        output = "https://%s" % (get_host_ip())

    if strip_http:
        return output[7:]
    else:
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

    start_time = start_time.replace(tzinfo=USCENTRAL)

    delta = (datetime.now(tzlocal()) - start_time)
    days = delta.days
    years = relativedelta(datetime.now(tzlocal()), start_time).years
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
        'templates',
        rel_path
    )
    return Template(open(tmp_file, "rb").read().decode())


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
        l = [str(i) for i in l]

    return " and ".join([
        ", ".join(l[:-1]),
        l[-1]
    ])


def list_compare(original_list, new_list):
    """ Compares 'original_list' to 'new_list' and returns two new lists,
    the first of which is a list of additions to 'original_list and and the
    second is a list of items to be removed from 'original_list'. """

    add = []
    for item in new_list:
        if item not in original_list:
            add.append(item)

    rm = []
    for item in original_list:
        if item not in new_list:
            rm.append(item)

    return add, rm


def list_compare_deluxe(list_1, list_2):
    """ Compares 'list_1' to 'list_2' and returns a string that
    can be used to visually diff the two lists. """

    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    output = []

    # Determine the maximum length of the elements in both lists
    max_length = max(max(len(item) for item in list_1), max(len(item) for item in list_2))

    # Determine the elements that exist in both lists
    common_elements = sorted(set(list_1).intersection(list_2))

    # Print the elements that exist in both lists
    for element in common_elements:
        output.append(f"{element.ljust(max_length)} | {element.ljust(max_length)}\n")

    # Determine the elements that exist only in list_1 and list_2 respectively
    elements_only_in_list_1 = sorted(set(list_1) - set(list_2))
    elements_only_in_list_2 = sorted(set(list_2) - set(list_1))

    # Print the interpolated elements
    for element_1, element_2 in zip(elements_only_in_list_1, elements_only_in_list_2):
        output.append(f"{element_1.ljust(max_length)} | {element_2.ljust(max_length)}\n")

    # Print any remaining elements from the longer list
    for element_1 in elements_only_in_list_1[len(elements_only_in_list_2):]:
        output.append(f"{element_1.ljust(max_length)} | {''.ljust(max_length)}\n")
    for element_2 in elements_only_in_list_2[len(elements_only_in_list_1):]:
        output.append(f"{''.ljust(max_length)} | {element_2.ljust(max_length)}\n")

    return ''.join(output)



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
HTTP_299 = flask.Response(
    response="This endpoint is deprecated!",
    status=299
)

# 400s
http_400 = flask.Response(response="Bad Request!", status=400)
http_401 = flask.Response(response="Authorization required", status=401)
http_402 = flask.Response(
    response="This is a subscribers-only endpoint!",
    status=402
)
http_403 = flask.Response(response="Unauthorized!", status=403)
HTTP_404 = flask.Response(response='Resource not found', status=404)
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
#   meta element of all API returns; related methods
#

def create_subscriptions_dict():
    """ Creates a dictionary representation of available subscription types."""

    settings_dict = settings.get('subscribers')

    output = {}
    for key, value in settings_dict.items():
        key_split = key.split("_")
        level_number = int(key_split[1])

        # set the handle and use it for the level number
        handle = 'level_%s' % level_number
        if not handle in output.keys():
            output[handle] = {}
        output[handle]['level'] = level_number

        # now process values
        if len(key_split) > 2:
            output[handle][key_split[2]] = value
        if len(key_split) == 2:
            output[handle]['desc'] = value


    return output


api_meta = {
    "meta": {
        'monster': {
            'copyright': (
                'Copyright © 2016 - %s Adam Poots Games, LLC. All Rights '
                'Reserved'
            ) % datetime.now().year,
            'version': versions.Version(
                handle=API.config['DEFAULT_GAME_VERSION'],
                no_assets=True
            ).serialize(),
        },
        "api": {
            "version": API.config['VERSION'],
            "age": get_time_elapsed_since(
                datetime.strptime('2016-10-13', '%Y-%m-%d'),
                units='age'
            ),
            'limits': {
                'nonsubscriber_settlements':
                    API.config['NONSUBSCRIBER_SETTLEMENT_LIMIT'],
            },
        },
        'server': {
            "hostname": socket.gethostname(),
            "debug": API.config['DEBUG'],
            'log_level': API.config['DEBUG'],
            'os': platform.platform(),
            'ipv4': get_host_ip(),
        },
        "info": {
            "about": "https://github.com/theLaborInVain/kdm-manager-api",
            "copyright": (
                "Copyright © 2015 - %s The Labor in Vain, Inc."
            ) % datetime.now().year,
            "license": {
                'url': (
                    "https://github.com/theLaborInVain/"
                    "kdm-manager-api/blob/master/LICENSE"
                ),
                'type': 'MIT license',
                'disclaimer': (
                    "The license covers application code in this "
                    "repository only. The license does not and cannot pertain "
                    "to the game assets (in the /app/assets folder), which "
                    "are the sole property of Adam Poots Games, LLC. and "
                    "which are presented here without authorization."
                ),
                'text': open(
                    os.path.join(API.root_path, '..', 'LICENSE'),
                    'r'
                ).read(),
            },
        },
        'subscriptions': create_subscriptions_dict(),   # remove in v4
        'kdm-manager':{
            'user_preferences': settings.get('users'),
            'subscriptions': create_subscriptions_dict(),
        },
        "object": {},
    },
}
