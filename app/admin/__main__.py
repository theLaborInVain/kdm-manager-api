"""

    This is what happens when __main__ gets called. We dance:

       - initialize an Administration object
       - process params, sort of like you would with optparse
       - analyze params, call methods of the Administration obect

"""
# standard library imports
import argparse
import getpass
from collections import OrderedDict
import socket
import sys
import time

# third party imports
from bson.objectid import ObjectId
import gridfs
from pymongo import MongoClient

# local imports
from app import API
from app import models, utils
from app.admin import clone, patch, purge

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

@utils.metered
def initialize():
    """ Completely initializes the application. Scorched earth. I'm not even
    kidding: unless you've got a database backup, there's no coming back from
    this one! YHBW
    """

    logger = utils.get_logger()
    MongoClient().drop_database(utils.settings.get('api','mdb'))
    logger.critical("Initialized database!")


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

        if not isinstance(m[k], dict):
            print("%s%s%s%s%s%s" % (
                tab, k, first_spacer, m[k], second_spacer, type(m[k])
                )
            )
        else:
            print(
                "%s%s%s%s%s%s" % (
                    tab, k, first_spacer, " " * gap_spaces, second_spacer, type(m[k])
                )
            )

            def dump_dict_key(dictionary, key, recursion_level=1):
                """ Lets us dump dictionary keys indefinitely and maintain
                CLI legibility by doing indents. """
                recursion_filler = "  " * recursion_level
                if isinstance(dictionary[key], dict):
                    print("%s%s%s" % (" " * gap_spaces, recursion_filler, key))
                    for r_key in dictionary[key].keys():
                        dump_dict_key(
                            dictionary[key],
                            r_key,
                            recursion_level + 1
                        )
                else:
                    print(
                        "%s%s`- %s: %s" % (
                            " " * gap_spaces,
                            recursion_filler,
                            key,
                            dictionary[key],
                        )
                    )

            for key in sorted(m[k].keys()):
                dump_dict_key(m[k], key)

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


        # dev / r&d
        #   clone (users)
        parser.add_argument('--dump_requests', dest='dump_requests',
                            default=None, metavar=5, type=int,
                            help="[DEV] Dumps the last N requests to the CLI.",
                            )
        parser.add_argument('--clone_user', dest='clone_user', default=None,
                            help="[DEV] "
                            "Clone one user from production to local.",
                            metavar="565f3d67421aa95c4af1e230")
        parser.add_argument('--clone_recent_users', dest='clone_recent_users',
                            default=False, action="store_true",
                            help="[DEV] "
                            "Clone recent production users to local."),

        #   admin (users)
        parser.add_argument('--user', dest='user', default=None,
                            help="Work with a user",
                            metavar="toconnell@tyrannybelle.com")
        parser.add_argument('--reset_password', dest='reset_pw', default=None,
                            help="[USER] Reset a user's password (manually)",
                            action='store_true')
        parser.add_argument("--admin", dest="user_admin", default=False,
                            action="store_true",
                            help=(
                                "[USER] "
                                "Toggle admin status (requires --user)."
                            ),
                            )
        parser.add_argument("--level", dest="user_subscriber_level", type=int,
                            help=(
                                "[USER] "
                                "Set subscriber level (requires --user)."
                            ),
                            metavar=2
                            )
        parser.add_argument("--settlements", dest="user_settlements",
                            default=False, action="store_true",
                            help=(
                                "[USER] "
                                "Dump user settlements (requires --user)."
                            ),
                            )

        # work with settlements
        parser.add_argument('--settlement', dest='settlement', default=None,
                            help=(
                                "[SETTLEMENT] "
                                "Work with a settlement"
                            ),
                            metavar="5d13762e84d8863941ed4e20")
        parser.add_argument('--dump_settlement', dest='dump_settlement',
                            default=None, help = (
                                "[SETTLEMENT] "
                                "Work with a settlement"
                            ),
                            action="store_true"),
        parser.add_argument('--event_log', dest='settlement_event_log',
                            help=(
                                "[SETTLEMENT] "
                                "Dump the settlement event log "
                                "(requires --settlement)."
                            ),
                            default=False,
                            action="store_true",
                            )

        # sysadmin / console cowboy / hacker shit
        parser.add_argument('--initialize', dest='initialize', default=False,
                            help=(
                                "[SYSADMIN] "
                                "Initialize the mdb database, '%s'"
                            ) % (
                                utils.settings.get('api','mdb'),
                            ), action="store_true",
                            )
        parser.add_argument('--patch', dest='apply_patch',
                            metavar="patch_method", default=None,
                            help=(
                                "[SYSADMIN] "
                                "Apply a patch (from the patches.py module)."
                            ),
                            )
        parser.add_argument("--purge_settlements", dest="purge_settlements",
                            help=(
                                "[SYSADMIN] "
                                "Drops settlements marked 'removed' from mdb. "
                                "Works recursively & drops 'removed' survivors."
                                " Max age is date removed + %s days."
                                ) % (
                                    utils.settings.get(
                                        'users',
                                        'removed_settlement_age_max'
                                    )
                                ),
                            action="store_true", default=False)

        self.options = parser.parse_args()
        self.validate_args()


    #
    #   methods for working with the arguments passed to the object
    #

    def validate_args(self):
        """ This is our general-purpose sanity-checker. """

        # 1.) too many clones:
        if (
            self.options.clone_user is not None
            and self.options.clone_recent_users == True):
            msg = (
                "The '--clone_user' and '--clone_recent_users' arguments may"
                "not be used together!"
            )
            raise AttributeError(msg)


    def process_args(self):
        """ Analyzes self.options and self.args and calls one of our class
        methods. """

        # first, check to see if we're patching / hot-fixing
        if self.options.apply_patch is not None:
            p_name = str(self.options.apply_patch)
            try:
                patch_method = getattr(patch, p_name)
            except AttributeError:
                print(" '%s' is not a known patch! Exiting...\n" % p_name)
                sys.exit(1)
            patch_method()
            print(' Patch applied successfully!\n')


        # idiot-proofing
        if (
            self.options.user is not None and
            self.options.settlement is not None
        ):
            msg = "Cannot work with a user and a settlement at the same time!"
            raise ValueError(msg)


        # purge settlements/survivors marked 'removed' from mdb
        if self.options.purge_settlements:
            print(" Purging 'removed' settlements from MDB...")
            purge_results = purge.purge_removed_settlements(arm=True)
            print(' Settlements purged: %s'% purge_results['settlements'])
            print(' Survivors purged: %s' % purge_results['survivors'])
            print(' Done!\n')

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
                    "\n Project initialized!",
                    Style.RED,
                    "ALL DATA REMOVED!!\n",
                    Style.END
                )

            print(' Exiting...\n')
            sys.exit()

        # dump request logs
        if self.options.dump_requests is not None:
            self.dump_request_logs(self.options.dump_requests)

        # clone user (by OID) from legacy webapp
        if self.options.clone_user is not None:
            self.clone_one_user()

        # clone many users (via API route)
        if self.options.clone_recent_users == True:
            self.clone_many_users()


        # work with user
        if self.options.user is not None:
            self.work_with_user()

        # work with settlement
        if self.options.settlement is not None:
            self.work_with_settlement()

        return 0


    #
    #   log browsing
    #

    def dump_request_logs(self, how_many=1):
        """ Dumps logs of recent requests. """

        logs = utils.mdb.api_response_times.find().sort(
            'created_on',
            -1
        ).limit(how_many)

        for log in logs:
            dump_doc_to_cli(log)


    #
    #   methods for cloning users from production
    #

    def clone_one_user(self, user_oid=None, force=False):
        """ Clones one user. Prompts to reset password. """

        # first, override 'user_oid' kwarg if we've got CLI input
        if self.options.clone_user is not None:
            user_oid = self.options.clone_user

        if not ObjectId.is_valid(user_oid):
            raise AttributeError("'%s' is not a valid OID!" % user_oid)

        # do it!
        print(" Requesting user OID %s from the legacy webapp!" % user_oid)
        new_oid = clone.one_user_from_legacy_webapp(
            utils.settings.get('legacy', 'webapp_url'),
            utils.settings.get('keys', 'legacy_webapp_admin_key'),
            user_oid
        )

        # initialize the user as an object
        user_object = models.users.User(_id=new_oid)
        print(' %s%s%s has been cloned!' % (
            Style.YELLOW,
            user_object.user['login'],
            Style.END,
            )
        )

        # password reset business logic
        approval = "Y"
        if not force:
            msg = " Reset password? Type YES to reset: "
            approval = input(msg)

        if len(approval) > 0 and approval[0].upper() == 'Y':
            user_object.update_password('password')
            print(' Password has been reset!\n')
        else:
            print(" Password has NOT been reset.\n")



    @utils.metered
    def clone_many_users(self):
        """Gets a list of recent production users, iterates through the list
        calling the self.clone_one_user() on each. """

        # set the request URL, call the method from clone.py:
        prod_api_url = utils.settings.get('server', 'prod_url')
        print("\n API: %s\n Initiating request...\n" % prod_api_url)

        admin_login = input(' Login: ')
        admin_password = getpass.getpass(' Password: ')

        users = clone.get_recent_users_from_api(
            prod_api_url,
            admin_login,
            admin_password
        )

        if len(users) == 0:
            print('\n No recent users to clone! Exiting...\n')
            sys.exit(255)
        print('\n Preparing to clone %s users...\n' % len(users))

        # iterate the results:
        for prod_user in users:
            oid = prod_user['_id']['$oid']
            self.clone_one_user(oid, force=True)

        # summarize what we did:
        for cloned_user in users:
            print("  %s - %s " % (
                cloned_user['_id']['$oid'],
                cloned_user['login']
                )
            )

        print('\n\tDone!\n')


    #
    #   methods for working with a local user
    #

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


        if self.options.reset_pw:
            default_pass = 'password'
            pw_1 = input(" New password ['%s']: " % default_pass)
            pw_2 = input(" New password (again): ")

            if pw_1 != pw_2:
                raise ValueError("New passwords must match!")

            # handle defaulting
            if pw_1 == '':
                um_object.User.update_password(new_password=default_pass)
            else:
                um_object.User.update_password(new_password=pw_1)

            print()
            warn('Reset password for %s' % um_object.User.user['login'])
            time.sleep(2)


        # now that we've done whatever we're doing, dump the user to stdout to
        #   show the changes

        um_object.dump()

        # finally, if we're dumping settlements, do it now
        if self.options.user_settlements:
            um_object.dump_settlements()


    #
    #   methods for working with a local settlement
    #

    def work_with_settlement(self):
        """ In which we perform settlement maintenance based on self.options."""

        # first, see if self.options.user it looks like an email address
        if not ObjectId.is_valid(self.options.settlement):
            msg = "'%s' does not look like a valid OID!" % (
                self.options.settlement
            )
            raise ValueError(msg)

        sm_object = SettlementManagementObject(
            oid=ObjectId(self.options.settlement)
        )
        sm_object.print_header()

        if self.options.dump_settlement:
            dump_settlement_to_cli(sm_object._id)

        if self.options.settlement_event_log:
            sm_object.dump_event_log()


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


class SettlementManagementObject:
    """ Like the UserManagementObject (above), the SettlementManagementObject
    is basically a special object used only by admin methods that allows the
    user to perform settlement maintenance. """

    def __init__(self, oid=None):
        """ """

        self._id = ObjectId(oid)
        self.Settlement = models.settlements.Settlement(_id=self._id)


    def print_header(self):
        """ Prints a little header to stdout about the settlement."""

        print(
            " Working with settlement",
            Style.YELLOW,
            self.Settlement.settlement['name'],
            Style.END,
            self._id,
        )

        creator = utils.mdb.users.find_one(
            {'_id': self.Settlement.settlement['created_by']}
        )
        print("  (created by: %s %s)" % (creator['login'], creator['_id']))


    def dump_event_log(self):
        """ Uses the vanilla Settlement object's built-in get_event_log() method
        to get the settlement's event log and print it in a CLI-friendly way."""

        event_log = self.Settlement.get_event_log(query_sort=1)
        for event in event_log:
            dump_doc_to_cli(event, gap_spaces=35)



if __name__ == '__main__':
    stat()
    ADMIN_OBJECT = AdministrationObject()
    ADMIN_OBJECT.process_args()
