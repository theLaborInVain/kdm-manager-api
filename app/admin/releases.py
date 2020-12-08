"""
    Methods for working with releases, including the releaseObject class
    definition live here.
"""

# standard library imports
from datetime import datetime, timedelta
import json

# second party imports
from bson import json_util
from bson.objectid import ObjectId
import flask
import pymongo

# local imports
from app import API, models, utils


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
    elif ObjectId.is_valid(action) and record is None:
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
        r_obj = releaseObject()
        return flask.Response(
            json.dumps(r_obj.record, default=json_util.default),
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

    r_obj = releaseObject(_id=release_oid['$oid'])

    if action == 'update':
        r_obj.update()
        return flask.Response(
            json.dumps(r_obj.record, default=json_util.default),
            status=200,
            mimetype="application/json"
        )
    elif action == 'delete':
        return flask.Response(
            json.dumps(r_obj.delete().raw_result, default=json_util.default),
            status=200,
            mimetype="application/json"
        )

    # if we're still here, throw an error, because obviously we've got POST data
    #   to some oddball/unknown endpoint...
    err = "'%s' method not allowed!" % action
    return flask.Response(err, status=405)



class releaseObject(models.StructuredObject):
    """ The releaseObject class definition. Initialize one of these to work
    with a release. Initialize with no arguments to use the values in the
    request.json. """


    def __init__(self, *args, **kwargs):
        """ Initialize with no args to create a new one. """

        # first, execute the init of our base class method
        super().__init__(self, *args, **kwargs)

        self.request = flask.request.get_json()
        self.logger = utils.get_logger(log_name='admin')
        self.mdb = utils.mdb.releases

        self.data_model = {
            'created_on': datetime,
            'created_by': ObjectId,
            'modified_on': datetime,
            'platform': str,
            'version': dict,
            'summary': str,
            'sections': list,
            'items': list,
            'details': list,
            'published': bool,
            'published_on': datetime,
        }

        self.load() # sets self._id if it isn't set


    def __repr__(self):
        """ A nice repr string that shows the platform and version. """

        return "%s release (%s)" % (self.platform, self.get_version_string())


    def load(self):
        """ Load a release record. """
        if getattr(self, '_id', None) is None:
            self.new()

        self.record = self.mdb.find_one({'_id': self._id})
        if self.record is None:
            err = "Release OID '%s' not found!" % self._id
            raise utils.InvalidUsage(err, status_code=400)

        for key, value in self.data_model.items():
            setattr(self, key, self.record.get(key, None))


    def new(self):
        """ Create a new release record. """

        platform = self.request.get('platform', None)
        if platform is None:
            raise utils.InvalidUsage(
                'Platform must be specified when creating a new release!',
                status_code=422
            )

        self.logger.info("Creating a new release for '%s'" % platform)
        self._id = self.mdb.insert({})

        self.created_on = datetime.now()
        self.created_by = flask.request.User._id
        self.platform = platform

        self.set_latest_version()
        self.save()


    def update(self):
        """ Updates attributes, saves. Uses the request JSON! """

        published_pre_update = getattr(self, 'published', False)

        # call the base class method; update attrs
        super().update(source=flask.request.get_json(), verbose=True)

        published_post_update = getattr(self, 'published', False)

        # handle published_on logic
        if not published_pre_update and published_post_update:
            self.published_on = datetime.now()
        elif published_pre_update and not published_post_update:
            self.published_on = None

        # sort things we want to sort
        self.sections = sorted(self.sections)

        self.modified_on = datetime.now()
        self.save(verbose=True)


    #
    #   gets/sets
    #

    def get_version_string(self):
        """ Returns the version dict as a string. """

        if self.version is None:
            self.version = {}

        return "%s.%s.%s" % (
            self.version.get('major', 0),
            self.version.get('minor', 0),
            self.version.get('patch', 0),
        )


    def set_latest_version(self):
        """ Uses self.platform to get the latest release for that platform and
        set the current self.version to that release's version. """

        # set default
        self.version = {'major': 0, 'minor': 0, 'patch': 0}

        # try to get latest
        latest = self.mdb.find_one(
            {'platform': self.platform},
            sort=[( 'created_on', pymongo.DESCENDING )]
        )

        # if latest a.) exists and b.) has a version, use it:
        if latest is not None and latest.get('version', None) is not None:
            for bit in ['major', 'minor', 'patch']:
                self.version[bit] = latest['version'].get(bit, 0)
