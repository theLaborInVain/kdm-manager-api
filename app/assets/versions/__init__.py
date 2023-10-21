"""

    Versions (formerly 'rules sets') are managed here.

    A version is a dictionary that includes information about a KD:M version and
    a key representing game assets that are updated in that version.



"""

# standard library
from datetime import datetime, timedelta

# asset module imports
from .._asset import Asset
from .._collection import Collection
from .definitions import *


class Assets(Collection):
    ''' Versions have their own, unique class method for creating a collection.
    object. Main reason being, they are a sort of 'meta' or governing object
    for other game assets, and thus cannot use the normal Collection() base
    class. '''


    def __init__(self, *args, **kwargs):
        """ There's a one-off method that gets called after init to add some
        info in; versions is sort of a sparse asset. """

        Collection.__init__(self, *args, **kwargs)
        self.set_version_vars()


    def set_version_vars(self):
        """ Sets self.version, which is a float, and self.version_string, which
        is also a float. Just kidding, it's a string. """

        versions_list = self.get_dicts()
        for a_dict in versions_list:

            handle = a_dict['handle']
            version = float(
                "%s.%s" % (a_dict['major'], a_dict['minor'])
            )

            self.assets[handle]['value'] = 0
            for attr in ['major', 'minor', 'patch']:
                self.assets[handle]['value'] += self.assets[handle].get(attr, 0)

            self.assets[handle]['version'] = version
            self.assets[handle]['version_string'] = str(version)
            self.assets[handle]['name'] = 'Version %s' % version

            released_summary = a_dict['released'].strftime('%B %Y')
            self.assets[handle]['released_summary'] = released_summary

            # next release
            if a_dict != versions_list[-1]:
                next_release = versions_list[versions_list.index(a_dict) + 1]
                eol = next_release['released'] - timedelta(1)
                self.assets[handle]['eol'] = eol
            else:
                self.assets[handle]['eol'] = datetime.now()


class Version():
    """ A version asset object is a special kind of game asset that has a unique
    class method, since the main assets.Asset() base class needs one of these to
    work correclty (so obviously it can't BE one of these simultaneously). """

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
        self.handle = self.kwargs.get('handle', None)

        if self.handle is None:
            err = "Version objects must be initialized with the 'handle' kwarg!"
            raise AttributeError(err)

        self.asset = VERSIONS[self.handle]

        if self.kwargs.get('no_assets'):
            self.remove_assets()


    def __repr__(self):
        ''' Custom repr. '''
        return self.__class__.__name__ + '(%s)' % self.handle


    def remove_assets(self):
        ''' Removes assets from the self.asset. '''

        if self.asset.get('assets', False):
            del self.asset['assets']


    def serialize(self):
        ''' Returns a dict. '''
        return dict(self.asset)
