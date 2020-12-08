"""

    Grinberg-style config, similiar to what he's got on
    blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms


"""

import os

class Config(object):
    DEBUG = True
    TESTING = True

    def __init__(self):
        """ Do some things whenever we initialize this module. """

        pass
