'''

    web helpers.

'''

# standard library imports
from datetime import datetime

# second party imports
from bson.objectid import ObjectId


def angular_to_python(incoming):
    ''' Scrubs through an incoming dictionary called 'incoming' and converts
    Angular/JSON idiom to python. '''

    for key in incoming:

        if isinstance(incoming[key], dict):
            if incoming[key].get('$oid', False):
                incoming[key] = ObjectId(incoming[key]['$oid'])
            elif incoming[key].get('$date', False):
                dt_fmt = datetime.utcfromtimestamp(incoming[key]['$date']/1000)
                incoming[key] = dt_fmt

    return incoming
