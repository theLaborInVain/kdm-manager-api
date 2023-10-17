"""

    This module is a traffic cop/laziness module meant to expose admin/panel
    methods and basically keep things moving.

    No real work is meant to be going on here.

    goal is to facilitate calls such as app.admin.pickle_login() or
    pickle = app.admin.AdminPickle(), etc.

"""

from app.admin import cli, panel, releases

