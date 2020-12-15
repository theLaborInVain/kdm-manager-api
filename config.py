"""

    Grinberg-style config, similiar to what he's got on
    blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms


"""

import os
import socket

class Config(object):
    DEBUG = True
    ENVIRONMENT = {'is_production': False}
    TESTING = True
    PRODUCTION = {
        'app_fqdn': 'advanced-kdm-manager.c.kdm-manager.internal'
    }

    def __init__(self):
        """ Do some things whenever we initialize this module. """

        if socket.getfqdn() == self.PRODUCTION['app_fqdn']:
            self.ENVIRONMENT['is_production'] = True

        pass
