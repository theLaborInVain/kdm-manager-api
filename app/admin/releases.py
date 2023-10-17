"""

    The public_router() and private_router() methods that handle traffic
    for dev log and other admin requests are here as well.

"""

# standard library imports
import json

# second party imports
from bson import json_util
from bson.objectid import ObjectId
import flask
import pymongo

# local imports
from app import API, utils
from app.models.admin import ChangeLog


def public_router(action):
    """ Our "broker" method for accepting public API requests to perform an
    action. The endpoints we support here are relatively basic, but we do
    support one that handles OIDs, so that gets kind of sticky. """

    # set platforms first, since actions below depend on knowing what platforms
    #   we support
    platforms = []
    for key, app_dict in API.config['KEYS'].items():
        platforms.append(
            {
                'app': app_dict['owner'],
                'api_key': key
            }
        )

    # 1.) first handle misc./public actions that return lists
    output = None
    if action in ['dump', 'releases','all']:
        output = list(utils.mdb.releases.find().sort('created_on', -1))
    elif action in ['latest', 'current']:

        if flask.request.method == 'POST':
            platform = flask.request.get_json().get('platform', None)
            if platform is not None:
                output = utils.mdb.releases.find_one(
                    {'platform': platform, 'published': True},
                    sort=[( 'published_on', pymongo.DESCENDING )]
                )
        else:
            output = []
            for platform in platforms:
                latest = utils.mdb.releases.find_one(
                    {'platform': platform['app'], 'published': True},
                    sort=[( 'published_on', pymongo.DESCENDING )]
                )
                if latest is not None:
                    output.append(latest)
    elif action in ['upcoming']:
        output = []
        for platform in platforms:
            upcoming = utils.mdb.releases.find(
                {
                    'platform': platform['app'],
                    '$or': [
                        {'published': False},
                        {'published': None}
                    ],
                },
                sort=[( 'created_on', pymongo.DESCENDING )]
            )
            if upcoming is not None:
                output.extend(upcoming)
    elif action == 'platforms':
        output = platforms

    if output is not None:
        return flask.Response(
            json.dumps(output, default=json_util.default),
            status=200,
            mimetype="application/json"
        )

    # finally, check and see if we're looking for a specific release
    record = utils.mdb.releases.find_one({'_id': ObjectId(action)})
    if ObjectId.is_valid(action) and record is not None:
        return flask.Response('got it!', 200)
    if ObjectId.is_valid(action) and record is None:
        return flask.Response('Release not found!', 404)

    err = "'%s' method not allowed!" % action
    return flask.Response(err, status=405)


def private_router(action):
    """ The private version of the previous method. This one handles routes
    where we require, at a minimum, a user that is recognized by the API as a
    registered user. We also check to see if they're an admin. """

    # we need to be an admin to get into here
    if not flask.request.User.user.get('admin', False):
        return utils.http_403

    if action == 'new':
        change_log = ChangeLog()
        return flask.Response(
            json.dumps(change_log.release, default=json_util.default),
            status=200,
            mimetype="application/json"
        )

    # 3.) JSON is required below, so sanity check for it here:
    if flask.request.get_json() is None:
        err = (
            "The '%s' action requires valid JSON in the POST (or is not a "
            "valid endpoint)!"
        )
        raise utils.InvalidUsage(err % action, 422)

    release_oid = flask.request.get_json().get('_id', None)
    if release_oid is None:
        raise utils.InvalidUsage('_id is required!', 422)

    change_log = ChangeLog(_id=release_oid['$oid'])

    if action == 'update':
        payload = utils.web.angular_to_python(flask.request.get_json())
        change_log.update(source=payload, verbose=True)
        return flask.Response(
            json.dumps(change_log.release, default=json_util.default),
            status=200,
            mimetype="application/json"
        )
    if action == 'delete':
        return flask.Response(
            json.dumps(
                change_log.remove(delete=True),
                default=json_util.default
            ),
            status=200,
            mimetype="application/json"
        )

    # if we're still here, throw an error, because obviously we've got POST data
    #   to some oddball/unknown endpoint...
    err = "'%s' method not allowed!" % action
    return flask.Response(err, status=405)
