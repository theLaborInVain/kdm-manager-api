"""

    Versions (formerly 'rules sets') are managed here.

"""

from datetime import datetime, timedelta

from app import models

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        """ There's a one-off method that gets called after init to add some
        info in; versions is sort of a sparse asset. """

        models.AssetCollection.__init__(self,  *args, **kwargs)
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


class Version(models.GameAsset):
    """ Initialize an individual version object this way. """

    def __init__(self, *args, **kwargs):
        models.GameAsset.__init__(self,  *args, **kwargs)
        self.assets = Assets()
        self.initialize()
