
# standard lib imports
import io
from configparser import SafeConfigParser
import inspect
import json
import logging
from optparse import OptionParser
import os
import sys

# third party imports

# local imports
from app import API, utils

class Settings:

    def __init__(self, settings_type=None):
        """ Initialize a Settings object as public or private. """

        self.logger = API.logger

        cfg_public = os.path.join(API.root_path, "..", "settings_private.cfg")
        cfg_private = os.path.join(API.root_path, "..", "settings.cfg")

        # fail if the dir with settings.py does not have a settings.cfg
        for cfg_file in [cfg_public, cfg_private]:
            if not os.path.isfile(cfg_file):
                raise OSError(
                    "%s: Settings file '%s' does not exist!" % (
                        sys.argv[0],
                        c_path
                    )
                )

        self.config = SafeConfigParser()
        self.config.optionxform = lambda option: option # disables case-insensitivity
#        self.config.file_path = c_path
#        self.config.readfp(open(self.config.file_path))
        self.config.read([cfg_public, cfg_private])
#        self.config.settings_type = settings_type



    def get(self, section, key):
        """ Gets a value. Tries to do some duck-typing. """

        raw_value = self.config.get(section,key)
        if raw_value in ["True", "False"]:
            return self.config.getboolean(section,key)
        else:
            try:
                return self.config.getint(section,key)
            except ValueError:
                pass

        return raw_value



def check_key(k=None):
    """ Laziness/convenience function to check a key without initializing a
    settings object. """

    S = Settings()
    if k in S.api_keys.keys():
        return S.api_keys[k]   # i.e. return the user name
    else:
        return False


def get(section=None, query=None, private=False):
    """ Laziness/convenience function to get a setting without initializing a
    Settings object. """

    if section is None:
        raise TypeError("settings.get() requires the 'section' kwarg!")

    S = Settings()
    if private:
        S = Settings("private")
        # this is deprecated
        err = "Use of the 'private' kwarg in settings.get() is deprecated!"
        S.logger.warn(err)

    if section is not None and query is None:
        return dict(S.config.items(section))

    return S.get(section, query)


def update(section=None, key=None, value=None):
    """ Sets a key/value in a section, writes a new file and exits. """
    if section is None or key is None or value is None:
        raise TypeError("update() does not accept None type arguments!")

    S = Settings()
    S.config.set(section, key, value)
    with open(S.config.file_path, 'wb') as c_file:
        S.config.write(c_file)


