"""

    In the 1.0.0 release, the so-called world daemon is discontinued in favor
    of a supervisord-managed process that initializes the API.

    All of that lives in this module, but not necessarily in __init__.py

"""

# standard library imports
import os
import sys


# general imports
import collections
from copy import copy
from datetime import datetime, timedelta
from functools import reduce
import json
import pwd
import shutil
import subprocess
import stat
import time


# second party imports
from bson.son import SON
from bson import json_util
from bson.objectid import ObjectId
import flask
import pymongo


# local imports
from app import API, utils
from app.admin import notifications

    # models
from app.models import killboard as killboard_model
from app.models import campaigns as campaigns_models
from app.models import epithets as epithets_models
from app.models import innovations as innovations_models
from app.models import monsters as monster_models
from app.models import principles as principles_mod
from app.models import expansions as expansions_models
from app.models import settlements as settlements_models
from app.models import survivors as survivors_models

    # assets
from . import assets as world_assets




def cli_dump(key, spacer, value, suppress_print=False):
    """ Returns a command line interface pretty string for use in admin scripts
    and other things that dump strings to CLI over STDOUT. """

    spaces = spacer - len(key)
    output = "%s:" % key
    output += " " * spaces
    output += "%s" % value
    output += "\n"
    return output


#
# World object below
#

class World(object):

    def __init__(self, query_debug=False):
        """ Initializing a World object doesn't get you much beyond the ability
        to call the methods below. Typically you shouldn't initialize one of
        these unless you're trying to update warehoused data or maybe get info
        on a specific piece of warehosued data (which can more easily be gotten
        from the /world route JSON.)

        NB: if you're trying to fiddle/filter or otherwise futz with final
        output, check the self.list() method. """

        self.logger = utils.get_logger()
        self.query_debug = query_debug
        self.assets = world_assets.GENERAL

        # common list of banned names (across all collections)
        # maybe this should come from a config file?
        self.ineligible_names = [
            "-",                                # the 'blank' cause of death
            "test", "Test", "TEST",
            "unknown", "Unknown", "UNKNOWN",
            "Anonymous", "anonymous",
            'Unnamed'
        ]

        self.total_refreshed_assets = 0

    @utils.metered
    def create_indexes(self, collections_in_scope=[
            'survivors','settlements','settlement_events'
        ]):

        """ Indexes the main user asset collections. """

        for collection in collections_in_scope:

            msg = "Creating indexes for '%s' collection!" % collection
            self.logger.warn(msg)

            # survivors and settlements
            if collection in ['survivors', 'settlements']:
                utils.mdb[collection].create_index(
                    [
                        ("created_by", pymongo.ASCENDING),
                        ("created_on", pymongo.DESCENDING)
                    ],
                    unique=True
                )

            # survivor special index
            if collection in ['survivors']:
                utils.mdb[collection].create_index([
                    ('created_by', pymongo.ASCENDING),
                    ('created_on', pymongo.DESCENDING),
                    ('settlement', pymongo.ASCENDING)
                ])

            # settlement event logs special index
            if collection in ['settlement_events']:
                utils.mdb[collection].create_index([
                    ('settlement_id', pymongo.ASCENDING),
                    ('created_by', pymongo.ASCENDING),
                    ('created_on', pymongo.DESCENDING),
                ])

            index_count = 1
            for index in utils.mdb[collection].list_indexes():
                self.logger.info('[%s] %s index: %s' % (
                    index_count, collection, index
                    )
                )
                index_count += 1


    @utils.metered
    def refresh_all_assets(self, force=False):
        """ Updates all assets. Set 'force' to True to ignore 'max_age' and
        'asset_max_age'. A wrapper for self.refresh_asset(). """

        if force:
            self.logger.warn('Beginning forced asset refresh...')
        else:
            self.logger.info("Refreshing stale warehouse assets...")

        self.total_refreshed_assets = 0

        for asset_key in list(self.assets.keys()):
            self.refresh_asset(asset_key, force=force)
            self.total_refreshed_assets += 1
            time.sleep(1)

        self.logger.info("Refreshed %s/%s assets." % (
            self.total_refreshed_assets,
            len(list(self.assets.keys()))
            )
        )


    @utils.metered
    def refresh_asset(self, asset_key=None, force=False):
        """ Updates a single asset. Checks the 'max_age' of the asset and falls
        back to settings.world.asset_max_age if it can't find one.

        Set 'force' to True if you want to force a refresh, regardless of the
        asset's age. """

        asset_dict = self.initialize_asset_dict(asset_key)

        # now determine whether we want to refresh it
        do_refresh = False
        current_age = None

        mdb_asset = utils.mdb.world.find_one({"handle": asset_key})

        if mdb_asset is None:
            self.logger.info("Asset handle '%s' not found in mdb!" % asset_key)
            do_refresh = True
        else:
            current_age = datetime.now() - mdb_asset["created_on"]

        if current_age is None:
            do_refresh = True
        elif current_age.seconds > asset_dict["max_age"]:
            if self.query_debug:
                msg = "Asset '%s' is %s seconds old (max age is %s seconds)."
                self.logger.debug(
                    msg % (
                        asset_key,
                        current_age.seconds,
                        asset_dict["max_age"]
                    )
                )
            do_refresh = True

        # finally, if we're going to force, just force it
        if force:
            do_refresh = True

        # now do the refresh, if necessary
        if do_refresh:
#            self.logger.debug("Refreshing '%s' asset..." % asset_key)
            try:
                self.update_asset_dict(asset_dict)
                self.update_mdb(asset_dict)
                self.logger.debug("Updated '%s' asset in mdb." % asset_key)
            except Exception as e:
                msg = "exception caught while refreshing '%s' asset!"
                self.logger.error(msg % asset_key)
                self.logger.exception(e)

        return asset_dict


    def initialize_asset_dict(self, asset_key):
        """ Turn an asset key (e.g. 'top_innovations', etc.) into a basic dict
        that is ready to be updated/processed. """

        # basic init
        if self.assets.get(asset_key, None) is None:
            msg = "Could not refresh '%s' asset: no such asset exists!" % asset_key
            self.logger.exception(msg)
            raise Exception(msg)

        asset_dict = self.assets[asset_key]
        asset_dict["handle"] = asset_key

        # default the asset's 'max_age' attribute if it hasn't got one
        if asset_dict.get("max_age", None) is None:
            asset_dict["max_age"] = utils.settings.get("world", "asset_max_age") * 60

        return asset_dict



    def update_asset_dict(self, asset_dict):
        """ This is where the magic happens: a valid asset_dict goes in and a
        fully fleshed-out asset dictionary with current data comes out.

        We actually use the API's built-in test_request_context() method and set
        bogus request params to do this, which helps us avoid tracebacks thrown
        by UserAsset objects that test the request context.
        """

        if asset_dict["handle"] not in dir(self):
            msg = (
                "Could not refresh '%s' asset:"
                "no such method found in world assets!" % asset_dict["handle"]
            )
            raise ValueError(msg)

        # first, try to get some fresh results from the update method, which is
        # a method of the World class object
        with API.test_request_context():
            flask.request.collection = None
            flask.request.log_response_time = None
            update_method = getattr(self, asset_dict["handle"])
            fresh_results = update_method()

        # now that we've got it, start updating the placeholder dict
        asset_dict.update({"created_on": datetime.now()})
        asset_dict.update({"value": fresh_results})

        # respect the asset dictionary's "limit" attrib, if extant
        if asset_dict.get("limit", None) is not None:
            asset_dict["value"] = asset_dict["value"][:asset_dict["limit"]]

        asset_dict["value_type"] = type(fresh_results).__name__

        return asset_dict


    def update_mdb(self, asset_dict):
        """ Creates a new document in mdb.world OR, if this handle already
        exists, updates an existing one. """

        existing_asset = utils.mdb.world.find_one(
            {"handle": asset_dict["handle"]}
        )
        if existing_asset is not None:
            asset_dict["_id"] = existing_asset["_id"]
        utils.mdb.world.save(asset_dict)
        utils.mdb.world.create_index("handle", unique=True)


    def remove(self, asset_id):
        """ Removes a single asset _id from mdb.world. """
        _id = ObjectId(asset_id)
        if utils.mdb.world.find_one({"_id": _id}) is not None:
            utils.mdb.world.remove(_id)
            self.logger.warn("Removed asset _id '%s'" % asset_id)
        else:
            self.logger.warn("Object _id '%s' was not found!" % asset_id)


    def list(self, output_type="JSON"):
        """ Dump world data in a few different formats."""

        # initialize our final dict
        d = copy(utils.api_meta)

        d["meta"]["object"]["panel_revision"] = utils.settings.get(
            "admin",
            "panel_revision"
        )

        d["world"] = collections.OrderedDict()


        # get the raw world info (we'll sort it later)
        raw_world = {}
        for asset in utils.mdb.world.find():
            raw_world[asset["handle"]] = asset
            raw_world_age = datetime.now() - asset['created_on']
            raw_world[asset["handle"]]["age_in_seconds"] = raw_world_age.seconds


        #
        # This is where we filter data key/value pairs from being returned
        #   by calls to the /world route
        #

        def recursive_key_del(chk_d, f_key):
            if f_key in list(chk_d.keys()):
                del chk_d[f_key]

            for k in list(chk_d.keys()):
                if type(chk_d[k]) == dict:
                    recursive_key_del(chk_d[k], f_key)

        for banned_key in ["max_age", "email", "admins"]:
            recursive_key_del(raw_world, banned_key)


        # sort the world dict
        key_order = sorted(raw_world, key=lambda x: raw_world[x]["name"])
        for k in key_order:
            d["world"][k] = raw_world[k]

        # output options from here down:

        spacer = 45
        if output_type == "CLI":
            spacer = 25
            print("\n\tWarehouse data:\n")
            for k, v in d["world"].items():
                cli_dump(k, spacer, v)
                print("")
        elif output_type == "keys":
            return list(d["world"].keys())
        elif output_type == "keys_cli":
            output = []
            for k in sorted(d["world"].keys()):
                output.append(cli_dump(k, spacer, d["world"][k]["_id"]))
            return "".join(output)
        elif output_type == dict:
            return d
        elif output_type == "JSON":
            return json.dumps(d, default=json_util.default)


    def dump(self, asset_handle):
        """ Prints a single asset to STDOUT. CLI admin functionality. """

        asset = utils.mdb.world.find_one({"handle": asset_handle})
        print(("\n\t%s\n" % asset_handle))
        spacer = 20
        for k, v in asset.items():
            cli_dump(k, spacer, v)
        print("\n")


    def debug_query(self, asset_key):
        """ Turns on debug mode, executes a query and returns its results dict
        as a pretty-formatted string.

        Intended for CLI debugging and admin reference/use. """

        self.query_debug = True
        # change the log level
        self.logger = utils.get_logger(log_level='DEBUG')

        self.logger.debug("Debugging '%s' query!" % asset_key)
        asset_dict = self.initialize_asset_dict(asset_key)
        msg = "'%s' asset dict initialized..." % asset_dict["handle"]
        self.logger.debug(msg)
        results = self.update_asset_dict(asset_dict)
        output = []
        for k in sorted(list(results.keys())):
            output.append(cli_dump(k, 20, results[k]))
        return "".join(output)

    #
    # refresh method helpers and shortcuts
    #

    def pretty_survivor(self, survivor):
        """ Clean a survivor up and make it 'shippable' as part of the world
        JSON. This initializes the survivor and will normalize it. """

        # init
        S = survivors_models.Survivor(_id=survivor["_id"], normalize_on_init=False)
        survivor["epithets"] = S.get_epithets("pretty")
        survivor["age"] = utils.get_time_elapsed_since(survivor["created_on"], "age")

        # redact/remove
        survivor["attribute_detail"] = 'REDACTED'

        # add settlement info
        settlement = utils.mdb.settlements.find_one({"_id": survivor["settlement"]})
        survivor["settlement_name"] = settlement["name"]

        return survivor

    @utils.metered
    def get_eligible_documents(self, collection=None, required_attribs=None,
                               limit=0, exclude_dead_survivors=True,
                               include_settlement=False, sort_on='created_on'):

        """ Returns a dict representing the baseline mdb query for a given
        collection.

        This should be used pretty much any time we need to go to the mdb for
        data. Writing direct queries is OK for one-offs, but this saves a lot of
        time and helps keep things DRY.
        """

        # base query dict; excludes ineligible names and docs w/o 'attrib'
        query = {"name": {"$nin": self.ineligible_names}}

        # add eligibility attrib if required
        if required_attribs is not None:
            if isinstance(required_attribs, list):
                for a in required_attribs:
                    query.update({a: {"$exists": True}})
            else:
                query.update({required_attribs: {"$exists": True}})

        # log if debugging
        if self.query_debug:
            self.logger.debug(
                "Gathering %s having '%s' values..." % (
                    collection,
                    required_attribs
                )
            )

        # exclude dead survivors switch
        if collection == "survivors" and exclude_dead_survivors:
            query.update({
                "dead": {"$exists": False},
            })

        # customize based on collection name
        if collection == "settlements":
            query.update({
                "lantern_year": {"$gt": 0},
                "population": {"$gt": 1},
                "death_count": {"$gt": 0},
            })
        elif collection == "survivors":
            pass
#            query.update({ })
        elif collection == "users":
            query.update({
                "removed": {"$exists": False},
            })
        elif collection == "killboard":
            query.update({
                "settlement_name": {"$nin": self.ineligible_names},
            })
        else:
            self.logger.error("The collection '%s' is not in world.py scope!")

        # get results
        if sort_on is not None:
            sort_params = [(sort_on, -1)]
        results = utils.mdb[collection].find(
            query,
            sort = sort_params
        ).limit(limit)

        # log an exception if results is None
        if results is None:
            self.logger.exception(utils.WorldQueryError(query=query))
            return None
        elif results.count() == 0:
            self.logger.exception(utils.WorldQueryError(query=query))
            return None

        # report on raw results if we're doing query_debug
        if self.query_debug:
            self.logger.debug(
                "Returning %s eligible %s!" % (results.count(), collection)
            )

        # change results from a query object to a list for return
        try:
            results = list(results)
        except pymongo.errors.OperationFailure as e:
#            self.logger.exception(e)
            self.logger.error(
                'Unable to return %s results as a list!' % results.count()
            )
            self.logger.debug('Attempting to re-sort by user...')
            results.rewind()
            results = list(results.sort('created_by', pymongo.DESCENDING))

        if len(results) == 1:
            return results[0]

        return results


    def get_minmax(self, collection=None, attrib=None):
        """ Gets the highest/lowest value for 'attrib' across all eligible
        documents in 'collection'. Returns a tuple. """

        sample_set = self.get_eligible_documents(collection, attrib)

        if sample_set is None:
            return (None, None)

        data_points = []
        for sample in sample_set:
            try:
                data_points.append(int(sample[attrib]))
            except TypeError:
                if self.query_debug:
                    err = "'%s' [%s] has non-int value for '%s': %s." % (
                        sample['name'], sample['_id'], attrib, sample[attrib],
                    ) + " Settlement excluded from sample set!"
                    self.logger.error(err)
        return min(data_points), max(data_points)


    def get_average(self, collection=None, attrib=None, precision=2,
                    return_type=float):

        """ Gets the average value for 'attrib' across all elgible documents in
        'collection' (as determined by the world.eligible_documents() method).

        Returns a float rounded to two decimal places by default. Use the
        'precision' kwarg to modify rounding precision and 'return_type' to
        coerce the return a str or int as desired. """

        # get the sample set
        sample_set = self.get_eligible_documents(collection, attrib)

        # some sanity check/debug stuff here
        if sample_set is None:
            return None

        if self.query_debug:
            msg = 'Calculating average for %s documents...'
            if isinstance(sample_set, list):
                self.logger.debug(msg % len(sample_set))
            elif isinstance(sample_set, pymongo.cursor.Cursor):
                self.logger.debug(msg % sample_set.count())

        # now gather datapoints, i.e. get the thing we want from the documents
        data_points = []
        for sample in sample_set:
            if sample.get(attrib, None) is None:
                if self.query_debug:
                    err = "'%s' [%s] has non-int value for '%s': %s." % (
                        sample['name'], sample['_id'], attrib, sample[attrib],
                    ) + " Settlement excluded from sample set!"
                    self.logger.error(err)
            else:
                try:
                    data_points.append(return_type(sample[attrib]))
                except: # in case we need to coerce a list to an int
                    data_points.append(return_type(len(sample[attrib])))

        # report on how many data points we've got before the reduce()
        if self.query_debug:
            self.logger.debug('Gathered %s data points.' % len(data_points))

        result = reduce(
            lambda x, y: x + y, data_points) / float(len(data_points)
        )

        # coerce return based on 'return_type' kwarg
        if return_type == int:
            return result
        elif return_type == float:
            return round(result, precision)
        else:
            return None


    def get_list_average(self, data_points):
        """ Super generic function for turning a list of int or float data into
        a float average. """

        list_length = float(len(data_points))
        if list_length == 0:
            return 0
        result = reduce(lambda x, y: x + y, data_points) / list_length
        return round(result, 2)


    def get_top(self, collection=None, attrib=None, limit=None, asset_type=str):
        """ Assuming that 'collection' documents have a 'attrib' attribute, this
        will return the top five most popular names along with their counts. """

        query = {attrib: {"$nin": self.ineligible_names, "$exists": True}}

        if self.query_debug:
            self.logger.debug("MDB  name:   %s" % utils.mdb.name)
            self.logger.debug("MDB query:   %s" % query)

        if asset_type == str:
            results = utils.mdb[collection].group(
                [attrib], query, {"count": 0}, "function(o, p){p.count++}"
            )

            sorted_list = sorted(results, key=lambda k: k["count"], reverse=True)
            for i in sorted_list:
                i["value"] = i[attrib]
                i["count"] = int(i["count"])

        elif asset_type == list:
            sample_set = self.get_eligible_documents(collection, attrib)
            if sample_set is None:
                return None
            master_list = []
            for s in sample_set:
                master_list.extend(s[attrib])
            master_dict = {}
            for i in master_list:
                if i in list(master_dict.keys()):
                    master_dict[i] += 1
                else:
                    master_dict[i] = 1
            return sorted(list(master_dict.items()), key=lambda x: x[1], reverse=True)

        else:
            raise Exception("%s is not a supported asset type for this query!" % asset_type)

        if self.query_debug:
            self.logger.debug("MDB results: %s" % sorted_list)

        if limit is not None:
            return sorted_list[:limit]
        else:
            return sorted_list


    #
    # actual refresh methods from here down (nothing after)
    #

    # application/meta
    def api_response_times(self):
        """ Fires off a fairly sophisticated aggregate() query to return a
        webapp-friendly representation of that data. """

        results = utils.mdb.api_response_times.aggregate([
            {"$group": {
                "_id": {
                    "url": "$url",
                    "method": "$method",
                },
                "avg_time": { "$avg": "$time"},
                "last_24_avg": {
                    "$avg": {"$gte":
                        ["$time", datetime.now() - timedelta(days=1)]},
                },
                "max_time": { "$max": "$time"},
                "min_time": { "$min": "$time"},
                "count": {"$sum": 1 },
                },
            },
            {"$sort": SON([("_id", 1)])},
        ])
        return [r for r in results]

    # survivors
    def total_survivors(self):
        """ Counts all survivors; returns an int."""
        return utils.mdb.survivors.find().count()

    def live_survivors(self):
        """ Counts *living* survivors; returns an int. """
        return utils.mdb.survivors.find({"dead": {"$exists": False}}).count()

    def dead_survivors(self):
        """ Counts *dead* survivors; returns an int. Includes living survivors
        from abandoned settlements (who are functionally dead). """

        natural_death_count = utils.mdb.survivors.find({"dead": {"$exists": True}}).count()

        # include *living* survivors from removed/abandoned settlements; treat
        # them as dead, for the purposes of this count.
        removed_count = 0
        pipeline = {"$or": [
            {"removed": {"$exists": True}},
            {"abandoned": {"$exists": True}},
        ]}
        for settlement in utils.mdb.settlements.find(pipeline):
            survivors = utils.mdb.survivors.find({"settlement": settlement["_id"]})
            for survivor in survivors:
                if survivor.get('dead', None) is None:
                    removed_count += 1

        return natural_death_count + removed_count

    # settlements
    def total_settlements(self):
        """ Counts settlements; returns an int."""
        return utils.mdb.settlements.find().count()

    def active_settlements(self):
        """ Counts settlements, subtracts abandoned ones; returns an int."""
        return self.total_settlements() - self.abandoned_settlements()

    def removed_settlements(self):
        """ Counts removed settlements that haven't been purged; returns
        an int. """
        return utils.mdb.settlements.find({"removed": {"$exists": True}}).count()

    def abandoned_settlements(self):
        """ Counts abandoned settlements that have NOT been removed. """
        return utils.mdb.settlements.find({
            "abandoned": {"$exists": True},
            "removed":  {"$exists": False}
        }).count()

    def abandoned_or_removed_settlements(self):
        return utils.mdb.settlements.find({"$or": [
            {"removed": {"$exists": True}},
            {"abandoned": {"$exists": True}},
        ]}).count()

    def new_settlements_last_30(self):
        """ Counts settlements created in the last 30 days; returns an int."""
        thirty_days_ago = datetime.now() - timedelta(days=30)
        return utils.mdb.settlements.find(
            {"created_on": {"$gte": thirty_days_ago}}
        ).count()

    # users
    def total_users(self):
        """ Counts all users; returns an int."""
        return utils.mdb.users.find().count()

    def total_users_last_30(self):
        thirty_days_ago = datetime.now() - timedelta(days=30)
        return utils.mdb.users.find(
            {"latest_activity": {"$gte": thirty_days_ago}}
        ).count()

    def new_users_last_30(self):
        thirty_days_ago = datetime.now() - timedelta(days=30)
        return utils.mdb.users.find(
            {'created_on': {'$gte': thirty_days_ago}}
        ).count()

    def total_subscribers(self):
        return utils.mdb.users.find({'subscriber.level': {'$gte': 1}}).count()


    def subscribers_by_level(self):
        """ Creates a list where each item is a dict describing the subscriber
        level and the number of users who are at that level. """

        possible_values = utils.mdb.users.find(
            {'subscriber.level': {'$gte': 1}}
        ).distinct('subscriber.level')

        if self.query_debug:
            self.logger.debug("Distinct levels: %s" % possible_values)

        output = []

        for v in sorted(possible_values):
            d = {"level": v}
            d['count'] = utils.mdb.users.find({'subscriber.level': v}).count()
            output.append(d)

        return output


    def recent_sessions(self):
        """ Counts the numbers of users whose 'latest_activity' datetime is
        within our recent user horizon (see settings.cfg). """

        recent_session_cutoff = datetime.now() - timedelta(
            hours=utils.settings.get("users", "recent_user_horizon")
        )
        return utils.mdb.users.find(
            {"latest_activity": {"$gte": recent_session_cutoff}}
        ).count()


    # min/max queries
    def max_pop(self):
        return self.get_minmax("settlements", "population")[1]

    def max_death_count(self):
        return self.get_minmax("settlements", "death_count")[1]

    def max_survival_limit(self):
        return self.get_minmax("settlements", "survival_limit")[1]

    # settlement averages
    def avg_ly(self):
        return self.get_average("settlements", "lantern_year")

    def avg_lost_settlements(self):
        return self.get_average("settlements", "lost_settlements")

    def avg_pop(self):
        return self.get_average("settlements", "population")

    def avg_death_count(self):
        return self.get_average("settlements", "death_count")

    def avg_survival_limit(self):
        return self.get_average("settlements", "survival_limit")

    def avg_milestones(self):
        return self.get_average("settlements", "milestone_story_events")

    def avg_storage(self):
        return self.get_average("settlements", "storage")

    def avg_defeated_monsters(self):
        return self.get_average("settlements", "defeated_monsters")

    def avg_expansions(self):
        return self.get_average("settlements", "expansions")

    def avg_innovations(self):
        return self.get_average("settlements", "innovations")

    def total_multiplayer_settlements(self):
        """ Iterates through all survivors, adding their settlement _id to a
        dict as its key; the value of that key is a list of
        survivor["created_by"] values. Any key whose list is longer than one
        is a multiplayer settlement. """

        all_settlements = {}
        all_survivors = utils.mdb.survivors.find()
        for s in all_survivors:
            if s["settlement"] not in list(all_settlements.keys()):
                all_settlements[s["settlement"]] = set([s["created_by"]])
            else:
                all_settlements[s["settlement"]].add(s["created_by"])

        multiplayer_count = 0
        for s in list(all_settlements.keys()):
            if len(all_settlements[s]) > 1:
                multiplayer_count += 1

        return multiplayer_count

    # survivor averages
    def avg_disorders(self):
        return self.get_average("survivors", "disorders")

    def avg_abilities(self):
        return self.get_average("survivors", "abilities_and_impairments")

    def avg_hunt_xp(self):
        return self.get_average("survivors", "hunt_xp")

    def avg_insanity(self):
        return self.get_average("survivors", "Insanity")

    def avg_courage(self):
        return self.get_average("survivors", "Courage")

    def avg_understanding(self):
        return self.get_average("survivors", "Understanding")

    def avg_fighting_arts(self):
        return self.get_average("survivors", "fighting_arts")


    # user averages
    # these happen in stages in order to work around the stable version of mdb
    # (which doesn't support $lookup aggregations yet).
    # FIX THIS AFTER 1.0.0 goes live!!!
    # Not super DRY, but it still beats using a relational DB.

    def avg_user_settlements(self):
        data_points = []
        for user in utils.mdb.users.find():
            data_points.append(
                utils.mdb.settlements.find({"created_by": user["_id"]}).count()
            )
        return self.get_list_average(data_points)


    def avg_user_survivors(self):
        data_points = []
        for user in utils.mdb.users.find():
            data_points.append(
                utils.mdb.survivors.find({"created_by": user["_id"]}).count()
            )
        return self.get_list_average(data_points)


    def avg_user_avatars(self):
        data_points = []
        for user in utils.mdb.users.find():
            data_points.append(
                utils.mdb.survivors.find(
                    {"created_by": user["_id"], "avatar": {"$exists": True}}
                ).count()
            )
        return self.get_list_average(data_points)


    # "latest" whatever queries start here
    def latest_kill(self):
        k = self.get_eligible_documents(
            collection="killboard",
            required_attribs=["handle"],
            limit=1
        )

        if k is not None:
            k["killed_date"] = k["created_on"].strftime(utils.ymd)
            k["killed_time"] = k["created_on"].strftime(utils.hms)
            return k


    def latest_survivor(self):
        """ Checks the 'survivors' collection for its latest entry. """
        s = self.get_eligible_documents(
            collection="survivors",
            limit=1,
            include_settlement=True
        )
        return self.pretty_survivor(s)


    def latest_fatality(self):
        s = self.get_eligible_documents(
            collection="survivors",
            required_attribs=["dead","cause_of_death"],
            limit=1,
            exclude_dead_survivors=False,
            include_settlement=True,
            sort_on="died_on",
        )
        return self.pretty_survivor(s)


    def latest_settlement(self):
        """ Get the latest settlement and punch it up with some additional info,
        since JSON consumers don't have MDB access and can't get it otherwise.
        """

        try:
            s = utils.mdb.settlements.find(
                {"name":
                    {"$nin": self.ineligible_names}
                }, sort=[("created_on",-1)]
            )[0]
        except IndexError:
            return None

        S = settlements_models.Settlement(_id=s["_id"])

        s["campaign"] = S.get_campaign("name")
        s["expansions"] = S.get_expansions("pretty")
        s["player_count"] = S.get_players("count")
        s["age"] = utils.get_time_elapsed_since(s["created_on"], 'age')

        for k in ['timeline',]:
            if k in list(s.keys()):
                s[k] = "REDACTED"

        return s


    #
    # compound returns below. Unlike the above functions, these return dict
    # and list type objects
    #

    def killboard(self):
        """ Create the killboard. Return a blank dict if there's nothing in the
        MDB to show, e.g. if it's a freshly initialized db. """

        # first, figure out what monster types are in the killboard collection
        known_types = list(utils.mdb.killboard.find().distinct("type"))
        if self.query_debug:
            self.logger.debug('Monster types in killboard: %s' % known_types)
        if known_types == []:
            return {}

        # log an error if we find the generic asset type in the known types:
        if 'monsters' in known_types:
            bad_type = utils.mdb.killboard.find({'type': 'monsters'})
            err = "%s killboard monsters with invalid type 'monsters' found!"
            self.logger.error(err % bad_type.count())

            # initialize the bogus entries, which will normalize/fix them
            for killed in bad_type:
                kbObject = killboard_model.Killboard(_id = killed['_id'])

            # finally, remove 'monsters' from known types:
            known_types.remove('monsters')

        # now, start creating the dictionary representation
        killboard = {}
        for t in known_types:
            killboard[t] = {}

        # iterate monster assert dicts and use them to create our base killboard
        monster_assets = monster_models.Assets()
        for m_asset in monster_assets.get_dicts():
            killboard[m_asset["sub_type"]][m_asset['handle']] = {
                "name": m_asset["name"],
                "count": 0,
                "sort_order": m_asset["sort_order"]
            }

        # now go and get the monsters, ignoring broken ones
        results = utils.mdb.killboard.find(
            {"handle": {"$exists": True}, "type": {"$exists": True}}
        )
        for d in results:
            killboard[d["type"]][d["handle"]]["count"] += 1

        for type in list(killboard.keys()):
            sort_order_dict = {}
            for m in list(killboard[type].keys()):
                m_dict = killboard[type][m]
                m_dict.update({"handle": m})
                sort_order_dict[int(m_dict["sort_order"])] = m_dict

            killboard[type] = []
            previous = -1
            for k in sorted(sort_order_dict.keys()):
                m_dict = sort_order_dict[k]
                if m_dict["sort_order"] <= previous:
                    self.logger.error("Sorting error! %s sort order (%s) is "\
                        "not greater than previous (%s)!" % (
                            m_dict["name"],
                            m_dict["sort_order"],
                            previous
                            )
                        )
                killboard[type].append(m_dict)
                previous = m_dict["sort_order"]

        return killboard

    def top_survivor_names(self):
        return self.get_top("survivors", "name")

    def top_settlement_names(self):
        return self.get_top("settlements", "name")

    def top_causes_of_death(self):
        return self.get_top("survivors", "cause_of_death", limit=10)

    def top_innovations(self):
        """ Does an innovations popularity contest, accounting for both names
        and handles (for legacy support). """

        I = innovations_models.Assets()
        I.filter("type", ["principle"])

        all_results = []
        for i_dict in I.get_dicts():
            aliases = [i_dict["name"], i_dict["handle"]]
            results = utils.mdb.settlements.find(
                {"innovations": {"$in": aliases}}
            )
            all_results.append({
                "name": i_dict["name"],
                "handle": i_dict["handle"],
                "count": results.count(),
            })

        return sorted(all_results, key=lambda x: x["count"], reverse=1)


    def principle_selection_rates(self):
        """ This is pretty much a direct port from V1. It's still a hot mess.
        This should probably get a refactor prior to launch.

        Release 1.0.0 update: this still hasn't been refactored since
        kdm-manager V1, which is insane. This really needs to be fixed.

        2020-11-04 update: added some debugging support, but have not yet
        refactored this in any meaningful way.
        """

        p_assets = principles_mod.Assets()
        mep_dict = p_assets.get_mutually_exclusive_principles()

        if self.query_debug:
            mep_meth = "models.principles.get_mutually_exclusive_principles()"
            self.logger.debug("%s output:" % mep_meth)
            self.logger.debug(mep_dict)

        popularity_contest = {}
        for principle in list(mep_dict.keys()):
            tup = mep_dict[principle]

            all_options = []
            for l in tup:
                all_options.extend(l)

            sample_set = utils.mdb.settlements.find(
                {"principles": {"$in": all_options} }
            ).count()

            popularity_contest[principle] = {
                "sample_size": sample_set,
                "options": []
            }

            for option_list in tup:
                total = utils.mdb.settlements.find(
                    {"principles": {"$in": option_list}}
                ).count()
                option_pretty_name = option_list[0]
                popularity_contest[principle]["options"].append(
                    option_pretty_name
                )
                popularity_contest[principle][option_pretty_name] = {
                    "total": total,
                    "percentage": int(utils.get_percentage(total, sample_set)),
                }

        return popularity_contest


    def settlement_popularity_contest_expansions(self):
        """ Uses the assets in assets/expansions.py to return a popularity
        contest dict re: expansions stored on settlement objects. """

        popularity_contest = {}
        reverse_lookup = {}

        expansions_assets = expansions_models.Assets()

        for e in expansions_assets.get_handles():
            e_dict = expansions_assets.get_asset(e)
            e_name_count = utils.mdb.settlements.find(
                {"expansions": {"$in": [e_dict["name"]]}}
            ).count()
            e_handle_count = utils.mdb.settlements.find(
                {"expansions": {"$in": [e]}}
            ).count()
            popularity_contest[e_dict["name"]] = e_name_count
            popularity_contest[e_dict["name"]] += e_handle_count
            reverse_lookup[e_dict['name']] = e_dict

        sorted_keys = sorted(
            popularity_contest,
            key=lambda x: popularity_contest[x],
            reverse=1
        )

        return [
            {
                'name': k,
                'count': popularity_contest[k],
                'sub_type': reverse_lookup[k]['sub_type']
            } for k in sorted_keys
        ]


    def settlement_popularity_contest_campaigns(self):
        """ Uses the assets in assets/campaigns.py to return a popularity
        contest dict re: campaigns. """


        popularity_contest = {
            "People of the Lantern": utils.mdb.settlements.find(
                {"campaign": {"$exists": False}}
            ).count(),
        }

        campaigns = utils.mdb.settlements.find(
            {"campaign": {"$exists": True}}
        ).distinct("campaign")

        C = campaigns_models.Assets()

        for c in campaigns:
            total = utils.mdb.settlements.find({"campaign": c}).count()

            if C.get_asset_from_name(c) is None:
                c = C.get_asset(c)["name"]

            if c in list(popularity_contest.keys()):
                popularity_contest[c] += total
            else:
                popularity_contest[c] = total

        return popularity_contest


    def current_hunt(self):
        """ Uses settlements with a 'current_quarry' attribute to determine who
        is currently hunting monsters.

        The mdb query is totally custom, so it's written out here, rather than
        stashed in a method of the World object, etc. """

        settlement = utils.mdb.settlements.find_one(
            {
                "removed": {"$exists": False},
                "abandoned": {"$exists": False},
                "name": {"$nin": self.ineligible_names},
                "current_quarry": {"$exists": True},
                "hunt_started": {
                    "$gte": datetime.now() - timedelta(minutes=180)
                },
            }, sort=[("hunt_started", -1)],
        )

        if settlement is None:
            return None

        hunters = utils.mdb.survivors.find({
            "settlement": settlement["_id"],
            "in_hunting_party": {"$exists": True},
        }).sort("name")

        if hunters.count() == 0:
            return None

        return {"settlement": settlement, "survivors": [h for h in hunters]}


    # meta/admin world stuff here

    def total_webapp_alerts(self):
        """ This is kind of dirty: this not only returns a count of alerts, but
        it also expires anything that's for a lower version of the manager, so
        it's not strictly just a query, which is sort of against the rules. """

        query = {'expired': False, 'type': 'webapp_alert'}

        # first, prune anything that needs a pruning
        alerts = utils.mdb.notifications.find(query)
        for a in alerts:
            if a['expiration'] == 'next_release':
                if a['release'] < API.config['VERSION']:
                    err_msg = 'Alert from v%s is lower than current! Removing!'
                    self.logger.warn(err_msg % a['release'])
                    A = notifications.Alert(_id=a['_id'])
                    A.expire()

        # now, check again
        return utils.mdb.notifications.find(query).count()


