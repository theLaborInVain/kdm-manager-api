""" The utilities module used by the API. """

# std lib imports
from datetime import datetime, timedelta
import functools
import socket

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
#   methods
#

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

#
# 	HTTP response objects
#

http_200 = flask.Response(response="OK!", status=200)
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
http_422 = flask.Response(
	response="Missing argument, parameter or value",
	status=422
)

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
            "age": get_time_elapsed_since(datetime.strptime('2016-10-13', '%Y-%m-%d'), units='age'),
            "hostname": socket.gethostname(),
            "mdb_name": settings.get("api","mdb"),
        },
        "admins": list(mdb.users.find({"admin": {"$exists": True}}).sort('login')),
        "object": {},
    },
}
