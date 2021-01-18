"""

    Patches and hotfixes go here.

    These should be methods with minimal imports that are used to fix database
    and/or other data quality issues.

    Do not write object-oriented or class code here!

"""

# standard library imports
import sys

# third party imports

# local imports
from app import utils, world
from app.models import users


def normalize_subscriber_level():
    """ Makes sure that all survivor level attributes are int type.

    The solution here is to find users with the deprecated 'patron' attribute,
    get their OID and initialize their user object, which will call the various
    baseline/normalize methods associated with initializing such a class.

    Afterwards, we run a world query to report on subscriber information.
    """

    patrons = utils.mdb.users.find({'patron': {'$exists': True}})
    print(" Found %s users with the 'patron' attribute!" % (patrons.count()))
    for patron in patrons:
        user_object = users.User(_id=patron['_id'])
    print(" Initialized %s user objects successfully!" % patrons.count())
    print(" World query 'subscribers_by_level' now looks like:\n" )

    # now, do the world query to check/verify
    world_object = world.World()
    query = world_object.debug_query('subscribers_by_level')
    print(query)


def rename_expansion(original_handle=None, new_handle=None):
    """ Updates settlements with 'original_handle' in their 'expansions' list
    to have 'new_handle' in its place. Preserves order.

    Sample syntax:

        ./admin.sh --patch rename_expansion --patch_args generic,swashbuckler

    """

    if original_handle is None or new_handle is None:
        err = "\n The 'original_handle' and 'new_handle' kwargs are required!\n"
        raise ValueError(err)

    original_handle = original_handle.strip()
    new_handle = new_handle.strip()

    targets = utils.mdb.settlements.find({'expansions': {'$in': [original_handle]}})

    msg = "\n Replace '%s' expansion with '%s' on %s settlements? [YES]: " % (
        original_handle,
        new_handle,
        targets.count()
    )

    approval = None
    while approval is None:
        try:
            approval = input(msg)
        except EOFError:
            pass

    # default to yes, e.g. if we just hit enter
    if approval is not None and len(approval) == 0:
        approval = 'Y'

    if approval[0].upper() != 'Y':
        print(' Exiting without making changes...\n')
        sys.exit(255)

    modified = 0

    print('\t    _id\t\t\t      created_on\t    name')

    for settlement in targets:
        old_handle_index = settlement['expansions'].index(original_handle)
        settlement['expansions'][old_handle_index] = new_handle
        utils.mdb.settlements.save(settlement)
        print('  [%s] %s %s' % (
                settlement['_id'],
                settlement['created_on'],
                settlement['name']
            )
        )
        modified += 1

    print('\n Modified %s settlements!\n' % modified)
