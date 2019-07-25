"""

    In the 1.0.0 release, we don't do the daemon stuff: all of that is
    outsourced to supervisord, for better or for worse.

    Start and stop the daemon using world.sh in the root dir of the app.

"""
# standard lib imports
import argparse
import time

# local imports
from app import utils, world
from app.admin import purge


def parse_arguments():
    """ Parse the CLI arguments to decide what we're doing here. """

    parser = argparse.ArgumentParser(description=' KDM API World Utility!')

    parser.add_argument("-l", "--list", dest="list", default=False,
                        action="store_true",
                        help="Dump a list of warehoused asset handles.")
    parser.add_argument("-u", "--update", dest="update_one_asset_handle",
                        metavar="top_innovations",
                        help="Refresh/reset ONE warehoused asset handle.")
    parser.add_argument("-r", "--refresh", dest="refresh", default=False,
                        action="store_true",
                        help="Refresh/reset ALL warehoused asset handles.")
    parser.add_argument("--index", dest="index_collections", default=False,
                        action="store_true", help="Creates indexes.")
    parser.add_argument("--daemon", dest="start_daemon", default=False,
                        action="store_true", help="Starts the world daemon.")
    parser.add_argument("--debug", dest="debug_query", metavar="avg_pop",
                        help=("Execute a query method and print results. "
                        "Writes debug results to log. DOES NOT update mdb."), )

    return parser.parse_args()


def start_daemon():
    """ Starts the daemon in an interactive session. Do this with supervisord
    for a more authentic daemon experience. """

    while True:
        purge.purge_removed_settlements(arm=True)
        WORLD.refresh_all_assets()
        time.sleep(utils.settings.get("world", "refresh_interval") * 60)


if __name__ == "__main__":

    # initialize a world object and parse args
    WORLD = world.World()
    options = parse_arguments()

    if options.index_collections:
        print('\n\tIndexing user asset collections!')
        WORLD.create_indexes()
        print('\tDone!\n')

    if options.refresh:
        WORLD.refresh_all_assets(force=True)

    if options.update_one_asset_handle:
        WORLD.refresh_asset(
            asset_key=options.update_one_asset_handle,
            force=True
        )
        print("\n\tDone!\n")

    if options.debug_query:
        results = WORLD.debug_query(options.debug_query)
        print("\n")
        print(results)
        msg = "\n See '%s' for complete query debug info!\n"
        print (msg % (WORLD.logger.handlers[0].baseFilename))

    if options.list:
        print(WORLD.list('keys_cli'))

    if options.start_daemon:
        start_daemon()


