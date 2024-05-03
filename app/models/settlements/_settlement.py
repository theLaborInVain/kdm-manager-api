"""

    This is a massive module. Most of the API lives here (haha seriously tho).

    In addition to the class definition for the settlement assets collection,
    which is used to create an asset that represents options fopr creating new
    settlements, etc., the class definition for the Settlement object is also
    here.


"""

# standard library imports
import collections
from copy import copy, deepcopy
from datetime import datetime
import inspect
import json
import os
import urllib

# second-party imports
from bson import json_util
from bson.objectid import ObjectId
import flask

# KDM API imports
from app import API, utils

import app.assets.kingdom_death as KingdomDeath

from ..survivors import Survivor
from .._data_model import DataModel
from .._user_asset import UserAsset
from .._decorators import deprecated, web_method, paywall

from ._storage import Storage as StorageObject


class Settlement(UserAsset):
    """ This is the base class for all expansions. Private methods exist for
    enabling and disabling expansions (within a campaign/settlement). """

    DATA_MODEL = DataModel()

    # meta
    DATA_MODEL.add('meta', dict)
    DATA_MODEL.add(
        'version', str, default_value=API.config['DEFAULT_GAME_VERSION']
    )

    # user stuff
    DATA_MODEL.add('admins', list)
    DATA_MODEL.add('hunt_started', datetime, required=False)
    DATA_MODEL.add(
        'survivor_groups', list, default = API.config['SURVIVOR_GROUPS']
    )

    # sheet
    DATA_MODEL.add('campaign', str, immutable=True)
    DATA_MODEL.add('death_count', int, minimum=0)
    DATA_MODEL.add('defeated_monsters', list)
    DATA_MODEL.add('endeavor_tokens', int, minimum=0, default=0)
    DATA_MODEL.add('expansions', list)
    DATA_MODEL.add('innovations', list)
    DATA_MODEL.add('inspirational_statue', str, required=False)
    DATA_MODEL.add('lantern_year', int, minimum=0)
    DATA_MODEL.add('lantern_research_level', int, required=False)
    DATA_MODEL.add('locations', list)
    DATA_MODEL.add('lost_settlements', int, minimum=0)
    DATA_MODEL.add('milestone_story_events', list)
    DATA_MODEL.add('name', str, default_value='Unknown')
    DATA_MODEL.add('patterns', list)
    DATA_MODEL.add('population', int, minimum=0)
    DATA_MODEL.add('principles', list)
    DATA_MODEL.add('quarries', list)
    DATA_MODEL.add('nemesis_monsters', list)
    DATA_MODEL.add('survival_limit', int, minimum=1)
    DATA_MODEL.add('storage', list)
    DATA_MODEL.add('strain_milestones', list)
    DATA_MODEL.add('timeline', list)


    @utils.metered
    def __init__(self, *args, **kwargs):
        ''' The Settlement object is the main thing we do here. Init is minimal,
        since we fall back to the base class UserAsset for a lot of work.

        DO NOT load any survivors here or in load(). Doing either will create a
        circular import scenario where each asset requires the other to load.
        '''

        # now initialize a generic settlement objec
        self.collection="settlements"

        # finally, call the base class __init__() method and set self.settlement
        UserAsset.__init__(self, *args, **kwargs) # calls load() as well

        # hang a bunch of other asset collections on the settlement object
        self._initialize_asset_collections()
        self._initialize_settlement_storage()

        # set self.campaign to be a campaigns.Campaign() asset if it hasn't been
        #   set already, e.g. by new() which sets it, etc.
        self.campaign = None
        self._initialize_self_campaign()

        # initialize the survivors after we've got assets loaded
        self.survivors_initialized = False
        self._initialize_survivors()    # sets a list of objects

        # finally, normalize
        self.normalize()


    @utils.metered
    def _initialize_asset_collections(self):
        """ Called during __init__(); these are used by numerous methods. """

        if not hasattr(self, 'settlement'):
            err = "Settlement object must be loaded before assets can init!"
            raise AttributeError(err)

        # this sets self.Versions and should eventually be the way we do this
        self._require_asset_collection_attributes([
            'once_per_lifetime',
        ])

        # eventually deprecate these:

        self.AbilitiesAndImpairments = \
            KingdomDeath.abilities_and_impairments.Assets(self.get_version(str))
        self.CursedItems = KingdomDeath.cursed_items.Assets(
            self.get_version(str)
        )
        self.Disorders = KingdomDeath.disorders.Assets(self.get_version(str))
        self.Endeavors = KingdomDeath.endeavors.Assets(self.get_version(str))
        self.Events = KingdomDeath.events.Assets()
        self.Expansions = KingdomDeath.expansions.Assets()
        self.FightingArts = KingdomDeath.fighting_arts.Assets()
        self.Gear = KingdomDeath.gear.Assets(self.get_version(str))
        self.Innovations = KingdomDeath.innovations.Assets()
        self.Locations = KingdomDeath.locations.Assets(self.get_version(str))
        self.Milestones = KingdomDeath.milestone_story_events.Assets()
        self.Monsters = KingdomDeath.monsters.Assets()
        self.Names = KingdomDeath.names.Assets()
        self.Principles = KingdomDeath.principles.Assets()
        self.Resources = KingdomDeath.resources.Assets(self.get_version(str))
        self.Saviors = KingdomDeath.saviors.Assets()
        self.SurvivalActions = KingdomDeath.survival_actions.Assets()
        self.StrainMilestones = KingdomDeath.strain_milestones.Assets()
        self.Tags = KingdomDeath.tags.Assets()

        # settlement sheet assets
        self.Macros = KingdomDeath.macros.Assets()
        self.PulseDiscoveries = KingdomDeath.pulse_discoveries.Assets()
        self.Storage = KingdomDeath.storage.Assets(self.get_version(str))

        # survivor sheet assets
        self.CausesOfDeath = KingdomDeath.causes_of_death.Assets()
        self.SpecialAttributes = KingdomDeath.special_attributes.Assets()
        self.SurvivorColorSchemes = KingdomDeath.color_schemes.Assets()
        self.Survivors = KingdomDeath.survivors.Assets()
        self.SurvivorStatusFlags = KingdomDeath.status_flags.Assets()
        self.WeaponProficiency = KingdomDeath.weapon_proficiency.Assets()

        # add the constellations
        if 'dragon_king' in self.settlement['expansions']:
            self.TheConstellations = KingdomDeath.the_constellations.Assets()


    def _require_asset_collection_attributes(self, attribs=[]):
        ''' Loops through 'attribs', which is a list of strings corresponding to
        game asset types, and makes sure that it's an attribute of self. '''

        if not isinstance(attribs, list):
            raise TypeError("The 'attribs' kwarg must be a list!")

        # the self.get_version() method requires self.Versions
        if not hasattr(self, 'Versions'):
            self.Versions = KingdomDeath.versions.Assets()

        for asset_type_snake in attribs:
            asset_type_camel = utils.snake_to_camel_case(asset_type_snake)
            if not hasattr(self, asset_type_camel):
                setattr(
                    self,
                    asset_type_camel,
                    getattr(
                        KingdomDeath,
                        asset_type_snake
                    ).Assets(
                        self.get_version(str)
                    )
                )
#                msg = "%s Set required collection -> self.%s (KingdomDeath.%s)"
#                self.logger.debug(msg, self, asset_type_camel, asset_type_snake)


    def _initialize_settlement_storage(self):
        ''' Uses attributes to initialize a settlement storage object that is
        used to support storage methods of the Settlement object. '''

        self.settlement_storage = StorageObject(
            gear = self.Gear,
            expansions = self.Expansions,
            resources = self.Resources,
        )


    def _initialize_self_campaign(self, force=False):
        ''' Initializes self.campaign, which is an initialized campaign asset.

        It's kind of all-important, since so many other assets are going to
        reference it at various points of working with the Settlement.

        This method Has some idiot-proofing so we don't accidentally do this
        more than once. Set 'force' to True if you want to do it anyway.'''

        # re-init with 'force' kwarg
        if getattr(self, 'campaign', None) is not None and not force:
            msg = '%s already has self.campaign (%s). '
            msg += "Use 'force' kwarg to re-initialize."
            self.logger.warning(msg, self, self.campaign)
            return True

        # if we're doing it, do it:
        if getattr(self, 'campaign', None) is None or force:
            self.campaign = KingdomDeath.campaigns.Campaign(
                handle = self.settlement['campaign'],
                collection_obj=API.kdm.collections.campaigns
            )

        msg = "%s self.campaign (%s) initialized! ('force'=%s)"
        self.logger.debug(msg, self, self.campaign.asset['name'], force)


    @utils.metered
    def _initialize_survivors(self):
        ''' Formerly, this is what you got by calling the
        get_survivors('initialize') method. For purposes of clarity and
        efficiency, it is now its own method that can be run exactly once. '''

        if self.survivors_initialized:
            err = 'Settlement %s has already initialized survivors!'
            raise AttributeError(err)

        self.survivors = []
        query = {
            "settlement": self.settlement["_id"],
            "removed": {"$exists": False}
        }

        all_survivors = utils.mdb.survivors.find(query).sort('name')

        for survivor in all_survivors:
            survivor_object = Survivor(
                _id = survivor["_id"],
                Settlement = self,
                normalize_on_init = False
            )
            self.survivors.append(survivor_object)

        self.survivors_initialized = True



    #
    #   PUBLIC METHODS START BELOW
    #


    def new(self):
        """ Creates a new settlement. Expects a fully-loaded request, i.e. with
        an initialized User object, json() params, etc.

        Think of this method as an alternate form of models.UserAsset.load()
        where, instead of getting a document from MDB and setting attribs from
        that, we have to create the document (and touch it up) to complete
        the load() request.

        The basic order-of-operations logic here is that we do a bunch of stuff
        to create what ammounts to the settlement 'sheet' and then save it to
        the MDB.

        IMPORTANT: this method initializes asset collections!

        Once it's saved, we call the base class load() method to initialize the
        object.

        Finally, once its initialized, we can use normal methods to apply what-
        ever other changes we need to apply (based on user params, etc.).

        """

        # before we do it, call the User object's validator method, which will
        #   bomb this out if they're at their limit.
        flask.request.User.can_create_settlement(raise_on_false=True)

        self.logger.info('%s is creating a new settlement!', flask.request.User)

        settlement = {
            # meta / admin
            "created_on": datetime.now(),
            "created_by": flask.request.User._id,
            "admins": [flask.request.User.login],
            "meta": {
                "timeline_version":     1.2,
                "campaign_version":     1.0,
                "monsters_version":     1.0,
                "expansions_version":   1.0,
                "innovations_version":  1.0,
                "locations_version":    1.0,
                "milestones_version":   1.0,
                "principles_version":   1.0,
                'storage_version':      1.0,
            },

            # sheet
            "name": flask.request.json.get("name", None),
            "campaign": flask.request.json.get(
                "campaign", "people_of_the_lantern"
            ),
            "lantern_year":             0,
            "population":               0,
            "death_count":              0,
            "survival_limit":           1,
            "lost_settlements":         0,
            "expansions":               [],
            "milestone_story_events":   [],
            "innovations":              [],
            "locations":                [],
            "defeated_monsters":        [],
            'patterns':                 [],
            "principles":               [],
            "storage":                  [],
            "strain_milestones":        [],
            "version":                  API.config['DEFAULT_GAME_VERSION'],
        }



        #   insert and load(); use self.settlement from here
        self._id = utils.mdb.settlements.insert(settlement)
        self.load() # uses self._id

        #   set required asset collections AFTER load()
        self._require_asset_collection_attributes(['names'])

        # set the settlement name before we save to MDB
        s_name = settlement['name']
        if s_name is None:
            s_name = "Unknown"
            if flask.request.json.get('random_name', False):
                s_name = self.Names.get_random_settlement_name()
        self.settlement['name'] = None
        self.set_name(s_name)

        # from here, we'll need self.campaign, so initialize it!
        self._initialize_self_campaign()

        # initialize methods
        self.initialize_sheet()
        self.initialize_timeline(save=False)

        # check params for additional expansions
        req_expansions = flask.request.json.get("expansions", [])
        for e in req_expansions:
            if e not in self.settlement["expansions"]:
                self.settlement["expansions"].append(e)

        # add all expansions
        all_expansions = self.settlement["expansions"]
        self.settlement["expansions"] = []
        if all_expansions != []:
            self.add_expansions(all_expansions)

        # handle macros, i.e. first story, seven swordsmen, etc.
        if self.params.get('macros', None) is not None:
            for macro_handle in self.params['macros']:
                self.apply_macro(macro_handle)

        # prefab survivors go here
        if self.params.get("survivors", None) is not None:
            warn = (
                'DEPRECATION WARNING: survivors cannot be added during new '
                'settlement creation!'
            )
            self.logger.warning(warn)


        # log settlement creation and save/exit
        self.save()


    @web_method
    def apply_macro(self, handle=None):
        """ Starting in January 2021, settlement macros can be applied
        arbitrarily and at will. """

        # require collections
        self._require_asset_collection_attributes([
            'abilities_and_impairments',
            'macros',
            'monsters',
            'once_per_lifetime',
            'special_attributes',
            'tags',
        ])

        # sanity check / initialize vars
        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params["handle"]

        macro = self.Macros.get_asset(handle=handle)

        self.log_event(
            action="apply",
            key="settlement",
            value=macro["name"],
            event_type='sysadmin'
        )

        # new October 2023: check expansions
        self.add_expansions(macro.get('expansions', []))

        # do random survivors
        if macro.get("random_survivors", None) is not None:
            for survivor_template in macro["random_survivors"]:
                new_survivor_attribs = copy(survivor_template)
                new_survivor_attribs.update({
                    "settlement": self._id,
                    'random_name': flask.request.json.get('random_name', False),
                })
                Survivor(
                    new_asset_attribs = new_survivor_attribs,
                    Settlement = self
                )

        # then storage
        if macro.get("storage", None) is not None:
            for d in macro["storage"]:
                for i in range(d["quantity"]):
                    self.settlement["storage"].append(d["name"])

        # current quarry
        if macro.get("current_quarry", None) is not None:
            self.set_current_quarry(macro["current_quarry"])
        if macro.get('showdown_type', None) is not None:
            self.set_showdown_type(macro['showdown_type'])

        # monsters
        for m_handle in macro.get('monsters', []):
            self.add_monster(m_handle)

        # events
        if macro.get("timeline_events", None) is not None:
            for event in macro["timeline_events"]:
                self.add_timeline_event(event)

        # update survivors
        if macro.get('living_survivors', None) is not None:
            for operation, attrib_dict in macro['living_survivors'].items():
                self.update_all_survivors(
                    operation = operation,
                    attrib_dict = attrib_dict,
                    exclude_dead = True,
                )



    def normalize(self):
        """ Makes sure that self.settlement is up to our current standards. """

        self.perform_save = False

        self.bug_fixes()
        self.baseline()

        if self.settlement.get("settlement_notes", None) is not None:
            raise utils.ConversionException()


        #
        #       timeline migrations
        #
        if self.settlement["meta"].get("timeline_version", None) is None:
            raise utils.ConversionException()

        if self.settlement["meta"]["timeline_version"] == 1.0:
            self.convert_timeline_quarry_events()
            self.perform_save = True

        if self.settlement["meta"]["timeline_version"] == 1.1:
            self.flatten_timeline_events()
            self.perform_save = True

        #
        #   November 2023: legacy conversions are no longer supported
        #
        for version_attrib in [
            'campaign', 'expansions', 'innovations', 'locations',
            'milestones', 'monsters', 'principles', 'storage'
        ]:
            handle = version_attrib + '_version'
            if self.settlement["meta"].get(handle, None) is None:
                raise utils.ConversionException()


        # enforce minimums
        self.enforce_minimums()

        # finally, apply the data model
        corrected_record = self.DATA_MODEL.apply(self.settlement)
        if corrected_record != self.settlement:
            self.logger.warning('[%s] data model corrections applied!', self)
#            self.settlement = corrected_record
            self.logger.info(self.settlement.keys())
            self.logger.warn(corrected_record.keys())
            meow
            self.perform_save = True

        # finish
        if self.perform_save:
            msg = "%s settlement modified during normalization!"
            self.logger.info(msg % self)
            self.save()


    @web_method
    def abandon(self, value=None):
        """ Abandons the settlement by setting self.settlement['abandoned'] to
        datetime.now(). Logs it. Expects a request context.
        """

        # optional check for params
        if value is None:
            value = self.params.get("value", None)

        if value == 'UNSET' and self.settlement.get('abandoned', False):
            del self.settlement['abandoned']
            self.log_event(
                '%s is no longer abandoned.' % self.settlement['name'],
                event_type='abandon_settlement'
            )
        else:
            self.settlement['abandoned'] = datetime.now()
            self.log_event(action='abandon', event_type='abandon_settlement')

        self.save()


    @web_method
    def remove(self):
        """ Marks the settlement as removed. """
        self.settlement['removed'] = datetime.now()

        # formulate a log message based on whether it's a user or CLI admin
        msg = '%s marked the settlement as removed!'
        if flask.has_request_context():
            msg = msg % flask.request.User.user['login']
        else:
            msg = msg % "CLI admin '%s'" % os.environ['USER']

        # log and save
        self.log_event(msg)
        self.save()


    def unremove(self, unremove_survivors=True):
        """ Deletes the 'removed' attribute from the settlement and, if the
        'unremove_survivors' kwarg is True, all surviors as well.

        Not sure whether this should be exposed via API yet, so for now, it's
        only available via admin.py.
        """

        if not self.settlement.get('removed', False):
            err = '%s Ignoring bogus request to unremove settlement...'
            self.logger.warning(err % self)
            return False

        del self.settlement['removed']
        self.log_event(action="unset", value="removed", event_type="sysadmin")
        if unremove_survivors:
            self.logger.debug("Unremoving survivors...")
            for s in utils.mdb.survivors.find(
                {'settlement': self.settlement['_id']}
            ):
                if s.get('removed',False):
                    S = Survivor(_id=s['_id'])
                    S.unremove()
        self.save()


    def _serialize_preflight(self):
        ''' Since serializing a settlement is ...basically the main thing the
        API does, this method does sanity checks before we let it rip. '''

        # 1. check for an initialized self.campaign
        if (
            not hasattr(self, 'campaign') or not
            isinstance(self.campaign, object) or not
            hasattr(self.campaign, 'asset')
        ):
            err = (
                "Settlement.serialize() requires a fully-initialized campaign "
                "asset to be assigned to self.campaign!"
                "self.campaign was this instead: %s"
            )
            raise TypeError(err % dir(getattr(self, 'campaign', None)))

    @utils.metered
    def serialize(self, return_type=None):
        """ Renders the settlement, including all methods and supplements, as
        a monster JSON object. This is where all views come from."""


        self._serialize_preflight()

        output = self.get_serialize_meta()

        # do some tidiness operations first
        for k in ["locations", "innovations"]:
            self.settlement[k] = sorted(self.settlement[k])

        # now start
        output["meta"].update({
            'creator_email': utils.mdb.users.find_one(
                {'_id': self.settlement["created_by"]}
            )['login'],
            'age': utils.get_time_elapsed_since(
                self.settlement["created_on"], units='age'
            ),
            'player_email_list': self.get_players('email'),
        })

        # retrieve user assets
        if return_type in [None, "sheet", 'campaign', 'survivors']:
            output.update({"user_assets": {}})
            output["user_assets"].update({"players": self.get_players()})
            output["user_assets"].update({"survivors": self.get_survivors()})
            output['user_assets'].update(
                {'survivor_oids_list': self.get_survivors('oid_strings')}
            )


        # create the sheet
        if return_type in [None, 'sheet', 'dashboard', 'campaign']:
            output.update({"sheet": self.settlement})
            output["sheet"].update({"campaign": self.campaign.handle})
            output["sheet"].update({"campaign_pretty": self.campaign.name})
            output["sheet"].update({"expansions": self.get_expansions()})
            output["sheet"].update({"expansions_pretty": self.get_expansions(str)})
            output["sheet"]["settlement_notes"] = self.get_settlement_notes()
            output["sheet"]["enforce_survival_limit"] = self.get_survival_limit(bool)
            output["sheet"]["minimum_survival_limit"] = self.get_survival_limit("min")
            output["sheet"]["minimum_death_count"] = self.get_death_count("min")
            output["sheet"]["minimum_population"] = self.get_population("min")
            output['sheet']['population_by_sex'] = self.get_population('sex')
            output['sheet']['monster_volumes'] = self.get_monster_volumes()
            output['sheet']['lantern_research_level'] = self.get_lantern_research_level()

            # add AKDM survivor sheet requirements
            output['sheet']['_additional_survivor_sheet_requirements'] =\
            self._get_additional_survivor_sheet_requirements()

            # log response time if we're doing that
            if flask.request.log_response_time:
                stop = datetime.now()
                duration = stop - flask.request.start_time
                self.logger.debug('serialize(%s) [%s] %s' % (return_type, duration, self))

        # create game_assets
        if return_type in [None, 'game_assets', 'campaign']:
            output.update({"game_assets": {}})
            for asset_package in [
                self.AbilitiesAndImpairments,
                self.CursedItems,
                self.Disorders,
                self.Endeavors,
                self.Events,
                self.FightingArts,
                self.Gear,
                self.Innovations,
                self.Monsters,
                self.OncePerLifetime,
                self.Resources,
                self.StrainMilestones,
                self.SurvivalActions,
                self.Tags,
                self.Versions
            ]:
                output['game_assets'].update(
                    self.get_available_assets(asset_package)
                )
            output["game_assets"].update(
                self.get_available_assets(
                    self.Locations,
                    only_include_selectable=True
                )
            )
            output["game_assets"].update(
                self.get_available_assets(self.CausesOfDeath, handles=False)
            )

            output["game_assets"]['weapon_proficiency_types'] = \
            self.get_available_assets(
                self.WeaponProficiency
            )['weapon_proficiency']

            # options (i.e. decks)
            output["game_assets"]["pulse_discoveries"] = self.PulseDiscoveries.get_dicts(sort_on_handles=True)
            output["game_assets"]["innovations_options"] = self.get_innovations_options()
            output['game_assets']['locations_options'] = self.get_locations_options()
            output['game_assets']['patterns_options'] = self.get_patterns_options()
            output["game_assets"]["principles_options"] = self.get_principles_options()
            output["game_assets"]["milestones_options"] = self.get_milestones_options()
            output["game_assets"]["milestones_dictionary"] = self.get_milestones_options(dict)

            # monster game assets
            output["game_assets"]["nemesis_options"] = self.get_monster_options("nemesis_monsters")
            output["game_assets"]["quarry_options"] = self.get_monster_options("quarries")
            for c in [
                "showdown_options",
                "special_showdown_options",
                "nemesis_encounters",
                "defeated_monsters"
            ]:
                output["game_assets"][c] = self.get_timeline_monster_event_options(c)

            # meta/other game assets
            output["game_assets"]["campaign"] = self.campaign.asset
            output["game_assets"]["expansions"] = self.get_expansions(dict)

            # misc helpers for front-end
            output['game_assets']['survivor_special_attributes'] = self.get_survivor_special_attributes()
            output["game_assets"]["survival_actions"] = self.get_survival_actions("JSON")
            output['game_assets']['inspirational_statue_options'] = self.get_available_fighting_arts(
                    exclude_dead_survivors=False, return_type='JSON'
            )
            output['game_assets']['monster_volumes_options'] = self.get_available_monster_volumes()

            if flask.request.log_response_time:
                stop = datetime.now()
                duration = stop - flask.request.start_time
                self.logger.debug("serialize(%s) [%s] %s" % (return_type, duration, self))

        # additional top-level elements for more API "flatness"
        if return_type in ['storage']:
            output['settlement_storage'] = self.get_settlement_storage()

        if return_type in [None, 'campaign']:
            output['survivor_color_schemes'] = self.SurvivorColorSchemes.get_sorted_assets()
            output["survivor_bonuses"] = self.get_bonuses("JSON")
            output["survivor_attribute_milestones"] = self.campaign.asset['survivor_attribute_milestones']
            output["eligible_parents"] = self.get_eligible_parents()
            output['survivor_status_flags'] = self.SurvivorStatusFlags.assets


        # campaign summary specific
        if return_type in ['campaign']:
            output.update({'campaign':{}})
            output['campaign'].update({'last_five_log_lines': self.get_event_log(lines=5)})
            output['campaign'].update({'most_recent_milestone': self.get_latest_milestone()})
            output['campaign'].update({'most_recent_hunt': self.get_latest_defeated_monster()})
            output['campaign'].update({'latest_death': self.get_latest_survivor('dead')})
            output['campaign'].update({'latest_birth': self.get_latest_survivor('born')})
            output['campaign'].update({'special_rules': self.get_special_rules()})
            output["user_assets"].update({'survivor_groups': self.get_survivors('groups')})

            # endeavors
            available_endeavors, available_endeavor_count = self.get_available_endeavors()
            output['campaign'].update({'endeavors': available_endeavors})
            output['campaign'].update({'endeavor_count': available_endeavor_count})

            if flask.request.log_response_time:
                stop = datetime.now()
                duration = stop - flask.request.start_time
                self.logger.debug("serialize(%s) [%s] %s" % (return_type, duration, self))

        # finally, try to dump it to JSON. If we get a TypeError, dump it to logs
        try:
            return json.dumps(output, default=json_util.default)
        except TypeError as err:
            self.logger.error(err)
            self.logger.error('The following could not be converted to JSON:')
            self.logger.error(output)
            raise AttributeError('JSON serialization failed!') from err


    #
    #   methods to get options (e.g. for building drop-downs, etc.)
    #

    def get_innovations_options(self, exclude_principles=True):
        """ Returns the settlement's available options for adding a new
        Innovation. """

        compatible = self.get_compatible_assets(self.Innovations)

        # list comp to exclude principles
        if exclude_principles: [
            compatible.remove(innovation) for
            innovation in compatible if
            innovation.get('sub_type', None) == 'principle'
        ]

        options = []
        for innovation in compatible:
            if innovation['handle'] not in self.settlement['innovations']:
                options.append(innovation)

        return options


    def get_locations_options(self):
        """ Similar to the other get_whatever_options() methods, this one
        returns a list of options for adding new locations to the settlement.
        Does not have 'return_type' options. Always returns a list of handles.
        """

        compatible = self.get_compatible_assets(self.Locations)

        options = []
        for location in compatible:
            if (
                location['handle'] not in self.settlement['locations'] and
                location.get('selectable', False)
            ):
                options.append(location)

        return options


    def get_milestones_options(self, return_type=list):
        """ Returns a list of dictionaries where each dict is a milestone def-
        inition. Useful for front-end stuff. """

        # die if we don't have a campaign asset
        if self.campaign.asset.get('milestones', []) == []:
            err = "self.campaign asset has no milestones! %s"
            raise AttributeError(err % self.campaign.asset)

        # handle returns
        if return_type==dict:
            output = {}
            for m_handle in self.campaign.asset['milestones']:
                output[m_handle] = self.Milestones.get_asset(m_handle)
            return output

        if return_type==list:
            output = []
            for m_handle in self.campaign.asset['milestones']:
                output.append(self.Milestones.get_asset(m_handle))
            return output

        err = "get_milestones_options() does not support return_type=%s"
        raise utils.InvalidUsage(err % return_type)


    def get_patterns_options(self):
        """ Similar to the other get_whatever_options() methods, this one
        returns a list of options for adding new patterns to the settlement.
        Does not have 'return_type' options. Always returns a list of handles.
        """

        compatible = self.get_compatible_assets(self.Gear)

        options = []
        for gear in compatible:
            if (
                gear['handle'] not in self.settlement.get('patterns', []) and
                gear.get('sub_type', None) == 'pattern'
            ):
                options.append(gear)

        return options


    def get_monster_options(self, monster_type):
        """ Returns a list of available nemesis or quarry monster handles for
        use with the Settlement Sheet controls.

        The 'monster_type' kwarg should be something such as 'nemesis_monsters'
        that will be present in our campaign and expansion definitions.
        """

        options = []

        # first check our campaign and expansion assets, and get all options
        if monster_type in self.campaign.asset:
            c_monsters = self.campaign.asset[monster_type]
            options.extend(c_monsters)

        for exp in self.get_expansions(dict):
            e_dict = self.get_expansions(dict)[exp]
            if monster_type in e_dict.keys():
                options.extend(e_dict[monster_type])

        # now convert our list into a set (just in case) and then go on to
        # remove anything we've already got present in the settlement
        option_set = set(options)
        for n in self.settlement.get(monster_type, []):
            if n in option_set:
                option_set.remove(n)

        # check the remaining to see if they're selectable:
        option_set = list(option_set)
        final_set = []
        for m_handle in option_set:
            monster_object = KingdomDeath.monsters.Monster(
                handle = m_handle,
                collection_obj = self.Monsters
            )
            if monster_object.is_selectable():
                final_set.append(m_handle)

        # remove any monsters that the campaign forbids
        forbidden_assets = self.campaign.asset.get('forbidden', {})
        forbidden_monsters = copy(forbidden_assets.get(monster_type, []))
        for m_handle in set(forbidden_monsters):
            if m_handle in final_set:
                final_set.remove(m_handle)

        # now turn our set
        output = []
        for m_handle in sorted(list(final_set)):
            monster_object = KingdomDeath.monsters.Monster(
                handle = m_handle,
                collection_obj = self.Monsters
            )
            output.append({
                "handle": monster_object.handle,
                "name": monster_object.name,
            })

        return output


    def get_principles_options(self):
        """ Returns a dict (JSON) meant to be interated over in an ng-repeat on
        the Settlement Sheet. """

        p_handles = self.campaign.asset['principles']
        all_principles = {}
        for p_handle in p_handles:
            p_dict = self.Principles.get_asset(p_handle)
            all_principles[p_dict["name"]] = p_dict

        sorting_hat = {}
        for p in all_principles.keys():
            sorting_hat[all_principles[p]["sort_order"]] = all_principles[p]

        output = []
        for n in sorted(sorting_hat.keys()):

            p_dict = sorting_hat[n]
            p_dict["options"] = {}

            for o in p_dict["option_handles"]:
                o_dict = self.Innovations.get_asset(o)

                selected=False
                if o_dict["handle"] in self.settlement["principles"]:
                    selected=True

                o_dict.update({
                    "input_id": "%s_%s_selector" % (p_dict["handle"], o),
                    "checked": selected
                })
                p_dict["options"][o] = o_dict

            p_dict["form_handle"] = "set_principle_%s" % p_dict["name"]
            output.append(p_dict)

        return output


    def get_timeline_monster_event_options(self, context=None):
        """ Returns a sorted list of strings (they call it an 'array' in JS,
        because they fancy) representing the settlement's possible showdowns,
        given their quarries, nemeses, etc.

        The idea here is that you specify a 'context' that has to do with user
        needs, e.g. 'showdown_options', to get back an appropriate list.
        """

        # use context to get a list of candidate handles

        candidate_handles = []
        if context == "showdown_options":
            candidate_handles.extend(self.settlement.get("quarries", []))
        elif context == "nemesis_encounters":
            candidate_handles.extend(
                self.settlement.get("nemesis_monsters", [])
            )
#            candidate_handles.append(self.campaign.asset['finale_monster'])
        elif context == "defeated_monsters":
            candidate_handles.extend(self.settlement.get("quarries", []))
            candidate_handles.extend(self.settlement.get("nemesis_monsters",[]))
            candidate_handles.extend(self._get_special_showdowns())
            candidate_handles.extend(self._get_endgame_showdowns())
        elif context == "special_showdown_options":
            candidate_handles.extend(self._get_special_showdowns())
        else:
            self.logger.warn(
                "Unknown 'context' for get_monster_options() method!"
            )

        # now create the output list based on our candidates
        output = []

        # uniquify candidate handles just in case
        candidate_handles = list(set(candidate_handles))

        for m_handle in candidate_handles:
            monster_object = KingdomDeath.monsters.Monster(
                handle = m_handle,
                collection_obj=self.Monsters
            )

            # hack the prologue White Lion / Crimson Croc in
            if monster_object.handle == "white_lion":
                output.append("White Lion (First Story)")
            if monster_object.handle == 'crimson_crocodile':
                output.append('Prologue Crimson Crocodile')

            if monster_object.is_unique():
                output.append(monster_object.name)
            else:
                blank_string = '%s lvl %s'
                if isinstance(monster_object.asset['levels'], int):
                    for l in range(monster_object.asset['levels']):
                        lvl = l+1
                        output.append(blank_string % (monster_object.name, lvl))
                elif isinstance(monster_object.asset['levels'], list):
                    for lvl in monster_object.asset['levels']:
                        output.append(blank_string % (monster_object.name, lvl))
                else:
                    err_msg = 'Monster levels must be integer or list types!'
                    raise utils.InvalidUsage(err_msg)

        output = sorted(output)

        return output



    #
    #   asset compatibility and gathering methods follow
    #

    def get_compatible_assets(self, asset_collection_obj):
        """ Returns a list of compatible assets from 'asset_collection_obj',
        which is an initialized asset collection object. """

        compatible_assets = []
        all_assets = copy(asset_collection_obj.assets)

        for handle in all_assets:
            if self.is_compatible(all_assets[handle]):
                compatible_assets.append(all_assets[handle])

        return compatible_assets


    def is_compatible(self, asset_dict={}):
        """Evaluates an asset's dictionary to determine it is compatible for
        use with this settlement. Always returns a bool (no matter what). """

        if type(asset_dict) != dict:
            asset_dict = asset_dict.__dict__

        # check minimum version
        if asset_dict.get('min_version', None) is not None:
            settlement_v = self.get_version()
            asset_v = self.Versions.get_asset(asset_dict['min_version'])
            if settlement_v['value'] < asset_v['value']:
                return False

        # check to see if the asset excludes certian campaign types
        if "excluded_campaigns" in asset_dict.keys():
            if self.campaign.handle in asset_dict["excluded_campaigns"]:
                return False


        # check to see if the asset belongs to an expansion
        if "expansion" in asset_dict.keys():

            #
            # special handling for KD Collection pseudo expansions
            #

            # farts/disorders pseudo
            if (
                asset_dict['type'] in ['fighting_arts','disorders'] and
                asset_dict['sub_type'] != 'secret_fighting_art'
            ):
                if 'kd_collection_fighting_arts_and_disorders' in self.settlement['expansions']:
                    if asset_dict['expansion'] in flask.request.User.user['collection']['expansions']:
                        return True

            # se pseudo
            if asset_dict.get('sub_type', None) == 'settlement_event':
                if 'kd_collection_settlement_events' in self.settlement['expansions']:
                    if asset_dict['expansion'] in flask.request.User.user['collection']['expansions']:
                        return True

            # normal test
            if asset_dict["expansion"] not in self.get_expansions():
                return False

        # check to see if the campaign forbids the asset
        for f_key in self.campaign.asset.get('forbidden', []):
            if asset_dict.get("type", None) == f_key:
                forbidden_assets = self.campaign.asset["forbidden"][f_key]
                if asset_dict["handle"] in forbidden_assets:
                    warn = "'%s' asset is forbidden by '%s' campaign."
                    self.logger.debug(
                        warn, asset_dict['handle'], self.campaign.name
                    )
                    return False

        return True



    #
    #   Initialization methods. Be careful with these because every single one
    #   of them does massive overwrites and doesn't ask for permission, if you
    #   know what I mean.
    #
    #   This needs to be refactored since these are first time / run once kind
    #   of methods: even though they're named 'init', they're more like  'new'
    #

    def initialize_sheet(self):
        """ Initializes the settlement sheet according to the campaign
        definition's 'settlement_sheet_init' attribute. Meant to be used when
        creating new settlements. """

        for init_key in self.campaign.asset['settlement_sheet_init'].keys():
            self.settlement[init_key] = copy(
                self.campaign.asset['settlement_sheet_init'][init_key]
            )
        msg = "%s initialized settlement sheet for '%s'"
        self.logger.info(msg, flask.request.User, self)


    def initialize_timeline(self, save=True):
        """ Meant to be called during settlement creation, this method
        completely overwrites the settlement's timeline with the timeline
        'template' from the settlement's campaign.

        DO NOT call this method on an active/live settlement, unless you really
        know what you're doing.

        """

        self.settlement['timeline'] = copy(self.campaign.asset['timeline'])
        if flask.request:
            warn = "%s initialized timeline for %s!"
            self.logger.warn(warn, flask.request.User, self)
        else:
            self.logger.warn("%s Timeline initialized from CLI!" % self)

        if save:
            self.save()


    #
    #   add/rm methods start here!
    #

    @web_method
    def add_defeated_monster(self, monster_string=None):
        """ Adds a monster to the settlement's defeated monsters. Updates the
        killboard. """

        if monster_string is None:
            self.check_request_params(['monster'])
            monster_string = self.params["monster"]

        monst_obj = self.Monsters.init_asset_from_name(monster_string)

        # do the killboard update
        killboard_dict = {
            'settlement_id': self.settlement['_id'],
            'settlement_name': self.settlement['name'],
            'kill_ly': self.get_current_ly(),
            'created_by': flask.request.User._id,
            'created_on': datetime.now(),
            'handle': monst_obj.handle,
            'name': monst_obj.name,
            'type': monst_obj.asset.get('type', None),
            'raw_name': monster_string,
        }
        for a in ['comment', 'level']:
            if hasattr(monst_obj, a):
                killboard_dict[a] = getattr(monst_obj, a)

        utils.mdb.killboard.insert(killboard_dict)
        msg = (
            "%s Updated the application killboard to include "
            "'%s' (%s) in LY %s"
        )
        self.logger.info(
            msg % (
                flask.request.User,
                monster_string,
                monst_obj.asset.get('type', None),
                self.get_current_ly()
            )
        )

        # add it and save
        self.settlement["defeated_monsters"].append(monster_string)
        self.log_event(
            action="add",
            key="Defeated Monsters list",
            value=monster_string,
            event_type="add_defeated_monster"
        )
        self.save()


    @web_method
    def rm_defeated_monster(self, monster_string=None):
        """ Removes a monster string from the settlement's list, i.e. the
        self.settlement["defeated_monsters"] list of strings, if that monster
        string is present. """

        if monster_string is None:
            self.check_request_params(['monster'])
            monster_string = self.params['monster']

        if monster_string not in self.settlement["defeated_monsters"]:
            msg = (
                "The string '%s' was not found in the settlement's list of "
                "defeated monsters!"
            )
            self.logger.error(msg % monster_string)
            raise utils.InvalidUsage(msg)

        self.settlement["defeated_monsters"].remove(monster_string)
        self.log_event(
            action="rm",
            key="Defeated Monsters list",
            value=monster_string,
            event_type="rm_defeated_monster"
        )
        self.save()


    @web_method
    def add_lantern_years(self, years=None):
        """ Adds 'years' lantern years to the timeline. Works with a request
        context. """

        if years is None:
            self.check_request_params(['years'])
            years = self.params['years']
        years = int(years)

        last_year_in_tl = self.settlement['timeline'][-1]['year']
        if last_year_in_tl >= 50:
            self.logger.error("%s Attempt to add more than 50 LYs to Timeline." % (flask.request.User))
            raise utils.InvalidUsage("Max Lantern Years is 50!")

        for y in range(years):
            ly = last_year_in_tl + 1 + y
            self.settlement['timeline'].append({'year': ly})

        self.log_event(action="add", key="Timeline", value="%s Lantern Years" % years)
        self.save()


    @web_method
    def rm_lantern_years(self, years=None):
        """ Removes 'years' lantern years from the timeline. Works with a request
        context. Will NOT remove an LY with events in it. """

        if years is None:
            self.check_request_params(['years'])
            years = self.params['years']
        years = int(years)

        lys_removed = 0

        for y in range(years):
            if len(self.settlement['timeline'][-1]) < 2:
                removed_year = self.settlement['timeline'].pop()
                self.logger.warn("%s Removed Lantern Year: %s" % (flask.request.User, removed_year))
                lys_removed +=1
            else:
                self.logger.warn("Refusing to remove LY %s (which has events)." % (self.settlement['timeline'][-1]['year']))

        self.log_event(action="rm", key="Timeline", value="%s Lantern Years" % lys_removed)
        self.save()


    @web_method
    def add_expansions(self, e_list=[], save=True):
        """ Takes a list of expansion handles and then adds them to the
        settlement, applying Timeline updates, etc. as required by the expansion
        asset definitions.

        While processing individual expansion handles, we determine (based on
        the output of self.get_current_ly() and the attribs of the handle),
        whether we want to do the normal, new settlement style add or whether
        we want to do the "late" addition, i.e. because we're at or after the
        LY that the content wants to be added.
        """

        # require asset collections 
        self._require_asset_collection_attributes(['events', 'expansions'])

        # create a list of expansions to add
        if e_list == []:
            self.check_request_params(['expansions'])
            e_list = self.params['expansions']

        #
        # sanity check / filter the incoming list
        #
        for e_handle in e_list:
            # filter bogus handles
            if e_handle not in self.Expansions.get_handles():
                e_list.remove(e_handle)
                warn = "%s Unknown expansion handle '%s' cannot be added!"
                self.logger.warning(warn, self, e_handle)
            # filter redundant handles
            if e_handle in self.settlement["expansions"]:
                e_list.remove(e_handle)
                warn = "%s Expansion handle '%s' already present. Ignoring..."
                self.logger.warn(warn, self, e_handle)

        #
        #   here is where we process the expansion dictionary
        #
        for e_handle in e_list:

            #
            #   private post-process methods; procedural code below
            #

            def normal_add():
                """ This is the normal (new settlement) process for adding an
                expansion to a settlement. """

                if "timeline_rm" in e_dict.keys():
                    [
                        self.rm_timeline_event(e, save=False)
                        for e
                        in e_dict["timeline_rm"]
                        if e["ly"] >= self.get_current_ly()
                    ]

                if "timeline_add" in e_dict.keys():
                    [
                        self.add_timeline_event(e, save=False)
                        for e
                        in e_dict["timeline_add"]
                        if e["ly"] >= self.get_current_ly()
                    ]

                if "rm_nemesis_monsters" in e_dict.keys():
                    for m in e_dict["rm_nemesis_monsters"]:
                        if m in self.settlement["nemesis_monsters"]:
                            self.settlement["nemesis_monsters"].remove(m)
                            self.log_event(
                                action="rm",
                                key="nemesis_monsters",
                                value=m
                            )

            def late_add():
                """ This is the method for adding expansion content to a a
                settlement whose current LY is >= the expansion's
                "maximum_intro_ly" value, if present. """

                self.add_timeline_event(
                    {
                        'handle': e_dict['late_intro_event'],
                        'ly': self.get_current_ly() + 1,
                    },
                    save = False
                )


            #
            #   procedural code starts
            #

            # grab the dict
            e_dict = self.Expansions.get_asset(e_handle)

            # add the handle (or else fail is_compatible() check)
            self.settlement["expansions"].append(e_handle)
            self.log_event(
                action="adding", key="expansions", value=e_dict['name']
            )

            # decide which post-process method to use
            if self.get_current_ly() >= e_dict.get('maximum_intro_ly', 666):
                late_add()
            else:
                normal_add()

        msg = "Successfully added %s expansions to %s"
        self.logger.debug(msg, len(e_list), self)
        if save:
            self.save()


    @web_method
    def rm_expansions(self, e_list=[], save=True):
        """ Takes a list of expansion handles and then removes them them from the
        settlement, undoing Timeline updates, etc. as required by the expansion
        asset definitions. """

        # initialize
        if e_list == []:
            self.check_request_params(['expansions'])
            e_list = self.params['expansions']

        # prune the list to reduce risk of downstream cock-ups
        for e_handle in e_list:
            if e_handle not in self.Expansions.get_handles():
                e_list.remove(e_handle)
                self.logger.warn("Unknown expansion handle '%s' is being ignored!" % (e_handle))
            if e_handle not in self.settlement["expansions"]:
                e_list.remove(e_handle)
                self.logger.warn("Expansion handle '%s' is not in %s" % (e_handle, self))

            # check if the campaign requires it
            if e_handle in self.campaign.asset['settlement_sheet_init'].get(
                'expansions',[]
            ):
                e_list.remove(e_handle)
                err = "Expansion handle '%s' is required and cannot be removed!"
                self.logger.warn(err % e_handle)

        #
        #   here is where we process the expansion dictionary
        #
        for e_handle in e_list:
            e_dict = self.Expansions.get_asset(e_handle)
            self.log_event(action="removing", key="expansions", value=e_dict['name'])

            self.settlement["expansions"].remove(e_handle)

            try:
                if "timeline_add" in e_dict.keys():
                   [self.rm_timeline_event(e, save=False) for e in e_dict["timeline_add"] if e["ly"] >= self.get_current_ly()]
            except Exception as e:
                self.logger.error("Could not remove timeline events for %s expansion!" % e_dict["name"])
                self.logger.exception(e)
            try:
                if "timeline_rm" in e_dict.keys():
                   [self.add_timeline_event(e, save=False) for e in e_dict["timeline_rm"] if e["ly"] >= self.get_current_ly()]
            except Exception as e:
                self.logger.error("Could not add previously removed timeline events for %s expansion!" % e_dict["name"])
                self.logger.exception(e)

            if "rm_nemesis_monsters" in e_dict.keys():
                for m in e_dict["rm_nemesis_monsters"]:
                    if m not in self.settlement["nemesis_monsters"]:
                        self.settlement["nemesis_monsters"].append(m)
                        self.logger.info("Added '%s' to %s nemesis monsters." % (m, self))

            self.logger.info("Removed '%s' expansion from %s" % (e_dict["name"], self))

        self.logger.info("Successfully removed %s expansions from %s" % (len(e_list), self))

        if save:
            self.save()


    @web_method
    @paywall
    def set_custom_url(self, save=True):
        ''' Checks the MDB to make sure the incoming requested URL is not in use
        and then sets it. '''

        self.check_request_params(['url'])
        new_url = self.params['url'].lower()

        # first, validate that it's actually a url
        parsed = urllib.parse.urlparse('https://kdm-manager.com/%s' % new_url)
        for forbidden in [parsed.params, parsed.query, parsed.fragment]:
            if forbidden != '':
                raise utils.InvalidUsage('This is not a valid URL!', 422)
        if len(parsed.path.split('/')) > 2:
            raise utils.InvalidUsage('Do not include slashes!', 422)
        if len(parsed.path.split(' ')) > 1:
            raise utils.InvalidUsage('Do not include white spaces!', 422)
        if len(new_url) < 4:
            raise utils.InvalidUsage('URLs must be at least 4 characters!', 422)

        # second, check reserved
        if new_url in API.config['RESERVED_SETTLEMENT_URLS']:
            raise utils.InvalidUsage('This URL is reserved!', 422)

        # finally, check uniquness
        existing = utils.mdb.settlements.find_one({'custom_url': new_url})
        if existing is not None:
            raise utils.InvalidUsage('This URL is already in use!', 422)

        self.settlement['custom_url'] = new_url

        if save:
            self.save()


    @web_method
    def set_expansions(self, save=True):
        """ Processes the incoming request, compares a list of expansion
        handles to what the settlement currently has, and then calls the
        self.add_expansions and self.rm_expansions methods as necessary.

        This method ONLY works with a request context, so DO NOT call it from
        the CLI or within another function (that does not have a request with
        the appropriate params)!
        """

        # first, sanity check the request
        self.check_request_params(['expansions'])
        new_expansions = self.params['expansions']

        # now create the two different action lists:
        add_expansions = []
        for expansion_handle in new_expansions:
            if expansion_handle not in self.settlement['expansions']:
                add_expansions.append(expansion_handle)

        rm_expansions = []
        for expansion_handle in self.settlement['expansions']:
            if expansion_handle not in new_expansions:
                rm_expansions.append(expansion_handle)

        # now, see if we have any to add/rm and then do it
        # be careful with self.add_expansions / self.rm_expansions, b/c they
        #   check for the same request params!
        if add_expansions != []:
            self.add_expansions(add_expansions, save=False)
        if rm_expansions != []:
            self.rm_expansions(rm_expansions, save=False)

        if save:
            self.save()


    @web_method
    def add_innovation(self, i_handle=None, save=True):
        """ Adds an innovation to the settlement. Request context optional.

        NB: this method (and rm_innovations(), which basically is its inverse)
        does NOT process current survivors.

        Which, to put that another way, means that you SHOULD NOT be using this
        method to add principle-type innovations to the settlement!
        """

        if i_handle is None:
            self.check_request_params(["handle"])
            i_handle = self.params["handle"]

        #
        #   SANITY CHECK
        #

        # verify the handle by initializing it
        i_dict = self.Innovations.get_asset(i_handle)

        # pass/ignore if we're trying to add an innovation twice:
        if i_handle in self.settlement['innovations']:
            self.logger.warn("%s Attempt to add duplicate innovation handle, '%s'. Ignoring... " % (flask.request.User, i_handle))
            return False

        # refuse to add principles
        if i_dict.get('sub_type', None) == 'principle':
            raise utils.InvalidUsage("'Principle-type innovations such as '%s' may not be added this way. Use the set_principle route instead." % (i_dict['name']))

        #
        #   UPDATE
        #

        # append (do not sort)
        self.settlement["innovations"].append(i_handle)

        # levels
        if i_dict.get("levels", None) is not None:
            self.settlement["innovation_levels"][i_handle] = 1

        # log here, before checking for 'current_survivor' attrib
        self.log_event(action="add", key="innovations", value=i_dict['name'], event_type="add_innovation")

        # check for 'current_survivor' attrib
        if i_dict.get('current_survivor', None) is not None:
            self.update_all_survivors('increment', i_dict['current_survivor'], exclude_dead=True)

        # (optional) save
        if save:
            self.save()


    @web_method
    def rm_innovation(self, i_handle=None, save=True):
        """ Removes an innovation from the settlement. Request context is
        optional.

        This method DOES NOT do anything to innovation levels, which stay saved
        on the settlement. If the user re-adds the innovation, it automatically
        sets the level back to one.

        Otherwise, this is just a mirror of add_innovation (above), so
        if you haven't read that doc string yet, I don't know what you're
        waiting for. """

        if i_handle is None:
            self.check_request_params(["handle"])
            i_handle = self.params["handle"]

        #
        #   SANITY CHECK
        #

        # verify the handle by initializing it
        i_dict = self.Innovations.get_asset(i_handle)

        # ignore bogus requests
        if i_handle not in self.settlement["innovations"]:
            self.logger.warn("%s Bogus attempt to remove non-existent innovation '%s'. Ignoring..." % (flask.request.User, i_dict['name']))
            return False

        # refuse to add principles
        if i_dict.get('sub_type', None) == 'principle':
            raise utils.InvalidUsage("'Principle-type innovations such as '%s' may not be removed this way. Use the set_principle route instead." % (i_dict['name']))

        #
        #   UPDATE
        #

        # remove
        self.settlement["innovations"].remove(i_handle)

        # check for 'current_survivor' attrib
        if i_dict.get('current_survivor', None) is not None:
            self.update_all_survivors('decrement', i_dict['current_survivor'], exclude_dead=True)

        # log and (optional) save
        self.log_event(action="rm", key="innovations", value=i_dict['name'], event_type="rm_innovation")
        if save:
            self.save()


    @web_method
    def add_location(self, loc_handle=None, save=True):
        "Adds a location to the settlement. Expects a request context"""

        if loc_handle is None:
            self.check_request_params(['handle'])
            loc_handle = self.params["handle"]

        #
        #   SANITY CHECK
        #

        # verify that the incoming handle is legit
        loc_dict = self.Locations.get_asset(loc_handle)

        # make sure it's not a dupe
        if loc_handle in self.settlement["locations"]:
            self.logger.error("Ignoring request to add duplicate location handle '%s' to settlement." % loc_handle)
            return False

        # check whether the loc is selectable; if not, refuse it
        if not loc_dict.get('selectable', True):
            raise utils.InvalidUsage("Refusing to add non-selectable '%s' location to settlement!" % loc_dict['name'])


        #
        #   UPDATE
        #

        # append it (do not sort)
        self.settlement["locations"].append(loc_handle)

        # do levels
        if "levels" in loc_dict.keys():
            self.settlement["location_levels"][loc_handle] = 1

        # log and (optional) save
        self.log_event(action="add", key="Locations", value=loc_dict['name'], event_type="add_location")
        if save:
            self.save()


    @web_method
    def rm_location(self, loc_handle=None, save=True):
        """ Removes a location from the settlement. Requires a request.User
        object, i.e. should not be called unless it is part of a request.  """

        if loc_handle is None:
            self.check_request_params(['handle'])
            loc_handle = self.params["handle"]

        #
        #   SANITY CHECK
        #

        # verify that the incoming handle is legit
        loc_dict = self.Locations.get_asset(loc_handle)

        # check to see if it's there to remove in the first place
        if loc_handle not in self.settlement["locations"]:
            self.logger.warn("Ignoring attempt to remove %s from %s locations  (because it is not there)." % (loc_handle, self))
            return False

        #
        #   UPDATE
        #

        # now do it
        self.settlement["locations"].remove(loc_handle)

        # log and (optional) save
        self.log_event(action="rm", key="Locations", value=loc_dict['name'], event_type="rm_location")
        if save:
            self.save()


    @web_method
    def add_milestone(self, handle=None):
        """ Adds a Milestone Story Event. Wants a request context. """

        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params['handle']

        # bail if it's already in here
        if handle in self.settlement['milestone_story_events']:
            warn = (
                "%s Attempting to add Milestone that is already present. "
                "Ignoring bogus request..."
            )
            self.logger.info(warn, self)
            return True

        # otherwise, let's do it
        milestone_asset = self.Milestones.get_asset(handle=handle)
        self.settlement['milestone_story_events'].append(handle)
        self.log_event(
            action="add",
            key="Milestone Story Events",
            value=milestone_asset['name'],
            event_type="add_milestone_story_event"
        )
        self.save()


    @web_method
    def rm_milestone(self, handle=None):
        """ Removes a Milestone Story Event. Wants a request context. """

        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params['handle']

        milestone_asset = self.Milestones.get_asset(handle=handle)
        if milestone_asset['handle'] not in self.settlement['milestone_story_events']:
            warn = (
                "%s Attempting to remove Milestone that is not present. "
                "Ignoring bogus request..."
            )
            self.logger.info(warn, self)
            return True

        self.settlement['milestone_story_events'].remove(milestone_asset['handle'])
        self.log_event(
            action="rm",
            key="Milestone Story Events",
            value=milestone_asset['name'],
            event_type="rm_milestone_story_event"
        )
        self.save()


    @web_method
    def add_monster(self, monster_handle=None):
        """ Adds quarry and nemesis type monsters to the appropriate settlement
        list, e.g. self.settlement["nemesis_monsters"], etc.

        CAN be used without a request context. """

        if monster_handle is None:
            self.check_request_params(["handle"])
            monster_handle = self.params["handle"]

        # Initialize the monster asset (die if the handle is bogus)
        m_dict = self.Monsters.get_asset(monster_handle)

        # get the type from the asset dict
        if m_dict["sub_type"] == 'quarry':
            target_list = self.settlement["quarries"]
        elif m_dict["sub_type"] == 'nemesis':
            target_list = self.settlement["nemesis_monsters"]
        else:
            err = "Monster 'sub_type' value of '%s' is not supported!'"
            raise utils.InvalidUsage(err % m_dict['sub_type'])

        # finally, add, log and save
        if monster_handle not in target_list:
            target_list.append(monster_handle)
            if m_dict.get("sub_type", None) == 'nemesis':
                self.settlement["nemesis_encounters"][monster_handle] = []

        self.log_event(
            action="add",
            key="%s monsters" % m_dict['sub_type'],
            value=m_dict["name"],
            event_type="add_monster"
        )

        self.save()


    @web_method
    def rm_monster(self, monster_handle=None):
        """ Removes a monster from the settlement's list of quarry or nemesis
        monsters. Basically the inverse of the add_monster() method (above)."""

        # get the handle from kwargs or from the request
        if monster_handle is None:
            self.check_request_params(["handle"])
            monster_handle = self.params["handle"]

        # sanity check the handle; load an asset dict for it
        m_dict = self.Monsters.get_asset(monster_handle)

        # figure out what type it is or die trying
        m_type = m_dict['sub_type']
        if m_type == 'quarry':
            target_list = self.settlement['quarries']
        elif m_type == 'nemesis':
            target_list = self.settlement['nemesis_monsters']
        else:
            # 1.) if we're failing, record the problem asset in the logs
            err_0 = "%s Unable to process 'rm_monster' operation on asset: %s"
            self.logger.error(err_0 % (self, m_dict))

            # 2.) return a descriptive, but not fully-detailed, error
            err_1 = (
                "Monster asset with type '%s' cannot be removed! "
                "Supported types are 'quarry' and 'nemesis'."
            )
            raise utils.InvalidUsage(
                err_1 % m_type
            )

        # general handling for both types
        if monster_handle in target_list:
            target_list.remove(monster_handle)
        else:
            err = "%s Ignoring attempt to remove non-existing item '%s' from %s"
            self.logger.error(err % (self, monster_handle, m_type))

        # additional handling for nemeses
        if (
            m_type == 'nemesis' and
            monster_handle in self.settlement['nemesis_encounters'].keys()
        ):
            del self.settlement["nemesis_encounters"][monster_handle]

        self.log_event(
            action="rm",
            key="%s monsters" % m_dict['type'],
            value=m_dict["name"],
            event_type="rm_monster"
        )

        self.save()


    @web_method
    def add_monster_volume(self):
        """
        Adds a Monster Volume string. Forces the
        self.settlement['monster_volumes'] to be unique. Expects a request
        context.
        """

        # initialize and validate
        self.check_request_params(['name'])
        vol_string = self.params['name']

        if vol_string in self.get_monster_volumes():
            err = "%s Monster volume '%s' already exists! Ignoring request..."
            self.logger.warning(err % (self, vol_string))
            return True

        # add the list if it's not present
        if not 'monster_volumes' in self.settlement.keys():
            self.settlement['monster_volumes'] = []
        self.settlement['monster_volumes'].append(vol_string)

        self.log_event(
            action="add",
            key="Monster Volumes",
            value=vol_string,
            event_type='add_monster_volume'
        )
        self.save()


    @web_method
    def rm_monster_volume(self):
        """ Removes a Monster Volume string. Fails gracefully if asked to remove
        a non-existent string. Assumes a request context. """

        # initialize
        self.check_request_params(['name'])
        vol_string=self.params['name']

        if vol_string not in self.get_monster_volumes():
            warn = (
                "%s Monster volume string '%s' is not recorded! "
                "Ignoring bogus request..."
            )
            self.logger.warn(warn, self, vol_string)
            return True

        # add the list if it's not present
        self.settlement['monster_volumes'].remove(vol_string)

        self.log_event(
            action="rm",
            key="Monster Volumes",
            value=vol_string,
            event_type='rm_monster_volume'
        )
        self.save()


    @web_method
    def set_admins(self):
        """ Replaces/supersedes the one-off add/rm methods. Requires a request.
        Proccesses a list of settlement administrators and adds or removes
        email addresses from the list as appropriate. """

        self.check_request_params(['admins'])
        new_list = self.params['admins']

        # get the add/rm lists
        add_list, rm_list = utils.list_compare(
            self.settlement['admins'],
            new_list
        )

        if add_list != []:
            [self.add_settlement_admin(login) for login in add_list]

        if rm_list != []:
            [self.rm_settlement_admin(login) for login in rm_list]

        self.save()


    @web_method
    def add_settlement_admin(self, user_login=None):
        """ Adds a user login (i.e. email address) to the
        self.settlement['admins'] list. Fails gracefully if the user is already
        there. Expects a request context. """

        if user_login is None:
            self.check_request_params(['login'])
            user_login = self.params['login']

        if user_login in self.settlement['admins']:
            err = "%s User '%s' is already a settlement admin! Ignoring..."
            self.logger.warning(err % (self, user_login))
            return True

        if utils.mdb.users.find_one({'login': user_login}) is None:
            err = "The email address '%s' does not belong to a registered user!"
            raise utils.InvalidUsage(err % user_login, status_code=400)

        self.settlement['admins'].append(user_login)
        self.log_event(action="add", key="administrators", value=user_login)
        self.save()


    @web_method
    def rm_settlement_admin(self, user_login=None):
        """ Removes a user login (i.e. email address) from the
        self.settlement['admins'] list. Fails gracefully if the user is already
        there. Expects a request context. """

        if user_login is None:
            self.check_request_params(['login'])
            user_login = self.params['login']

        if user_login not in self.settlement['admins']:
            err = "%s User '%s' is not a settlement admin! Ignoring..."
            self.logger.warning(err % (self, user_login))
            return True

        if utils.mdb.users.find_one({'login': user_login}) is None:
            err = "The email address '%s' does not belong to a registered user!"
            raise utils.InvalidUsage(err % user_login, status_code=400)

        self.settlement['admins'].remove(user_login)
        self.log_event(action="rm", key="administrators", value=user_login)
        self.save()


    def add_settlement_note(self, n={}):
        """ Adds a settlement note to MDB. Expects a dict. """

        author = utils.mdb.users.find_one({'_id': ObjectId(n['author_id'])})

        ly = n.get('lantern_year', self.get_current_ly())
        author_email = n.get('author', author['login'])

        note_dict = {
            "note": n["note"].strip(),
            "created_by": author['_id'],
            "author": author_email,
            "created_on": datetime.now(),
            "settlement": self.settlement["_id"],
            "lantern_year": ly,
        }

        note_oid = utils.mdb.settlement_notes.insert(note_dict)
        return flask.Response(
            response=json.dumps(
                {'note_oid': note_oid}, default=json_util.default),
                status=200
            )


    @web_method
    def rm_settlement_note(self, n_id=None):
        """ Removes a note from MDB. Expects a dict with one key. """

        if n_id is None:
            self.check_request_params(['_id'])
            n_id = self.params['_id']

        n_id = ObjectId(n_id)

        n = utils.mdb.settlement_notes.remove(
            {
                "_id": n_id,
                "settlement": self.settlement["_id"]
            }
        )
        msg = "%s User '%s' removed a settlement note"
        self.logger.info(msg % (self, flask.request.User.login))


    @web_method
    @paywall
    def add_survivor(self):
        """ Uses the request context to add a pre-fab survivor. Requires a valid
        'handle' value in the POST. """

        # sanity check first; get the 'handle' from the POST
        self.check_request_params(['handle'])
        survivor_handle = self.params['handle']

        # now, copy the asset to start a new MDB survivor record
        survivor_dict = copy(self.Survivors.get_asset(survivor_handle))
        attribs = survivor_dict["attribs"]
        attribs.update(
            {
                "settlement": self._id,
                'vignette_survivor_handle': survivor_handle,
            }
        )

        # initialize the survivor using the Survivor object class
        Survivor(new_asset_attribs=attribs, Settlement=self)

        # finally, if the incoming survivor is from an expansion, add that
        # expansion to the settlement expansions 
        if survivor_dict.get('expansion', None) is not None:
            self.add_expansions([survivor_dict['expansion']])

        # no settlement event logging here, since everything else we do in this
        # method has its own settlement event logging...


    def add_timeline_event(self, e={}, save=True):
        """ Adds a timeline event to self.settlement["timeline"]. Expects a dict
        containing the whole event's data: no lookups here. """

        self._require_asset_collection_attributes(['events'])


        # ensure that the incoming event specifies the target LY
        t_index = e.get('ly', None)
        if t_index is None:
            err = (
                "To add an event to the Timeline, the incoming event dict must "
                "specify a Lantern Year, e.g. {'ly': 3}"
            )
            raise utils.InvalidUsage(err)

        # if we can, "enhance" the incoming dict with additional asset info
        if e.get('handle', None) is not None:
            e.update(self.Events.get_asset(e['handle']))

        # if we don't know the event's sub_type, we have to bail
        if e.get('sub_type', None) is None:
            err = (
                "To add an event to the Timeline, the incoming event dict must "
                "specify the 'sub_type' of the event, e.g. {'sub_type': "
                "'nemesis_encounter'}"
            )
            utils.InvalidUsage(err)
            return False

        # compatibility check!
        if not self.is_compatible(e):
            err = (
                "Event '%s' is not compatible with this campaign! Ignoring "
                "reuqest to add..."
            )
            self.logger.warn(err, e['name'])
            return False


        #
        #   Add it!
        #

        # remove the target LY (we're going to update it and insert it back in
        target_ly = self.settlement["timeline"][t_index]
        self.settlement['timeline'].remove(target_ly)

        # update the target LY list to include a dict for our incoming sub_type
        #    if it doesn't already have one
        if target_ly.get(e['sub_type'], None) is None:
            target_ly[e['sub_type']] = []

        target_ly[e['sub_type']].append(e)

        # re-insert and save if successful
        self.settlement['timeline'].insert(t_index, target_ly)

        self.log_event(
            action='add',
            key="timeline (LY %s)" % t_index,
            value=e["name"],
            event_type="sysadmin"
        )

        # finish with a courtesy save
        if save:
            self.save()


    def rm_timeline_event(self, e={}, save=True):
        """ This method supports the removal of an event from the settlement's
        Timeline.

        At a bare minimum, the 'e' kwarg must be an event dict that includes the
        'ly' key (which should be an int representing the target LY) and the
        'handle' key, which will be used to determine other values.

        If you want to remove an event WITHOUT using the 'handle' key, you must
        then include the following keys (at a minimum):
            - 'ly'
            - 'name'
            - 'sub_type'

        Finally, this method was revised to support Timeline version 1.2, so
        Timelines later/earlier than that may not work correctly with it.
        """

        #
        #   Initialization and Sanity Checks!
        #

        # ensure that the incoming event specifies the target LY to remove it
        #   from. The LY of the incoming event is also the index of the year
        #   dict we want to with (since Timelines start with LY 0)
        t_index = e.get('ly', None)
        if t_index is None:
            raise utils.InvalidUsage(
                "To remove an event from the Timeline, the incoming event dict "
                "must specify a Lantern Year, e.g. {'ly': 3}"
            )

        # if we can, "enhance" the incoming dict with additional asset info
        if e.get('handle', None) is not None:
            e.update(self.Events.get_asset(e['handle']))

        # if we don't know the event's sub_type, we have to bail
        if e.get('sub_type', None) is None:
            utils.InvalidUsage(
                "To remove an event from the Timeline, the incoming event dict "
                "must specify the 'sub_type' of the event, "
                "e.g. {'sub_type': 'story_event'}"
            )
            return False

        # finally, get the target LY from the timeline; fail gracefully if there
        #   are no events of our target sub_type
        target_ly = self.settlement['timeline'][t_index]
        if target_ly.get(e['sub_type'], None) is None:
            self.logger.error(
                "Lantern Year %s does not include any '%s' events! Ignoring "
                "attempt to remove..." % (t_index, e['sub_type'])
            )
            return False


        #
        #   Timeline Update
        #

        # initialize a generic success toke
        success = False

        # get the timeline and remove the target year, since we're going to
        # update it and then re-insert it when we're done
        timeline = self.settlement["timeline"]
        timeline.remove(target_ly)

        # figure out if we're removing by name or handle
        rm_attrib = 'handle'
        if e.get('handle', None) is None:
            rm_attrib = 'name'

        # now iterate through all events of our target sub_type in our target LY
        #   and kill them, if they match our handle/name (see: issue #277)
        for e_dict in target_ly[e['sub_type']]:
            if e_dict.get(rm_attrib, None) == e[rm_attrib]:
                target_ly[e['sub_type']].remove(e_dict)
                self.log_event(
                    action='rm',
                    key="timeline (LY %s)" % t_index,
                    value=e["name"],
                    event_type="sysadmin"
                )
                success = True

        # insert our updated year back into the TL and save
        timeline.insert(t_index, target_ly)

        # check our success flag and, if we were successful, save. Otherwise, we
        #   freak the fuck out and panic (j/k: fail gracefully, but log/email
        #   the error back to home base
        if success:
            self.settlement["timeline"] = timeline
            if save:
                self.save()
        else:
            utils.InvalidUsage(
                "Event could not be removed from timeline! %s" % (e)
            )



    #
    #   misc. methods
    #

    @web_method
    def return_survivors(self, aftermath=None):
        """ Returns all survivors with departing=True (i.e. initializes the
        survivor and calls Survivor.return_survivor() on it and then processes
        showdown/hunt attributes.

        Assumes a request context (because why else would you be doing this?)
        """

        # determine (or default) the showdown type
        showdown_type = self.settlement.get('showdown_type', 'normal')

        # initialize!
        if aftermath is None:
            self.check_request_params(['aftermath'])
            aftermath = self.params['aftermath']
        if aftermath not in ['victory','defeat']:
            raise Exception("The 'aftermath' value of '%s' is not allowed!" % (aftermath))

        # 1.) handle the current quarry/showdown monst 
        if aftermath == 'victory' and self.settlement.get('current_quarry', None) is not None:
            self.add_defeated_monster(self.settlement['current_quarry'])
            del self.settlement['current_quarry']

        # 2.) remove misc meta data
        for tmp_key in ['hunt_started','showdown_type']:
            if tmp_key in self.settlement.keys():
                self.logger.debug("%s Removed tmp attribute: '%s'." % (self, tmp_key))
                del self.settlement[tmp_key]

        # 3.) process survivors, keeping a list of IDs for later
        returned = []
        for s in self.survivors:
            if s.is_departing():
                s.return_survivor(showdown_type)
                returned.append(s)

        # 4.) remove 'skip_next_hunt' from anyone who sat this one out
        if showdown_type == 'normal':
            for s in self.get_survivors(list, excluded=[s._id for s in returned], exclude_dead=True):
                if 'skip_next_hunt' in s.keys():
                    S = Survivor(_id=s['_id'], Settlement=self)
                    S.toggle_boolean('skip_next_hunt')

        # 5.) log the return
        live_returns = []
        for s in returned:
            if not s.is_dead():
                live_returns.append(s.survivor['name'])

        msg = "Departing Survivors returend to the settlement in %s." % (aftermath)
        if live_returns != []:
            returners = utils.list_to_pretty_string(live_returns)
            if showdown_type == 'special':
                msg = "%s healed %s." % (flask.request.User.login, returners)
            else:
                msg = "%s returned to the settlement in %s." % (returners, aftermath)
        else:
            if showdown_type == 'special':
                msg = 'No survivors were healed after the Special Showdown.'
            else:
                msg = "No survivors returned to the settlement."
        self.log_event(msg, event_type="survivors_return_%s" % aftermath)


        # 6.) increment endeavors
        if showdown_type == 'normal' and live_returns != [] and aftermath == "victory":
            self.update_endeavor_tokens(len(live_returns), save=False)


        # 7.) increment LY, if necessary
        if self.params.get('increment_ly', False):
            if not self.get_current_ly() >= self.get_max_ly():
                self.set_current_lantern_year(self.get_current_ly() + 1)

        self.save()


    #
    #   set methods
    #

    @web_method
    def set_current_lantern_year(self, ly=None):
        """ Sets the current Lantern Year. Supports a request context, but does
        not require it. """

        if ly is None:
            self.check_request_params(['ly'])
            ly = self.params['ly']
        ly = int(ly)

        # ignore bogus updates
        if self.settlement['lantern_year'] == ly:
            self.logger.warn('%s Ignoring attempt to set LY to current.' % self)
            return True

        self.settlement['lantern_year'] = ly
        self.log_event(action='set', key="current Lantern Year", value=ly)
        self.save()


    @web_method
    def set_inspirational_statue(self):
        """ Set the self.settlement['inspirational_statue'] to a fighting art
        handle. Assumes a request context. """

        self.check_request_params(['handle'])
        fa_handle = self.params['handle']

        try:
            fa_dict = self.FightingArts.get_asset(fa_handle)
        except:
            err = "Fighting Art handle '%s' is not a known asset handle!"
            raise utils.InvalidUsage(err % fa_handle)

        self.settlement['inspirational_statue'] = fa_handle
        self.log_event(
            action="set", key="Inspirational Statue", value=fa_dict['name']
        )
        self.save()


    @web_method
    def set_lantern_research_level(self):
        """ Sets the self.settlement['lantern_research_level'] to incoming
        'value' param. Requires a request context."""

        self.check_request_params(['value'])
        level = self.params['value']

        # create the attrib if it doesn't exist
        self.settlement['lantern_research_level'] = level
        self.log_event(action="set", key="Lantern Research level", value=level)
        self.save()


    @web_method
    def set_lost_settlements(self):
        """ Updates settlement["lost_settlements"] to a new int type value. """

        # two-part sanity check; part one: param exists
        self.check_request_params(['value'])
        new_value = self.params['value']

        # part two: param is an int
        try:
            new_value = int(new_value)
        except ValueError as e:
            self.logger.error(e)
            err = "Cannot set non-integer value '%s'!" % new_value
            self.logger.error(err)
            raise utils.InvalidUsage(err)

        # now set it, but don't go below zero
        if new_value <= 0:
            self.settlement["lost_settlements"] = 0
        else:
            self.settlement["lost_settlements"] = new_value

        self.log_event(key="Lost Settlements count", value=new_value)
        self.save()


    @web_method
    def set_milestones(self):
        """ This web method lets an app post a list of settlement milestones and
        then does the dirty work of figuring out whether they're being added or
        removed (and then making the appropriate method call). """

        # get the new list
        self.check_request_params(["milestone_story_events"])
        new_milestones = self.params['milestone_story_events']

        # compare to the old list and see if we can ignore
        old_milestones = self.settlement['milestone_story_events']
        if sorted(new_milestones) == sorted(old_milestones):
            self.logger.warn('Old/new milestone lists match. Ignoring...')
            return True

        # now process the add/remove jobs
        milestones_union = set(old_milestones).union(set(new_milestones))
        for milestone_handle in milestones_union:
            if (
                milestone_handle in new_milestones and
                milestone_handle not in old_milestones
            ):
                self.add_milestone(milestone_handle)
            elif (
                milestone_handle not in new_milestones and
                milestone_handle in old_milestones
            ):
                self.logger.warn('would rm %s' % milestone_handle)
                self.rm_milestone(milestone_handle)


    @web_method
    def set_name(self, new_name=None):
        """ Looks for the param key 'name' and then changes the Settlement's
        self.settlement["name"] to be that value. Works with or without a
        request context. """

        if new_name is None:
            self.check_request_params(['name'])
            new_name = self.params["name"]

        if new_name == "":
            new_name = "UNKNOWN"
        new_name = utils.html_stripper(new_name.strip())

        old_name = self.settlement["name"]
        self.settlement["name"] = new_name

        if old_name is None:
            msg = "%s named the settlement '%s'."
            msg = msg % (flask.request.User.login, new_name)
        else:
            msg = "%s changed settlement name from '%s' to '%s'"
            msg = msg % (flask.request.User.login, old_name, new_name)

        self.log_event(action="set", key="name", value=new_name)
        self.save()


    @web_method
    def set_principle(self):
        """ Basically, we're looking for incoming JSON to include a 'principle'
        key and an 'election' key.

        The 'principle' should be something such as,
        'new_life', 'conviction', 'new_life_potsun', etc. The 'election' should
        be an Innovation (principle) handle such as, 'barbaric', 'romantic, etc.

        Alternately, the 'principle' can be a boolean False. If this is the case
        we 'unset' the principle from the settlement.
        """

        # initialize
        self.check_request_params(["principle", "election"])
        principle = self.params["principle"]
        election = self.params["election"]

        # validate the principle first
        principles = self.Principles.assets

        if principle in principles.keys():
            p_dict = principles[principle]
        else:
            msg = "The principle handle '%s' is not recognized!" % principle
            self.logger.error(msg)
            raise utils.InvalidUsage(msg, status_code=400)

        # now validate the election
        unset = False
        if election in self.Innovations.get_handles():
            e_dict = self.Innovations.get_asset(election)
        elif type(election) == bool:
            unset = True
        else:
            msg = "The '%s' principle election handle '%s' is not recognized!" % (p_dict["name"], election)


        def remove_principle(principle_handle):
            """ private, internal fun for removing a principle. """
            principle_dict = self.Innovations.get_asset(principle_handle)
            self.settlement["principles"].remove(principle_handle)
            self.logger.debug("%s removed '%s' from %s principles" % (flask.request.User, principle_handle, self))
            if principle_dict.get("current_survivor", None) is not None:
                self.update_all_survivors("decrement", principle_dict["current_survivor"], exclude_dead=True)


        # do unset logic
        if unset:
            removed = 0
            for option in p_dict["option_handles"]:
                if option in self.settlement["principles"]:
                    remove_principle(option)
                    removed += 1
            if removed >= 1:
                self.log_event(
                    action="unset",
                    key="'%s' principle" % p_dict['name'],
                    event_type="set_principle"
                )
                self.save()
#            else:
#                self.logger.debug(
#                    "%s Ignoring bogus 'unset princple' request." % (self)
#                )
            return True
        else:
            # ignore re-clicks
            if e_dict["handle"] in self.settlement["principles"]:
                err = "%s Ignoring duplicate principle handle '%s' (%s)"
                self.logger.warn(
                    err % (flask.request.User, e_dict["handle"], self)
                )
                return True

        # remove the opposite principle
        for option in p_dict["option_handles"]:
            if option in self.settlement["principles"]:
                remove_principle(option)

        # finally, add the little fucker
        self.settlement["principles"].append(e_dict["handle"])
        self.log_event(action="set", key="'%s' principle" % p_dict['name'], value=e_dict['name'])

        # if we're still here, go ahead and save since we probably updated
        self.save()

        # post-processing: add 'current_survivor' effects
        if e_dict.get("current_survivor", None) is not None:
            self.update_all_survivors("increment", e_dict["current_survivor"], exclude_dead=True)


    @web_method
    def set_showdown_type(self, showdown_type=None):
        """ Expects a request context and looks for key named 'type'. Uses the
        value of that key as self.settlement['showdown_type']. """

        if showdown_type is None:
            self.check_request_params(['showdown_type'])
            showdown_type = self.params['showdown_type']

        self.settlement['showdown_type'] = showdown_type
        self.save()


    @web_method
    def set_storage(self):
        """ Takes in a list of JSON dictionaries from a request and updates the
        self.settlement['storage'] list. """

        self.check_request_params(['storage'])
        dict_list = self.params['storage']

        for d in dict_list:
            handle = d['handle']
            a_obj = self.settlement_storage.item_handle_to_item_object(d['handle'])
            value = int(d['value'])

            # remove all occurrences of handle from storage
            self.settlement['storage'] = list(
                filter(lambda a: a != handle, self.settlement['storage'])
            )
            for i in range(value):
                self.settlement['storage'].append(handle)

            self.log_event("%s updated settlement storage: %s x %s" % (
                flask.request.User.login,
                a_obj.name,
                value)
            )

        self.save()


    @web_method
    def set_version(self):
        """ Replaces the current 'version' key (which is a str handle) with one
        from the request params. """

        # initialize
        self.check_request_params(["version"])
        new_version = self.params["version"]

        try:
            v_object = KingdomDeath.versions.Version(handle=new_version)
        except Exception as err:
            self.logger.error(err)
            err = "Version '%s' is not a known version handle!"
            raise utils.InvalidUsage(err % new_version)

        self.settlement['version'] = new_version
        self.log_event(
            action="set",
            key="Version",
            value=v_object.get_float(),
            event_type='sysadmin'
        )

        self.save()




    #
    #   set methods
    #

    @web_method
    def set_attribute(self):
        """ Starting in 2021, this is our workhorse method. We're going to start
        deprecating specialized methods from the perspective of external users
        and using this method to 'route' out to those specialized (read: chock
        full of business logic) methods."""

        self.check_request_params(['attribute','value'])
        attribute = self.params["attribute"]
        value = self.params["value"]

        # routing to specialized methods!
        if attribute == 'abandoned':
            return self.abandon(value=value)

        # generic handling follows
        self.settlement[attribute] = value
        pretty_attribute = attribute.title().replace('_',' ')
        msg = "%s set settlement %s to %s"
        self.log_event(
            msg % (
                flask.request.User.login,
                pretty_attribute,
                self.settlement[attribute]
            )
        )
        self.save()


    @web_method
    def set_current_quarry(self, new_quarry=None):
        """ Sets the self.settlement["current_quarry"] attrib. """

        if new_quarry is None:
            new_quarry = self.params["current_quarry"]

        self.settlement["hunt_started"] = datetime.now()
        self.settlement["current_quarry"] = new_quarry
        self.log_event("%s set target monster to %s" % (flask.request.User.login, new_quarry), event_type="set_quarry")
        self.save()


    @web_method
    def set_location_level(self):
        """ Sets self.settlement["location_levels"][handle] to an int. """

        if self.check_request_params(["handle","level"], True):
            handle = self.params["handle"]
            level = self.params["level"]
        else:
            self.logger.error("Could not set settlement location level!")
            raise Exception

        L = locations.Assets()
        loc_dict = L.get_asset(handle)

        if handle not in self.settlement["locations"]:
            self.logger.error("Could not set settlement location level for '%s', which is not in %s locations: %s" % (handle, self, self.settlement["locations"]))
        else:
            self.settlement["location_levels"][handle] = int(level)

        self.log_event("%s set '%s' location level to %s." % (flask.request.User.login, loc_dict["name"], level), event_type="set_location_level")

        self.save()


    @web_method
    def set_innovation_level(self):
        """ Sets self.settlement["innovation_levels"][handle] to an int. """

        if self.check_request_params(["handle","level"], True):
            handle = self.params["handle"]
            level = self.params["level"]
        else:
            self.logger.error("Could not set settlement innovation level!")
            raise Exception

        i_dict = self.Innovations.get_asset(handle)

        if handle not in self.settlement["innovations"]:
            self.logger.error("Could not set settlement innovation level for '%s', because that innovation is not included in the %s innovations list: %s" % (handle, self, self.settlement["innovations"]))
        else:
            self.settlement["innovation_levels"][handle] = int(level)

        self.log_event("%s set '%s' innovation level to %s." % (flask.request.User.login, i_dict["name"], level), event_type="set_innovation_level")

        self.save()



    #
    #   Replace Methods! These are Watcher-style methods for updating multiple
    #   data elements at once. 
    #

    @web_method
    def replace_game_assets(self):
        """ Works just like the method of the same name in the survivor class,
        but for settlements.

        This one REQUIRES A REQUEST CONTEXT and cannot be called without one. It
        also does not accept any arguments, because, again, it should only be
        called when there's a POST body to parse for arguments.

        Must like the Survivor version, this creates two lists: handles to add
        and handles to remove, and then does them one by one. If it fails at any
        point, the whole thing is a wash and we don't save any changes.
        """

        self.check_request_params(['type','handles'])
        asset_class = self.params['type']
        asset_handles = self.params['handles']

        if asset_class not in self.settlement.keys():
            raise utils.InvalidUsage("The settlement objects does not have an '%s' attribute!" % asset_class)
        elif type(self.settlement[asset_class]) != list:
            raise utils.InvalidUsage("The settlement object '%s' attribute is not a list type and cannot be updated with this method!" % asset_class)
        elif type(asset_handles) != list:
            raise utils.InvalidUsage("'handles' value must be a list/array type!")

        # special check (transitional) for supported attribs
        supported_attribs = ['innovations','locations']
        if asset_class not in supported_attribs:
            raise utils.InvalidUsage("This route currently only supports updates to the following attribute keys: %s!" % utils.list_to_pretty_string(supported_attribs, quote_char="'"))

        # 0.) force incoming asset_handles to be a set
        asset_handles = set(asset_handles)

        # 1.) initialize holder sets
        handles_to_add = [h for h in asset_handles if h not in self.settlement[asset_class]]
        handles_to_rm = [h for h in self.settlement[asset_class] if h not in asset_handles]

        # 1.a) bail if we've got no changes to make
        if handles_to_add == [] and handles_to_rm == []:
            self.logger.warn("%s Incoming replace_game_assets() request makes no changes! Ignoring..." % self)
            return True

        # 2.) if we're still here, iterate over the lists
        if asset_class == 'innovations':
            for r in handles_to_rm:
                self.rm_innovation(r, save=False)
            for a in handles_to_add:
                self.add_innovation(a, save=False)
        elif asset_class == 'locations':
            for r in handles_to_rm:
                self.rm_location(r, save=False)
            for a in handles_to_add:
                self.add_location(a, save=False)


        self.save()


    @web_method
    def set_lantern_year(self):
        """ Sets a lantern year. Requires a request context. """

        self.check_request_params(['ly'])
        new_ly = self.params['ly']

        # thanks to LY zero, Lantern Years correspond to Timeline list indexes.
        del self.settlement['timeline'][new_ly['year']]
        self.settlement['timeline'].insert(new_ly['year'], new_ly)

        err = "%s updated Timeline events for Lantern Year %s."
        self.log_event(
            err % (flask.request.User.login, new_ly['year'])
        )
        self.save()


    @web_method
    def set_patterns(self, save=True):
        """ Updates the settlements 'patterns' list. Initializes gear objects
        to do it, so watch out for that. """

        # sanity check the request
        self.check_request_params(['patterns'])
        new_list = self.params['patterns']

        # get the add/rm lists 
        add_list, rm_list = utils.list_compare(
            self.settlement['patterns'],
            new_list
        )

        def update_list(action, handle):
            """ Initialize a Gear object from the handle. Evaluate it and, if it
            checks out, do the needful and log about it. """

            # initialize the gear
            gear_asset = self.Gear.get_asset(handle)

            # sanity check the gear
            gear_sub_type = gear_asset.get('sub_type', None)
            if gear_sub_type != 'pattern':
                err = "%s must be 'pattern' sub_type, not '%s'"
                raise utils.InvalidUsage(err % (gear_asset, gear_sub_type))

            # do the action
            if action == 'rm':
                self.settlement['patterns'].remove(handle)
            elif action == 'add':
                self.settlement['patterns'].append(handle)
            else:
                raise utils.InvalidUsage('Invalid action! Failing...')

            self.log_event(
                action = action,
                key = "Patterns",
                value = gear_asset.get('name', None)
            )


        if add_list != []:
            [update_list('add', handle) for handle in add_list]

        if rm_list != []:
            [update_list('rm', handle) for handle in rm_list]

        if save:
            self.save()


    @web_method
    def set_strain_milestones(self, save=True):
        """ Wraps the toggle_strain_milestone() method below. Pass in the
        settlement sheet's 'strain_milestones' list as 'strain_milestones' in
        the request parameters to use it. """

        # sanity check the request
        self.check_request_params(['strain_milestones'])
        new_list = self.params['strain_milestones']

        # get the add/rm lists 
        add_list, rm_list = utils.list_compare(
            self.settlement['strain_milestones'],
            new_list
        )

        def update_list(action, handle):
            """ Private function to update the settlement's Strain Milestones.
            Does an asset lookup and writes a nice semantic log entry. """

            # find the asset or die
            strain_milestone_asset = self.StrainMilestones.get_asset(handle)
            if strain_milestone_asset is None:
                err = "'%s' is not a valid Strain Milestone handle!" % handle
                raise utils.InvalidUsage(err)

            # do the action
            if action == 'rm':
                self.settlement['strain_milestones'].remove(handle)
            elif action == 'add':
                self.settlement['strain_milestones'].append(handle)
            else:
                raise utils.InvalidUsage('Invalid action! Failing...')

            self.log_event(
                action=action,
                key="Strain Milestones",
                value=strain_milestone_asset['name']
            )


        if add_list != []:
            [update_list('add', handle) for handle in add_list]

        if rm_list != []:
            [update_list('rm', handle) for handle in rm_list]

        if save:
            self.save()


    @web_method
    @deprecated
    def toggle_strain_milestone(self, handle=None):
        """ DEPRECATED JUNE 2021. Goes away with version four of the web app.
        Toggles a strain milestone on or off, i.e. adds/rms it from the list.
        """

        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params['handle']

        # find the asset or die
        strain_milestone_asset = self.StrainMilestones.get_asset(handle)
        if strain_milestone_asset is None:
            err = "'%s' is not a valid Strain Milestone handle!" % handle
            raise utils.InvalidUsage(err)

        # now do the toggle
        action = 'add'
        if handle not in self.settlement['strain_milestones']:
            self.settlement['strain_milestones'].append(handle)
        else:
            self.settlement['strain_milestones'].remove(handle)
            action = 'rm'

        self.log_event(
            action=action,
            key="Strain Milestones",
            value=strain_milestone_asset['name']
        )
        self.save()





    #
    #   get methods
    #

    def get_available_assets(self, asset_collection=None, handles=True,
            only_include_selectable=False, exclude_sub_types=None):

        """ Generic function to return a dict of available game assets based on
        their family.

        'asset_collection' kwarg MUST be one of the Collection objects that gets
        added to the settlement as an attribute, e.g. self.FightingArts or
        self.Disorders or something.

        Use the 'handles' kwarg (boolean) to determine whether to return a
        dictionary of dictionaries (where asset handles are the keys) or a flat
        list of asset dictionaries (set 'handles' False to get a list back).

        'only_include_selectable' removes ALL assets from the output if they do
        not have the 'selectable' key as part of their definition.
        """

        # initialize the output container, 'available'
        if handles:
            available = collections.OrderedDict()   # NOT A REGULAR DICT!!!
        else:
            available = []

        # create the output; get_sorted_assets sorts on 'name' attributes
        for a_handle, a_dict in asset_collection.get_sorted_assets().items():
            asset_available = False

            # first, check compatibiltiy
            if self.is_compatible(a_dict):
                asset_available = True

            # apply the selectability criterion
            if only_include_selectable and not a_dict.get('selectable', False):
                asset_available = False

            # apply the sub_types filter
            if exclude_sub_types is not None:
                for s_type in exclude_sub_types:
                    if a_dict.get('sub_type', None) == s_type:
                        asset_available = False

            # finally, add it to the output container
            if asset_available:
                if handles:
                    available.update({a_handle: a_dict})
                else:
                    available.append(a_dict)

        asset_collection_name = asset_collection.__module__.split('.')[-1]
        return {asset_collection_name: available}


    def _get_additional_survivor_sheet_requirements(self):
        ''' New in October 2023; supports Advanced KDM (and some expansion
        content that came out before) by using settlement expansion content to
        create a dictionary that defines additional Survivor Sheet requirements.

        Requirements might be a boolean or a flag or something.
        '''

        output = {}

        for e_handle in self.settlement['expansions']:
            e_dict = self.Expansions.get_asset(e_handle)

            # sealed gear (Badar / 2023-05)
            if e_dict.get('sealed_gear', False):
                output['sealed_gear'] = e_dict['sealed_gear']

        return output


    def _get_timeline_year(self, target_ly=0):
        """ Accepts an int 'ly' and returns that LY's dictionary (as a copy). """

        for ly in self.settlement['timeline']:
            if int(ly['year']) == int(target_ly):
                return copy(ly)

        err = (
            '_get_timeline_year() error! Attempted to get LY %s, '
            'but could not find it in the settlement timeline! '
        )
        self.logger.error(err % target_ly)
        self.logger.error('Returning empty dictionary...')
        return {}


    def get_available_endeavors(self, return_total=True):
        """ Returns a list of endeavor handles based on campaign, innovations,
        locations, survivors and settlement events. """
        total = 0
        available = {
            'campaign': [],
            'innovations': [],
            'locations': [],
            'survivors': [],
            'settlement_events': [],
            'storage': [],
        }

        #
        #   Private method to check if an endeavor is possible
        #

        def get_eligible_endeavors(e_list):
            """ Returns a bool if the settlement can endeavor here. """

            eligible_endeavor_handles = []
            for e_handle in e_list:
                e_dict = self.Endeavors.get_asset(e_handle)
                eligible = True
                if e_dict.get('hide_if_location_exists', None) in self.settlement['locations']:
                    eligible = False
                elif e_dict.get('hide_if_innovation_exists',None) in self.settlement['innovations']:
                    eligible = False
                if e_dict.get('hide_if_settlement_attribute_exists', None) in self.settlement.keys():
                    eligible = False
                for req_inno in e_dict.get('requires_innovations', []):
#                    if req_inno not in self.settlement['innovations']:
                    if req_inno not in self.get_innovations(include_principles=True):
                        eligible = False
                if eligible:
                    eligible_endeavor_handles.append(e_handle)
            return eligible_endeavor_handles

        #
        #   all of these must be a list of dictionaries!
        #

        # campaign-specific
        if self.campaign.asset.get('endeavors', None) is not None:
            bogus_dict = {'name': self.campaign.name, 'endeavors': []}
            for e_handle in self.campaign.asset['endeavors']:
                bogus_dict['endeavors'].append(e_handle)
            available['campaign'].append(bogus_dict)

        # innovations and locations
        for a_list in ['innovations']:
            for a_dict in self.list_assets(a_list):
                if a_dict.get('endeavors', None) is not None:
                    eligible_endeavor_handles = get_eligible_endeavors(
                        a_dict['endeavors']
                    )
                    if len(eligible_endeavor_handles) >= 1:
                        a_dict['endeavors'] = eligible_endeavor_handles
                        available[a_list].append(a_dict)

        # locations - refactored 2021-11-05 for version support
        for location_handle in self.settlement['locations']:
            loc_dict = copy(self.Locations.get_asset(location_handle))
            eligible_endeavor_handles = get_eligible_endeavors(
                loc_dict.get('endeavors', [])
            )
            if len(eligible_endeavor_handles) >= 1:
                loc_dict['endeavors'] = eligible_endeavor_handles
                available['locations'].append(loc_dict)

        # storage
        for i_handle in self.settlement['storage']:
            i_obj = self.settlement_storage.item_handle_to_item_object(i_handle)
            if hasattr(i_obj, 'endeavors'):
                eligible_endeavor_handles = get_eligible_endeavors(i_obj.endeavors)
                if len(eligible_endeavor_handles) >= 1:
                    i_obj.endeavors = eligible_endeavor_handles
                    available['storage'].append(i_obj.serialize(dict))

        # check survivors
        survivor_endeavors = []
        for s in self.survivors:
            available_e = s.get_available_endeavors()
            if available_e != []:
                s_dict = s.synthesize()
                s_dict['endeavors'] = available_e
                survivor_endeavors.append(s_dict)
        available['survivors'] = survivor_endeavors

        # settlement events - crazy hacks here
        settlement_events = []
        current_ly = self._get_timeline_year(self.get_current_ly())
        events = current_ly.get('settlement_event', None)
        if events is not None:
            for event_dict in events:
                if event_dict.get('handle', None) is not None:
                    event_asset = self.Events.get_asset(event_dict['handle'])
                    if event_asset.get('endeavors',None) is not None:
                        eligible_endeavor_handles = get_eligible_endeavors(
                            event_asset['endeavors']
                        )
                        if len(eligible_endeavor_handles) >= 1:
                            event_asset['endeavors'] = eligible_endeavor_handles
                            available['settlement_events'].append(event_asset)
                else:
                    err = (
                        "%s Timeline event dictionary does not have a handle "
                        "key! Dict was: %s"
                    ) % (self, event_dict)
                    self.logger.warn(err)

        # return a tuple, if we're returning the total as well
        if return_total:
            for k in available.keys():
                for d in available[k]:
                    total += len(d.get('endeavors', []))
            return available, total

        return available


    def get_available_fighting_arts(
            self, exclude_dead_survivors=True, return_type=False
        ):
        """ This is meant to be used ONLY when doing things like checking to see
        what options the settlement has for its Inspirational Statue! This is
        NOT the same as checking compatibility!

        Use self.get_available_assets() for that type of stuff!

        Returns a uniqified list of farting art handles based on LIVING
        survivors unless otherwise specified with the 'exclude_dead_survivors'
        kwarg. """

        # 1.) create a set for live survivors and a set for dead survivors
        dead_survivors = set()
        live_survivors = set()
        for s in self.survivors:
            if s.is_dead():
                dead_survivors = dead_survivors.union(s.survivor['fighting_arts'])
            else:
                live_survivors = live_survivors.union(s.survivor['fighting_arts'])

        # 2.) if we're NOT excluding dead survivors, the final set is the union
        #   of both sets above; otherwise, its just the living survivors' set
        if not exclude_dead_survivors:
            fa_handles = dead_survivors.union(live_survivors)
        else:
            fa_handles = live_survivors

        # 3.) now, initialize our master set and remove the SFA's
        for fa_handle in fa_handles:
            fa_dict = self.FightingArts.get_asset(
                fa_handle,
                raise_exception_if_not_found=False
            )
            if fa_dict is not None and fa_dict.get('sub_type', None) == 'secret_fighting_art':
                fa_handles.remove

        # 4.) now create the output based on requested 'return_type'
        if return_type in [False, list]:
            return sorted(list(fa_handles))
        elif return_type == "JSON":
            output = []
            for fa_handle in sorted(fa_handles):
                fa_dict = self.FightingArts.get_asset(
                    fa_handle,
                    raise_exception_if_not_found=False
                )
                if fa_handle in dead_survivors and fa_handle not in live_survivors:
                    fa_dict['select_disabled'] = True
                output.append(fa_dict)
            return output

        # raise an exception for un-handled return type
        err = 'get_available_fighting_arts() does not support %s returns!'
        raise utils.InvalidUsage(err % return_type)


    def get_available_monster_volumes(self):
        """ Returns a list of strings that are eligible for addition to the
        settlement's self.settlement['monster_volumes'] list. """

        options = set()

        for m_name in self.settlement['defeated_monsters']:
            monster_obj = self.Monsters.init_asset_from_name(m_name)
            if hasattr(monster_obj, 'level'):
                line = '%s Vol. %s' % (monster_obj.name, monster_obj.level)
                options.add(line)

        for vol_string in self.get_monster_volumes():
            if vol_string in options:
                options.remove(vol_string)

        return sorted(list(options))


    def get_bonuses(self, return_type=None):
        """ Returns settlement and survivor bonuses according to 'return_type'.
        Supported types are:

            - dict (same as None/unspecified)
            - "JSON"

        The JSON type return is especially designed for front-end developers,
        and includes a pseudo-buff group called "all" that includes all buffs.
        Also, the JSON type return sorts by innovation name, which is nice.
        """

        output = {
            "settlement_buff": {},
            "survivor_buff": {},
            "departure_buff": {},
        }

        if return_type == "JSON":
            output = {
                "settlement_buff": [],
                "survivor_buff": [],
                "departure_buff": [],
                "all": [],
            }

        for handle,d in self.get_innovations(return_type=dict, include_principles=True).items():
            for k in d.keys():
                if k in output.keys():
                    if return_type == "JSON":
                        dict_repr = {"name": d["name"], "desc": d[k]}
                        output[k].append(dict_repr)
                        output["all"].append(dict_repr)
                    else:
                        output[k][handle] = d[k]


        # sort, if we're doing JSON, and save the UI guys the trouble
        if return_type == "JSON":
            for buff_group in output:
                output[buff_group] = sorted(output[buff_group], key=lambda k: k['name'])

        return output


    def get_death_count(self, return_type=int):
        """ By default this returns the settlement's total number of deaths as
        an int.

        This method can accept the following values for 'return_type':

            - int
            - "min"

        Setting return_type='min' will return the settlement's minimum death
        count, i.e. the number of survivors in the settlement with
        survivor["dead"] = True. """

        if return_type == "min":
            min_death_count = 0
            for s in self.survivors:
                if s.is_dead():
                    min_death_count += 1
            return min_death_count

        return self.settlement["death_count"]


    def get_endeavor_tokens(self):
        """ Returns settlement Endeavor Tokens as an int. Does some aggressive
        duck-typing to prevent legacy data model issues from fucking everything
        up and causing us to throw a 500. """

        try:
            return int(self.settlement["endeavor_tokens"])
        except:
            return 0


    def get_expansions(self, return_type=None):
        """ Returns a list of expansions if the 'return_type' kwarg is left
        unspecified.

        Otherwise, 'return_type' can be either 'dict' or 'comma_delimited'.

        Setting return_type="dict" gets a dictionary where expansion 'name'
        attributes are the keys and asset dictionaries are the values. """

        s_expansions = copy(self.settlement['expansions'])

        if return_type == dict:
            exp_dict = {}
            for exp_handle in s_expansions:
                exp_dict[exp_handle] = self.Expansions.get_asset(exp_handle)
            return exp_dict
        elif return_type == "comma-delimited":
            if s_expansions == []:
                return None
            else:
                return ", ".join(s_expansions)
        elif return_type in ['pretty', str]:
            output = []
            for e in s_expansions:
                output.append(
                    self.Expansions.get_asset(e)["name"]
                )
            return utils.list_to_pretty_string(output)

        return s_expansions


    def get_event_log(self, return_type=None, ly=None, lines=None,
            get_lines_after=None, survivor_id=None, query_sort=-1):

        """ Returns the settlement's event log as a cursor object unless told to
        do otherwise.

        Checks for a request and, if one exists, tries to search for lines after
        a certain time.
        """

        if flask.request and hasattr(self, 'params'):
            if 'lines' in self.params:
                lines = self.params['lines']
            if 'get_lines_after' in self.params:
                get_lines_after = self.params['get_lines_after']
            if 'survivor_id' in self.params:
                survivor_id = self.params['survivor_id']
            if 'ly' in self.params:
                ly = self.params['ly']

        query = {"settlement_id": self.settlement["_id"]}

        # modify the query, if we're doing that
        if get_lines_after is not None and ly is None:
            target_line = utils.mdb.settlement_events.find_one({'_id': ObjectId(get_lines_after)})
            query.update({"created_on": {'$gt': target_line['created_on']}})
        elif ly is not None and get_lines_after is None:
            query.update({'ly': int(ly)})

        if survivor_id is not None:
            query = {'survivor_id': ObjectId(survivor_id)}

        # now do the query
        event_log = utils.mdb.settlement_events.find(query).sort(
            "created_on", query_sort
            )

        # limit, if we're doing that
        if lines is not None:
            event_log.limit(lines)

        # process 'return_type' and wrap up
        if return_type=="JSON":
            return json.dumps(list(event_log),default=json_util.default)

        return list(event_log)


    def get_eligible_parents(self):
        """ Returns a dictionary with two lists of survivors who are able to do
        the mommy-daddy dance: one for male survivors and one for female
        survivors.

        This method uses methods of the Survivor class to assess preparedness to
        do the deed. Check those methods for more info on how survivors are
        assessed.

        Important! The lists only contain survivor names and OIDs (i.e. you do
        NOT get a fully serialized survivor back in this list. """

        eligible_parents = {"male":[], "female":[]}

        for S in self.survivors:
            if S.can_be_nominated_for_intimacy():
                s_dict = {
                    "name": S.survivor["name"],
                    "_id": S.survivor["_id"],
                    "oid_string": str(S.survivor["_id"]),
                }

                if S.get_sex() == "M":
                    eligible_parents["male"].append(s_dict)
                elif S.get_sex() == "F":
                    eligible_parents["female"].append(s_dict)

        return eligible_parents


    def get_founder(self):
        """ Helper method to rapidly get the mdb document of the settlement's
        creator/founder. """

        return utils.mdb.users.find_one({"_id": self.settlement["created_by"]})


    def get_game_asset_from_handle(self, handle):
        """ Returns an initialized GameAsset object or dies trying. """

        if handle in self.Gear.handles:
            return KingdomDeath.gear.Gear(
                handle, collection_obj=self.Gear
            )
        elif handle in self.Resources.handles:
            return KingdomDeath.resources.Resource(
                handle, collection_obj=self.Resources
            )

        raise LookupError('Unknown game asset handle: %s' % handle)


    def get_gear_lookup(self, organize_by="sub_type"):
        """ This is a sort of...meta-method that renders the settlement's Gear
        and resource options as JSON. """

        # initialize 
        all_gear = copy(self.Gear.assets)

        # set compatible gear list
        compatible_gear = []
        for k in all_gear.keys():
            if self.is_compatible(all_gear[k]):
                compatible_gear.append(all_gear[k])

        output = {}
        for handle in all_gear.keys():
            gear_dict = all_gear[handle]
            if self.is_compatible(gear_dict):
                org_key = gear_dict[organize_by]
                if org_key not in output.keys():
                    output[org_key] = []
                output[org_key].append(gear_dict)

        return json.dumps(compatible_gear, default=json_util.default)


    def get_innovations(self, return_type=None, include_principles=False):
        """ Returns self.settlement["innovations"] by default; specify 'dict' as
        the 'return_type' to get a dictionary back instead. """

        s_innovations = copy(self.settlement["innovations"])
        if include_principles:
            s_innovations.extend(self.settlement["principles"])

        if return_type == dict:
            output = {}
            for i_handle in s_innovations:
                i_dict = self.Innovations.get_asset(i_handle)
                if i_dict is not None:
                    output[i_handle] = i_dict
                else:
                    self.logger.error("Ignoring unknown Innovation handle '%s'!" % i_handle)
            return output

        return s_innovations


    def get_innovation_deck(self, return_type=False):
        """ Uses the settlement's current innovations to create an Innovation
        Deck, which, since it's a pure game asset, is returned as a list of
        names, rather than as an object or as handles, etc.

        Unlike other methods, this one accepts a 'debug' kwarg. This was intro-
        duced to help resolve issue #503, which was occurring in production and
        not in test.
        """

        debug = self.params.get('debug', False)
        if debug:
            self.logger.debug("%s get_innovation_deck() debug enabled!" % self)

        #
        #   This is a port of the legacy method, but this method combines every-
        #   thing that the legacy app did in like, three different places to be
        #   the ultimately, single/central source of truth
        #
        #   The general logic of this method is that we start with a huge list
        #   of all possible options and then filter it down to a baseline.
        #
        #   Once we've got that baseline, we check the individual innovations
        #   we've got left to see if we keep them in the deck. 


        if 'return_type' in self.params:
            return_type = self.params['return_type']

        #
        #   1.) baseline 'available' innovations
        #

        available = dict(
            self.get_available_assets(self.Innovations)["innovations"]
        )

        if debug:
            self.logger.debug(
                "%s available innovations: %s" % (self, available.keys())
            )

        # remove principles and ones we've already got
        for a in list(available.keys()):
            if a in self.settlement["innovations"]:
                del available[a]
                if debug:
                    self.logger.debug("%s already has '%s' innovation!" % (self, a))
            if self.Innovations.get_asset(a).get("sub_type", None) == "principle":
                del available[a]
                if debug:
                    msg = "%s removed '%s' principle from available innovations"
                    self.logger.debug("msg" % (self, a))

        if debug:
            self.logger.debug("%s available innovations AFTER removing principles and assets in the settlement's list: %s" % (self, available.keys()))


        #
        #   2.) now, create a list of consequences (handles) from innovations
        #

        # consequences are a set until we need to sort them!
        consequences = set()
        for i_handle in self.settlement["innovations"]:
            cur_asset = self.Innovations.get_asset(i_handle)
            cur_asset_consequences = cur_asset.get("consequences", [])
            if debug:
                self.logger.debug("%s adding '%s' consequences: %s" % (self, i_handle, cur_asset_consequences))
            consequences = consequences.union(cur_asset_consequences)

        # now change from set to list and sort
        consequences = sorted(list(consequences))
        if debug:
            self.logger.debug("%s ALL consequences: %s" % (self, consequences))


        # now, remove all consequences that aren't available; this upgrades the
        #   'consequences' to 'available consequences', if you think about it
        for c in consequences:
            if c not in available.keys():
                consequences.remove(c)
                if debug:
                    self.logger.debug("%s removing UNAVAILABLE consequence: '%s'" % (self, c))

        # if we're debugging, list our current consequences and check the list
        # for any unavailable consequences that the previous iteration might
        # have mysteriously spared
        if debug:
            self.logger.debug("%s consequences after removing all UNAVAILABLE consequences: %s" % (self, consequences))
            for c in consequences:
                if c not in available.keys():
                    self.logger.error("%s consequences list includes UNAVAILABLE consequence '%s'" % (self, c))

        # 
        #   3.) initialize the deck dict using 'available consequences' (see
        #       above); now we have a proper deck to work with
        #
        deck_dict = {}
        for c in consequences:
            if c not in self.settlement["innovations"] and c in available.keys():
                asset_dict = self.Innovations.get_asset(c)
                deck_dict[c] = asset_dict

        if debug:
            self.logger.debug("%s deck dict initialized based on AVAILABLE consequences: %s" % (self, deck_dict.keys()))

        #
        #   4.) now iterate through remaining 'available' assets and give them
        #       a 'last chance' (i.e. see if we want them, even though they're
        #       not consequences)
        #

        for i_handle, i_dict in available.items():
            if i_dict.get("available_if", None) is not None:
                for tup in i_dict['available_if']:
                    asset, collection = tup
                    if asset in self.settlement[collection]:
                        deck_dict[i_handle] = i_dict
                        self.logger.debug("%s Found value '%s' in settlement['%s']. Adding '%s' to innovation deck." % (self, asset, collection, i_dict['name']))

        #
        #   sanity/QA check on the way out
        #

        for c in deck_dict.keys():
            if c not in available.keys():
                self.logger.error("%s Unavailable consequence '%s' present in innovation deck!" % (self, c))


        #
        #   5.) now that we have a deck, make a sorted list version of it
        #
        deck_list = []
        for k in sorted(deck_dict.keys()):
            deck_list.append(deck_dict[k]["name"])
        deck_list = sorted(deck_list)

        #
        #   6.) optional dict-style return; requires 'consequences' cleanup
        #

        if return_type in ['dict', dict]:

            output = collections.OrderedDict()

            sorting_hat = {}
            for k, v in deck_dict.items():
                sorting_hat[v['name']] = k

            for i_name in sorted(sorting_hat.keys()):
                i_dict = deepcopy(deck_dict[sorting_hat[i_name]])
                for c_handle in i_dict.get('consequences', []):
                    consequences_dict = self.Innovations.get_asset(c_handle)
                    if not self.is_compatible(consequences_dict):
                        i_dict['consequences'].remove(c_handle)
                output[i_dict['handle']] = i_dict

            return json.dumps(output)

        #   Default return (i.e. dump the list of strings)
        return json.dumps(deck_list)



    def get_lantern_research_level(self):
        """ Returns self.settlement['lantern_resarch_level']. Always an int."""

        return self.settlement.get('lantern_research_level', 0)


    def get_latest_defeated_monster(self):
        """ Tries to get the last handle in the defeated monsters list. Returns
        None if there is no such thing. """

        try:
            return self.settlement['defeated_monsters'][-1]
        except:
            return None


    def get_latest_milestone(self):
        """ Tries to get the last handle in the milestones list. Returns None if
        there is no such thing. """

        try:
            return self.settlement['milestone_story_events'][-1]
        except:
            return None


    def get_latest_survivor(self, category='dead'):
        """ Gets the latest survivor, based on the 'category' kwarg value. """

        if category == 'dead':
            s = utils.mdb.survivors.find({'dead': True}).sort('died_on')
            if s.count() >= 1:
                return s[0]
        elif category == 'born':
            s = utils.mdb.survivors.find({'born_in_ly': {'$exists': True}}).sort('created_on')
            if s.count() >= 1:
                return s[0]

        return None


    def get_monster_volumes(self):
        """ Returns the settlement's self.settlement['monster_volumes'] list,
        which is a list of unique strings. """

        return self.settlement.get('monster_volumes', [])
    def get_parents(self):
        """ Returns a list of survivor couplings, based on the 'father'/'mother'
        attributes of all survivors in the settlement. """

        couples = {}
        for s in self.get_survivors(list):
            if 'father' in s.keys() and 'mother' in s.keys():
                couple_id = "%s+%s" %(str(s['father']), str(s['mother']))
                couple = {'father': s['father'], 'mother': s['mother']}
                if couples.get(couple_id, None) is None:
                    couples[couple_id] = {'father': s['father'], 'mother': s['mother'], 'children': []}
                couples[couple_id]['children'].append(s['_id'])

        output = []
        for c in couples.keys():
            output.append(couples[c])

        return output


    def get_population(self, return_type=int):
        """ By default, this returns settlement["population"] as an int. Use the
        'return_type' kwarg to get different returns:

            - "min" -> returns the minimum population based on living survivors
            - "sex" -> returns a dictionary of M/F survivor counts

        """

        if return_type == "min":
            min_pop = 0
            for s in self.survivors:
                if not s.is_dead():
                    min_pop += 1
            return min_pop
        elif return_type == 'sex':
            output = {'M':0, 'F':0}
            for s in self.survivors:
                if not s.is_dead():
                    output[s.get_sex()] += 1
            return output

        return int(self.settlement["population"])


    def get_settlement_notes(self):
        """ Returns a list of mdb.settlement_notes documents for the settlement.
        They're sorted in reverse chronological, because the idea is that you're
        goign to turn this list into JSON and then use it in the webapp. """

        notes = utils.mdb.settlement_notes.find(
            {"settlement": self.settlement["_id"]}
        ).sort("created_on",-1)
        if notes is None:
            return []
        return [n for n in notes]


    def get_settlement_storage(self, include_rollups=False):
        """ Returns a JSON-ish representation of settlement storage, meant to
        facilitate front-end design.

        We're basically constructing a data structure/schema here, so it gets a
        little messy.
        """

        # get available storage locations into a dictionary of dicts
        storage_repr = self.get_available_assets(self.Storage)['storage']

        # now update the dictionaries in the big dict to have a new key
        # called 'inventory' where we will park asset handles
        for loc_key, loc_asset in storage_repr.items():

            # add COMPATIBLE item dicts to the locations 'assets' list
            self.settlement_storage.add_location(location=loc_asset)
            for item_obj in self.settlement_storage.locations[loc_key]['assets']:
                if self.is_compatible(item_obj.asset):
                    self.settlement_storage.add_item_to_storage(
                        handle = item_obj.handle,
                        quantity = self.settlement['storage'].count(
                            item_obj.handle
                        )
                    )
            del self.settlement_storage.locations[loc_key]['assets'] # can't serialize
            storage_repr[loc_key] = self.settlement_storage.locations[loc_key]


        # first thing we do is sort all handles from settlement storage into our
        # 'inventory' lists
        for item_handle in sorted(self.settlement['storage']):

            # first, get  an object and make sure it's a modern on (not legacy)
            item_obj = self.settlement_storage.item_handle_to_item_object(item_handle)
            item_type = item_obj.asset.get('sub_type', None)
            if item_type is None or not hasattr(item_obj, 'asset'):
                err = '%s item has no sub_type. Was legacy init used?'
                raise AttributeError(err % (item_obj))

            if item_type in storage_repr.keys():
                storage_repr[item_type]['inventory'].append(item_handle)
                if item_handle in storage_repr[item_type]['digest'].keys():
                   storage_repr[item_type]['digest'][item_handle]['count'] += 1
                else:
                    storage_repr[item_type]['digest'][item_handle] = {
                        'count': 1,
                        'name': item_obj.name,
                        'handle': item_obj.handle,
                        'desc': item_obj.asset['desc'],
                        'keywords': item_obj.asset['keywords'],
                        'rules': item_obj.asset.get('rules', []),
                    }


        # now turn the digest dict into a list of dicts for easy iteration
        for k in storage_repr.keys():
            orig_digest = copy(storage_repr[k]['digest'])
            storage_repr[k]['digest'] = []
            for key, value in orig_digest.items():
                storage_repr[k]['digest'].append(value)


        #
        #   POST PROCESS
        #
        gear_dict = {
            'storage_type': 'gear',
            'name': 'Gear',
            'locations': [],
        }
        reso_dict = {
            'storage_type': 'resources',
            'name': 'Resource',
            'locations': [],
        }

        #finally, package up our main dicts for export as JSON
        if include_rollups:

            g_kw, g_rules, g_total = self.get_settlement_storage_rollup(
                'gear', 'all'
            )
            gear_dict['keywords'] = g_kw
            gear_dict['rules'] = g_rules
            gear_dict['total'] = g_total

            r_kw, r_rules, r_total = self.get_settlement_storage_rollup(
                'resources', 'all'
            )
            reso_dict['keywords'] = r_kw
            reso_dict['rules'] = r_rules
            reso_dict['total'] = r_total


        # look through all dictionaries in strorage_repr(esentation) and make
        # each into a member of the 'locations' list for the appropriate
        # outbound dict
        for loc_key in storage_repr:
            if storage_repr[loc_key]['sub_type'] == 'gear':
                gear_dict['locations'].append(storage_repr[loc_key])
            if storage_repr[loc_key]['sub_type'] == 'resources':
                reso_dict['locations'].append(storage_repr[loc_key])

        return json.dumps([reso_dict, gear_dict])


    def get_settlement_storage_rollup(self, asset_type=None, rollup_type=None):
        """ Returns a rollup dictionary (or count) based on 'asset_type' and
        'rollup_type':

            - asset_type = 'gear'
            - asset_type = 'resources'

            - rollup_type = 'keywords'      -- returns a dict
            - rollup_type = 'resources'     -- returns a dict
            - rollup_type = 'total'         -- returns an int

            - rollup_type = 'all'           -- gets all three as a tuple

        Finally, leave both kwargs set to None to get everything back as JSON.

        """

        # start the tallies
        gear_count = 0
        resources_count = 0

        gear_kw_list = []
        resources_kw_list = []
        gear_rules_list = []
        resources_rules_list = []

        for handle in set(self.settlement['storage']):
            item_count = self.settlement['storage'].count(handle)
            item_obj = self.get_game_asset_from_handle(handle)

            if item_obj.asset['type'] == 'gear':
                gear_count += item_count
                gear_kw_list.extend(item_obj.asset['keywords'])
            elif item_obj.asset['type'] == 'resources':
                resources_count += item_count
                resources_kw_list.extend(item_obj.asset['keywords'])


        def list_to_rollup(input_list):
            """ private convenience/DRYness method for making a rollup dict"""
            output = collections.OrderedDict()
            for item in sorted(input_list):
                output[item] = input_list.count(item)
            return output

        if asset_type == 'gear' and rollup_type == 'total':
            return gear_count
        elif asset_type == 'resources' and rollup_type == 'total':
            return resources_count
        elif asset_type == 'gear' and rollup_type == 'keywords':
            return list_to_rollup(gear_kw_list)
        elif asset_type == 'gear' and rollup_type == 'rules':
            return list_to_rollup(gear_rules_list)
        elif asset_type == 'gear' and rollup_type == 'all':
            return (
                list_to_rollup(gear_kw_list),
                list_to_rollup(gear_rules_list),
                gear_count
            )
        elif asset_type == 'resources' and rollup_type == 'keywords':
            return list_to_rollup(resources_kw_list)
        elif asset_type == 'resources' and rollup_type == 'rules':
            return list_to_rollup(resources_rules_list)
        elif asset_type == 'resources' and rollup_type == 'all':
            return (
                list_to_rollup(resources_kw_list),
                list_to_rollup(resources_rules_list),
                resources_count
            )

        # finall, if no kwargs, return everything:
        output = {
            'gear': {
                'keywords': list_to_rollup(gear_kw_list),
                'rules': list_to_rollup(gear_rules_list),
                'total': gear_count
            },
            'resources': {
                'keywords': list_to_rollup(resources_kw_list),
                'rules': list_to_rollup(resources_rules_list),
                'total': resources_count
            },
        }
        return json.dumps(output)


    def get_survivor_special_attributes(self):
        """ Special Attributes are ones that are unique to a campaign or to an
        expansion (so far). These are basically booleans that we set on the
        Survivor sheet. """

        output = []
        for h in self.campaign.asset.get('survivor_special_attributes', []):
            output.append(self.SpecialAttributes.get_asset(h))
        return output


    def get_survivors(self, return_type=None, excluded=[], exclude_dead=False):
        """ This method is the ONE AND ONLY exception to the Settlement Object
        rule about never initializing survivors. This is the ONE AND ONLY place
        that suvivors are ever initialized by this class/object.

        Use the following 'return_type' kwargs to control output:

            - 'departing' -> returns a list of survivor dictionaries where all
                the survivors have self.is_departing==True
            - 'groups' -> this should only be used by Campaign Summary type
                views. It returns a specialized dictionary of survivor info that
                is JSON-ish and meant to be used by front-end.

        The default output (i.e. no 'return_type') is a list of survivior
        dictionaries.

        Use the 'excluded' and 'exclude_dead' kwargs to control default output.
        """

        if return_type == 'initialize':
            err = "This method no longer supports the 'initialize' return type!"
            raise utils.InvalidUsage(err)

        # now make a copy of self.survivors and work it to fulfill the request
        output_list = copy(self.survivors)

        # do filters
        for survivor in output_list:
            if exclude_dead and survivor.is_dead() and survivor in output_list:
                output_list.remove(survivor)
            if (
                excluded != [] and survivor._id in excluded and
                survivor in output_list
            ):
                output_list.remove(survivor)


        #
        #   returns
        #

        if return_type == 'oid_strings':
            return [str(survivor._id) for survivor in output_list]

        if return_type == 'departing':
            return [s.synthesize() for s in output_list if s.is_departing()]

        if return_type == 'groups':
            # This is where we do the whole dance of organizing survivors for
            # the Campaign Summary. This is a LOOSE port of the legacy app
            # version of this method, and skips...a lot of its BS.

            groups = {
                'departing': {
                    'name': 'Departing',
                    'bgcolor': '#FFF',
                    'color': '#000',
                    'title_tip': 'Survivors in this group are currently <b>Departing</b> for a Showdown.',
                    'sort_order': '0',
                    'survivors': [],
                },
                'favorite':  {
                    'name': 'Favorite',
                    'title_tip': 'Survivors in this group are your favorite survivors.',
                    'sort_order': '1',
                    'survivors': []
                },
                'available': {
                    'name': 'Available',
                    'bgcolor': '#FFF',
                    'color': '#000',
                    'title_tip': 'Survivors in this group are currently in the Settlement and available to <b>Depart</b> or to participate in <b>Endeavors</b>.',
                    'sort_order': '2',
                    'survivors': [],
                },
                'skip_next': {'name': 'Skipping Next Hunt', 'sort_order': '3', 'survivors': []},
                'retired':   {'name': 'Retired', 'sort_order': '4', 'survivors': []},
                'the_dead':  {
                    'name': 'The Dead',
                    'bgcolor': '#FFF',
                    'color': '#000',
                    'title_tip': 'Dead survivors are memorialized here.',
                    'sort_order': '5',
                    'survivors': [],
                },
            }

            for s in output_list:
                if s.survivor.get('departing', None) == True:
                    groups['departing']['survivors'].append(s.synthesize())
                elif s.survivor.get('dead', None) == True:
                    groups['the_dead']['survivors'].append(s.synthesize())
                elif s.survivor.get('retired', None) == True:
                    groups['retired']['survivors'].append(s.synthesize())
                elif s.survivor.get('skip_next_hunt', None) == True:
                    groups['skip_next']['survivors'].append(s.synthesize())
                elif 'favorite' in s.survivor.keys() and flask.request.User.login in s.survivor['favorite']:
                    groups['favorite']['survivors'].append(s.synthesize())
                else:
                    groups['available']['survivors'].append(s.synthesize())

            # make it JSON-ish
            output = []
            for k in sorted(groups.keys(), key=lambda k: groups[k]['sort_order']):
                groups[k]['handle'] = k
                output.append(groups[k])
            return output

        # default return; assumes that we want a list of dictionaries
        return [s.synthesize() for s in output_list]


    def get_survival_actions(self, return_type=dict):
        """ Returns a dictionary of survival actions available to survivors
        based on campaign type. Individual SAs are either 'available' or not,
        depending on whether they're unlocked. """


        # first, build the master dict based on the campaign def
        sa_dict = {}
        sa_handles = self.campaign.asset['survival_actions']
        for handle in sa_handles:
            sa_dict[handle] = self.SurvivalActions.get_asset(handle)

        # set innovations to unavailable if their availablility is not defined
        # already within their definition:
        for k in sa_dict.keys():
            if not "available" in sa_dict[k]:
                sa_dict[k]["available"] = False
                sa_dict[k]["title_tip"] = "'%s' has not been unlocked yet." % sa_dict[k]["name"]

        # second, udpate the master list to say which are available
        for k, v in self.get_innovations(dict).items():
            innovation_sa = v.get("survival_action", None)
            if innovation_sa in sa_dict.keys():
                sa_dict[innovation_sa]["available"] = True
                sa_dict[innovation_sa]["title_tip"] = "Settlement innovation '%s' unlocks this ability." % v["name"]

        # support a JSON return type:
        if return_type=="JSON":
            j_out = []
            for sa_key in sa_dict.keys():
                j_out.append(sa_dict[sa_key])
            return sorted(j_out, key=lambda k: k['sort_order'])

        # dict return
        return sa_dict


    def get_survival_limit(self, return_type=int):
        """ By default, this returns the settlement's Survival Limit as an
        integer.

        This method accepts the following values for 'return_type':
            - int (default)
            - bool
            - 'min'

        Setting the 'return_type' kwarg to bool when calling this method will
        return a boolean representing whether the settlement is enforcing the
        survival limit (based on expansions, etc.).

        Setting 'return_type' to "min" will return the minimum possible value
        that the settlement's Survival Limit may be set to.
        """

        if return_type == bool:
            for e_dict in self.list_assets("expansions"):
                if not e_dict.get("enforce_survival_limit", True):
                    return False
            return True

        if return_type == 'min':

            minimum = 1

            # process innovations
            for i_dict in self.list_assets("innovations"):
                minimum += i_dict.get("survival_limit", 0)

            # process principles (separately)
            for p in self.settlement["principles"]:
                p_dict = self.Innovations.get_asset(p)
                minimum += p_dict.get("survival_limit", 0)

            return minimum

        return int(self.settlement["survival_limit"])


    def get_timeline(self, return_type=None):
        """ Returns the timeline. """

        timeline = self.settlement['timeline']

        if return_type=="JSON":
            return json.dumps(timeline, default=json_util.default)

        return timeline


    def get_version(self, return_type=object):
        """ Returns the version object. """

        # get it, fail back to earliest vers as a default:
        version_str = self.settlement.get('version', 'core_1_3')
        version_object = self.Versions.get_asset(version_str)

        # handle 'return_type' kwarg
        if return_type == str:
            return version_object['handle']

        return version_object


    def get_special_rules(self):
        """ Assets that can have special rules (so far) are these:

            - Campaign
            - Expansions
            - Locations

        This method checks all assets belonging to the settlement and returns a
        set of special rules dictionaries.
        """

        output = []

        # campaign
        if self.campaign.asset.get('special_rules', None) is not None:
            for r in self.campaign.asset['special_rules']:
                output.append(r)

        # expansions and locations
        for a_list in ['expansions','locations']:
            for a_dict in self.list_assets(a_list):
                if a_dict.get('special_rules', None) is not None:
                    for r in a_dict['special_rules']:
                        output.append(r)

        return list(output)


    def _get_endgame_showdowns(self):
        ''' Returns a list of the so-called 'endgame' showdowns, i.e. core and
        finale type monsters for the campaign. '''

        output = []

        for m_type in ['core_monster', 'finale_monster']:
            if self.campaign.asset.get(m_type, None) is not None:
                output.append(self.campaign.asset[m_type])

        return output



    def _get_special_showdowns(self):
        """ Returns a list of monster handles representing the available special
        showdown monsters, given campaign and expansion assets. """

        output = []

        if "special_showdowns" in self.campaign.asset:
            output.extend(self.campaign.asset["special_showdowns"])

        for exp in self.get_expansions(dict).keys():
            e_dict = self.get_expansions(dict)[exp]
            if "special_showdowns" in e_dict.keys():
                output.extend(e_dict["special_showdowns"])

        return list(set(output))




    @web_method
    def rm_player(self):
        """ Expects a request with the param 'login'. Iterates all survivor
        records for the settlement and swaps 'login' for the settlement's
        creator. """

        self.check_request_params(['login'])
        player_login = self.params["login"]

        founder = self.get_founder()

        self.log_event("Removed %s from the settlement." % player_login)

        for survivor_obj in self.survivors:
            if survivor_obj.survivor.get('email', None) == player_login:
                survivor_obj.set_email(founder['login'])



    #
    #   Update methods; these should ONLY be internal non-web methods
    #

    def update_all_survivors(self, operation=None, attrib_dict={}, exclude_dead=False):
        """ Performs bulk operations on all survivors. Use 'operation' kwarg to
        either 'increment' or 'decrement' all attributes in 'attrib_dict'.

        'attrib_dict' should look like this:

        {
            'Strength': 1,
            'Courage': 1,
            'abilities_and_impairments': ['sword_specialization', 'ageless'],
        }

        The 'increment' or 'decrement' values call the corresponding methods
        on the survivors.
        """

        if operation not in ['set', 'increment', 'decrement']:
            err = "update_all_survivors() cannot process '%s' operations!"
            self.logger.exception(err, operation)
            raise utils.InvalidUsage(err % operation)

        for s in self.survivors:
            if exclude_dead and s.is_dead():
                pass
            else:
                for attribute, modifier in attrib_dict.items():
                    if operation == 'increment':
                        if attribute == 'abilities_and_impairments':
                            for ai_handle in modifier:  # 'modifier' is a list here
                                s.add_game_asset('abilities_and_impairments', ai_handle)
                        else:
                            s.update_attribute(attribute, modifier)
                    elif operation == 'decrement':
                        if attribute == 'abilities_and_impairments':
                            for ai_handle in modifier:  # 'modifier' is a list here
                                s.rm_game_asset('abilities_and_impairments', ai_handle)
                        else:
                            s.update_attribute(attribute, -modifier)
                    elif operation == 'set':
                        s.set_attribute(attribute, modifier)


    @web_method
    def update_attribute(self):
        """ Assumes a request context and looks for 'attribute' and 'modifier'
        keys in self.params. Uses them to increment (literally adds) the current
        self.settlement[attribute] value.

        Since this method only supports integers, non-existing attributes are
        assumed/defaulted to zero!
        """

        self.check_request_params(['attribute','modifier'])
        attribute = self.params["attribute"]
        modifier = self.params["modifier"]

        # default non-existing attributes to zero and update
        new_value = self.settlement.get(attribute, 0) + modifier
        self.settlement[attribute] = new_value

        # now log it as a settlement event
        attribute_pretty = attribute.title().replace('_',' ')
        msg = "%s updated settlement %s to %s"
        self.log_event(
            msg % (
                flask.request.User.login,
                attribute_pretty,
                self.settlement[attribute]
            )
        )

        # save
        self.save()


    @web_method
    def update_endeavor_tokens(self, modifier=0, save=True):
        """ Updates settlement["endeavor_tokens"] by taking the current value,
        which is normalized (above) to zero, if it is not defined or set, and
        adding 'modifier' to it.

        To increment ETs, do 'modifier=1'; to decrement, do 'modifier=-1'.
        """

        if "modifier" in self.params:
            modifier = self.params["modifier"]

        new_val = self.get_endeavor_tokens() + int(modifier)
        if new_val < 0:
            new_val = 0
        self.settlement["endeavor_tokens"] = new_val
        msg = "%s set endeavor tokens to %s"
        self.log_event(msg % (flask.request.User.login, new_val))

        if save:
            self.save()


    @web_method
    def update_nemesis_levels(self):
        """ Updates a settlement's 'nemesis_encounters' array/list for a nemesis
        monster handle. Fails if the nemesis is not in the settlement's nemesis
        list (this is intentionall and for your safety/sanity). """

        self.check_request_params(["handle", "levels"])
        handle = self.params["handle"]
        levels = list(self.params["levels"])

        m_dict = self.Monsters.get_asset(handle)

        # die if the nemesis hasn't  been added to the settlement yet
        if handle not in self.settlement["nemesis_monsters"]:
            err = "Nemesis handle '%s' is not in the 'nemesis_monsters' list!"
            self.logger.error(err, handle)
            raise utils.InvalidUsage(err)

        # if we're still here, do it / log it
        self.settlement["nemesis_encounters"][handle] = levels
        self.log_event('%s updated %s encounters to include %s' % (
            flask.request.User.login,
            m_dict["name"],
            utils.list_to_pretty_string(levels)
            )
        )
        self.save()


    def update_population(self, modifier=None):
        """ Updates settlement["population"] by adding 'modifier' to it. Will
        never go below zero."""

        if modifier is None:
            self.check_request_params(["modifier"])
            modifier = self.params["modifier"]

        current = self.settlement["population"]
        new = current + modifier

        if new < 0:
            new = 0

        self.settlement["population"] = new

        msg = "%s updated settlement population to %s"
        self.log_event(
            msg % (flask.request.User.login, self.settlement["population"])
        )
        self.save()


    @web_method
    def update_survivors(self, include=None, attribute=None, modifier=None):
        """ This method assumes a request context and should not be called from
        outside of a request.

        Use this to modify a single attribute for one of the following groups of
        survivors:

            'departing': All survivors with 'departing': True

        NB: this is a waaaaaaay different method from update_all_survivors(), so
        make sure you know the difference between the two. """

        # initialize; assume a request context
        if include is None:
            self.check_request_params(['include', 'attribute', 'modifier'])
            include = self.params['include']
            attribute = self.params['attribute']
            modifier = self.params['modifier']

        # now check the include and get our targets
        target_group = []
        if include == 'departing':
            target_group = utils.mdb.survivors.find(
                {
                    'settlement': self.settlement['_id'],
                    'departing': True,
                    'dead': {'$exists': False}
                }
            )
        else:
            err = "update_survivors() cannot process the 'include' value '%s'"
            raise InvalidUsage(err % include)

        # now initialize survivors and update them with update_attribute()
        for survivor in target_group:
            survivor_obj = Survivor(_id=survivor['_id'], Settlement=self)
            survivor_obj.update_attribute(attribute, modifier)



    #
    #   bug fix, conversion and migration functions start here!
    #

    def baseline(self):
        """ This checks the mdb document to make sure that it has basic aux-
        iliary and supplemental attribute keys. If it doesn't have them, they
        get added and we set self.perform_save = True. """


        #
        #   general data model 
        #

        if not "endeavor_tokens" in self.settlement.keys():
            self.settlement["endeavor_tokens"] = 0
            self.perform_save = True

        # data model - required lists
        for req_list in ['nemesis_monsters','quarries','strain_milestones', 'patterns']:
            if not req_list in self.settlement.keys():
                self.settlement[req_list] = []
                self.perform_save = True

        # data model - required dictionaries
        for req_dict in ['nemesis_encounters','innovation_levels','location_levels']:
            if not req_dict in self.settlement.keys():
                self.settlement[req_dict] = {}
                self.perform_save = True

        # make sure we have a version; the lowest 'version' we support is
        #   'core_1_5', so set that as the default; if the settlement has
        #   a 'rules' key, normalize it to 'version'
        if not "version" in self.settlement.keys():
            self.logger.info("Creating 'rules' key for %s", self)
            self.settlement["rules"] = 'core_1_5'
            self.perform_save = True

        if 'rules' in self.settlement.keys():
            self.logger.info("Converting 'rules' key for %s", self)
            self.settlement['version'] = self.settlement['rules']
            del self.settlement['rules']
            self.perform_save = True


        #
        #   updates/changes/fixes to assets
        #

        if "white_box" in self.settlement['expansions']:
            wb_index = self.settlement['expansions'].index('white_box')
            self.settlement['expansions'].insert(wb_index, 'promo')
            self.settlement['expansions'].remove('white_box')
            self.logger.warning("Converted 'white_box' expansion to 'promo'.")
            self.perform_save=True

        #
        #   This is where we add the 'meta' element; note that we actually
        #   convert from the old/initial implementation of 'meta' in this code
        #

        if not "meta" in self.settlement.keys():
            self.logger.info("Creating 'meta' key for %s", self)
            self.settlement["meta"] = {}
            for meta_key in [
                "timeline_version", "monsters_version","expansions_version"
            ]:
                if meta_key in self.settlement:
                    self.settlement["meta"][meta_key] = self.settlement[meta_key]
                    del self.settlement[meta_key]
                    msg = "Moved meta key '%s' to settlement 'meta' dict for %s"
                    self.logger.info(msg, meta_key, self)
            self.perform_save = True

        if not "admins" in self.settlement.keys():
            self.logger.info("Creating 'admins' key for %s", self)
            creator = utils.mdb.users.find_one(
                {"_id": self.settlement["created_by"]}
            )
            self.settlement["admins"] = [creator["login"]]
            self.perform_save = True

        founder = self.get_founder()
        if not founder["login"] in self.settlement["admins"]:
            self.settlement["admins"].append(founder["login"])
            msg = "Adding founder '%s' to %s admins list."
            self.logger.debug(msg, founder["login"], self)
            self.perform_save = True

        if not "expansions" in self.settlement.keys():
            self.logger.info("Creating 'expansions' key for %s", self)
            self.settlement["expansions"] = []
            self.perform_save = True


        # Duck Typing!

        for attrib in ['survival_limit', 'population', 'death_count']:
            try:
                self.settlement[attrib] = int(self.settlement[attrib])
            except TypeError:
                err = 'Illegal %s value: %s! Resetting to zero!'
                self.log_event(err % (attrib, self.settlement[attrib]))
                self.settlement[attrib] = 0
                self.perform_save = True


    def bug_fixes(self):
        """ In which we burn CPU cycles to fix our mistakes. """

        # 2018-03-23 - storage handles with apostrophes
        for i in self.settlement['storage']:
            item_index = self.settlement['storage'].index(i)
            if i == "manhunter's_hat":
                self.settlement['storage'].remove(i)
                self.settlement['storage'].insert(item_index, 'manhunters_hat')
                self.logger.warning("%s BUG FIX: changed %s to 'manhunters_hat'" % (self,i))
                self.perform_save = True
            elif i == "hunter's_heart":
                self.settlement['storage'].remove(i)
                self.settlement['storage'].insert(item_index, 'hunters_heart')
                self.logger.warning("%s BUG FIX: changed %s to 'hunters_heart'" % (self,i))
                self.perform_save = True
            elif i == "jack_o'_lantern":
                self.settlement['storage'].remove(i)
                self.settlement['storage'].insert(item_index, 'jack_o_lantern')
                warn = "%s BUG FIX: changed %s to 'jack_o_lantern'"
                self.logger.warning(warn, self, i)
                self.perform_save = True

        # 2018-03-20 - missing timeline bug
        if self.settlement.get('timeline', None) is None:
            err = "%s has no Timeline! Initializing Timeline..."
            self.logger.error(err, self)
            self.initialize_timeline()

        # 2017-12-16 - principles in the innovations list
        for i in self.list_assets('innovations'):
            if i.get('sub_type', None) == 'principle':
                self.settlement['innovations'].remove(i['handle'])
                warn  = "%s Removed principle '%s' from innovations list!"
                self.logger.warning(warn, self, i['name'])

        # 2017-10-05 - missing settlement attrib
        if self.settlement.get("expansions", None) is None:
            self.settlement["expansions"] = []
            self.perform_save = True


    def convert_timeline_quarry_events(self):
        """ Takes a 1.0 timeline and converts its "quarry_events" to
        "showdown_events", making it 1.1. """

        new_timeline = []
        for y in self.settlement["timeline"]:
            for event_key in y.keys():
                if event_key == "quarry_event":
                    y["showdown_event"] = y[event_key]
                    del y[event_key]
            new_timeline.append(y)

        self.settlement["timeline"] = new_timeline
        self.settlement["meta"]["timeline_version"] = 1.1
        self.logger.warning("Migrated %s timeline to version 1.1", self)


    def flatten_timeline_events(self):
        """ Takes a 1.1 timeline and un-expands detailed dictionary info."""

        new_timeline = []
        for orig_year in self.settlement['timeline']:
            new_year = {}
            for event_group in orig_year.keys():
                if event_group != 'year':
                    new_event_group = []
                    try:
                        for event in orig_year[event_group]:
                            # if we have a 'name' and not a 'handle', prefer it
                            if (
                                event.get('name', None) is not None and
                                event.get('handle', None) is None
                            ):
                                new_event_group.append(event)
                            else:
                                new_event_group.append(
                                    {'handle': event['handle']}
                                )
                        new_year[event_group] = new_event_group
                    except KeyError as error:
                        msg = 'Timeline event could not be migrated! %s' % event
                        self.logger.exception(error)
                        self.logger.error(msg)
                else:
                    new_year['year'] = orig_year['year']
            new_timeline.append(new_year)

        self.settlement["timeline"] = new_timeline
        self.settlement["meta"]["timeline_version"] = 1.2
        self.logger.warning("Migrated %s timeline to version 1.2", self)


    def enforce_minimums(self):
        """ Enforces settlement minimums for Survival Limit, Death Count, etc.
        """

        # TK this isn't very DRY; could probably use some optimization

        min_sl = self.get_survival_limit("min")
        if self.settlement["survival_limit"] < min_sl:
            self.settlement["survival_limit"] = min_sl
            self.log_event(
                "Survival Limit automatically increased to %s" % min_sl,
                event_type="sysadmin"
            )
            self.perform_save = True

        min_pop = self.get_population("min")
        if self.settlement["population"] < min_pop:
            self.settlement["population"] = min_pop
            self.log_event(
                "Population automatically increased to %s" % min_pop,
                event_type="sysadmin"
            )
            self.perform_save = True

        min_death_count = self.get_death_count("min")
        if self.settlement["death_count"] < min_death_count:
            self.settlement["death_count"] = min_death_count
            self.log_event(
                "Death Count automatically increased to %s" % min_death_count,
                event_type="sysadmin"
            )
            self.perform_save = True



    #
    #   DEPRECATED
    #

    @web_method
    @deprecated
    def add_admin(self):
        """ DEPRECATED. Use add_settlement_admin_instead. """
        self.add_settlement_admin()

    @web_method
    @deprecated
    def rm_admin(self):
        """ DEPRECATED. Use add_settlement_admin_instead. """
        self.rm_settlement_admin()

    @web_method
    @deprecated
    def rm_note(self):
        """ DEPRECATED. Use add_settlement_admin_instead. """
        self.rm_settlement_note()



    #
    #   finally, the request response router and biz logic. Don't write model
    #   methods below this one.
    #

    def request_response(self, action=None):
        """ Follows the guidance in the base class method. """

        #
        #   custom returns for endpoints that ARE NOT web methods
        #

        if action == "get":
            return self.json_response()
        if action == 'get_summary':
            return flask.Response(
                response=self.serialize('dashboard'),
                status=200,
                mimetype="application/json"
            )
        if action == 'get_sheet':
            return flask.Response(
                response=self.serialize('sheet'),
                status=200,
                mimetype="application/json"
            )
        if action == 'get_survivors':
            return flask.Response(
                response=self.serialize('survivors'),
                status=200,
                mimetype="application/json"
        )
        if action == 'get_game_assets':
            return flask.Response(
                response=self.serialize('game_assets'),
                status=200,
                mimetype="application/json"
            )
        if action == 'get_campaign':
            return flask.Response(
                response=self.serialize('campaign'),
                status=200,
                mimetype="application/json"
            )
        if action == 'get_storage':
            return flask.Response(
                response=self.get_settlement_storage(),
                status=200,
                mimetype="application/json"
            )
        if action == 'get_storage_rollups':
            return flask.Response(
                response=self.get_settlement_storage_rollup(),
                status=200,
                mimetype="application/json"
            )
        if action == "get_event_log":
            return flask.Response(
                response=self.get_event_log("JSON"),
                status=200,
                mimetype="application/json"
            )
        if action == "gear_lookup":
            return flask.Response(
                response=self.get_gear_lookup(),
                status=200,
                mimetype="application/json"
            )
        if action == "get_innovation_deck":
            return flask.Response(
                response=self.get_innovation_deck(),
                status=200,
                mimetype="application/json"
            )
        if action == "get_timeline":
            return flask.Response(
                response=self.get_timeline("JSON"),
                status=200,
                mimetype="application/json"
            )
        if action == "add_note":
            return self.add_settlement_note(self.params)

        return super().request_response(action)


# ~fin
