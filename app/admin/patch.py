"""

    Patches and hotfixes go here.

    These should be methods with minimal imports that are used to fix database
    and/or other data quality issues.

    Do not write object-oriented or class code here!

"""

# standard library imports

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

