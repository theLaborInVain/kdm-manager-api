"""

    This is a confusing module, because we import a class definition and
    expose it at models.survivors.Survivor() for the initialization of an
    end-user's individual survivor records.

    Over in assets, we also supply a class definition for a collection of
    refab survivors and expose that at assets.survivors.Assets().

"""

# second party imports
from bson import json_util

# module imports
from ._survivor import Survivor


def create_many_survivors(params):
    """
    This method can be called without initializing a settlement, so it goes
    really, really fast.

    Adds many survivors to a settlement. Returns a list of the new survivors
    as dicts (and ready to be schleped wherever).

    """

    settlement_id = ObjectId(params.get('settlement_id', None))

    male = params.get('male', 0)
    female = params.get('female', 0)
    father = params.get('father', None)
    mother = params.get('mother', None)
    public = params.get('public', True)

    for s_count in [male, female]:
        if s_count < 0:
            s_count = 0

    output = []
    for dummy in range(male):
        survivor_obj = Survivor(new_asset_attribs={
            'settlement': settlement_id,
            'sex': 'M',
            'father': father,
            'mother': mother,
            'public': public,
        })
        output.append(survivor_obj.synthesize())
    for dummy in range(female):
        survivor_obj = Survivor(new_asset_attribs={
            'settlement': settlement_id,
            'sex': 'F',
            'father': father,
            'mother': mother,
            'public': public,
        })
        output.append(survivor_obj.synthesize())

    return output
