"""

    This is what happens when __main__ gets called. We dance:

       - initialize an Administration object
       - process params, sort of like you would with optparse
       - analyze params, call methods of the Administration obect

"""
# standard library imports
import argparse
from collections import OrderedDict
import socket
import sys

# third party imports
from bson.objectid import ObjectId

# local imports
from app import API
from app import models, utils
from app.admin import clone

#
#   misc. helper methods for CLI admin tasks
#

# CLI colors
class Style:
    """ A bogus class used to make it easier to inject color into print()
    statements (of which we have more than a few in this module)."""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# API stat
def stat():
    """ Summarizes the state of the API. """
    output_str = ["", "*", " "*7, "API:"]
    api_str = []
    for key in ['version', 'mdb']:
        api_str.append("%s: %s" % (key, API.settings.get('api', key)))
    output_str.append(", ".join(api_str))
    print(" ".join(output_str) + "\n")


# fancy print
def warn(message=None):
    """ Prints 'message', a str, to stdout with some formatting. """
    print(Style.GREEN, " *", Style.END, Style.BOLD, message, Style.END)


#   Database methods start here
#

def initialize():
    """ Completely initializes the application. Scorched earth. I'm not even
    kidding: unless you've got a database backup, there's no coming back from
    this one! YHBW
    """
    avatars = 0
    for survivor in utils.mdb.survivors.find():
        if "avatar" in survivor.keys():
            gridfs.GridFS(mdb).delete(survivor["avatar"])
            avatars += 1
    print("\n Removed %s avatars from GridFS!" % avatars)

    for collection in [
        "users",
        "sessions", # this is re: the legacy webapp; its days are numbered
        "survivors",
        "settlements",
        "settlement_events",
        "user_admin",
        'response_times']:
        utils.mdb[collection].remove()



#   Dumpers start here: these basically dump a dictionary to the CLI so that the
#       administrator can read it

# dictionary dumper
def dump_doc_to_cli(m, tab_spaces=2, gap_spaces=20, buffer_lines=0):
    """ Dumps a single MDB record to stdout using print() statements.

    Also works for dict objects. You know. Becuase they're the same thing.
    """

    tab = " " * tab_spaces
    buffer_spacer = "%s" % "\n" * buffer_lines

    print(buffer_spacer)

    # respecognize ordered dict key order
    if isinstance(m, OrderedDict):
        keys = m.keys()
    else:
        keys = sorted(m.keys())

    for k in keys:
        first_spacer = " " * (gap_spaces - len(k))
        if gap_spaces >= 30:
            second_spacer = " " * (gap_spaces - len(str(m[k])))
        else:
            second_spacer = " " * ((gap_spaces * 2) - len(str(m[k])))
        print("%s%s%s%s%s%s" % (
            tab, k, first_spacer, m[k], second_spacer, type(m[k])
        ))

    print(buffer_spacer)


# survivor dumper
def dump_survivor_to_cli(s_id):
    """ Dump a simplified representation of a survivor to the CLI buffer. """

    spacer = 30

    s = utils.mdb.survivors.find_one({'_id': s_id})
    print(
        "  %s\t" % s['_id'],
        "%s | %s" % (s['sex'], s['name']),
        " " * (spacer - len(s['name'])),
        "created: %s" % (s['created_on'].strftime(utils.ymd)),
        end=''
    )

    if s.get('removed', False):
        print(" / removed: %s" % (s['removed'].strftime(utils.ymd)), end='')

    print()


# settlement dumper
def dump_settlement_to_cli(s_id, verbose=False):
    """ Dump a simplified representation of a settlement dict 's' to the
    command line. """

    s = utils.mdb.settlements.find_one({'_id': s_id})

    if verbose:
        dump_doc_to_cli(s)
    else:
        s_repr = OrderedDict()

        attrs = ['_id', 'name', 'campaign', 'expansions',
                 'created_by', 'created_on']
        for attr in attrs:
            try:
                s_repr[attr] = s[attr]
            except:
                s_repr[attr] = None
        dump_doc_to_cli(s_repr)

    if s.get('removed', False):
        print(' \x1b[1;31;40m Removed on %s \x1b[0m \n' % s['removed'])

    survivors = utils.mdb.survivors.find({'settlement': s['_id']})
    removed_survivors = utils.mdb.survivors.find(
        {'settlement': s['_id'], 'removed': {'$exists': True}}
    )

    print("  %s survivors found. %s have been removed.\n" % (
        survivors.count(),
        removed_survivors.count()
    ))

    for survivor in survivors:
        dump_survivor_to_cli(survivor['_id'])

    print()



#
#   class methods below:
#       - AdministrationObject
#       - UserManagementObject
#

class AdministrationObject:
    """ The AdministrationObject class is basically just a way of making
    argument parsing and processing a little more OO and therefore easier to
    remember/debug. """

    def __init__(self):
        """
            DO NOT INITIALIZE ONE OF THESE UNLESS __name__ == '__main__'

        Once initialized, this object is used to perform an admin function and,
        therefore, all of its methods return an exit status.

        """

        parser = argparse.ArgumentParser(description=' KDM API Administration!')
        parser.add_argument('--initialize', dest='initialize', default=False,
                            help="Initialize the mdb database, '%s'" % (
                                utils.settings.get('api','mdb'),
                            ), action="store_true", )
        parser.add_argument('--clone_user', dest='clone_user', default=None,
                            help="Clone one user from production to local.",
                            metavar="565f3d67421aa95c4af1e230")
        parser.add_argument('--user', dest='user', default=None,
                            help="Work with a user",
                            metavar="toconnell@tyrannybelle.com")
        parser.add_argument("--admin", dest="user_admin", default=False,
                            action="store_true",
                            help="Toggle admin status (requires --user).")
        parser.add_argument("--level", dest="user_subscriber_level", type=int,
                            help="Set subscriber level (requires --user).",
                            metavar=2,
                            )
        parser.add_argument("--settlements", dest="user_settlements",
                            default=False, action="store_true",
                            help="Dump user settlements (requires --user).")

        self.options = parser.parse_args()


    def process_args(self):
        """ Analyzes self.options and self.args and calls one of our class
        methods. """

        # initialize MDB
        if self.options.initialize:
            # sanity/env check
            print(" hostname: %s" % socket.gethostname())
            if socket.gethostname() not in ["mona"]:
                print(" Holy shit! This is not the dev machine! Exiting...\n")
                sys.exit(1)

            msg = (
                ' Initialize the project and',
                '%sremove all data%s?' % (Style.YELLOW, Style.END),
                'Type "YES" to proceed: ',
            )
            manual_approve = input(" ".join(msg))
            if manual_approve == "YES":
                initialize()
                print(
                    Style.BOLD,
                    "Project initialized!",
                    Style.RED,
                    "ALL DATA REMOVED!!\n",
                    Style.END
                )

            print(' Exiting...\n')
            sys.exit()

        # clone user (by OID) from legacy webapp
        if self.options.clone_user is not None:
            self.clone_one_user()

        # work with user
        if self.options.user is not None:
            self.work_with_user()


    def clone_one_user(self):
        """ Clones one user. Prompts to reset password. """
        if not ObjectId.is_valid(self.options.clone_user):
            raise AttributeError(
                "'%s' is not a valid OID!" % self.options.clone_user
            )

        # do it!
        new_oid = clone.one_user_from_legacy_webapp(
            utils.settings.get('legacy', 'webapp_url'),
            utils.settings.get('legacy', 'admin_key', private=True),
            self.options.clone_user
        )

        user_object = models.users.User(_id=new_oid)
        print(' %s has been cloned!' % user_object.user['login'])
        msg = " Reset password? Type YES to reset: "
        approval = input(msg)

        if len(approval) > 0 and approval[0].upper() == 'Y':
            user_object.update_password('password')
            print(' Password has been reset!\n')
        else:
            print(" Password has NOT been reset.\n")


    def work_with_user(self):
        """ In which we perform user maintenance based on self.options. """

        # first, see if self.options.user it looks like an email address
        if (not ObjectId.is_valid(self.options.user)
                and '@' in self.options.user):
            u_oid = models.users.get_user_id_from_email(self.options.user)
            um_object = UserManagementObject(oid=u_oid)
        else:
            um_object = UserManagementObject(oid=self.options.user)
        um_object.print_header()

        # now that we have a UserManagementObject initialized, see what it
        #   looks like the administrator wants to do with the user

        if self.options.user_admin:
            um_object.User.toggle_admin_status()
            warn('Set admin status to %s!' % um_object.User.is_admin())

        if isinstance(self.options.user_subscriber_level, int):
            um_object.User.set_subscriber_level(
                self.options.user_subscriber_level
            )
            warn('Set subscriber level to %s!' % (
                um_object.User.get_subscriber_level()
            ))


        # now that we've done whatever we're doing, dump the user to stdout to
        #   show the changes

        um_object.dump()

        # finally, if we're dumping settlements, do it now
        if self.options.user_settlements:
            um_object.dump_settlements()


class UserManagementObject:
    """ The UserManagementObject (UMO in releases < 1.0.0) is basically an
    object with a bunch of goofy/one-off methods for doing user management
    operations via CLI. """

    def __init__(self, oid=None):
        """ Initializes a user the normal way, and sets the initialized user
        object as self.User, e.g. if you want to call User object methods.

        Also has a bunch of its own methods that are not available via the
        normal User object, and are admin-specific. """

        if not ObjectId.is_valid(oid):
            print("The user ID '%s' is not a valid Object ID." % (oid))
            sys.exit(1)
        self._id = ObjectId(oid)
        self.User = models.users.User(_id=self._id)
        self.login = self.User.user['login']


    def dump(self):
        """ Dump the user to stdout in a colorful, highly human readable sort
        of way. """

        serialized_user = self.User.serialize(dict)['user']
        mini_repr = OrderedDict()
        if 'admin' in self.User.user.keys():
            mini_repr['admin'] = self.User.user['admin']

        for time_attr in ['created_on', 'latest_sign_in', 'latest_activity',
                          'latest_authentication']:
            try:
                mini_repr[time_attr] = utils.get_time_elapsed_since(
                    serialized_user[time_attr], 'age'
                )
            except KeyError:
                mini_repr[time_attr] = None
        for attr in ['settlements_created', 'survivors_created']:
            mini_repr[attr] = serialized_user[attr]
        dump_doc_to_cli(mini_repr, gap_spaces=25)

        print(" User subscriber status:")
        dump_doc_to_cli(self.User.user['subscriber'])

        if self.User.user['preferences'] != {}:
            print(' User Preferences:')
            dump_doc_to_cli(self.User.user['preferences'], gap_spaces=35)


    def dump_settlements(self):
        """ Dump a CLI summary of the user's settlements. """
        settlements = utils.mdb.settlements.find({'created_by': self._id})
        if settlements is not None:
            ok = input(str(
                "\n Press a key to dump %s settlements: " % settlements.count()
            ))
            print("\n", Style.BOLD, "User settlements:", Style.END)
            for s in settlements:
                dump_settlement_to_cli(s['_id'])


    def print_header(self):
        """ Prints a little header to stdout that says who we're working on."""

        print(
            " Working with user", Style.YELLOW, self.login, Style.END, self._id,
        )



if __name__ == '__main__':
    stat()
    ADMIN_OBJECT = AdministrationObject()
    sys.exit(ADMIN_OBJECT.process_args())