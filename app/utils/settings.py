#!/usr/bin/python2.7


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
from app import api


class Settings:

    def __init__(self, settings_type=None):
        """ Initialize a Settings object as public or private. """

        if settings_type == 'private':
            c_path = os.path.join(api.root_path, "..", "settings_private.cfg")
        else:
            c_path = os.path.join(api.root_path, "..", "settings.cfg")

        # fail if the dir with settings.py does not have a settings.cfg
        if not os.path.isfile(c_path):
            raise OSError("%s: Settings file '%s' does not exist!" % (sys.argv[0], c_path))

        self.config = SafeConfigParser()
        self.config.file_path = c_path
        self.config.readfp(open(self.config.file_path))
        self.config.settings_type = settings_type

        self.load_api_keys()


    def load_api_keys(self):
        """ Looks for an API keys file and tries to read it. If it doesn't
        find one, it sets self.secret_keys to be an empty dict. """

        self.api_keys = {}

        try:
            fh = file(self.get("api","api_keys_file"), "rb")
        except:
            return False

        lines = fh.readlines()
        for line in lines:
            line = line.strip()
            key, ident = line.split("|~|")
            self.api_keys[key] = ident


    def get(self, section, key):
        """ Gets a value. Tries to do some duck-typing. """

        raw_value = self.config.get(section,key)
        if raw_value in ["True","False"]:
            return self.config.getboolean(section,key)
        else:
            try:
                return self.config.getint(section,key)
            except ValueError:
                pass

        return raw_value


    def jsonify(self):
        """ Renders the config object as JSON, set it as an attribute of the
        settings object AND returns it (just in case you need it right away. """

        d = {}

        for section in self.config.sections():
            d[section] = {}
            for option in self.config.options(section):
                d[section][option] = self.get(section,option)
        self.config.json = json.dumps(d)

        return self.config.json



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

    if section is None or query is None:
        raise TypeError("settings.get() does not accept None type arguments.")
    if not private:
        S = Settings()
    else:
        S = Settings("private")
    return S.get(section,query)


def update(section=None, key=None, value=None):
    """ Sets a key/value in a section, writes a new file and exits. """
    if section is None or key is None or value is None:
        raise TypeError("update() does not accept None type arguments!")

    S = Settings()
    S.config.set(section, key, value)
    with open(S.config.file_path, 'wb') as c_file:
        S.config.write(c_file)


