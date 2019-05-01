"""

    This module is concerned only with dropping old, unwanted/unused
    data from the local mdb.

    All methods here can be called from wherever (there's no class or
    object code here), e.g. from the admin module or from world or
    what have you.

    Do not write object-oriented code here.

"""

# standard lib imports
from datetime import datetime, timedelta

# third party imports
import pymongo

# local imports
from app import utils

# initialize a generic logger, so we get purge.log in the logs dir
LOG = utils.get_logger()



#
#   purge methods
#


def purge_settlement(settlement):
    """ Recursively purges a settlement, purging all survivors along with it.

    Returns the number of survivors purged (as an int) if successful.
    """

    LOG.warning(
        "Purging settlement: %s [%s]" % (settlement['name'], settlement['_id'])
    )

    # first, purge the survivors
    survivors_to_purge = utils.mdb.survivors.find(
        {'settlement': settlement['_id']}
    ).count()
    removed_survivors = utils.mdb.survivors.delete_many(
        {'settlement': settlement['_id']}
    )
    if removed_survivors.deleted_count == survivors_to_purge:
        LOG.critical("Purged %s/%s survivors!" % (
            survivors_to_purge,
            removed_survivors.deleted_count
            )
        )
    else:
        raise pymongo.errors.PyMongoError('Survivors could not be purged!')

    # now, purge the settlement
    removed_settlement = utils.mdb.settlements.delete_one(settlement)
    if removed_settlement.deleted_count == 1:
        LOG.critical('Purged settlement!')
    else:
        raise pymongo.errors.PyMongoError('Settlement was not purged!')

    return removed_survivors.deleted_count


#
#   wrappers for core methods above
#

@utils.metered
def purge_removed_settlements(arm=False):
    """ Finds settlements whose 'removed' date is outside of the grace period
    (which can be found in settings.get('users', 'removed_settlement_age_max')
    and, if armed, drops them from MDB.

    Which, to put that another way, is to say that this method is a dry run,
    unless explicitly set to actually do the purge.

    Set the 'arm' kwarg to True to purge. Otherwise, this just returns a list of
    settlements that would be purged.
    """

    LOG.warning("Purging 'removed' settlements from MDB!")

    all_removed_settlements = utils.mdb.settlements.find(
        {'removed': {'$exists': True}}
    )
    LOG.info(
        "Found %s 'removed' settlements" % all_removed_settlements.count()
    )

    eligible = []
    for settlement in all_removed_settlements:
        reference_date = (
            settlement['removed']
            + timedelta(
                days = utils.settings.get('users', 'removed_settlement_age_max')
            )
        )

        if reference_date < datetime.now():
            eligible.append(settlement)

    LOG.info("%s 'removed' settlements are eligible for purge." % len(eligible))

    if arm:
        settlements_purged = 0
        survivors_purged = 0
        for settlement in eligible:
            survivors_purged += purge_settlement(settlement)
            settlements_purged += 1
        LOG.warning(
            'Purged %s settlements and %s survivors!' % (
                settlements_purged,
                survivors_purged
            )
        )
        return {'settlements': settlements_purged, 'survivors': survivors_purged}
    else:
        LOG.info('Method is not armed. Exiting without performing purge...')
