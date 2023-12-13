'''

    The magic module / skeleton key to KD:M game assets.

    This file also defines a class method for initializing an object called
    'Monster', which is a representation of Kingdom Death: Monster that allows
    for programmatic access to collections.

'''

# second party imports
import flask

# KD:M API imports
from . import (
    abilities_and_impairments,
    campaigns,
    cursed_items,
    disorders,
    endeavors,
    events,
    expansions,
    fighting_arts,
    gear,
    innovations,
    locations,
    monsters,
    names,
    principles,
    resources,
    rules,
    saviors,
    settlements,
    strain_milestones,
    survival_actions,
    survivors,              # these are prefab/vignette survivors
    tags,
    the_constellations,
    versions,
)

# survivor sheet pseudo assets
from .survivors import causes_of_death
from .survivors import color_schemes
from .survivors import once_per_lifetime
from .survivors import special_attributes
from .survivors import status_flags
from .survivors import weapon_proficiency

# settlement sheet pseudo assets
from .settlements import macros
from .settlements import pulse_discoveries
from .settlements import storage
from .campaigns import milestone_story_events


#
#   Monster class method follows
#

class Monster():
    ''' Objects of this class represent Kingdom Death: Monster. '''

    _asset_modules = [
        gear,
        monsters,
#        names,
    ]
    _kdm_monster_object = True
    _collections_initialized = None

    def __init__(self, flask_app=None, logger=None):
        ''' These objects must be initialized with an instance of the KD:M API
        as an attribute. This is used to set various attributes, etc. '''

        # first, make sure a.) we have an instance of the Flask app and b.) that
        #   the instance doesn't already have a KD:Monster object
        #   Then, make sure we've got a valid logger

        if not isinstance(flask_app, flask.Flask):
            err = "KD:Monster object init requires an instance of the KD:M API!"
            raise ValueError(err)

        for attr, attr_value in vars(flask_app).items():
            err = "The KD:Monster object has already been initialized!"
            if isinstance(attr_value, object):
                if hasattr(attr_value, '_kdm_monster_object'):
                    raise RuntimeError(err)

        if logger is None:
            raise ValueError('KD:Monster object init requires a logger!')

        # start logging
        self.logger = logger
        self.logger.info('Initializing KD:Monster object!')
        msg = 'API version %s (instance uuid: %s)'
        self.logger.info(msg, flask_app.config['VERSION'], flask_app.uuid)

        # set game assets
        self.version = versions.Version(
            handle = flask_app.config['DEFAULT_GAME_VERSION']
        )
        self.collections = None
        self._register_collections()
        self._validate_assets()

        # finally, log a summary
        self.logger.info(
            'KD:Monster object initialized! Game version %s (%s collections)',
            self.version.get_float(),
            self._collections_initialized,
        )


    def _register_collections(self):
        ''' Run once at initialization to add collections to this object. '''

        if self._collections_initialized is not None:
            err = 'KD:Monster object collections are already initalized!'
            raise TypeError(err)

        class Collections:
            def __init__(self, modules=None, version_handle=None):
                for module in modules:
                    setattr(
                        self,
                        module.__name__.split('.')[-1],
                        module.Assets(assets_version=version_handle)
                    )

        self.collections = Collections(
            modules = self._asset_modules,
            version_handle = self.version.handle
        )

        self._collections_initialized = 0
        for collection in self.collections.__dict__:
            self.logger.info(
                'Initialized collection: %s',
                getattr(self.collections, collection)
            )
            self._collections_initialized += 1


    def _validate_assets(self):
        ''' Checks all asset handles in all collections. Raises an exception if
        it detects issues.

        This is the right place to do this, because handles might change with
        versions, and the need to validate handles is therefore part of
        validating a version of the game.

        (i.e. validating the asset definitions on the file system might not give
        you the right answer.)
        '''

        all_asset_handles = {}
        for collection in self.collections.__dict__:
            for handle in getattr(self.collections, collection).get_handles():
                if handle in all_asset_handles.keys():
                    err = (
                        "Asset collection '%s' includes handle '%s', which is "
                        "registered in KD:M version %s by the %s collection!"
                    ) % (
                        collection, handle,
                        self.version.get_float(),
                        all_asset_handles[handle]
                    )
                    raise AttributeError(err)
                all_asset_handles[handle] = collection
