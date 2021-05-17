"""

    Grinberg-style config, similiar to what he's got on
    blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms


"""

import os
import socket

class Config(object):
    ACTIVE_USER_HORIZON = 15    # minutes
    DEBUG = True
    DEFAULT_METHODS = ['GET','POST','OPTIONS']
    DEV_SSL_CERT = 'deploy/dev_cert.pem'
    DEV_SSL_KEY = 'deploy/dev_key.pem'
    ENVIRONMENT = {'is_production': False}
    TESTING = True
    MDB = "kdm-manager"
    NONSUBSCRIBER_SETTLEMENT_LIMIT = 3
    PORT = 8013
    PRODUCTION = {
        'app_fqdn': 'advanced-kdm-manager.c.kdm-manager.internal',
        'url': 'https://api.kdm-manager.com'
    }
    VERSION = "1.69.461"

    if socket.getfqdn() == PRODUCTION['app_fqdn']:
        ENVIRONMENT['is_production'] = True
