'''

    These settlement 'assets' are not the same as end-user setttlement assets.

    Instead, these settlement 'assets' are basically used to show available
    options for creating a new UserAsset

'''

from .._collection import Collection

from app.assets import campaigns, expansions
from app.assets.settlements import macros

class Assets(Collection):
    """ The "asset collection" that we expose at /game_asset/settlements is
    actually a pseudo collection made up of a number of different assets from
    various parts of the API.

    Read the doc string under the (very customized) __init__ method for more.

    Otherwise, initialize this odd-ball Assets() 'collection' to get a
    representation of available options for creating a new settlement. """


    def __init__(self, *args, **kwargs):
        """ We create the self.assets dictionary for this pseudo collection by
        loading the campaigns, expansions and survivors modules from /app/models
        and then initializing them.

        Next, we go through their individual self.assets dictionaries and,
        making some minor alterations, add them to our new self.assets.

        Next, we load the available macros as an attribute of our little asset.

        Finally (and this is really important, so listen to this), we DO NOT
        initialize the base class. This cuts us off from all of the methods and
        attributes that get added when you do that.

        YHBW
        """

        self.assets = {'campaigns': []}

        campaign_collection = campaigns.Assets()
        for c_dict in campaigns.Assets().get_dicts():
            asset_repr = {
                "handle": c_dict['handle'],
                "name": c_dict["name"]
            }
            for optional_key in ["subtitle", "default"]:
                if c_dict.get(optional_key, None) is not None:
                    asset_repr[optional_key] = c_dict[optional_key]
            self.assets['campaigns'].append(asset_repr)

        self.assets['expansions'] = expansions.Assets().assets
        self.assets["macros"] = macros.Assets().assets

