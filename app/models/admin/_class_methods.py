"""

    Class methods for admin panel and related objects live here.

    These are imported by app/admin/__init__.py so that we can do calls such
    as a = admin.AdminObject() or r = admin.ReleaseObject(), etc.


"""

# standard library
from datetime import datetime

# second party imports
import flask
import pymongo

# KDM API imports
from app import utils

from .._data_model import DataModel
from .._user_asset import UserAsset

class ChangeLog(UserAsset):
    ''' This is the class definition for a 'ChangeLog' which is a kind of user
    object where the administrator is the user who creates the asset. '''

    DATA_MODEL = DataModel('release')
    DATA_MODEL.add('items', list, required=True)
    DATA_MODEL.add('platform', str, required=True)
    DATA_MODEL.add('published', bool, required=False, default=False)
    DATA_MODEL.add('published_on', datetime, required=False, unset_on_none=True)
    DATA_MODEL.add('sections', list, required=True)
    DATA_MODEL.add('summary', str, trusted_html=True)
    DATA_MODEL.add('version', dict)

    def __repr__(self):
        """ A nice repr string that shows the platform and version. """

        return "%s release (%s)" % (
            self.get_platform(), self.get_version_string()
        )

    def __init__(self, *args, **kwargs):
        """ Initialize with no args to create a new one. """

        # overwrite the default logger since this is an admin model
        self.logger = utils.get_logger(log_name='admin')
        self.collection='releases'
        UserAsset.__init__(self, *args, **kwargs)


    def new(self, params=None):
        """ Create a new release record. The 'params' kwarg should be a dict.
        Defaults to the incoming JSON from the request. """

        # default params to request
        if params is None:
            params = flask.request.get_json()

        platform = params.get('platform', None)
        if platform is None:
            raise utils.InvalidUsage(
                'Platform must be specified when creating a new release!',
                status_code=422
            )

        # make a new release record and save it
        self.logger.info("Creating a new release for '%s'", platform)
        self.release = self.DATA_MODEL.new()

        # set initial release values
        self.release.update({
            'created_by': flask.request.User._id,
            'platform': platform,
        })
        self.set_latest_version()   # needs self.release['platform']

        # finally, insert the record and use the _id to set self_id
        self._id = utils.mdb[self.collection].insert(self.release)



    def update(self, source=None, verbose=False):
        """ Updates attributes, saves. If calling as part of a request, set
        'source' to be flask.request.get_json()"""

        published_pre_update = self.release.get('published', False)

        # call the base class method; update attrs
        self.release = self.DATA_MODEL.apply(source, force_type=True)

        published_post_update = self.release.get('published', False)

        # handle published_on logic
        if not published_pre_update and published_post_update:
            self.release['published_on'] = datetime.now()
        elif published_pre_update and not published_post_update:
            del self.release['published_on']

        # sort things we want to sort
        self.release['sections'] = sorted(self.release['sections'])

        # save
        self.save(verbose=verbose, set_modified_on=True)


    #
    #   gets/sets
    #


    def get_platform(self):
        ''' Returns the 'platform' attribute of the record. '''
        return self.release.get('platform', None)


    def get_version_string(self):
        """ Returns the version dict as a string. """

        version = self.release.get('version', {})

        return "%s.%s.%s" % (
            version.get('major', 0),
            version.get('minor', 0),
            version.get('patch', 0),
        )


    def set_latest_version(self):
        """ Uses self.release['platform'] to get the latest release for that
        platform and set the current self.release['version'] to that release's
        version. """

        # set default
        self.release['version'] = {'major': 0, 'minor': 0, 'patch': 0}

        # try to get latest
        latest = utils.mdb[self.collection].find_one(
            {'platform': self.release['platform']},
            sort=[('created_on', pymongo.DESCENDING)]
        )

        # if latest a.) exists and b.) has a version, use it:
        if latest is not None and latest.get('version', None) is not None:
            for bit in ['major', 'minor', 'patch']:
                self.release['version'][bit] = latest['version'].get(bit, 0)
