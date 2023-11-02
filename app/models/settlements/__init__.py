"""

    Settlement class objects are imported here.

"""

# second-party imports
from bson.objectid import ObjectId

# KDM API imports
from ._settlement import Settlement, Survivor
from ._storage import Storage


def create_many_survivors(params):
    """
    This method can be called without initializing a settlement, so it goes
    really, really fast.

    Adds many survivors to a settlement. Returns a list of the new survivors
    as dicts (and ready to be schleped wherever).

    """

    settlement_id = ObjectId(params.get('settlement_id', None))
    settlement_object = Settlement(_id=settlement_id)

    output = []

    for sex in ['male', 'female']:
        for survivor in range(params.get(sex, 0)):
            survivor_obj = Survivor(
                new_asset_attribs={
                    'settlement': settlement_id,
                    'sex': sex[0].upper(),
                    'father': params.get('father', None),
                    'mother': params.get('mother', None),
                    'public': params.get('public', True),
                    'random_name': params.get('random_name', False),
                    'apply_new_survivor_buffs': params.get(
                        'apply_new_survivor_buffs', False
                    ),
                },
                Settlement = settlement_object,
            )
            output.append(survivor_obj.synthesize())

    return output
