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
from app import models, utils


def do(action):
    """ Our "broker" method for accepting API requests to perform an action.
    Most of what we do here is directing traffic based on the 'action' value
    and what we're able to parse from the request. """

    logger = utils.get_logger(log_name='admin')

    # first handle misc./admin actions
    if action == 'dump':
        releases = utils.mdb.releases.find().sort('created_on', -1)
        return flask.Response(
            json.dumps(list(releases), default=json_util.default),
            status=200,
            mimetype="application/json"
        )

    # since 'new' is a special action, handle it separately
    if action == 'new':
        r_obj = releaseObject()
        return flask.Response(
            json.dumps(r_obj.record, default=json_util.default),
            status=200,
            mimetype="application/json"
        )

    # now work with objects; if we're still here, we need an oid
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

    err = '%s method not allowed!' % action
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
