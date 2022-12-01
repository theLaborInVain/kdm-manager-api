"""
    This module contains methods for returning admin panel JSON. Try not to
    stash anything else here: use the app/admin/__init__.py file for sysadmin
    type stuff.

"""

# standard library imports
from datetime import datetime, timedelta
import json

# second party imports
from bson import json_util

# local imports
from app import API, utils



def get_settlement_data():
    """ Returns JSON about recently updated settlements. Also serializes those
    settlements and gets their event_log. """

    recent_cutoff = datetime.now() - timedelta(
        hours=utils.settings.get("users", "recent_user_horizon")
    )

    ids = utils.mdb.settlements.find(
        {'last_accessed': {'$gte': recent_cutoff}}
    ).distinct('_id')

    sorting_hat = {}
    for s_id in ids:
        last_updated = utils.mdb.settlement_events.find(
            {'settlement_id': s_id}
        ).limit(1).sort("created_on", -1)[0]['created_on']
        sorting_hat[last_updated] = s_id

    sorted_ids = []
    for timestamp in sorted(sorting_hat.keys(), reverse=True):
        sorted_ids.append(sorting_hat[timestamp])

    # create the recent settlements array
    recent_settlements = []
    for settlement in utils.mdb.settlements.find(
        {
            "_id": {"$in": sorted_ids}
        }
    ):
        # add settlement creator email (for easy display)
        settlement['creator_email'] = utils.mdb.users.find_one(
            {'_id': settlement['created_by']}
        )['login']

        # add settlement age
        settlement['age'] = utils.get_time_elapsed_since(
            settlement['created_on'],
            'age'
        )

        # add a list of players
        settlement['players'] = utils.mdb.survivors.find(
            {"settlement": settlement['_id']}
        ).distinct('email')

        recent_settlements.append(settlement)

    return json.dumps(recent_settlements, default=json_util.default)



def get_user_data():
    """ Returns JSON about active and recently active users, as well as info
    about user agents, etc. """

    # first, do the user agent popularity contest, since that's simple
    results = utils.mdb.users.group(
        ['latest_user_agent'],
        {'latest_user_agent': {'$exists': True}},
        {"count": 0},
        "function(o, p){p.count++}"
    )
    sorted_list = sorted(results, key=lambda k: k["count"], reverse=True)
    for i in sorted_list:
        i["value"] = i['latest_user_agent']
        i["count"] = int(i["count"])
    ua_data = sorted_list[:25]


    # next, get active/recent users
    recent_user_cutoff = datetime.now() - timedelta(
        hours=utils.settings.get("users", "recent_user_horizon")
    )
    recent_users = utils.mdb.users.find(
        {"latest_activity": {"$gte": recent_user_cutoff}}
    ).sort("latest_activity", -1)

    active_user_count = 0
    recent_user_count = 0

    final_user_output = []
    for user in recent_users:
        user['age'] = utils.get_time_elapsed_since(user['created_on'], 'age')
        user['latest_activity_age'] = utils.get_time_elapsed_since(
            user['latest_activity'],
            'age'
        )

        if user["latest_activity"] > (datetime.now() - timedelta(
            minutes=API.config['ACTIVE_USER_HORIZON']
        )):
            active_user_count += 1
            user['is_active'] = True
        else:
            recent_user_count += 1
            user['is_active'] = False
        final_user_output.append(user)

    # create the final output dictionary
    output = {
        "meta": {
            "active_user_horizon": API.config['ACTIVE_USER_HORIZON'],
            "active_user_count": active_user_count,
            "recent_user_horizon": utils.settings.get(
                "users",
                "recent_user_horizon"
            ),
            "recent_user_count": recent_user_count,
        },
        "user_agent_stats": ua_data,
        "user_info": final_user_output,
    }

    # and return it as json
    return json.dumps(output, default=json_util.default)
