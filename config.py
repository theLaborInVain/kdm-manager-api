"""

    Grinberg-style config, similiar to what he's got on
    blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms


"""

import pytz
import socket

class Config():
    ''' Already inherits from object; does not neet to inherit explicitly.'''

    ACTIVE_USER_HORIZON = 15    # minutes
    ADMIN_EMAIL_ADDRESSES = ['toconnell@thelaborinvain.com']
    ADMIN_PANEL_RELEASES_DEFAULT_SECTIONS = [
        'Administration',
        'Corrections and fixes',
        'Documentation',
        'Enhancements',
        'Expansion content',
        'Game Assets',
        'Deprecations',
        'kingdomDeath.css',
        'Refactor',
        'Version 3',
        'Version 4',
    ]
    ADMIN_PANEL_RELEASES_VISIBLE = 5
    AVATAR_DIMENSIONS = [450, 600]
    DEBUG = True
    DEFAULT_HEADERS = (
        'ACCESS-CONTROL-ALLOW-ORIGIN, API-KEY, AUTHORIZATION, CONTENT-TYPE'
    )
    DEFAULT_METHODS = ['GET', 'POST', 'OPTIONS']
    DEFAULT_GAME_VERSION = 'core_1_6'
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
    RESERVED_SETTLEMENT_URLS = [
        'campaign',
        'custom', 'custom_url',
        'deadrock', 'dead_rock',
        'settlement',
        'kingdom_death', 'kingdomdeath',
        'none',
        'potlantern', 'people_of_the_lantern', 'peopleofthelantern',
        'potstars', 'people_of_the_stars', 'peopleofthestars',
        'potsun', 'people_of_the_sun', 'peopleofthesun',
        'blacklantern', 'the_black_lantern', 'theblacklantern',
        'monster', 'monsters'
    ]
    TIMEZONE = pytz.timezone('US/Central')
    USER_ASSET_COLLECTIONS = ['releases', 'settlements', 'survivors', 'users']
    VERSION = "1.172.1049"
    WORLD_ASSET_MAX_AGE = 15    # minutes
    WORLD_REFRESH_INTERVAL = 5  # minutes

    if socket.getfqdn() == PRODUCTION['app_fqdn']:
        ENVIRONMENT['is_production'] = True
