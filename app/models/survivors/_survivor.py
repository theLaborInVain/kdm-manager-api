"""

    models.survivors.Survivor

    The class definition for the survivor object is defined here.

    It takes the UserAsset base class (from _user_asset.py).

"""

# standard library imports
import base64
from copy import copy
from io import BytesIO
from datetime import datetime
import json
import math
import random

# second party imports
import flask
from flask import request, Response
import pyheif
import whatimage
from PIL import Image # PIL.__init__ is empty!
from bson import json_util
from bson.objectid import ObjectId
import gridfs

# local imports
from app import API, utils

from .._user_asset import UserAsset
from .._data_model import DataModel
from .._decorators import deprecated, web_method, paywall



class Survivor(UserAsset):
    """ This is the class object for survivor objects. It sub-classes the
    UserAsset (e.g. just like settlements) and tries to fallback and/or
    super() back to that base class when possible. """

    DATA_MODEL = DataModel('settlement')

    # admin
    DATA_MODEL.add(
        'meta',
        dict,
        {
            "abilities_and_impairments_version": 1.0,
            "disorders_version": 1.0,
            "favorites_version": 1.0,
            "fighting_arts_version": 1.0,
            "special_attributes_version": 1.0,
            "weapon_proficiency_type_version": 1.0,
        }
    )
    DATA_MODEL.add("email", str)
    DATA_MODEL.add('settlement', ObjectId, immutable=True)
    DATA_MODEL.add('public', bool)

    # sheet
    DATA_MODEL.add('name', str, default_value='Anonymous')
    DATA_MODEL.add('sex', str, 'R', options=['M', 'F'])
    DATA_MODEL.add("survival", int, minimum=0)
    DATA_MODEL.add("Insanity", int, minimum=0)

    # attributes
    for attr in ['Accuracy', 'Evasion', 'Luck', 'Speed', 'Strength']:
        DATA_MODEL.add(attr, int)
    DATA_MODEL.add('Movement', int, 5, minimum=1)
    DATA_MODEL.add(
        'attribute_detail',
        dict,
        {
            "Movement": {"tokens": 0, "gear": 0},
            "Accuracy": {"tokens": 0, "gear": 0},
            "Strength": {"tokens": 0, "gear": 0},
            "Evasion":  {"tokens": 0, "gear": 0},
            "Luck":     {"tokens": 0, "gear": 0},
            "Speed":    {"tokens": 0, "gear": 0},
        }
    )

    # secondary attribs
    DATA_MODEL.add('affinities', dict, {"red": 0, "blue": 0, "green": 0})
    DATA_MODEL.add("Understanding", int, 0, minimum=0, maximum=9)
    DATA_MODEL.add("Courage", int, 0, minimum=0, maximum=9)
    DATA_MODEL.add("hunt_xp", int, 0, minimum=0)
    DATA_MODEL.add('returning_survivor', list)
    DATA_MODEL.add("Weapon Proficiency", int)
    DATA_MODEL.add("weapon_proficiency_type", str)
    DATA_MODEL.add("weapon_proficiency_type_sealed", str, required=False)
    DATA_MODEL.add(
        'weapon_proficiency_sealed', str, required=False, unset_on_none=True
    )

    # other
    DATA_MODEL.add('born_in_ly', int)
    DATA_MODEL.add("bleeding_tokens", int)
    DATA_MODEL.add('color_scheme', str, required=False)
    DATA_MODEL.add("max_bleeding_tokens", int, 5)
    DATA_MODEL.add('partner_id', ObjectId, required=False)

    # user stuff
    DATA_MODEL.add('departing', bool)
    DATA_MODEL.add('groups', list, required=False)

    # misc
    DATA_MODEL.add('inherited', dict, {'father': {}, 'mother': {}})
    DATA_MODEL.add("favorite", list)
    DATA_MODEL.add("fighting_arts_levels", dict)

    # armor locations
    for location in ['Head', 'Body', 'Arms', 'Waist', 'Legs']:
        DATA_MODEL.add(location, int, category='armor_location')

    # game asset handle lists
    for asset_list in [
        'abilities_and_impairments',
        'cursed_items',
        'disorders',
        'fighting_arts',
        'tags'
    ]:
        DATA_MODEL.add(asset_list, list, category='game_asset_list')

    #
    # optional attributes start here
    #
    for parent in ['father', 'mother']:
        DATA_MODEL.add(parent, ObjectId, required=False)

    DATA_MODEL.add('retired', bool, required=False)
    DATA_MODEL.add('retired_in', int, required=False)

    DATA_MODEL.add('died_on', datetime, required=False, category='death')
    DATA_MODEL.add('died_in', int, required=False, category='death')
    DATA_MODEL.add('cause_of_death', str, required=False, category='death')
    DATA_MODEL.add('dead', bool, required=False, category='death')

    # damage locations
    for location in [
        "brain_damage_light",
        "head_damage_heavy",
        "arms_damage_light",    "arms_damage_heavy",
        "body_damage_light",    "body_damage_heavy",
        "waist_damage_light",   "waist_damage_heavy",
        "legs_damage_light",    "legs_damage_heavy",
    ]:
        DATA_MODEL.add(
            location, bool, required=False,
            category='damage_location'
        )

    # transient flags
    for flag in [
        'cannot_activate_two_handed_weapons',
        'cannot_activate_two_plus_str_gear',
        'cannot_consume',
        'cannot_be_nominated_for_intimacy',
        'cannot_gain_bleeding_tokens',
        'cannot_spend_survival',
        'cannot_use_fighting_arts',
        'departing',
        'skip_next_hunt',
        'sotf_reroll',
    ]:
        DATA_MODEL.add(flag, bool, required=False, category='flag')

    # Gambler's Chest arc survivors
    DATA_MODEL.add('body_count', int, required=False)

    #
    # silly stuff / after-thoughts / one-offs, etc.
    #

    DATA_MODEL.add('constellation', str, required=False)
    DATA_MODEL.add(
        'sword_oath', dict, {'sword': None, 'wounds': 0}, required=False
    )
    DATA_MODEL.add('weak_spot', str, required=False)




    def __repr__(self):
        """ Writes a pretty __repr__ if self.survivor exists. Otherwise, falls
        back to the base class __repr__(). """

        if hasattr(self, 'survivor'):
            return "%s [%s] (%s)" % (
                self.survivor["name"],
                self.survivor["sex"],
                self.survivor["_id"]
            )

        return super().__repr__()


    def __init__(self, *args, **kwargs):
        """ Child/private class method for initializing a survivor object. """

        self.collection="survivors"

        # require an intitialized settlement object; we need it for game assets
        self.Settlement = kwargs.get('Settlement', None)
        if (
            self.Settlement is None or
            not hasattr(self.Settlement, 'settlement')
        ):
            err = '%s.__init__() requires initialized Settlement object! %s\n%s'
            raise TypeError(
                err % (
                    self.__class__.__name__,
                    self.Settlement,
                    dir(self.Settlement),
                )
            )

        # update the self.DATA_MODEL to include special attributes:
        for sa_key in self.Settlement.SpecialAttributes.assets:
            self.DATA_MODEL.add(
                sa_key, bool, required=False, category='special_attributes'
            )
        for sa_key in self.Settlement.OncePerLifetime.assets:
            self.DATA_MODEL.add(
                sa_key, bool, required=False, category='once_per_lifetime'
            )

        # if we're doing a new survivor, it will happen when we subclass the
        #   UserAsset class; otherwise, the base class method will call
        #   self.load():
        super().__init__(*args, **kwargs)

        # asset normalization!
        self.perform_save = False
        if self.kwargs.get('normalize_on_init', False):
            self.normalize()


    def new(self):
        """ Creates a new survivor.

        Leverages the DataModel() object to create a "blank" or default
        survivor sheet, and then uses the incoming 'new_asset_attribs' kwarg
        or the post params (as a fallback) to populate user-supplied values.

        """

        # get incoming survivor attribs before anything else
        attribs = self.kwargs.get('new_asset_attribs', {})
        if attribs == {}:
            attribs = self.params

        # initialize a settlement | no longer required October 2023
#        self.Settlement = settlements.Settlement(_id=attribs["settlement"])

        # 0. create a record that we're going to save to MDB and use to
        #   initialize the new survivor
        self.survivor = self.DATA_MODEL.new()
        self.survivor.update({
            "email":        request.User.login,
            "born_in_ly":   self.get_current_ly(),
            "created_on":   datetime.now(),
            "created_by":   request.User._id,
            "settlement":   self.Settlement._id,
        })

        # 0.a apply/overwrite attribs that go with our data model
        for attr, value in attribs.items():
            if self.DATA_MODEL.is_valid(attr, value):
                self.survivor[attr] = value

        # 0.b if sex is outside the data model, pick a random sex from the model
        if not self.DATA_MODEL.is_valid('sex', self.survivor["sex"]):
            self.survivor["sex"] = self.DATA_MODEL.random_choice('sex')

        # 0.e check for an avatar and add it BEFORE we save
        if 'avatar' in attribs.keys():
            self.set_avatar(attribs['avatar'], log_event=False, save=False)

        # 1. insert the record we've been developing and call the base class
        #   load() method, which will initialize and let us use class methods
        self._id = utils.mdb.survivors.insert(self.survivor)
        self.load()

        # 2. set the name
        s_name = self.survivor['name']
        if (
            s_name == "Anonymous" and
            attribs.get('random_name', False)
        ):
            s_name = self.Settlement.Names.get_random_survivor_name(
                self.survivor["sex"]
            )
        self.set_name(s_name, save=False, update_survival=False)

        # log the creation HERE
        self.log_event(action="create")

        # 3. parents and newborn status/operations, including inheritance
        self.__survivor_birth(attribs)

        # 4. increment survivial if we're named
        if (
            self.survivor["name"].upper() != "ANONYMOUS" and
            self.survivor["survival"] == 0
        ):
            msg = "Automatically added 1 survival to %s"
            self.log_event(
                msg = msg % self.pretty_name(),
                event_type='sysadmin'
            )
            self.survivor["survival"] += 1

        # 5. settlement buffs - move this to a separate function
        if attribs.get('apply_new_survivor_buffs', False):

            # grab the campaign: we'll need it in a second
            #c_dict = self.get_campaign(dict)

            def apply_buff_list(l):
                """ Private helper to apply a dictionary of bonuses. """
                for d in l:
                    for k in d.keys():
                        if k == "affinities":
                            self.update_affinities(d[k])
                        elif k == "abilities_and_impairments":
                            if not isinstance(d[k], list):
                                msg = (
                                    "The 'abilities_and_impairments' bonus must"
                                    " be a list! Failing on %s"
                                )
                                self.logger.exception(msg, d)
                                raise Exception(msg)
                            for a_handle in d[k]:
                                self.add_game_asset(
                                    "abilities_and_impairments", a_handle
                                )
                        else:
                            self.update_attribute(k, d[k])


            buff_sources = set()
            buff_list = []

            # look for bonuses from 
            for attrib in ["principles", "innovations"]:
                for d in self.Settlement.list_assets(attrib):
                    if d.get("new_survivor", None) is not None:
                        buff_list.append(d["new_survivor"])
                        buff_sources.add(d["name"])
                    if self.newborn:
                        if d.get("newborn_survivor", None) is not None:
                            buff_list.append(d["newborn_survivor"])
                            buff_sources.add(d["name"])

            # ...and also from the campaign definition for now
            # self.Settlement.campaign.asset is the campaign definition
            if self.Settlement.campaign.asset.get('new_survivor', None) is not None:
                buff_list.append(self.Settlement.campaign.asset['new_survivor'])
                buff_sources.add("'%s' campaign" % self.Settlement.campaign.asset["name"])
            if self.newborn:
                if self.Settlement.campaign.asset.get('newborn_survivor', None) is not None:
                    buff_list.append(self.Settlement.campaign.asset['newborn_survivor'])
                    buff_sources.add("'%s' campaign" % self.Settlement.campaign.asset["name"])

            if buff_list != []:
                buff_string = utils.list_to_pretty_string(buff_sources)
                self.log_event(
                    action='apply',
                    key=self.pretty_name(),
                    value='%s bonuses' % buff_string
                )
                apply_buff_list(buff_list)
        else:
            msg = (
                "Settlement bonuses where not applied to %s due to user "
                "preference."
            )
            self.log_event(msg % self.pretty_name())

        # Add our campaign's founder epithet if the survivor is a founder
        if self.is_founder():
            founder_epithet = self.Settlement.campaign.asset.get(
                "founder_epithet", "founder"
            )
            self.add_game_asset("tags", founder_epithet)

        # log and save
        msg = "%s created by %s (%s)"
        self.logger.info(msg, self, request.User, self.Settlement)
        self.save()

        return self._id


    def __survivor_birth(self, attribs={}):
        '''
        This is basically a carve out from the new() method. All of the
        procedural stuff below use to happen in that sequence, but we are doing
        it in its own method for clarity, maintainability, etc.
        '''

        def process_one_parent(parent_type, parent_oid, primary_donor_parent=False):
            """ Private method for processing ONE of a new survivor's parents.
            Updates the survivor as well as self.parent_names, which is used
            below.

            This is the main place where we do survivor inheritance!
            """

            # initialize inheritance template - this is the full scope of what
            #   can be inherited during survivor birth
            self.survivor['inherited'][parent_type] = {
                'abilities_and_impairments': [],
                'disorders': [],
                'fighting_arts': [],
                'weapon_proficiency_type': '',
                'Weapon Proficiency': 0,
                'surname': None,
            }

            # now initialize the parent
            parent_oid = ObjectId(parent_oid)
            P = Survivor(_id=parent_oid, Settlement=self.Settlement)
            self.parent_names.append(P.survivor["name"])
            self.survivor[parent_type] = parent_oid

            p_log_str = "%s (%s)" % (P.pretty_name(), parent_type)

            # check the parent for inheritable A&Is
            for ai in P.list_assets('abilities_and_impairments'):
                if ai.get('inheritable', False):
                    self.survivor['inherited'][parent_type]['abilities_and_impairments'].append(ai['handle'])
                    self.add_game_asset(
                        'abilities_and_impairments',
                        ai['handle'],
                        log_event=False
                    )
                    self.log_event(
                        action="inherit",
                        key=p_log_str,
                        value=ai['name'],
                        agent="automation",
                        event_type="inherit"
                    )

            # if this parent happens to be the primary donor (for inheritance)
            # check settlement innovations for ones with a primary_donor_parent
            if primary_donor_parent:

                for i_dict in self.Settlement.list_assets('innovations'):
                    if i_dict.get('primary_donor_parent', None) is not None:
                        for attr in i_dict['primary_donor_parent'].get('attributes', []):
                            self.survivor[attr] = P.survivor[attr]
                            self.survivor['inherited'][parent_type][attr] = P.survivor[attr]
                            self.log_event(
                                action="inherit", key=p_log_str, value=attr,
                                agent="automation", event_type="inherit"
                            )
                        for special in i_dict['primary_donor_parent'].get('specials', []):
                            if special == "surname":
                                if P.get_surname() is not None:
                                    surname = P.get_surname()
                                    new_survivor_name = " ".join([
                                        self.survivor['name'],
                                        surname
                                    ])
                                    self.set_name(new_survivor_name, save=False)
                                    self.survivor['inherited'][parent_type]['surname'] = surname
                                    self.log_event(action="inherit", key=p_log_str, value="surname '%s'" % surname, agent="automation", event_type="inherit")
                            elif special == "one_half_weapon_proficiency":
                                self.survivor['Weapon Proficiency'] = math.floor(P.survivor['Weapon Proficiency']*0.5)
                                self.survivor['inherited'][parent_type]['Weapon Proficiency'] = self.survivor['Weapon Proficiency']
                                self.log_event(action="inherit", key=p_log_str, value="1/2 weapon proficiency levels", agent="automation", event_type="inherit")
                            else:
                                msg = (
                                    "Unrecognized primary donor parent "
                                    "'special' key '%s' is ignored!"
                                )
                                self.logger.warning(msg % special)


        # 1.) process parents here and do inheritance
        self.parent_names = []
        for parent_type in ["father","mother"]:
            primary_donor_parent = attribs.get('primary_donor_parent', False)
            if primary_donor_parent == parent_type:
                primary_donor_parent = True
            else:
                primary_donor_parent = False
            if parent_type in attribs.keys() and attribs[parent_type] is not None:
                process_one_parent(parent_type, attribs[parent_type], primary_donor_parent)

        # 2.) if the survivor is a newborn, do newborn operations
        self.newborn = False
        if self.parent_names != []:
            self.newborn = True
            parent_string = ' and '.join(self.parent_names)

        # 3.d log the birth/joining
        if self.newborn:
            self.log_event("%s born to %s!" % (self.pretty_name(), parent_string), action="born", agent="automation")
        else:
            self.log_event(
                msg = '%s joined the settlement!' % self.pretty_name(),
                event_type="survivor_join"
            )

        return True


    def save(self, set_modified_on=False, verbose=True):
        ''' Formerly __post_process, this is our last chance to inflict business
        logic and/or game rules on a survivor BEFORE saving it back to mdb.'''

        # only call validation methods here!
        self._validate_max_bleeding_tokens()
        self._validate_partnership()
        self._validate_weapon_proficiency_type()

        super().save()


    def normalize(self):
        """ In which we force the survivor's mdb document to adhere to the biz
        logic of the game and our own data model. """

        self.__bug_fixes()
        self.__baseline()


        #
        #   asset migrations (names to handles)
        #

        if self.survivor["meta"].get("abilities_and_impairments_version", None) is None:
            self.__convert_abilities_and_impairments()
            self.perform_save = True

        if self.survivor["meta"].get("disorders_version", None) is None:
            self.__convert_disorders()
            self.perform_save = True

        if self.survivor["meta"].get("favorites_version", None) is None:
            self.__convert_favorite()
            self.perform_save = True

        if self.survivor["meta"].get("fighting_arts_version", None) is None:
            self.__convert_fighting_arts()
            self.perform_save = True

        if self.survivor["meta"].get("special_attributes_version", None) is None:
            self.__convert_special_attributes()
            self.perform_save = True

        if self.survivor["meta"].get("weapon_proficiency_type_version", None) is None:
            self.__convert_weapon_proficiency_type()
            self.perform_save = True


        #
        #   user asset normalization
        #

        # handle orphan partners
        if self.survivor.get('partner_id', None) is not None:
            partner = utils.mdb.survivors.find_one(
                {'_id': self.survivor['partner_id']}
            )
            if partner.get('partner_id', None) != self.survivor['_id']:
                self.set_partner("UNSET")

        # add the savior key if we're dealing with a savior
        if self.is_savior() and "savior" not in self.survivor.keys():
            self.survivor["savior"] = self.is_savior()
            self.perform_save = True

        # finally, apply the data model
        corrected_record = self.DATA_MODEL.apply(self.survivor)
        if corrected_record != self.survivor:
            self.logger.warning('[%s] data model corrections applied!', self)
            self.survivor = corrected_record
            self.perform_save = True

        if self.perform_save:
            msg = "%s survivor modified during normalization! Saving changes..."
            self.logger.info(msg % self)
            self.save()


    def synthesize(self):
        """ Renders a dictionary representing the Survivor's Sheet, but with
        additional data that is critical to business logic in the API and in
        consumer webapps. """

        output = {}

        # build the sheet: don't forget to add cursed items to it
        output["sheet"] = self.get_record()
        output["sheet"].update({"effective_sex": self.get_sex()})
        output["sheet"].update({"can_be_nominated_for_intimacy": self.can_be_nominated_for_intimacy()})
        output["sheet"].update({"can_gain_bleeding_tokens": self.can_gain_bleeding_tokens()})
        output["sheet"].update({"can_gain_survival": self.can_gain_survival()})
        output["sheet"].update({"cannot_activate_weapons": self.cannot_activate_weapons()})
        output["sheet"].update({"cannot_activate_two_handed_weapons": self.cannot_activate_two_handed_weapons()})
        output["sheet"].update({"cannot_activate_two_plus_str_gear": self.cannot_activate_two_plus_str_gear()})
        output["sheet"].update({"cannot_be_nominated_for_intimacy": self.cannot_be_nominated_for_intimacy()})
        output["sheet"].update({"cannot_consume": self.cannot_consume()})
        output["sheet"].update({"cannot_spend_survival": self.cannot_spend_survival()})
        output["sheet"].update({"cannot_use_fighting_arts": self.cannot_use_fighting_arts()})
        output["sheet"].update({"skip_next_hunt": self.skip_next_hunt()})
        output["sheet"].update({"founder": self.is_founder()})
        output["sheet"].update({"savior": self.is_savior()})
        output['sheet'].update({'parents': self.get_parents(dict)})

        # survivors whose campaigns use dragon traits get a top-level element
        if self.Settlement.campaign.asset.get("dragon_traits", False):
            output["dragon_traits"] = {}
            output["dragon_traits"].update({"trait_list": self.get_dragon_traits()})
            output["dragon_traits"].update({"active_cells": self.get_dragon_traits("active_cells")})
            output["dragon_traits"].update({"available_constellations": self.get_dragon_traits("available_constellations")})

        # now add the additional top-level items
        output.update({"notes": self.get_notes()})
        output.update({"survival_actions": self.__get_survival_actions("JSON")})


        return output


    @web_method
    def remove(self):
        """ Marks the survivor removed."""
        self.survivor['removed'] = datetime.now()
        self.log_event(
            '%s marked the survivor as removed!' % request.User.user['login']
        )
        self.save()


    def unremove(self):
        """ Deletes the 'removed' attribute. Saves. """
        del self.survivor['removed']
        self.log_event("Survivor %s un-removed!" % self, event_type="sysadmin")
        self.save()


    #
    #   normalization/enforcement helper methods
    #

    def apply_survival_limit(self, save=False):
        """ Check the settlement to see if we're enforcing Survival Limit. Then
        enforce it, if indicated. Force values less than zero to zero. """

        # no negative numbers
        if self.survivor["survival"] < 0:
            self.survivor["survival"] = 0

        # see if we want to enforce the Survival Limit
        if self.Settlement.get_survival_limit(bool):
            if self.survivor["survival"] > self.Settlement.get_survival_limit():
                self.survivor["survival"] = self.Settlement.get_survival_limit()

        # save, if params require
        if save:
            self.save()




    #
    #   update/set methods
    #

    @web_method
    def add_cursed_item(self, handle=None):
        """ Adds a cursed item to a survivor. Does a bit of biz logic, based on
        the asset dict for the item.

        If the 'handle' kwarg is None, this method will look for a request
        param, e.g. as if this was a reqeuest_response() call.
        """

        # initialize
        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params["handle"]
        ci_dict = self.Settlement.CursedItems.get_asset(handle)

        # check for the handle (gracefully fail if it's a dupe)
        if ci_dict["handle"] in self.survivor["cursed_items"]:
            err = "%s already has cursed item '%s'"
            self.logger.error(err, self, ci_dict["handle"])
            return False

        # log to settlement event
        msg = "%s is cursed! %s added %s to survivor."
        self.log_event(
            msg % (
                self.pretty_name(), request.User.login, ci_dict["name"],
            ),
            event_type="survivor_curse"
        )

        # add related A&Is
        if ci_dict.get("abilities_and_impairments", None) is not None:
            for ai_handle in ci_dict["abilities_and_impairments"]:
                self.add_game_asset('abilities_and_impairments', ai_handle)

        self.add_game_asset("tags", "cursed")

        # append it, save and exit
        self.survivor["cursed_items"].append(ci_dict["handle"])
        self.save()


    @web_method
    def rm_cursed_item(self, handle=None):
        """ Removes cursed items from the survivor, to include any A&Is that go
        along with that cursed item. Does NOT remove any A&Is that are caused by
        any remaining cursed items, i.e. so you can have multiple items with the
        King's Curse, etc. """

        # initialize
        if handle is None:
            self.check_request_params(['handle'])
            handle = self.params['handle']
        ci_dict = self.Settlement.CursedItems.get_asset(handle)

        # check for the handle (gracefully fail if it's no thtere)
        if ci_dict["handle"] not in self.survivor["cursed_items"]:
            err = "%s does not have cursed item '%s'. Ignoring bogus request..."
            self.logger.error(err % (self, ci_dict["handle"]))
            return False

        # log to settlement event
        msg = "%s removed %s from %s"
        self.log_event(
            msg % (request.User.login, ci_dict["name"], self.pretty_name())
        )

        # remove any A&Is that are no longer required/present
        if ci_dict.get("abilities_and_impairments", None) is not None:

            # create a set of the curse A&Is that are sticking around
            remaining_curse_ai = set()

            for ci_handle in self.survivor["cursed_items"]:
                if ci_handle == ci_dict["handle"]:     # ignore the one we're processing currently
                    pass
                else:
                    remaining_ci_dict = self.Settlement.CursedItems.get_asset(ci_handle)
                    if remaining_ci_dict.get("abilities_and_impairments", None) is not None:
                        remaining_curse_ai.update(remaining_ci_dict["abilities_and_impairments"])

            # now check the CI we're processing against the list we created
            for ai_handle in ci_dict["abilities_and_impairments"]:
                if ai_handle not in remaining_curse_ai:
                    self.rm_game_asset('abilities_and_impairments', ai_handle)
                else:
                    self.logger.info("%s Not removing '%s' A&I; survivor is still cursed." % (self, ai_handle))

        # rm the epithet if we have no curses
        if self.survivor['cursed_items'] == []:
            self.rm_game_asset("tags", "cursed")

        # remove it, save and exit
        self.survivor["cursed_items"].remove(ci_dict["handle"])
        self.save()


    @web_method
    def add_favorite(self, user_email=None):
        """Adds the value of the incoming 'user_email' kwarg to the survivor's
        'favorite' attribute (which is a list of users who have favorited the
        survivor. """

        if user_email is None:
            self.check_request_params(['user_email'])
            user_email = self.params['user_email']

        if user_email in self.survivor['favorite']:
            err = (
                "%s User '%s' is already in this survivor's favorite list. "
                "Ignoring bogus add request."
            )
            self.logger.error(err % (self, user_email))
            return True

        self.survivor['favorite'].append(user_email)
        self.log_event(
            '%s added %s to their favorite survivors.' % (
                user_email,
                self.pretty_name()
            )
        )

        self.save()


    @web_method
    def rm_favorite(self, user_email=None):
        """Removes the value of the incoming 'user_email' kwarg from the
        survivor's 'favorite' attribute (which is a list of users who have
        favorited the survivor. """

        if user_email is None:
            self.check_request_params(['user_email'])
            user_email = self.params['user_email']

        if user_email not in self.survivor['favorite']:
            err = (
                "%s User '%s' is not in this survivor's favorite list. "
                "Ignoring bogus remove request."
            )
            self.logger.error(err % (self, user_email))
            return True

        self.survivor['favorite'].remove(user_email)
        self.log_event(
            '%s removed %s from their favorite survivors.' % (
                user_email,
                self.pretty_name()
            )
        )

        self.save()


    @web_method
    def add_game_asset(self, asset_class=None, asset_handle=None,
                       apply_related=True, save=True, log_event=True):

        """ Allows the addition of 'asset_handle' to the survivor, according to
        'asset_class'.

        If the 'asset_class' value is None, then the method assumes that it is
        being called by a request_response() method and looks for request
        params.

        Important! All incoming asset handles are turned into asset dicts using
        their AssetCollection class's get_asset() method! Any handle that cannot
        be turned into a dict in this way will bomb out and raise an exception!

        Here is the order of operations on how an incoming handle is evaluated:

            1.) the "max" attribute of any incoming asset is respected. The
                asset WILL NOT be added if doing so would go above the asset's
                "max", as defined by its asset dict. The call will return False.
            2.) if an asset dict contains one of our survivor 'flag' values,
                this method will try to set it, if the flag's value evaluates to
                Boolean True.
            3.) any keys of the asset dictionary are also attributes of the
                self.survivor dict get a call to self.update_attribute, i.e. to
                add them to whatever the survivor's existing attribute happens
                to be.
            3.5.) if the '_set_attributes' key comes over, we iterate it and do
                whatever it says.
            4.) if the asset dict has an 'epithet' key, the value of that key
                (which should always be an epithet handle) will be added to the
                survivor.
            5.) the survivor's permanent affinities are modified if the asset
                dict contains the 'affinities' key
            6.) similarly, if the asset dict has a 'related' key, any related
                asset handles are applied to the survivr.

        Once added to the survivor, the following 'post-processing' business
        logic is automatically handled by this method:

            1.) Weapon masteries get a log_event() call. They are also added
                to the settlement's Innovations (via add_innovation() call.)


        That's it! Have fun!
        """

        #initialize
        asset_class, asset_dict = self.asset_operation_preprocess(
            asset_class,
            asset_handle
        )


        # 1.) MAX - check the asset's 'max' attribute:
        # assets WITHOUT a 'max' DO NOT HAVE A MAX
        if asset_dict.get("max", None) is not None:
            if self.survivor[asset_class].count(asset_dict["handle"]) >= asset_dict["max"]:
                err = (
                    "%s max for '%s' (%s) has already been reached! Ignoring..."
                )
                self.logger.warning(
                    err % (self, asset_dict["handle"], asset_class)
                )
                return False

        # 2.) STATUS - set status flags if they're in the dict
        for flag in self.DATA_MODEL.category('flag'):
            if asset_dict.get(flag, None) is True:
                self.set_status_flag(flag)

        # 3.) ATTRIBS - now check asset dict keys for survivor dict attribs
        for asset_k, asset_v in asset_dict.items():
            if (
                isinstance(asset_v, int) and
                not isinstance(asset_v, bool) and
                self.DATA_MODEL.is_valid(asset_k, asset_v, log_errors=True)
            ):
                model = getattr(self.DATA_MODEL, asset_k)
                if model.get('absolute', False):
                    self.set_attribute(asset_k, asset_v, save=False)
                else:
                    self.update_attribute(asset_k, asset_v, save=False)

        # 3.5 ATTRIBS - custom flags
        if asset_dict.get('_set_attributes', False):
            for attribute in asset_dict['_set_attributes']:
                self.set_attribute(
                    attribute,
                    asset_dict['_set_attributes'][attribute],
                    save = False
                )


        # RETIRED mostly this is for the 'Fear of the Dark' disorder, TBH
        if 'retire' in asset_dict.keys():
            self.set_retired(True)

        # levels!?
        if asset_dict.get('levels', None) is not None:
            self.survivor["fighting_arts_levels"][asset_dict["handle"]] = [0]

        # 4.) EPITHETS - check for 'epithet' key
        if asset_dict.get("epithet", None) is not None:
            self.add_game_asset("tags", asset_dict["epithet"], save=save)

        # 5.) AFFINITIES - some assets add permanent affinities
        if asset_dict.get('affinities', None) is not None:
            self.update_affinities(asset_dict["affinities"])

        # 6.) RELATED - add any related
        if apply_related and asset_dict.get("related", None) is not None:
            self.logger.info("Automatically applying %s related asset handles to %s" % (len(asset_dict["related"]), self))
            for related_handle in asset_dict["related"]:
                self.add_game_asset(
                    asset_class,
                    related_handle,
                    apply_related=False,
                    save=save
                )

        # 7.) EXCLUDED - rm any excluded
        for excluded_handle in asset_dict.get('excluded', []):
            self.rm_game_asset(asset_class, excluded_handle, save=False)

        # finally, if we're still here, add it and log_event() it
        self.survivor[asset_class].append(asset_dict["handle"])
        self.survivor[asset_class].sort()
        if log_event:
            self.log_event(action="add", key=asset_class, value=asset_dict['name'])


        # special handling for weapon mastery
        if asset_dict.get("sub_type", None) == "weapon_mastery":

            self.log_event("%s has mastered the %s!" % (
                self.pretty_name(),
                asset_dict["weapon_name"]),
                event_type="survivor_mastery"
            )

            if asset_dict.get("add_to_innovations", True):
                self.Settlement.add_innovation(asset_dict["handle"])


        # finally, save the survivor and return
        if save:
            self.save()


    def asset_operation_preprocess(self, collection=None, asset_handle=None):
        """ As its name suggests, the purpose of this method is to 'stage up' or
        prepare to do the add_game_asset() method (above). The idea is that you
        call this method at the beginning of add_game_asset() to sanity check it
        and do any other preprocessing tasks.

        Set 'collection' kwarg to the string of an asset collection and
        'asset_handle' to any handle within that asset collection and this
        func will return the value of 'collection' and an asset dict for the
        'asset_handle' value.

        This method will back off to the incoming request if 'asset_type' is
        None.
        """

        #
        #   1.) initialize the request. Try to use kwargs, but back off to
        #   request params if incoming kwargs are None
        #

        if collection is None:
            self.check_request_params(["type", "handle"])
            collection = self.params["type"]
            asset_handle = self.params["handle"]
        elif collection is not None and asset_handle is None:
            self.check_request_params(["handle"])
            asset_handle = self.params["handle"]


        #   2.) initialize/import the AssetModule and an AssetCollection object
        collection_obj = getattr(
            self.Settlement, utils.snake_to_camel_case(collection)
        )


        #   3.) handle the _random pseudo/bogus/magic handle; start with
        #   asset_handle: '_random'; end with asset_handle: 'real_handle'
        if asset_handle == "_random":
            msg = "%s selecting random '%s' asset from %s"
            self.logger.info(msg % (self, collection, collection_obj))
            available = copy(
                self.Settlement.get_available_assets(
                    asset_collection = collection_obj,
                    exclude_sub_types = ['secret_fighting_art']
                )[collection]  # e.g. 'disorders'
            )

            # filter out assets that the survivor already has
            for a_handle in self.survivor[collection]:
                if available.get(a_handle, None) is not None:
                    del available[a_handle]

            # filter out 'strain' fighting arts that we haven't unlocked; don't
            #   iterate the dict directly, since we're gonna modify it (probably)
            for a_handle in list(available.keys()):
                a_dict = available[a_handle]
                strain_milestone = a_dict.get('strain_milestone', None)
                if strain_milestone is not None:
                    if strain_milestone not in \
                    self.Settlement.settlement['strain_milestones']:
                        del available[a_handle]

            asset_handle = random.choice(list(available.keys()))
            msg = "%s selected '%s' asset handle at random."
            self.logger.info(msg, self, asset_handle)


        #   4.) try to get the asset
        asset_dict = collection_obj.get_asset(asset_handle)

        # exit preprocessing with a valid class name and asset dictionary
        return collection, asset_dict


    @web_method
    def set_affinities(self):
        """ New in API release >= 1.50.n. Uses request context params to set
        the survivor's affinity values. All keys are required:

        {'red': 0, 'green': 1, 'blue': 69}

        Note: missing keys will be considered zeroes! YHBW.

        """

        # no param enforcement here
        for color in ['red', 'green', 'blue']:
            self.survivor["affinities"][color] = self.params.get(color, 0)

        # log it
        msg = "%s set %s affinities: red %s, green %s, blue %s."
        self.log_event(
            msg % (
                request.User.login,
                self.pretty_name(),
                self.survivor['affinities']['red'],
                self.survivor['affinities']['green'],
                self.survivor['affinities']['blue'],
            )
        )

        self.save()


    @web_method
    def set_avatar(self, avatar=None, log_event=True, save=True):
        """ Expects a request context. This port of a legacy app method adds an
        incoming avatar to the GridFS and sets the self.survivor['avatar'] key
        to the OID of the image. Also does the resizing, etc.

        Avatar rules!
            - if you're calling this directly, 'avatar' should be a string that
                we can base64 encode.
            - similarly, if we're reading a request, the 'avatar' key must
                be a base64 encoded string.
            - we're going to validate them here as well, so they better be a
                real image by the time you call this method!
            - avatars are going to be auto-resized by this method

        """

        # initialize from request, if we're doing that
        if avatar is None:
            self.check_request_params(['avatar'])
            avatar = self.params['avatar']

        if len(avatar) % 4:
            avatar += '=' * (4 - len(avatar) % 4)

        avatar = base64.b64decode(avatar)

        # now set the type. this validates that we've got an actual image
        # in the incoming string/object
        try:
            avatar_type = whatimage.identify_image(avatar)
        except TypeError:
            raise utils.InvalidUsage(
                "Image type of incoming file could not be determined!"
            )

        # since we've now got what we THINK is a valid image, use PIL to start
        # working with it; initialize, resize and save to PNG

        processed_image = BytesIO()
        try:
            # issue #50; HEIF/iPhone support
            if avatar_type in ['heic', 'avif']:
                heif_object = pyheif.read_heif(avatar)
                im = Image.frombytes(
                    mode=heif_object.mode,
                    size=heif_object.size,
                    data=heif_object.data
                )
            else:
                im = Image.open(BytesIO(avatar))
        except Exception as e:
            err = "Image could not be processed! "
            self.logger.exception(e)
            raise utils.InvalidUsage(err + str(e))

        resize_tuple = tuple(
            [int(n) for n in API.config['AVATAR_DIMENSIONS']]
        )
        im.thumbnail(resize_tuple, Image.LANCZOS)
        im.save(processed_image, format="PNG")

        # now that we're sure we've got a valid avatar to work with, spin up
        # GridFS; remove a previous one (if necessary) and save

        fs = gridfs.GridFS(utils.mdb)

        # check for/remove previous
        if 'avatar' in self.survivor.keys():
            fs.delete(self.survivor['avatar'])
            self.logger.debug(
                "%s Removed an avatar image '%s' from GridFS.",
                request.User.login, self.survivor['avatar']
            )

        # save new
        avatar_id = fs.put(
            processed_image.getvalue(),
            content_type=avatar_type,
            created_by=request.User._id,
            created_on=datetime.now(),
        )

        # update the survivor, log and save
        self.survivor["avatar"] = ObjectId(avatar_id)
        if log_event:
            self.log_event(
                '%s set a new avatar for %s.' % (
                    request.User.login, self.pretty_name()
                ),
                event_type="avatar_update",
            )
        if save:
            self.save()

        return Response(
            response=json.dumps(
                {'avatar_oid': avatar_id}, default=json_util.default
            ), status=200
        )


    @web_method
    def set_fighting_art_level(self, save=True):
        ''' Web-only method for setting a Fighting Art 'levels' list.

        In the data model, survivors have a top-level key called
        'fighting_arts_levels', which is a dictionary: the keys of that dict
        are Fighting Art handles and the values of those keys are lists of
        integers.

        'survivor': {
            'fighting_arts_levels': {
                'silk_surgeon': [
                    1, 2
                ]
            },
        }
        '''

        self.check_request_params(['handle', 'levels'])

        # set the FA for logging purposes
        fighting_art_handle = self.params['handle']
        fighting_art = self.Settlement.FightingArts.get_asset(
            fighting_art_handle
        )

        # idiot-proof the levels list
        new_levels = sorted(
            list(
                set(
                    [int(lvl) for lvl in self.params['levels']]
                )
            )
        )

        # add a handle if one doesn't exist
        if not self.survivor['fighting_arts_levels'].get(
            fighting_art_handle, False
        ):
            self.survivor['fighting_arts_levels'][fighting_art_handle] = []

        # finally, set it and log
        self.survivor['fighting_arts_levels'][fighting_art_handle] = new_levels

        msg = "%s set %s Fighting Art levels for '%s' to include %s"
        self.log_event(msg %
            (
                request.User.login,
                self.pretty_name(),
                fighting_art['name'],
                new_levels
            )
        )

        if save:
            self.save()


    @web_method
    @paywall
    def set_color_scheme(self):
        ''' Web-only method that processes a request to update the survivor's
        color_scheme attribute. '''

        # first, handle unsets
        if (
            'unset' in self.params and
            self.survivor.get('color_scheme', None) is not None
        ):
            del self.survivor['color_scheme']
            msg = '%s unset the color scheme for %s'
            self.log_event(msg % (request.User.login, self.pretty_name()))
            self.save()
            return True

        if (
            'unset' in self.params and
            self.survivor.get('color_scheme', None) is None
        ):
            msg = '%s Ignoring bogus request to unset color scheme...' % self
            self.logger.warning(msg)
            return False


        # now, try to get the color scheme handle from the request params
        cs_handle = self.params.get('value', None)
        if cs_handle is None:
            cs_handle = self.params.get('handle', None)

        if cs_handle is None:
            self.check_request_params(['value'])

        self.survivor['color_scheme'] = cs_handle
        scheme_dict = self.Settlement.SurvivorColorSchemes.get_asset(
            handle=cs_handle
        )
        msg = "%s set the color scheme to '%s' for %s."
        self.log_event(
            msg % (
                request.User.login,
                scheme_dict['name'],
                self.pretty_name()
            )
        )
        self.save()


    @web_method
    def set_gear_grid(self):
        """ Updates the survivor's 'gear_grid' attribute, which is a dictionary
        of grid locations:

        {
            'top_left': 'bone_blade',
            'top_middle': 'rawhide_headband',
            'middle_left': 'brain_mint',
            'center': 'bug_trap',
            'bottom_right': 'lantern_gauntlets'
        }

        We don't do updates with this method, i.e. whatever we pull from the
        params sets the whole grid.
        """

        self.check_request_params(['gear_grid'])

        # check the keys for invalid keys
        valid_keys = [
            'top_left',     'top_middle',       'top_right',
            'middle_left',  'middle_middle',    'middle_right',
            'bottom_left',  'bottom_middle',    'bottom_right'
        ]

        for location_key in self.params['gear_grid']:
            if location_key not in valid_keys:
                err = "The Gear Grid location keys '%s' is not supported!"
                raise utils.InvalidUsage(err % location_key)

        # if we're still here, set it and save it
        self.survivor['gear_grid'] = self.params['gear_grid']

        self.log_event()
        self.save()


    @web_method
    def set_many_game_assets(self):
        """ Much like the set_many_attributes() route/method, this one WILL ONLY
        WORK WITH A REQUEST object present.

        Iterates over a list of assets to add and calls add_game_asset() once
        for every asset in the array. """

        # initialize and sanity check!
        self.check_request_params(['game_assets','action'])
        action = self.params['action']
        updates = self.params['game_assets']

#        if type(updates) != list:
        if not isinstance(updates, list):
            err = (
                "The add_many_game_assets() method requires the 'assets' param "
                "to be an array/list!"
            )
            raise utils.InvalidUsage(err)
        if action not in ['add','rm']:
            err = "add_many_game_assets() 'action' param must be 'add' or 'rm'."
            raise utils.InvalidUsage(err)

        for u in updates:
            asset_class = u.get('type', None)
            asset_handle = u.get('handle', None)

            err = "set_many_game_assets() is unable to process hash: %s" % u
            usg = " Should be: {handle: 'string', type: 'string'}"
            err_msg = err + usg

            if asset_class is None:
                raise utils.InvalidUsage(err_msg)
            if asset_handle is None:
                raise utils.InvalidUsage(err_msg)

            if action == 'add':
                self.add_game_asset(
                    str(asset_class),
                    str(asset_handle),
                    save=False
                )
            elif action == 'rm':
                self.rm_game_asset(
                    str(asset_class),
                    str(asset_handle),
                    save=False
                )

        self.save()


    @web_method
    def set_weak_spot(self):
        ''' Sets the survivor's 'weak_spot' attribute to be a string. The string
        is a location value, e.g. 'head', 'arms', etc. '''

        self.check_request_params(['weak_spot'])
        weak_spot = self.params['weak_spot']

        # handle unset
        if weak_spot == 'UNSET' and self.survivor.get('weak_spot') is not None:
            del self.survivor['weak_spot']
        else:
            weak_spot = weak_spot.capitalize() # idiot-proof

            # sanity check
            if weak_spot not in self.DATA_MODEL.category('armor_location'):
                err = "'%s' is not a valid armor location!"
                raise utils.InvalidUsage(err % weak_spot)

            self.survivor['weak_spot'] = weak_spot

        self.log_event()
        self.save()


    @web_method
    def replace_game_assets(self):
        """ Much like set_many_game_assets(), this route facilitates The Watcher
        UI/UX and SHOULD ONLY BE USED WITH A REQUEST OBJECT since it pulls all
        params from there and cannot be called directly.

        This one takes a game asset category and overwrites it with an incoming
        list of handles.
        """

        self.check_request_params(['type','handles'])
        asset_class = self.params['type']
        asset_handles = self.params['handles']

        if asset_class not in self.DATA_MODEL.category('game_asset_list'):
            err = (
                "The replace_game_assets() method cannot modify asset type "
                "'%s'. Allowed types include: %s"
            )
            raise utils.InvalidUsage(
                err % (
                    asset_class, self.DATA_MODEL.category('game_asset_list')
                )
            )

        # first, turn our two lists into dictionaries where we count the handles
        current_dict = {h: self.survivor[asset_class].count(h) for h in self.survivor[asset_class]}
        incoming_dict = {h: asset_handles.count(h) for h in asset_handles}

        # next, compare the current dict to the incoming dict and figure out
        # what to keep and what to rm

        handles_to_rm = []
        for h in current_dict.keys():
            delta = current_dict[h] - incoming_dict.get(h, 0)
            if delta > 0:
                for dummy in range(delta):
                    handles_to_rm.append(h)

        handles_to_add = []
        for h in incoming_dict.keys():
            delta = incoming_dict[h] - current_dict.get(h, 0)
            if delta > 0:
                for dummy in range(delta):
                    handles_to_add.append(h)


        # bail if we've got no changes
        if handles_to_add == [] and handles_to_rm == []:
            self.logger.warning('Ignoring bogus replace_game_assets() operation: no changes to make...')
            return True

        # otherwise, if we're doing changes, do them one at a time
        for h in handles_to_rm:
            self.rm_game_asset(asset_class, h, save=False)
        for h in handles_to_add:
            self.add_game_asset(asset_class, h, save=False)

        self.save()


    @web_method
    def rm_game_asset(self, asset_class=None, asset_handle=None, rm_related=True, save=True):
        """ The inverse of the add_game_asset() method, this one most all the
        same stuff, except it does it in reverse order:

        One thing it does NOT do is check the asset dict's 'max' attribute, since
        that is irrelevant.
        """

        asset_class, asset_dict = self.asset_operation_preprocess(
            asset_class,
            asset_handle
        )

        # 1.) fail gracefully if this is a bogus request
        if asset_dict["handle"] not in self.survivor[asset_class]:
            warn = (
                "%s Ignoring attempt to remove non-existent key '%s' from "
                "'self.survivor.%s' "
            )
            self.logger.warning(warn, self, asset_dict["handle"], asset_class)
            return False

        # 2.) STATUS - unset status flags if they're in the dict
        for flag in self.DATA_MODEL.category('flag'):
            if asset_dict.get(flag, None) is True:
                self.set_status_flag(flag, unset=True)

        # 3.) ATTRIBS - now check asset dict keys for survivor dict attribs
        for asset_k, asset_v in asset_dict.items():
            if (
                isinstance(asset_v, int) and
                not isinstance(asset_v, bool) and
                self.DATA_MODEL.is_valid(asset_k, asset_v, log_errors=True)
            ):
                model = getattr(self.DATA_MODEL, asset_k)
                if model.get('absolute', False):
                    self.default_attribute(asset_k, save=False)
                else:
                    self.update_attribute(asset_k, asset_v, save=False)

        # 3.5 ATTRIBS - custom
        if asset_dict.get('_set_attributes', False):
            for attribute in asset_dict['_set_attributes']:
                self.default_attribute(attrib=attribute, save=False)

        # RETIRED mostly this is for the 'Fear of the Dark' disorder, TBH
        if 'retire' in asset_dict.keys():
            self.set_retired(False)

        # 4.) EPITHETS - check for 'epithet' key
        if asset_dict.get("epithet", None) is not None:
            self.rm_game_asset("tags", asset_dict["epithet"])

        # 5.) AFFINITIES - some assets add permanent affinities: rm those
        if asset_dict.get('affinities', None) is not None:
            self.update_affinities(asset_dict["affinities"], operation="rm")

        # 6.) RELATED - rm any related
        if rm_related and asset_dict.get("related", None) is not None:
            self.logger.info("Automatically removing %s related asset handles from %s" % (len(asset_dict["related"]), self))
            for related_handle in asset_dict["related"]:
                self.rm_game_asset(asset_class, related_handle, rm_related=False)

        # finally, if we're still here, add it and log_event() it
        self.survivor[asset_class].remove(asset_dict["handle"])
        self.log_event(action="rm", key=asset_class, value=asset_dict['name'])

        if save:
            self.save()


    #
    #   survivor notes!
    #

    @web_method
    def add_note(self):
        """ Adds a Survivor note to the mdb."""

        self.check_request_params(['note'])
        note = self.params['note']

        #
        #   notes have to come in as dicts, so we do some sanity-checking here
        #

        # enforce dict type
        if not isinstance(note, dict):
            self.logger.error('Rejecting attempt to add a note as a string!')
            raise utils.InvalidUsage(
                'In 1.14.89 and later, notes must be dict type!',
                status_code=400
            )

        # require 'note' key, i.e. the note body
        malformed_msg = (
            "The 'note' key/value pair is required! "
            "Its value may not be blank!."
        )
        if note.get('note', None).strip() == '':
            raise utils.InvalidUsage(malformed_msg, status_code=400)

        note_dict = {
            "created_by": request.User._id,
            "created_on": datetime.now(),
            "survivor_id": self.survivor["_id"],
            "settlement_id": self.Settlement.settlement['_id'],
            "note": note['note'],
            "pinned": note.get('pinned', False)
        }

        note_oid = utils.mdb.survivor_notes.insert(note_dict)
        self.log_event(action="add", key="notes", value="a note")

        return Response(response=json.dumps(
            {'note_oid': note_oid},
            default=json_util.default),
            status=200
        )


    @web_method
    def update_note(self):
        """ Updates a survivor note: we only allow certain attributes to be
        updated and don't use a data model. All of the business logic and rules
        are in this function. """

        self.check_request_params(['note'])
        incoming_note = utils.deserialize_json(self.params['note'])

        mdb_note = utils.mdb.survivor_notes.find_one({
            '_id': incoming_note['_id']
        })

        for attrib in ['pinned', 'note']:
            mdb_note[attrib] = incoming_note[attrib]

        utils.mdb.survivor_notes.save(mdb_note)
        self.logger.info(
            '%s UPDATED survivor note %s' % (
                request.User.login,
                mdb_note['_id']
            )
        )


    @web_method
    def rm_note(self):
        """ Removes a Survivor note from the MDB. Expects a request context. """

        self.check_request_params(['_id'])
        _id = ObjectId(self.params['_id'])
        utils.mdb.survivor_notes.remove({'_id': _id})
        self.logger.info(
            '%s REMOVED survivor note %s' % (request.User.login, _id)
        )


    #
    #   update methods!
    #

    @deprecated
    def update_affinities(self, aff_dict={}, operation="add"):
        """ Set the kwarg 'operation' to either 'add' or 'rm' in order to
        do that operation on self.survivor["affinities"], which looks like this:

            {'red': 0, 'blue': 0, 'green': 0}

        The 'aff_dict' should mirror the actual affinities dict, except without
        all of the color keys. For example:

            {'red': 1, 'blue': 2}
            {'green': -1}

        If 'aff_dict' is unspecified or an empty dict, this method will assume
        that it is being called by request_response() and check for 'aff_dict'
        in self.params.
        """

        # initialize
        if aff_dict == {}:
            self.check_request_params(['aff_dict'])
            aff_dict = self.params["aff_dict"]
            if 'operation' in self.params:
                operation = self.params["operation"]

        # sanity check
        if operation not in ["add", "rm"]:
            msg = "The '%s' operation is not supported by the update_affinities() method!" % (operation)
            self.logger.exception(msg)
            raise utils.InvalidUsage(msg, status_code=400)

        # now do it and log_event() the results for each key
        for aff_key in aff_dict.keys():
            if operation == "add":
                self.survivor["affinities"][aff_key] += aff_dict[aff_key]
            elif operation == 'rm':
                self.survivor["affinities"][aff_key] -= aff_dict[aff_key]
            self.log_event("%s set %s '%s' affinity to %s" % (request.User.login, self.pretty_name(), aff_key, self.survivor["affinities"][aff_key]))

        self.save()


    @web_method
    def update_attribute(self, attribute=None, modifier=None, save=True):
        """ Adds 'modifier' value to self.survivor value for 'attribute'. """

        if attribute is None or modifier is None:
            self.check_request_params(['attribute','modifier'])
            attribute = self.params["attribute"]
            modifier = self.params["modifier"]

        # hand off to update_survival or damage_brain if that's the shot
        if attribute == 'survival':
            return self.set_survival(
                value = self.survivor['survival'] + modifier,
                save=save
            )
        if attribute == 'brain_event_damage':
            return self.__damage_brain(modifier)

        # validate the change
        self.DATA_MODEL.is_valid(attribute, modifier, raise_on_failure=True)

        # make the update; control for min/max
        self.survivor[attribute] = self.DATA_MODEL.minmax(
            attribute,
            self.survivor[attribute] + modifier
        )

        # log completion of the update
        self.log_event("%s updated %s attribute '%s' to %s" % (
                request.User.login,
                self.pretty_name(),
                attribute,
                self.survivor[attribute]
            )
        )

        if save:
            self.save()


    def update_returning_survivor_years(self, add_year=None, save=True):
        """ Adds the current LY to the survivor's 'returning_survivor' attrib
        (i.e. list) by default. Set 'add_year' to any integer to add an
        arbitrary value. """

        if add_year is None:
            add_year = self.Settlement.get_current_ly()

        if 'returning_survivor' not in self.survivor.keys():
            self.survivor['returning_survivor'] = []

        self.survivor['returning_survivor'].append(add_year)

        self.survivor['returning_survivor'] = list(
            set(self.survivor['returning_survivor'])
        )

        if save:
            self.save()


    #
    #   toggles and flags!
    #

    @web_method
    def toggle_damage(self):
        """ toggles survivor damage boxes on/off. Requires a request context. """

        # initialize from request
        self.check_request_params(['location'])
        loc = self.params['location']

        #
        #   sanity check
        #

        if loc not in self.DATA_MODEL.category('damage_location'):
            err = "The damage location '%s' cannot be toggled!" % loc
            raise utils.InvalidUsage(err)

        #
        #   update
        #

        if loc in self.survivor.keys():
            del self.survivor[loc]
            self.log_event(value=loc, key="OFF")
        else:
            self.survivor[loc] = True
            self.log_event(value=loc, key="ON")
        self.save()


    @web_method
    def toggle_fighting_arts_level(self):
        """ Toggles a fighting arts level on or off, e.g. by adding it to or
        removing it from the array for a particular Fighting Art's handle.

        Assumes that this is an API request and does not process any args that
        do not come in the request object.

        Basically you get this:

            'fighting_arts_levels': {
                'silk_surgeon': [
                    1, 2
                ]
            },

        """

        self.check_request_params(['handle', 'level'])
        fa_handle = self.params["handle"]
        fa_level = int(self.params["level"])

        fa_dict = self.Settlement.FightingArts.get_asset(fa_handle)

        if fa_handle not in self.survivor['fighting_arts_levels'].keys():
            self.survivor["fighting_arts_levels"][fa_handle] = []

        if fa_level in self.survivor['fighting_arts_levels'][fa_handle]:
            toggle_operation = "off"
            self.survivor['fighting_arts_levels'][fa_handle].remove(fa_level)
        else:
            toggle_operation = "on"
            self.survivor['fighting_arts_levels'][fa_handle].append(fa_level)

        self.survivor['fighting_arts_levels'][fa_handle] = sorted(
            self.survivor['fighting_arts_levels'][fa_handle]
        )

        msg = "%s toggled '%s' fighting art level %s %s for %s."
        self.log_event(
            msg % (
                request.User.login,
                fa_dict["name"],
                fa_level,
                toggle_operation,
                self.pretty_name()
            )
        )

        self.save()


    @web_method
    def toggle_sotf_reroll(self):
        """ toggles the survivor's Survival of the Fittest once-in-a-lifetime
        reroll on or off. This is self.survivor["sotf_reroll"] and it's a bool
        and it's not part of the data model, so creating it is necessary some
        times. """

        msg = "%s toggled SotF reroll %s for %s"

        if "sotf_reroll" not in self.survivor.keys():
            self.survivor["sotf_reroll"] = True
            self.log_event(msg % (request.User.login, 'on', self.pretty_name()))
        elif self.survivor["sotf_reroll"]:
            self.survivor["sotf_reroll"] = False
            self.log_event(
                msg % (request.User.login, 'off', self.pretty_name())
            )
        elif not self.survivor["sotf_reroll"]:
            self.survivor["sotf_reroll"] = True
            self.log_event(msg % (request.User.login, 'on', self.pretty_name()))
        else:
            self.logger.error("Unhandled logic in toggle_sotf_reroll() method!")
            raise Exception

        self.save()




    #
    #   special game controls
    #

    @web_method
    def controls_of_death(self):
        """ Manage all aspects of the survivor's death here. This is tied to a
        a number of settlement methods/values, so be cautious with this one. """

        self.check_request_params(["dead"])
        dead = self.params["dead"]

        if dead is False:
            for death_key in ["died_on","died_in","cause_of_death","dead"]:
                if death_key in self.survivor.keys():
                    del self.survivor[death_key]
                    self.logger.debug(
                        "%s Removed '%s' from %s", request.User, death_key, self
                    )
            self.log_event(
                "%s has resurrected %s!" % (
                    request.User.login, self.pretty_name()
                )
            )
        else:
            self.survivor["dead"] = True
            self.survivor["died_on"] = datetime.now()

            # this isn't very DRY, but we've got to strictly type here
            if 'died_in' in self.params:
                self.survivor['died_in'] = int(self.params["died_in"])
            else:
                self.survivor["died_in"] = self.Settlement.get_current_ly()

            # now set the cause
            self.survivor['cause_of_death'] = "Unspecified"
            if 'cause_of_death' in self.params:
                try:
                    self.survivor['cause_of_death'] = str(self.params["cause_of_death"])
                except Exception as e:
                    self.logger.exception(e)
                    raise utils.InvalidUsage(
                        "Could not set custom type of death! '%s'" % e
                    )

            self.log_event(
                '%s has died! Cause of death: %s' % (
                    self.pretty_name(),
                    self.survivor["cause_of_death"]
                ),
                event_type="survivor_death"
            )
            self.Settlement.update_population(-1)

        self.save()


    def __damage_brain(self, dmg=0):
        """ Inflicts brain event damage on the survivor."""

        remainder = self.survivor['Insanity'] - dmg

        log_damage = False
        if remainder < 0:
            if self.survivor.get('brain_damage_light', None) is None:
                self.survivor['brain_damage_light'] = 'checked' #transitional
                log_damage = True
            self.survivor['Insanity'] = 0
        elif remainder == 0:
            self.survivor['Insanity'] = 0
        elif remainder > 0:
            self.survivor['Insanity'] = remainder
        else:
            raise Exception('%s Impossible damage_brain() result!' % self)

        self.log_event("%s inflicted %s Brain Event Damage on %s. The survivor's Insanity is now %s" % (request.User.login, dmg, self.pretty_name(), self.survivor["Insanity"]), event_type="brain_event_damage")
        if log_damage:
            self.log_event("%s has suffered a Brain injury due to Brain Event Damage!" % (self.pretty_name()))
        self.save()


    def return_survivor(self, showdown_type=None):
        """ Returns the departing survivor. This is a minimized port of the legacy
        webapp's heal() method (which was super overkill in the first place).

        This method assumes a request context, so don't try if it you haven't got
        a request object initialized and in the global namespace. """


        #
        #   initialize/sanity check
        #

        if not 'departing' in self.survivor.keys():
            self.logger.warning('%s is not a Departing Survivor! Skipping bogus return() request...' % self)

        def finish():
            """ Private method for concluding the return. Enhances DRYness. """
            msg = "%s returned %s to %s" % (request.User.login, self.pretty_name(), self.Settlement.settlement['name'])
            self.log_event(msg, event_type="survivor_return")
            self.save()


        #
        #   Living and dead survivor return operations
        #

        # 1.) update meta data
        self.survivor['departing'] = False

        if showdown_type == 'normal':
            self.update_returning_survivor_years(save=False)

        # 2.) remove armor
        for loc in self.DATA_MODEL.category('armor_location'):
            self.survivor[loc] = 0

        # 3.) remove tokens/gear modifiers
        self.reset_attribute_details(save=False)

        # 4.) heal injury boxes
        self.reset_damage(save=False)

        # 5.) finish if the survivor is dead
        if self.is_dead():
            finish()


        #
        #   Living survivors only from here!
        #

        # 6.) zero-out bleeding tokens
        self.set_bleeding_tokens(0, save=False)

        # 7.) increment Hunt XP
#        if self.is_savior():
#            self.update_attribute('hunt_xp', 4)
#        else:
#            self.update_attribute('hunt_xp', 1)

        # 8.) process disorders with 'on_return' attribs
        for d in self.survivor['disorders']:
            d_dict = self.Settlement.Disorders.get_asset(d)
            if d_dict.get('on_return', None) is not None:
                for k, v in d_dict['on_return'].items():
                    self.survivor[k] = v

        finish()




    #
    #   set methods!
    #

    @web_method
    def set_abilities_and_impairments(self, save=True):
        ''' A web-only method that allows the survivor's
        'abilities_and_impairments' list to be set, automatically handling add
        and remove operations. '''

        self.check_request_params(['value'])
        new_list = self.params['value']

        if not isinstance(new_list, list):
            err = "The 'value' param should be a list of handles."
            raise utils.InvalidUsage(err)

        # get the add/rm lists
        add_list, rm_list = utils.list_compare(
            self.survivor['abilities_and_impairments'],
            new_list
        )

        if add_list != []:
            [
                self.add_game_asset('abilities_and_impairments', ai)
                for ai in add_list
            ]

        if rm_list != []:
            [
                self.rm_game_asset('abilities_and_impairments', ai)
                for ai in rm_list
            ]

        if save:
            self.save()


    @web_method
    def set_attribute(self, attrib=None, value=None, save=True):
        """ Adds 'modifier' value to self.survivor value for 'attribute'. If the
        'attrib' kwarg is None, the function assumes that this is part of a call
        to request_response() and will get request params. """


        # if kwarg 'attrib' is None, we're processing a request
        if attrib is None:
            self.check_request_params(['attribute','value'])
            attrib = self.params["attribute"]
            value = self.params['value']

        #
        # divert certain attributes to specialized set methods:
        #
        for divert in [
            'abilities_and_impairments',
            'bleeding_tokens',
            'color_scheme',
            'damage',
            'public',
            'retired',
            'sex',
            'survival',
            'weapon_proficiency_type'
        ]:
            if attrib == divert:
                return getattr(self, 'set_%s' % divert)()

        # special diversion for damage locations
        if attrib in self.DATA_MODEL.category('damage_location'):
            return self.__set_damage()

        # duck type
        value = self.DATA_MODEL.duck_type(attrib, value)

        # necessity check - issue 434
        if self.survivor.get(attrib, 'VALUENOTDEFINED') == value:
            err = "%s No change to '%s' attrib (%s -> %s). Ignoring..."
            self.logger.info(err, self, attrib, self.survivor[attrib], value)
            return True

        # validate
        self.DATA_MODEL.is_valid(attrib, value, raise_on_failure=True)

        # set it and log it
        self.survivor[attrib] = self.DATA_MODEL.minmax(attrib, value)
        self.log_event(
            "%s set %s '%s' to %s" % (
                request.User.login, self.pretty_name(), attrib, value
            )
        )

        # enforce
        self.survivor = self.DATA_MODEL.apply(self.survivor)

        # optional save
        if save:
            self.save()


    @web_method
    def set_many_attributes(self):
        """ This basically reads a list of attributes to update and then updates
        them in the order they appear. """

        # initialize from the request
        attr_updates = []
        detail_updates = []
        if 'attributes' in self.params.keys():
            attr_updates = self.params['attributes']
        if 'attribute_details' in self.params.keys():
            detail_updates = self.params['attribute_details']

        # type check
#        if type(attr_updates) != list or type(detail_updates) != list:
        if (
            not isinstance(attr_updates, list) or not
            isinstance(detail_updates, list)
        ):
            err = (
                "The set_many_attributes() method requires 'attributes' and "
                "'attribute_details' params to be array/list types!"
            )
            raise utils.InvalidUsage(err)

        # do attr_updates first
        for u in attr_updates:
#            if type(u) != dict:
            if not isinstance(u, dict):
                err = (
                    "The set_many_attributes() method 'attributes' must be "
                    "hashes (i.e. dictionaries)!"
                )
                raise utils.InvalidUsage(err)

            attrib = u.get('attribute', None)
            value = u.get('value', None)

            err = "set_many_attributes() is unable to process hash: %s" % u
            usg = " Should be: {attribute: 'string', value: 'int'}"
            err_msg = err + usg

            if attrib is None:
                raise utils.InvalidUsage(err_msg)
            if value is None:
                raise utils.InvalidUsage(err_msg)

            if self.survivor[attrib] != value:
                self.set_attribute(str(attrib), int(value), False)

        # do detail updates
        for u in detail_updates:
#            if type(u) != dict:
            if not isinstance(u, dict):
                err = (
                    "The set_many_attributes() method 'attribute_details' must "
                    "be hashes (dictionaries)!"
                )
                raise utils.InvalidUsage(err)
            attrib = u.get('attribute',None)
            detail = u.get('detail',None)
            value  = u.get('value',None)
            for v in [attrib, detail, value]:
                if v is None:
                    raise utils.InvalidUsage("The '%s' attribute of %s may not be undefined!" % (v, u))
            if self.survivor['attribute_detail'][attrib][detail] != value:
                self.set_attribute_detail(attrib, detail, value, False)

        self.save()


    def set_public(self):
        ''' Expects a request but isn't a web method. We divert to this one from
        self.set_attribute() calls. '''

        self.check_request_params(['attribute', 'value'])
        if self.params.get('attribute', None) == 'public':
            self.survivor['public'] = self.params["value"]

        msg = '%s may be managed by any player.' % self.pretty_name()
        if not self.survivor['public']:
            msg = "%s is no longer a public survivor." % self.pretty_name()
        self.log_event(msg)

        self.save()


    @web_method
    def set_attribute_detail(self, attrib=None, detail=None, value=False, save=True):
        """ Use to update the 'attribute_detail' dictionary for the survivor.
        If this is called without an 'attrib' value, it will assume that it is
        being called as part of a request_response() call and look for request
        parameters.

        The 'attrib' value should be 'Strength', 'Luck', etc. and the 'detail'
        should be one of the following:

            - 'tokens'
            - 'gear'

        The 'value' must be an int.

        """

        if attrib is None:
            self.check_request_params(["attribute","detail","value"])
            attrib = self.params["attribute"]
            detail = self.params["detail"]
            value =  int(self.params["value"])

        if attrib not in self.survivor["attribute_detail"].keys():
            msg = "Survivor attribute '%s' does not support details!" % (attrib)
            self.logger.error(msg)
            raise utils.InvalidUsage(msg, status_code=400)

        if detail not in ['tokens','gear']:
            msg = "Survivor 'attribute_detail' detail type '%s' is not supported!" % (detail)
            self.logger.error(msg)
            raise utils.InvalidUsage(msg, status_code=400)

        self.survivor["attribute_detail"][attrib][detail] = value
        self.log_event("%s set %s '%s' detail '%s' to %s" % (request.User.login, self.pretty_name(), attrib, detail, value))

        # now save if we're saving
        if save:
            self.save()


    @web_method
    def set_bleeding_tokens(self, value=None, save=True):
        """ Sets self.survivor['bleeding_tokens'] to 'value', respecting the
        survivor's max and refusing to go below zero.

        REFACTOR THIS TO USE self.DATA_MODEL
        """

        if value is None:
            self.check_request_params(['value'])
            value = int(self.params["value"])

        self.survivor['bleeding_tokens'] = value

        # enforce min/max
        if self.survivor["bleeding_tokens"] < 0:
            self.survivor["bleeding_tokens"] = 0
        elif (
            self.survivor["bleeding_tokens"] >
            self.survivor["max_bleeding_tokens"]
        ):
            self.survivor["bleeding_tokens"] = self.survivor["max_bleeding_tokens"]

        self.log_event(
            '%s set %s bleeding tokens to %s.' % (
                request.User.login,
                self.pretty_name(),
                self.survivor["bleeding_tokens"]
            )
        )

        if save:
            self.save()


    @web_method
    def set_constellation(self, constellation=None, unset=None):
        """ Sets or unsets the survivor's self.survivor["constellation"]. """

        current_constellation = self.survivor.get("constellation", False)

        # figure out if we're unsetting
        if unset is not None or self.params.get('unset', False):
            unset = True

        # if we're going to unset, do unset
        if unset and current_constellation:
            del self.survivor["constellation"]
            self.log_event("%s unset Constellation" % request.User.login)
            self.rm_game_asset(
                "tags",
                "the_%s" % current_constellation.lower()
            )
            return True

        if unset and not current_constellation:
            self.logger.warning(
                "%s has no Constellation! Ignoring unset request...", self
            )
            return False

        # if we're NOT doing an unset, we're doing a set, so get params
        if constellation is None:
            self.check_request_params(['constellation'])
            constellation = self.params["constellation"]

        # check if this is redundant, if not, do the update
        if current_constellation == constellation:
            err = "%s Constellation is already %s. Ignoring request..."
            self.logger.warning(err, self.pretty_name(), constellation)
            return False


        #
        # if we're still here, get ready to do the work
        #

        # validate first
        self.DATA_MODEL.is_valid(
            'constellation', constellation, raise_on_failure=True
        )

        # unset the current constellation's related game assets
        if current_constellation:
            self.rm_game_asset(
                "tags",
                "the_%s" % current_constellation.lower()
            )

        # make the update
        self.survivor["constellation"] = constellation
        self.add_game_asset("tags", "the_%s" % constellation.lower())

        # event log the update
        self.log_event(
            "%s set %s constellation to '%s'" % (
                request.User.login,
                self.pretty_name(),
                constellation
            ),
            event_type = "potstars_constellation"
        )

        # event log the PotStars event
        if not current_constellation:
            log_msg = "%s has become one of the People of the Stars!"
            self.log_event(
                log_msg % self.pretty_name(),
                event_type="potstars_constellation"
            )

        self.save()


    @web_method
    def set_email(self, new_email=None):
        """ Validates an incoming email address and attempts to set it as the
        survivor's new email. It has to a.) be different, b.) look like an email
        address and c.) belong to a registered user before we'll set it."""

        if new_email is None:
            self.check_request_params(["email"])
            new_email = self.params["email"]

        # sanity checks
        if new_email == self.survivor["email"]:
            msg = "%s Survivor email unchanged! Ignoring request..." % self
            self.logger.warning(msg)
            return Response(response=msg, status=200)

        if not '@' in new_email:
            msg = "'%s Survivor email '%s' does not look like an email address! Ignoring..." % (self, new_email)
            self.logger.warning(msg)
            return Response(response=msg, status=422)

        if utils.mdb.users.find_one({'login': new_email}) is None:
            msg = "The email address '%s' is not associated with any known user." % new_email
            self.logger.error(msg)
            return Response(response=msg, status=422)

        # if we're still here, do it.
        old_email = self.survivor["email"]
        self.survivor["email"] = new_email

        self.log_event("%s changed the manager of %s from '%s' to '%s'." % (
            request.User.login,
            self.survivor['name'],
            old_email,
            self.survivor["email"]
            )
        )
        self.save()
        return utils.http_200


    @web_method
    def set_name(self, new_name=None, update_survival=True, save=True):
        """ Sets the survivor's name. Logs it. """

        #
        #   Initialize, normalize and sanity check!
        #
        if new_name is None:
            self.check_request_params(["name"])
            new_name = self.params["name"]

        # normalize incoming names, which can contain HTML an prefix/suffix
        #   white space, both of which are banned
        new_name = utils.html_stripper(new_name).strip()

        # handle blanks, i.e. set the survivor to 'Anonymous'
        if new_name in ["", u""]:
            new_name = "Anonymous"

        # bail if we don't have a change.
        if new_name == self.survivor["name"]:
            warn = "%s Survivor name unchanged! Ignoring set_name() call..."
            self.logger.warning(warn, self)
            return True

        # now do it!
        old_name = self.survivor["name"]
        self.survivor["name"] = new_name

        if save:
            self.log_event(
                "%s renamed %s to %s" % (
                    request.User.login, old_name, new_name
                )
            )
            self.save()

        if (
            update_survival and
            old_name.upper() == "ANONYMOUS" and
            new_name.upper() != old_name.upper()
        ):
            self.set_survival(
                value = self.survivor['survival'] + 1,
                save=save
            )


    @web_method
    def set_parent(self, role=None, oid=None):
        """ Sets the survivor's 'mother' or 'father' attribute. """

        if role is None or oid is None:
            self.check_request_params(['role', 'oid'])
            role = self.params['role']
            oid = self.params['oid']

        oid = ObjectId(oid)

        if role not in ['father', 'mother']:
            err = "Parent 'role' value must be 'father' or 'mother'!"
            raise utils.InvalidUsage(err)

        new_parent = utils.mdb.survivors.find_one({"_id": oid})

        if new_parent is None:
            raise utils.InvalidUsage("Parent OID '%s' does not exist!" % oid)

        if new_parent['settlement'] != self.survivor['settlement']:
            err = 'Parent and child must belong to the same settlement!'
            raise utils.InvalidUsage(err)

        if oid == self.survivor.get(role, None):
            err = "%s %s is already %s. Ignoring request..."
            self.logger.warning(err, self, role, new_parent["name"])
            return True

        self.survivor[role] = ObjectId(oid)
        msg = "%s updated %s lineage: %s is now %s"
        self.log_event(
            msg % (
                request.User.login,
                self.pretty_name(),
                role,
                new_parent["name"]
            )
        )
        self.save()


    @web_method
    def set_partner(self, partner_oid=None, update_partner=True):
        """ Request context optional. Sets (or unsets) the survivor's partner
        if 'partner_oid' is set to 'UNSET' (all caps).

        Also has the ability to update their previous/outgoing/incoming partner
        via the 'update_partner' (boolean) kwarg.
        """

        # back off to the request to get params or die trying
        if partner_oid is None:
            self.check_request_params(['partner_id'])
            partner_oid = self.params['partner_id']

        # bail if the request is bogus
        if (
            partner_oid == 'UNSET' and not
            self.survivor.get('partner_id', False)
        ):
            self.logger.warning('%s has no partner!', self)
            warn = '%s Ignoring bogus request to unset partner...' % self
            self.logger.warning(warn)
            return True


        #
        #   do actual work
        #

        # process unset requests first
        if partner_oid == 'UNSET' and self.survivor.get('partner_id', False):

            # unset the partner, if 'updater_partner' kwarg == True
            if update_partner:
                p_obj = Survivor(
                    _id=self.survivor['partner_id'],
                    Settlement=self.Settlement
                )
                p_obj.set_partner(partner_oid='UNSET', update_partner=False)

            # unset the survivor
            del self.survivor['partner_id']
            self.log_event("%s no longer has a partner." % self.pretty_name())
            self.save()
            return True


        # if we're still here, make sure we've got a valid oid for the incoming
        #   partner and then initialize them
        partner_obj = Survivor(_id=partner_oid, Settlement=self.Settlement)

        # bail if partner_obj is already our survivor's partner
        if partner_obj._id == self.survivor.get('partner_id', None):
            msg = "%s Ignoring bogus request to set partner (is already %s)."
            self.logger.warning(msg, self, partner_obj)
            return True

        # if our survivor HAS a partner but it is NOT the incoming one, unset
        #   the old/outgoing partner's partner (i.e. our survivor)
        if (
            self.survivor.get('partner_id', None) is not None and
            partner_obj._id != self.survivor['partner_id']
        ):
            if update_partner:
                partner_obj.set_partner(
                    partner_oid='UNSET',
                    update_partner=False
                )

        # set the NEW/incoming partner on our current survivor
        self.survivor['partner_id'] = ObjectId(partner_oid)
        msg = '%s is partners with %s!'
        self.log_event(msg % (self.pretty_name(), partner_obj.survivor['name']))
        self.save()

        # finally, if we're updating the partner to have our survivor as their
        #   partner, do that and return True
        if update_partner:
            partner_obj.set_partner(
                partner_oid=self.survivor['_id'], update_partner=False
            )

        return True


    @web_method
    def set_retired(self, retired=None):
        """ Set to true or false. Backs off to request params is 'retired' kwarg
        is None. Does a little user-friendliness/sanity-checking."""

        if retired is None:
            retired = self.params.get("retired", None)
            if retired is None:
                retired = self.params.get('value', None)
                if retired is None:
                    raise utils.InvalidUsage("'retired' or 'value' required!")

        if not isinstance(retired, bool):
            raise utils.InvalidUsage('Boolean required!')

        if self.survivor.get('retired', 'UNDEFINED') == retired:
            err = "%s Already has 'retired' = '%s'. Ignoring bogus request..."
            self.logger.warning(err, self, retired)
            return True

        self.survivor["retired"] = retired
        if self.survivor["retired"]:
            self.log_event("%s has retired %s." % (
                request.User.login,
                self.pretty_name()
                )
            )
            self.survivor['retired_in'] = self.get_current_ly()
        else:
            del self.survivor["retired"]
            try:
                del self.survivor['retired_in']
            except Exception as error:
                self.logger.debug(error)
            self.log_event("%s has taken %s out of retirement." % (
                    request.User.login,
                    self.pretty_name()
                )
            )
        self.save()


    @web_method
    def set_savior_status(self, color=None, unset=False):
        """ Makes the survivor a savior or removes all savior A&Is. """

        if "unset" in self.params:
            unset = True

        # handle 'unset' operations first
        if unset and self.is_savior():
            s_dict = self.Settlement.Saviors.get_asset_by_color(
                self.is_savior()
            )

            for ai_handle in s_dict["abilities_and_impairments"]:
                self.rm_game_asset(
                    "abilities_and_impairments", ai_handle, rm_related=False
                )

            del self.survivor["savior"]
            self.save()
            msg = "%s unset savior status for %s"
            self.log_event(msg, request.User.login, self.pretty_name())
            return True

        if unset and not self.is_savior():
            self.logger.error(
                "%s Not a savior: cannot unset savior status!", self
            )
            return False

        # now handle 'set' operations
        if color is None:
            self.check_request_params(["color"])
            color = self.params["color"]

        # bail if this is redundant/double-click
        if color == self.is_savior():
            self.logger.error(
                "%s is already a %s savior. Ignoring...", self, color
            )
            return False

        # remove previous if we're switching
        if self.is_savior() and color != self.is_savior():
            msg = "%s changing savior color from %s to %s..."
            self.logger.warning(msg, self, self.is_savior(), color)
            s_dict = self.Settlement.Saviors.get_asset_by_color(
                self.is_savior()
            )
            for ai_handle in s_dict["abilities_and_impairments"]:
                self.rm_game_asset(
                    "abilities_and_impairments", ai_handle, rm_related=False
                )

        # finally, if we're still here, set it
        self.survivor["savior"] = color
        s_dict = self.Settlement.Saviors.get_asset_by_color(color)
        for ai_handle in s_dict["abilities_and_impairments"]:
            self.add_game_asset(
                "abilities_and_impairments", ai_handle, apply_related=False
            )

        self.log_event(
            "A savior is born! %s applied %s savior status to %s" % (
                request.User.login,
                color,
                self.pretty_name()),
                event_type="savior_birth"
            )

        self.save()


    @web_method
    def set_sex(self, sex=None):
        """ Sets self.survivor["sex"] attribute. Can only be 'M' or 'F'.

        Note that this should not be used to set the survivor's 'effective sex',
        i.e. in the event of a Gender Swap curse, etc.

        'Effective sex' is determined automatically (see the get_effective_sex()
        method in this module for more info.

        If the 'sex' kwarg is None, this method assumes that it is being called
        by request_response() and will look for 'sex' in self.params.
        """

        # try to get a kwarg, a post param and a backoff post param
        if sex is None:
            sex = self.params.get('value', None)
            if sex is None:
                sex = self.params.get("sex", None)

        sex = sex.upper()

        if sex not in ["M", "F"]:
            msg = "'sex' must be 'M' or 'F'. Survivor sex cannot be '%s'." % sex
            self.logger.exception(msg)
            raise utils.InvalidUsage(msg, status_code=400)

        self.survivor["sex"] = sex
        self.log_event(
            "%s set %s sex to '%s'." % (
                request.User.login,
                self.pretty_name(),
                sex
            )
        )
        self.save()


    @web_method
    def set_special_attribute(self):
        """ Sets an arbitrary attribute handle on the survivor. Saves. Expects a
        request context. """

        # initialize and validate
        self.check_request_params(['handle','value'])
        handle = self.params['handle']
        value = self.params['value']

        sa_dict = self.Settlement.SpecialAttributes.get_asset(handle)

        self.survivor[handle] = value

        if value and 'epithet' in sa_dict:
            self.add_game_asset('tags', sa_dict['epithet'])
        elif not value and 'epithet' in sa_dict:
            self.rm_game_asset('tags', sa_dict['epithet'])

        if value:
            msg = "%s added '%s' to %s." % (
                request.User.login, sa_dict['name'], self.pretty_name()
            )
        else:
            msg = "%s removed '%s' from %s." % (
                request.User.login, sa_dict['name'], self.pretty_name()
            )
        self.log_event(msg)

        self.save()


    @web_method
    def set_status_flag(self, flag=None, unset=False):
        """ Sets or unsets a status flag, regardless of previous status of that
        flag.

        If 'flag' is None, this method assumes that it is being called by the
        request_response() method and will check for incoming params.

        Set the 'unset' kwarg to True to force unset the value.
        """

        if flag is None:
            self.check_request_params(['flag'])
            flag = self.params["flag"]

        if 'unset' in self.params or self.params.get('value', None) is False:
            unset = True

        if flag not in self.DATA_MODEL.category('flag'):
            msg = "Survivor status flag '%s' cannot be set!" % flag
            raise utils.InvalidUsage(msg, status_code=400)

        flag_pretty = flag.replace("_", " ").capitalize()

        if unset and self.survivor.get(flag, None) is not None:
            del self.survivor[flag]
            self.log_event(
                "%s removed '%s' from %s" % (
                    request.User.login,
                    flag_pretty,
                    self.pretty_name()
                )
            )
        else:
            self.survivor[flag] = True
            self.log_event(
                "%s set '%s' on %s" % (
                    request.User.login,
                    flag_pretty,
                    self.pretty_name()
                )
            )

        self.save()


    @web_method
    def set_survival(self, value=None, save=True):
        """ Sets survivor["survival"] to 'value'. Respects settlement rules
        about whether to enforce the Survival Limit. Will not go below zero. """

        if value is None:
            self.check_request_params(["value"])
            value = self.params['value']

        if value is None:
            value = 0
        value = int(value)

        # bail if no change
        if value == self.survivor['survival']:
            return True

        # analyze the change; enforce certain attributes
        orig_survival = copy(self.survivor['survival'])

        operation = 'set'
        if value > orig_survival:
            operation = 'add'
        elif value < orig_survival:
            operation = 'decrease'

        if operation == 'add' and not self.can_gain_survival():
            self.log_event("%s cannot gain survival! Ignoring attempt to increase it..." % self.survivor['name'])
            return False

        # make the change; call apply_survival_limit()
        self.survivor["survival"] = value
        self.apply_survival_limit()

        # finally, if check to see if any change actually occured:
        if self.survivor["survival"] == orig_survival:
            return True

        # log it
        if operation == 'add':
            self.log_event(action='add', key="Survival", value=self.survivor['survival'] - orig_survival)
        elif operation == 'decrease':
            self.log_event(action='dec', key="Survival", value=orig_survival - self.survivor['survival'])
        else:
            self.log_event(action='set', key="Survival", value=self.survivor['survival'])

        if save:
            self.save()


    @web_method
    def set_sword_oath(self):
        """ From the Echoes of Death 3 expansion; 'sword_oath' is a dict that we
        save on the survivor, similar to a special campaign attrib. """

        self.check_request_params(['sword', 'wounds'])

        # initialize it if we don't have it
        if self.survivor.get('sword_oath', None) is None:
            self.survivor['sword_oath'] = {}

        self.survivor['sword_oath']['sword'] = str(self.params['sword'])
        self.survivor['sword_oath']['wounds'] = int(self.params['wounds'])

        # look up the gear handle
        sword = self.Settlement.Gear.get_asset(
            self.survivor['sword_oath']['sword']
        )

        msg = (
            "%s updated Sword Oath values for %s. Sword is '%s' and wounds "
            "are set to %s."
        ) % (
            request.User.login,
            self.pretty_name(),
            sword['name'],
            self.survivor['sword_oath']['wounds']
        )

        self.log_event(msg)

        self.save()


    @web_method
    def set_weapon_proficiency_type(self, handle=None, unset=False, save=True):
        """ Sets the self.survivor["weapon_proficiency_type"] string to a
        handle. """

        # if this is a request, and has the 'unset' param, process it and
        #   return immediately
        if (
            self.params.get('unset', None) is not None or
            unset == True
        ):
            self.survivor['weapon_proficiency_type'] = ''
            msg = '%s unset weapon proficiency type for %s.' % (
                request.User.login,
                self.pretty_name()
            )
            self.log_event(msg)
            self.save()
            return True

        # now, do normal processing
        if handle is None:
            self.check_request_params(["handle"])
            handle = self.params["handle"]

        # bail if we get a blank/empty handle (it's not a change)
        if handle == '':
            return True

        # bail if this is unnecessary
        if self.survivor['weapon_proficiency_type'] == handle:
            self.logger.debug(
                "%s No change to Weapon Proficiency type. Ignoring...", self
            )
            return True

        # now, validate and UPDATE THE ATTRIB
        if self.DATA_MODEL.is_valid(
            'weapon_proficiency_type', handle, raise_on_failure=True
        ):
            self.survivor["weapon_proficiency_type"] = handle

        # log it
        w_dict = self.Settlement.WeaponProficiency.get_asset(handle)
        msg = "%s set weapon proficiency type to '%s' for %s" % (
            request.User.login,
            w_dict["name"],
            self.pretty_name()
        )
        self.log_event(msg)

        if save:
            self.save() # <-- calls _validate_weapon_proficiency_type()


    #
    #   validation methods, i.e. business- and game-logic enforcement
    #       IMPORTANT! These never save(), because they get called during save()
    #


    def _validate_max_bleeding_tokens(self):
        ''' Makes sure we never go below one. '''
        if self.survivor.get('max_bleeding_tokens', 1) < 1:
            self.set_attribute(attrib='max_bleeding_tokens', value=1)


    def _validate_partnership(self):
        ''' Make sure if the survivor has a partner, they have the partnership
        AI added to their record. '''

        if (
            self.survivor.get('partner_id', None) is not None and not
            'partner' in self.survivor['abilities_and_impairments']
        ):
            msg = "%s has the 'partner_id' attribute and is missing the AI!"
            self.logger.warning(msg, self)
            self.add_game_asset(
                asset_class='abilities_and_impairments',
                asset_handle='partner'
            )


    def _validate_weapon_proficiency_type(self):
        ''' Makes sure that if our survivor qualifies for a specialization or
        mastery A&I that it gets auto-applied. DOES NOT SAVE. '''

        wp_handle = self.survivor.get('weapon_proficiency_type', None)

        # catch values with a literal/string 'None'
        if wp_handle == 'None':
            warn = "%s Weapon proficiency type is 'None' (str)!"
            self.logger.warning(warn, self)
            self.set_weapon_proficiency_type(unset=True)
            wp_handle = None

        # return True if we don't actually have one set or don't care
        if (
            wp_handle is None or
            wp_handle == '' or
            self.survivor.get('weapon_proficiency_sealed', False)
        ):
            return True

        try:
            wp_dict = self.Settlement.WeaponProficiency.get_asset(wp_handle)
        except utils.InvalidUsage:
            msg = "%s Unknown Weapon Proficiency '%s' cannot be validated!"
            self.logger.warning(msg, self, wp_handle)
            return True

        thresholds = [
            {'value': 3, 'ai': 'specialist_ai', 'desc': 'specialization'},
            {'value': 8, 'ai': 'mastery_ai', 'desc': 'mastery'},
        ]

        for threshold in thresholds:
            if self.survivor.get('Weapon Proficiency', 0) >= threshold['value']:
                if (
                    wp_dict.get(threshold['ai'], None) not in
                    self.survivor['abilities_and_impairments']
                ):
                    msg = "%s Weapon %s reached, but A&I not present!"
                    self.logger.info(msg, self, threshold['desc'])
                    self.add_game_asset(
                        "abilities_and_impairments",
                        wp_dict['specialist_ai'],
                        save=False,
                        log_event=True
                    )


    #
    #   defaults and resets
    #

    @web_method
    def default_attribute(self, attrib=None, save=True):
        ''' Sets 'attrib' to its default value (as defined in the Survivor
        class data model. '''

        # get the attrib
        if attrib is None:
            self.check_request_params(['attribute'])
            attrib = self.params["attribute"]

        # get the model
        model = getattr(self.DATA_MODEL, attrib)

        # use the model's default
        self.survivor[attrib] = model['default']

        msg = "%s defaulted %s '%s' to %s"
        self.log_event(
            msg % (
                request.User.login,
                self.pretty_name(),
                attrib,
                self.survivor[attrib]
            )
        )

        if save:
            self.save()


    @web_method
    def reset_attribute_details(self, save=True):
        """ Zero-out all attribute_detail values and will overwrite with
        extreme prejudice. """

        self.survivor["attribute_detail"] = {
            "Strength": {"tokens": 0, "gear": 0},
            "Evasion":  {"tokens": 0, "gear": 0},
            "Movement": {"tokens": 0, "gear": 0},
            "Luck":     {"tokens": 0, "gear": 0},
            "Speed":    {"tokens": 0, "gear": 0},
            "Accuracy": {"tokens": 0, "gear": 0},
        }

        if save:
            self.save()


    def __set_damage(self, save=True):
        ''' Private diversion route from the public set_attribute() method.
        Requires a request. Sets a damage location to a bool value. '''

        attrib = self.params.get("attribute", None)     # location
        value = bool(self.params.get('value', False))   # boolean on/off

        self.DATA_MODEL.is_valid(attrib, value, raise_on_failure=True)

        self.survivor[attrib] = value

        if value:
            self.log_event(value=attrib, key="ON")
        else:
            self.log_event(value=attrib, key="OFF")

        if save:
            self.save()



    @web_method
    def reset_damage(self, save=True):
        """ Remove all damage attribs/bools from the survivor. """

        for dmg_loc in self.DATA_MODEL.category('damage_location'):
            if dmg_loc in self.survivor.keys():
                del self.survivor[dmg_loc]

        if save:
            self.save()


    #
    #   get methods
    #

    def pretty_name(self):
        """ Returns the survivor's name in a prettified way, e.g. 'Timothy [M]'.
        Meant to be an alternative for the __repr__() way of doing it, which
        includes the asset's OID. Use this method when calling log_event().

        NB! This returns the survivor's effective sex (i.e. calls self.get_sex()
        instead of using the base attribute), which is different from the way
        the __repr__() method does it!
        """

        return "%s [%s]" % (self.survivor["name"], self.get_sex())


    def get_available_endeavors(self, return_type=None):
        """ Works like a miniature version of the Settlement method of the same
        name. Returns a list of handles instead of a big-ass JSON thing,
        however.

        Set 'return_type' to dict to get a dictionary instead of a list of
        handles.
        """

        endeavors_obj = self.Settlement.Endeavors

        def check_availability(e_handle):
            """ Private method that checks whether an endeavor is currently
            available to the survivor. """
            e_dict = endeavors_obj.get_asset(e_handle)
            available = True
            if e_dict.get('requires_returning_survivor', False):
                r_years = self.survivor.get('returning_survivor', [])
                if (
                    self.get_current_ly() not in
                    r_years and
                    self.get_current_ly() - 1 not in r_years
                ):
                    available = False
            return available


        e_handles = set()
        for asset_family in ['abilities_and_impairments', 'fighting_arts']:
            for a_dict in self.list_assets(asset_family):
                for e_handle in a_dict.get('endeavors', []):
                    if check_availability(e_handle):
                        e_handles.add(e_handle)
        e_handles = sorted(list(e_handles))

        # return dictionary.
        if return_type == dict:
            output = {}
            for e_handle in e_handles:
                output[e_handle] = endeavors_obj.get_asset(e_handle)
            return output

        return e_handles


    def get_dragon_traits(self, return_type=dict):
        """ Returns survivor Dragon Traits. """

        traits = []

        # check Understanding for 9+
        if int(self.survivor["Understanding"]) >= 9:
            traits.append("9 Understanding (max)")

        # check self.survivor["expansion_attribs"] for "Reincarnated surname",
        #   "Scar","Noble surname"
        for attrib in [
            "potstars_reincarnated_surname",
            "potstars_scar",
            "potstars_noble_surname"
        ]:
            if self.survivor.get(attrib, False):
                a_dict = self.Settlement.SpecialAttributes.get_asset(attrib)
                traits.append(a_dict['name'])

        # check the survivor name too
        split_name = self.survivor["name"].split(" ")
        for surname in ["Noble","Reincarnated"]:
            if surname in split_name and "%s surname" % surname not in traits:
                traits.append(surname + " surname")

        # check A&Is for Oracle's Eye, Iridescent Hide, Pristine,
        for a_dict in [
            self.Settlement.AbilitiesAndImpairments.get_asset('oracles_eye'),
            self.Settlement.AbilitiesAndImpairments.get_asset('pristine'),
            self.Settlement.AbilitiesAndImpairments.get_asset('iridescent_hide')
        ]:
            if a_dict["handle"] in self.survivor["abilities_and_impairments"]:
                traits.append("%s ability" % a_dict["name"])

        # check for any weapon mastery
        for wm_asset in \
        self.Settlement.AbilitiesAndImpairments.get_assets_by_sub_type(
            sub_type = 'mastery',
            return_type = dict
        ):
            if wm_asset["handle"] in self.survivor["abilities_and_impairments"]:
                traits.append("Weapon Mastery")

        # check disorders for "Destined"
        if "destined" in self.survivor["disorders"]:
            traits.append("Destined disorder")

        # check fighting arts for "Fated Blow", "Frozen Star",
        #   "Unbreakable", "Champion's Rite"
        for fa_handle in [
            'champions_rite', 'fated_blow', 'frozen_star', 'unbreakable'
        ]:
            if fa_handle in self.survivor["fighting_arts"]:
                fa_dict = self.Settlement.FightingArts.get_asset(fa_handle)
                fa_name = copy(fa_dict["name"])
                if fa_name == "Frozen Star":
                    fa_name = "Frozen Star secret"
                traits.append("%s fighting art" % fa_name)

        # check for 3+ strength
        if int(self.survivor["Strength"]) >= 3:
            traits.append("3+ Strength attribute")

        # check for 1+ Accuracy
        if int(self.survivor["Accuracy"]) >= 1:
            traits.append("1+ Accuracy attribute")

        # check Courage for 9+
        if int(self.survivor["Courage"]) >= 9:
            traits.append("9 Courage (max)")

        # support multiple return_type vars
        if return_type == "active_cells":
            cells = set()
            the_constellations = self.Settlement.TheConstellations
            c_map = the_constellations.get_asset('lookups')["map"]
            for trait in traits:
                if trait in c_map.keys():
                    cells.add(c_map[trait])
            return list(cells)

        if return_type == 'available_constellations':
            constellations = set()
            active_cells = self.get_dragon_traits('active_cells')
            the_constellations = self.Settlement.TheConstellations
            c_formulae = the_constellations.get_asset('lookups')["formulae"]

            # k = "Witch", v = set(["A1","A2","A3","A4"])
            for key, value in c_formulae.items():
                if value.issubset(active_cells):
                    constellations.add(key)
            return list(constellations)

        # if no return_type, just return the trait list
        return traits



    def get_lineage(self):
        """ DO NOT call this method during normal serialization: it is a PIG and
        running it on more than one survivor at once is a really, really bad
        idea.

        Also, it returns a Response object. So yeah.

        This method creates a dictionary of survivor lineage information. """

        # initialize
        output = {
            'intimacy_partners': set(),
            'siblings': { 'full': [], 'half': [] },
        }

        # PROCESS parents first w the survivor version of get_parents() b/c that's easy
        survivor_parents = self.get_parents(dict)
        output['parents'] = survivor_parents

        # now PROCESS the settlement's get_parents() output for partners, children and sibs
        children = set()
        siblings = {'full': set(), 'half': set()}

        couplings = self.Settlement.get_parents()
        for coupling in couplings:
            if self.survivor['_id'] == coupling['father']:
                output['intimacy_partners'].add(coupling['mother'])
                children = children.union(coupling['children'])
            elif self.survivor['_id'] == coupling['mother']:
                output['intimacy_partners'].add(coupling['father'])
                children = children.union(coupling['children'])

            # full-blood sibs
            if self.survivor['_id'] in coupling['children']:
                siblings['full'] = coupling['children'] # you can only have one set of full-blood sibs, right?

            # half-blood sibs
            if survivor_parents != {'father': None, 'mother': None}:
                if survivor_parents['father']['_id'] == coupling['father'] and survivor_parents['mother']['_id'] != coupling['mother']:
                    siblings['half'] = siblings['half'].union(coupling['children'])
                if survivor_parents['father']['_id'] != coupling['father'] and survivor_parents['mother']['_id'] == coupling['mother']:
                    siblings['half'] = siblings['half'].union(coupling['children'])


        #
        #   Post-process
        #

        # process sibling oids and make lists of dictionaries
        for k in siblings: # i.e. 'half' or 'full'
            for sib in siblings[k]:
                if sib == self.survivor["_id"]:
                    pass # can't be your own sib
                else:
                    output['siblings'][k].append(
                        utils.mdb.survivors.find_one({'_id': sib})
                    )

        # retrieve children from mdb; process oid lists into dictionaries
        output['children'] = {}
        for parent in output['intimacy_partners']:
            output['children'][str(parent)] = []
        for child in children:
            child_dict = utils.mdb.survivors.find_one({'_id': child})
            if child_dict['father'] == self.survivor['_id']:
                output['children'][str(child_dict['mother'])].append(child_dict)
            elif child_dict['mother'] == self.survivor['_id']:
                output['children'][str(child_dict['father'])].append(child_dict)

        # sort the children on their born in LY
        for p_id in output['children']:
            output['children'][p_id] = sorted(
                output['children'][p_id], key=lambda k: k['born_in_ly']
            )

        # get fuck buddy survivor data from mdb
        output['intimacy_partners'] = [
            utils.mdb.survivors.find_one({'_id': s}) for
            s in output['intimacy_partners']
        ]

        output['events'] = self.Settlement.get_event_log(survivor_id=self._id)

        return Response(
            response=json.dumps(output, default=json_util.default),
            status=200,
            mimetype="application/json"
        )


    def get_notes(self):
        """ Gets the survivor's notes as a list of dictionaries. """
        notes = utils.mdb.survivor_notes.find({
            "survivor_id": self.survivor["_id"],
            "created_on": {"$gte": self.survivor["created_on"]}
        }, sort=[("created_on",1)])
        return list(notes)


    def get_parents(self, return_type=None):
        """ Returns survivor OIDs for survivor parents by default. Set
        'return_type' to 'dict' (w/o the quotes) to get survivor dictionaries
        back. """

        parents = []
        for parent in ["father", "mother"]:
            if parent in self.survivor.keys():
                parents.append(self.survivor[parent])

        if return_type == dict:
            output = {'mother': None, 'father': None}
            for p_oid in parents:
                p_record = utils.mdb.survivors.find_one({'_id': p_oid})
                if p_record is not None:
                    if p_record["sex"] == 'M':
                        output['father'] = p_record
                    elif p_record['sex'] == 'F':
                        output['mother'] = p_record
                    else:
                        raise ValueError('Invalid sex: %s' % p_record['sex'])
            return output

        return parents


    def get_sex(self):
        """ Returns a string value of 'M' or 'F' representing the survivor's
        current effective sex. The basic math here is that we start from the
        survivor's sheet on their sex and then apply any curses, etc. to get
        our answer. """

        sex = self.survivor["sex"]

        def invert_sex(s_sex):
            if s_sex == "M":
                return "F"
            return "M"

        for ai_dict in self.list_assets("abilities_and_impairments"):
            if ai_dict.get("reverse_sex", False):
                sex = invert_sex(sex)

        return sex


    def get_surname(self):
        """ Splits the survivor's name on whitespace and returns the last part.
        Returns None if the survivor has no surname. """

        split_name = self.survivor['name'].split(" ")
        if len(split_name) == 1:
            return None
        return split_name[-1]




    def get_tags(self, return_type=None):
        ''' Returns survivor tags as a list. '''

        if return_type == "pretty":
            tags_obj = self.Settlement.Tags
            output = ""
            for t_handle in self.survivor['tags']:
                t_asset = tags_obj.get_asset(t_handle)
                output += t_asset["name"]
            return output

        return self.survivor['tags']



    #
    #   evaluation / biz logic methods
    #



    def can_be_nominated_for_intimacy(self):
        """ Returns a bool representing whether the survivor can do the
        mommmy-daddy dance. """


        for ai_dict in self.list_assets("abilities_and_impairments"):
            if ai_dict.get("cannot_be_nominated_for_intimacy", False):
                return False

        if self.is_dead():
            return False

        return True


    def can_gain_survival(self):
        """ Returns a bool representing whether or not the survivor can GAIN
        survival. This is not whether they can SPEND survival. """

        for ai_dict in self.list_assets("abilities_and_impairments"):
            if ai_dict.get("cannot_gain_survival", False):
                return False

        return True


    def can_gain_bleeding_tokens(self):
        """ Returns a bool describing whether the survivor can gain bleeding
        tokens. """

        if self.survivor.get('cannot_gain_bleeding_tokens', None) is None:
            return True
        return False


    def cannot_activate_two_handed_weapons(self):
        """ Returns a bool representing whether the survivor can activate +2 str
        gear. """

        if 'cannot_activate_two_handed_weapons' in self.survivor.keys():
            return self.survivor['cannot_activate_two_handed_weapons']

        for ai_dict in self.list_assets('abilities_and_impairments'):
            if ai_dict.get('cannot_activate_two_handed_weapons', False):
                return True

        return False


    def cannot_activate_two_plus_str_gear(self):
        """ Returns a bool representing whether the survivor can activate +2 str
        gear. """

        if 'cannot_activate_two_plus_str_gear' in self.survivor.keys():
            return self.survivor['cannot_activate_two_plus_str_gear']

        for ai_dict in self.list_assets('abilities_and_impairments'):
            if ai_dict.get('cannot_activate_two_plus_str_gear', False):
                return True

        return False


    def cannot_be_nominated_for_intimacy(self):
        """ Returns a bool for the negative way of asking this question."""

        if 'cannot_be_nominated_for_intimacy' in self.survivor.keys():
            return self.survivor['cannot_be_nominated_for_intimacy']

        for ai_dict in self.list_assets('abilities_and_impairments'):
            if ai_dict.get('cannot_be_nominated_for_intimacy', False):
                return True

        return False


    def cannot_consume(self):
        """ Returns a bool representing whether the survivor can activate +2 str
        gear. """

        if 'cannot_consume' in self.survivor.keys():
            return self.survivor['cannot_consume']

        for ai_dict in self.list_assets('abilities_and_impairments'):
            if ai_dict.get('cannot_consume', False):
                return True

        return False


    def cannot_activate_weapons(self):
        """ Returns a bool representing whether the survivor can activate
        weapons. As far as 1.5 and expansion content goes, there's only one
        scenario that causes this to come back false. """

        if self.survivor['abilities_and_impairments'].count('dismembered_arm') == 2:
            return True
        return False


    def cannot_spend_survival(self):
        """ Returns a bool representing whether or not the survivor can SPEND
        survival. This is not whether they can GAIN survival. """

        if self.survivor.get("cannot_spend_survival", None) is True:
            return True

        for ai_dict in self.list_assets("abilities_and_impairments"):
            if ai_dict.get("cannot_spend_survival", False):
                return True

        return False


    def cannot_use_fighting_arts(self):
        """Returns a bool representing whether or not the survivor can use
        Fighting Arts. """

        if self.survivor.get("cannot_use_fighting_arts", None) is True:
            return True

        for ai_dict in self.list_assets("abilities_and_impairments"):
            if ai_dict.get("cannot_use_fighting_arts", False):
                return True

        return False


    def is_dead(self):
        """Returns a bool of whether the survivor is dead."""

        if "dead" in self.survivor.keys():
            return True

        return False


    def is_departing(self):
        """ Returns a bool of whether the survivor is departing. """

        return self.survivor.get('departing', False)


    def is_founder(self):
        """Returns a bool of whether the survivor is a founding survivor. """

        if self.survivor["born_in_ly"] == 0:
            return True

        return False


    def is_savior(self):
        """ Returns False if the survivor is NOT a savior; returns their color
        if they are (which should evaluate to Boolean true wherever we evaluate
        it, right?). """

        # automatically return false if the campaign doesn't have saviors
#        if self.get_campaign(dict).get("saviors", None) is None:
        if self.Settlement.campaign.asset.get('saviors', None) is None:
            return False

        # automatically return the survivor's 'savior' attrib if the survivor
        # is a savior
        if self.survivor.get("savior", False):
            return self.survivor["savior"]

        # now do the legacy check
        for s_dict in self.Settlement.Saviors.get_dicts():
            for s_ai in s_dict["abilities_and_impairments"]:
                if s_ai in self.survivor["abilities_and_impairments"]:
                    return s_dict["color"]

        return False


    def skip_next_hunt(self):
        """Returns a bool representing whether or not the survivor has to sit
        the next one out. """

        if self.survivor.get("skip_next_hunt", None) is True:
            return True

        return False


    #
    #   private get and evaluation methods
    #

    def __get_survival_actions(self, return_type=dict):
        """ Returns the SA's available to the survivor based on current
        impairments, etc. Use 'return_type' = 'JSON' to get a list of dicts
        back, rather than a single dict.

        Important! There's a ton of business logic here, given that there's a
        lot of interplay among game assets, so read this carefully and all the
        way through before making changes!
        """

        # tiny helper called later in the func
        def update_available(sa_key_list, available=False, title_tip=None):
            """ Inline helper func to update the list of available_actions while
            iterating over survivor attributes. """

            for sa_key in sa_key_list:
                if not available:
                    if sa_key in available_actions.keys():
                        available_actions[sa_key]["available"] = False
                        available_actions[sa_key]["title_tip"] = title_tip
                elif available:
                    s_action = self.Settlement.SurvivalActions.get_asset(sa_key)
                    s_action["available"] = True
                    s_action["title_tip"] = title_tip
                    available_actions[sa_key] = s_action


        #
        #   action starts here. initialize and set defaults first:
        #

        available_actions = self.Settlement.get_survival_actions()

        # check A&Is and FAs/SFAs   # disorders coming soon! TKTK
        attrib_keys = ['abilities_and_impairments', 'fighting_arts']

        for attr_key in attrib_keys:
            for a_dict in self.list_assets(attr_key):       # iterate assets
                if "survival_actions" in a_dict.keys():     # check for key

                    # handle 'enable' keys; special logic re: can't use FAs
                    if (
                        attr_key == 'fighting_arts' and
                        self.cannot_use_fighting_arts()
                    ):
                        pass
                    else:
                        update_available(
                            a_dict["survival_actions"].get("enable", []),
                            available=True,
                            title_tip="Available due to '%s'" % a_dict["name"],
                        )

                    # handle 'disable' keys
                    slug="Impairment '%s' prevents %s from using this ability."
                    update_available(
                        a_dict["survival_actions"].get("disable", []),
                        available=False,
                        title_tip=slug % (a_dict["name"], self.survivor["name"])
                    )


        # support JSON return
        if return_type == 'JSON':
            output = []
            for dummy, action_dict in available_actions.items():
                output.append(action_dict)
            return sorted(output, key=lambda k: k['sort_order'])

        # dict return
        return available_actions


    #
    #   private conversion and normalization methods
    #

    def __baseline(self):
        """ Baselines the MDB doc to bring it into compliance with our general
        data model for survivors.

        We update the actual data in the MDB, rather than simply having a base-
        line model (e.g. in a config file somewhere) and then initializing new
        assets such that they overwrite/fill-in the blanks.

        This might seem like an odd design decision, but the data is designed to
        be portable, so we inflict/enforce a lot of the model on the 'database'.
        """

        if "meta" not in self.survivor.keys():
            self.logger.warning("Creating 'meta' key for %s", self)
            self.survivor["meta"] = {}
            self.perform_save = True

        if "attribute_detail" not in self.survivor.keys():
            self.reset_attribute_details(save=False)
            self.perform_save = True

        if 'affinities' not in self.survivor.keys():
            self.survivor["affinities"] = self.DATA_MODEL.affinities['default']
            self.perform_save = True

        if 'bleeding_tokens' not in self.survivor.keys():
            self.survivor["bleeding_tokens"] = 0
            msg = "Adding baseline 'bleeding_tokens' (int) attrib to %s"
            self.logger.info(msg, self)
            self.perform_save = True

        if 'max_bleeding_tokens' not in self.survivor.keys():
            self.survivor["max_bleeding_tokens"] = 5
            msg = "Adding baseline 'max_bleeding_tokens' (int) attrib to %s"
            self.logger.info(msg, self)
            self.perform_save = True

        if 'cursed_items' not in self.survivor.keys():
            self.survivor["cursed_items"] = []
            self.perform_save = True

        if 'public' not in self.survivor.keys():
            self.survivor["public"] = False
            self.perform_save = True
        elif self.survivor["public"] == "checked":
            self.survivor["public"] = True
            self.perform_save = True

        if 'fighting_arts_levels' not in self.survivor.keys():
            self.survivor['fighting_arts_levels'] = {}
            self.perform_save = True

        if 'in_hunting_party' in self.survivor.keys():
            if self.survivor['in_hunting_party'] is True:
                self.survivor['departing'] = True
            else:
                self.survivor['departing'] = False
            del self.survivor['in_hunting_party']
            msg = "Removed deprecated attribute 'in_hunting_party' from %s"
            self.logger.info(msg, self)
            self.perform_save = True

        if 'favorite' not in self.survivor.keys():
            self.survivor["favorite"] = []
            self.perform_save = True

        if self.survivor.get('epithets', None) is not None:
            self.__deprecate_epithets()
            self.perform_save = True


    def __bug_fixes(self, force_save=False):
        """ This should be called during normalize() BEFORE you call baseline().

        Compare with the way this works on the Settlement object. Make sure all
        bugs are dated and have a ticket number, so we can remove them after a
        year has passed.
        """

        # 2017-10-25 The "king's_step" bug
        if "king's_step" in self.survivor['fighting_arts']:
            msg = "%s King's Step bad asset handle detected! Fixing..."
            self.logger.debug(msg, self)
            self.survivor['fighting_arts'].remove("king's_step")
            self.survivor['fighting_arts'].append('kings_step')
            self.perform_save = True

        # 2017-10-28 The "weak spot" bug (other bad A&Is)
        for bad_handle in [
            'Weak Spot',
            'Intracranial hemmorhage',
            'Weak spot: arms',
            "Weak spot is body.",
        ]:
            if bad_handle in self.survivor['abilities_and_impairments']:
                msg = "%s Bad asset handle '%s' detected! Fixing..."
                self.logger.debug(msg, self, bad_handle)
                self.survivor['abilities_and_impairments'].remove(bad_handle)
                self.perform_save = True

        # 2017-10-22 'acid_palms' asset handle Issue #341
        # https://github.com/toconnell/kdm-manager/issues/341

        if 'acid_palms' in self.survivor['abilities_and_impairments']:
            self.logger.warning(
                "[BUG] Detected 'acid_palms' in survivor A&I list!"
            )
            self.survivor['abilities_and_impairments'].remove('acid_palms')
            if 'gorm' in self.Settlement.get_expansions():
                self.survivor['abilities_and_impairments'].append(
                    'acid_palms_gorm'
                )
                msg = "%s Replaced 'acid_palms' with 'acid_palms_gorm'"
                self.logger.info(msg, self)
            elif 'dragon_king' in self.Settlement.get_expansions():
                self.survivor['abilities_and_impairments'].append(
                    'acid_palms_dk'
                )
                msg = "%s Replaced 'acid_palms' with 'acid_palms_dk'"
                self.logger.info(msg, self)
            else:
                self.logger.error(
                    "Unable to replace 'acid_palms' A&I with a real handle!"
                )
            self.perform_save = True


        # now, if we're forcing a save (e.g. because the settlement is calling
        # method or something, do it
        if force_save and hasattr(self, 'perform_save') and self.perform_save:
            self.save()


    def __convert_abilities_and_impairments(self):
        """ Swaps out A&I names for handles. """

        new_ai = []

        for ai_dict in self.list_assets(
            "abilities_and_impairments", log_failures=True
        ):
            new_ai.append(ai_dict["handle"])
            msg = "%s Migrated A&I '%s' to '%s'"
            self.logger.info(msg, self, ai_dict["name"], ai_dict["handle"])

        self.survivor["abilities_and_impairments"] = new_ai
        self.survivor["meta"]["abilities_and_impairments_version"] = 1.0
        msg = "Converted A&Is from names (legacy) to handles for %s"
        self.logger.info(msg, self)


    def __convert_disorders(self):
        """ Swaps out disorder names for handles. """

        new_d = []

        for d_dict in self.list_assets("disorders", log_failures=True):
            new_d.append(d_dict["handle"])
            msg = "%s Migrated Disorder '%s' to '%s'"
            self.logger.info(msg, self, d_dict["name"], d_dict["handle"])

        self.survivor["disorders"] = new_d
        self.survivor["meta"]["disorders_version"] = 1.0
        msg = "Converted Disorders from names (legacy) to handles for %s"
        self.logger.info(msg, self)


    def __convert_favorite(self):
        """ Turns the 'favorite' attribute from a string to a list of email
        addresses. """

        if self.survivor.get('favorite', None) is None:
            self.survivor['favorite'] = []
        else:
            self.survivor['favorite'] = []
            self.add_favorite(self.survivor["email"])

        self.survivor["meta"]["favorites_version"] = 1.0
        msg = "Converted 'favorite' attrib from str (legacy) to list for %s"
        self.logger.info(msg, self)


    def __convert_fighting_arts(self):
        """ Tries to convert Fighting Art names to to handles. Drops anything
        that it cannot convert. """

        new_fa_list = []

        for fa_dict in self.list_assets("fighting_arts"):
            if fa_dict is None:
                pass
            else:
                new_fa_list.append(fa_dict["handle"])
                msg = "%s Converted '%s' Fighting Art name to handle '%s'"
                self.logger.info(
                    msg, self, fa_dict["name"], fa_dict["handle"]
                )

        self.survivor["fighting_arts"] = new_fa_list
        self.survivor["meta"]["fighting_arts_version"] = 1.0
        msg = "Converted Fighting Arts from names (legacy) to handles for %s"
        self.logger.info(msg, self)


    def __convert_special_attributes(self):
        """ This one's...a hot mess on account of this feature having never
        been properly implemented in the legacy app.

        Basically, there's a list of known special attribute names, and we're
        going to manually crosswalk them to modern handles.
        """

        crosswalk = [
            ('Purified', 'potsun_purified'),
            ('Sun Eater', 'potsun_sun_eater'),
            ('Child of the Sun', 'potsun_child_of_the_sun'),
            ('Scar', 'potstars_scar'),
            ('Reincarnated surname', 'potstars_noble_surname'),
            ('Noble surname', 'potstars_reincarnated_surname'),
        ]

        if 'expansion_attribs' in self.survivor.keys():
            for i in crosswalk:
                name, handle = i
                if name in self.survivor['expansion_attribs'].keys():
                    self.survivor[handle] = True
            del self.survivor['expansion_attribs']
        else:
            pass

        self.survivor["meta"]["special_attributes_version"] = 1.0
        self.logger.info(
            "Converted survivor special attributes for %s", self
        )


    def __convert_weapon_proficiency_type(self):
        """ No longer supported, as of October 2023. """

        raise utils.ConversionException()


    def __deprecate_epithets(self):
        ''' Changes self.survivor['epithets'] to self.survivor['tags']. '''
        self.survivor['tags'] = copy(self.survivor.get('epithets', []))
        del self.survivor['epithets']
        self.logger.info("Converted epithets to tags for %s", self)





    #
    #   NO METHODS BELOW THIS POINT other than request_response()
    #


    def request_response(self, action=None):
        """ Initializes params from the request and then response to the
        'action' kwarg appropriately. This is the ancestor of the legacy app
        assets.Survivor.modify() method. """

        # methods with returns first; nothing comes after if these are the
        #   incoming action we're responding to
        if action == "get":
            return self.json_response()
        if action == "get_lineage":
            return self.get_lineage()
        if action == "set_email":
            return self.set_email()
        if action == "set_avatar":
            return self.set_avatar()

        # now, process 'action', routing to the appropriate web method above
        #   with special handling for if the action is 'add_note'
        if action == 'add_note':
            if 'serialize_on_response' in self.params:
                self.add_note()
            else:
                return self.add_note()
        else:
            # first, if we have a method matching 'action', try to execute it
            #   as long as it's not an internal-only method
            if getattr(self, action, None) is not None:
                method = getattr(self, action)
                if getattr(method, '_web_method', False):
                    method()
                else:
                    err = "The %s endpoint is mapped to an internal method!"
                    return flask.Response(response=err % action, status=400)
            else:
                err = "Survivor action '%s' is not imlemented!" % action
                return flask.Response(response = err, status=501)


        # finish successfully if we executed a method but haven't returned
        if self.params.get('serialize_on_response', False):
            return Response(
                response=self.serialize(),
                status=200,
                mimetype="application/json"
            )

        return utils.http_200

# ~fin
