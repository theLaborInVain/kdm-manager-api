authorization_token_management = {
    "authorization_check": {
        "name": "/authorization/check",
        "desc": """\
<p><b>GET</b> or <b>POST</b> to this endpoint to determine if your Authorization
header is still valid or if it has expired.</p>""",
    },
    "authorization_refresh": {
        "name": "/authorization/refresh",
        "desc": """\
<p> Use the standard 'Authorization' header and <b>POST</b> an empty request to
this route to recieve a new Auth token based on the previous one.</p>
<p> On the back end, this route reads the incoming 'Authorization' header and,
even if the JWT token is expired, will check the 'login' and 'password' (hash)
keys: if they check out, you get a 200 and a brand new token.</p>
<p> Finally, the KDM API does NOT use refresh tokens (it just feels like
overkill, you know?).</p>\
"""
    },
}

administrative_views_and_data = {
    "admin_view_panel": {
        "name": "/admin/view/panel",
        "methods": ["GET","OPTIONS"],
        "desc": """\
<p>Access the API Admin panel. Uses HTTP basic auth (no cookies/no sessions)
and requires a user have the 'admin' bit flipped on their user.</p>
        """,
    },
    "admin_get_user_data": {
        "name": "/admin/get/user_data",
        "methods": ["GET","OPTIONS"],
        "desc": """\
<p>Retrieves a nice, juicy hunk of JSON re: recent users of the API.</p>
        """,
    },
    "admin_get_logs": {
        "name": "/admin/get/logs",
        "methods": ["GET","OPTIONS"],
        "desc": """\
<p>Dumps the contents of a number of system logs from the local filesystem where
the API is running and represents them as JSON.</p>
        """,
    },
}


user_management = {
    "user_get": {
        "name": "/user/get/&lt;user_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": """\
<p>Retrieve a serialized version of the user who owns &lt;user_id&gt;,
to include some additional usage and meta facts about that user.</p>
<p>Like many of the <code><b>GET</b></code> routes supported by the KD:M API,
this route will return user info whether you use <code><b>POST</b></code> or
any other supported method.</p>
        """,
    },
    "z_user_can_create_settlement": {
        "name": "/user/can_create_settlement/&lt;user_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": """\
<p>Returns a Boolean representing whether or not a user is able to create a
new settlement.</p>
<p><b>Important!</b> This always checks the KD:M API's instance-level
configuration settings and is therefore more reliable than other methods,
especially hard-coded integer comparisons, etc.</p>
        """,
    },
    "z_user_dashboard": {
        "name": "/user/dashboard/&lt;user_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": """\
<p>This fetches a serialized version of the user that includes the
<code>/world</code> output as well as a bunch of info about the
user, including their friends, settlements they own or are
playing in, etc.</p>
<p>Here's a run-down of the key elements:</p>
<pre><code>{
    "is_application_admin": true,
    "meta": {...},
    "user": {...},
    "preferences": [...],
    "dashboard": {
        "campaigns": [...],
        "settlements": [...],
    },
}</code></pre>
<p>The top-level <code>dashboard</code> element includes two arrays:
<code>campaigns</code> and <code>settlements</code>.</p>
<p>The <code>campaigns</code> array is a <b>reverse-chronological</b> list
of OIDs of all settlements where the user owns a survivor (i.e.
the survivor's <code>email</code> attribute matches the users
<code>login</code> attribute.</p>
<p>This list can include settlements owned/created by other users:
the basic idea behing the <code>campaigns</code> list is that
you probably want to show these settlements to the user when they
sign in or when they choose which settlement they want to view.</p>
<p>The <code>campaigns</code> array <u>does not</u> include any
'abandoned' settlements (i.e. any settlement with a Boolean True
value for the <code>abandoned</code> attribute.</p>
<p>See <a href="/#settlementAbandon"><code>/settlement/abandon/oid</code>
 (below)</a> for more on abandoning a settlement. </p>
<p>Conrastively, the <code>settlements</code> array is a
<b>chronologically</b> sorted list of all settlement OIDs that belong
 to the current user, whether abandoned or not.</p>
<p>This is more of an archival/historical sort of list, meant to
facilitate that kind of view/list/UX.</p>
""",
    },
    "user_set": {
        "name": "/user/set/&lt;user_id&gt;",
	"subsection": "user_attribute_management",
        "desc": """\
<p>This route supports the assignment of user-specified key/value
attributes to the user object.</p><p>To set an attribute, include
JSON in the body of the request that indicates the key/value to set.</p>
Supported attribute keys include:
    <table class="embedded_table">
        <tr><th>key</th><th>value</th></tr>
        <tr>
            <td>current_settlement</td>
            <td class="text">
                OID of an existing,non-removed settlement.
            </td>
        </tr>
    </table>
Use multiple key/value pairs to set multiple attributes in a single
request, e.g. <code>{"current_settlement": $oid, "current_session":
$oid}</code>
</p>
<p><b>Important!</b> This route does not support the assignment of
arbitrary keys and will completely fail any request that includes
unsupported keys!</p>
        """,
    },
    "user_set_preferences": {
        "name": "/user/set_preferences/&lt;user_id&gt;",
	"subsection": "user_attribute_management",
        "desc": """\
<p><b>POST</b> a list of hashes to this endpoint to set user preferences.</p>
<p>Your list has to be named <code>preferences</code> and your
hashes have to be key/value pairs where they key is a valid
preferences handle and the key is a Boolean:</p>
<code>{preferences: [{handle: "beta", value: true}, {...}]}</code>
<p>Since this is mostly a sysadmin/back-of-house kind of route,
it fails pretty easily if you try to <b>POST</b> something it doesn't
like. The good news, is that it should fail pretty descriptively.</p>
        """,
    },
    "user_add_expansion_to_collection": {
        "name": "/user/add_expansion_to_collection/&lt;user_id&gt;",
        "subsection": "user_collection_management",
        "desc": """\
<p>Starting in July of 2021, this endpoint is deprecated.</p>
<p>Please use <code>/user/set_expansions/&lt;user_id&gt;</code> instead.</p>
        """,
    },
    "user_rm_expansion_from_collection": {
        "name": "/user/rm_expansion_from_collection/&lt;user_id&gt;",
        "subsection": "user_collection_management",
        "desc": """\
<p>Starting in July of 2021, this endpoint is deprecated.</p>
<p>Please use <code>/user/set_expansions/&lt;user_id&gt;</code> instead.</p>
        """,
    },
    "user_set_collection": {
        "name": "/user/set_collection/&lt;user_id&gt;",
        "subsection": "user_collection_management",
        "desc": """\
<p>This endpoint facilitates all-at-once updates to a user's
<code>collection</code>, which basically looks like this:</p>
<pre><code>
'collection': {
    'expansions': [
        'manhunter',
        'flower_knight'
    ],
}
</pre></code>
<p>The idea behind this endpoint is that you want to <b>POST</b> the actual
<code>collection</code> to it, so the JSON you post is going to have a key,
'collection', and that key's value is going to be a hash, and that hash will
have the 'expansions' key, etc.</p>
<p>Just follow the example JSON above.</p>
        """,
    },
}


create_assets = {
    "new_settlement": {
        "name": "/new/settlement",
        "methods": ["POST","OPTIONS"],
        "desc": (
            '<p>Use <code>handle</code> values from the '
            '<code>/kingdom_death</code> pubilc route as params, like this:</p>'
            """\
<code><pre>{
    "campaign": "people_of_the_lantern",
    "expansions": ["dung_beetle_knight", "lion_god"],
    "survivors": ["adam", "anna"],
    "name": "Chicago",
    "macros": ["create_first_story_survivors"]
}</pre></code>
"""
            '<p>If successful, this route returns a serialized version '
            'of the new settlement, including its OID, as JSON.</p>'
        ),
    },
    "new_survivor": {
        "name": "/new/survivor",
	"methods": ["POST", "OPTIONS"],
        "desc": """\
<p>This works differently from <code>/new/settlement</code> in
a number of significant ways.</p>
<p> In a nutshell, the basic idea here is that the only required key
in the JSON you <b>POST</b> to this route is an object ID for the settlement
to which the survivor belongs:</p>
<code>{'settlement': '59669ace4af5ca799c968c94'}</code>
<p> Beyond that, you are free to supply any other attributes of the
survivor, so long as they comply with the data model for survivors.</p>
<p> Consult the <a href="/#survivorDataModel">Survivor Data Model (below)</a> for a
complete reference on what attributes of the survivor may be set at
creation time.</p>
<p>As a general piece of advice, it typically makes more sense to
just initialize a new survivor with defaults and then operate on it
using the routes below, unless you're doing something inheritance.</p>
<p>For normal inheritance, simply <b>POST</b> the OID's of one or
more of the survivor's parents like so:</p>
<code>{settlement: '59669ace4af5ca799c968c94', father: '5a341e6e4af5ca16907c2dff'}</code>
<p>...or like so:</p>
<code>{settlement: '59669ace4af5ca799c968c94', father: '5a341e6e4af5ca16907c2dff', mother: '5a3419c64af5ca11240f519f'}</code>
<p>This will cause normal inheritance rules to be triggered when the
new survivor is created.</p>
<p>In order to trigger conditional or special inheritance, e.g. where
an innovation requires the user to select a single parent as the donor,
you <u>must</u> specify which parent is the donor using the <code>
primary_donor_parent</code> key and setting it to 'father' or 'mother':</p>
<code>{settlement: '59669ace4af5ca799c968c94', father: '5a341e6e4af5ca16907c2dff', mother: '5a3419c64af5c
a11240f519f', primary_donor_parent: 'father'}</code>
<p>This will cause normal inheritance rules to be triggered when the
new survivor is created.</p>
<p>In order to trigger conditional or special inheritance, e.g. where
an innovation requires the user to select a single parent as the donor,
you <u>must</u> specify which parent is the donor using the <code>
primary_donor_parent</code> key and setting it to 'father' or 'mother':</p>
<code>{settlement: '59669ace4af5ca799c968c94', father: '5a341e6e4af5ca16907c2dff', mother: '5a3419c64af5ca11240f519f', primary_donor_parent: 'father'}</code>
<p>This will cause innovations such as <b>Family</b> to use the primary
donor parent to follow one-parent inheritance rules for that innovation.</p>
<p>As of API releases > 0.77.n, survivors can be created with an avatar.
Inclde the <code>avatar</code> key in the <b>POST</b> body, and let
that key's value be a string representation of the image that should
be used as the survivor's avatar.</p>
<p>(<a href="/#setAvatarAnchor">See <code>/survivor/set_avatar/<oid></code> route below</a> for more
information on how to post string representations of binary content.</p>
<p><b>Important!</b>Just like the <code>/new/settlement</code> route,
a successful <b>POST</b> to the <code>/new/survivor</code> route will return
a serialized version (i.e. JSON) of the new survivor, complete with
the <code>sheet</code> element, etc.</p>
        """,
    },
    "new_survivors": {
        "name": "/new/survivors",
	"methods": ["POST", "OPTIONS"],
        "desc": """\
<p>Not to be confused with <code>/new/survivor</code> (above),
this route adds multiple new survivors, rather than just one.</p>
<p>The JSON you have to <b>POST</b> to this route is a little different
and more limited than what you would post to <code>/new/survivor</code>.</p>
<p>The following <b>POST</b> key/value pairs are the only ones supported
by this route:</p>
<table class="embedded_table">
<tr><th>key</th><th>O/R</th><th>value type</th><th>comment</th>
<tr>
    <td>settlement_id</td>
    <td><b>R</b></td>
    <td>settlement OID</td>
    <td class="text">The OID of the settlement to which the new survivors belong.</td>
</tr>
<tr>
    <td>public</td>
    <td>O</td>
    <td>boolean</td>
    <td class="text">
        The value of the new survivors'<code>public</code> attribute.
        Defaults to <code>true</code>.
    </td>
</tr>
<tr>
    <td>male</td>
    <td>O</td>
    <td>arbitrary int</td>
    <td class="text">The number of male survivors to create.</td>
</tr>
<tr>
    <td>female</td>
    <td>O</td>
    <td>arbitrary int</td>
    <td class="text">The number of female survivors to create.</td>
</tr>
<tr>
    <td>father</td>
    <td>O</td>
    <td>survivor OID</td>
    <td class="text">The OID of the survivor that should be the father of the new survivors.</td>
</tr>
<tr>
    <td>mother</td>
    <td>O</td>
    <td>survivor OID</td>
    <td class="text">The OID of the survivor that should be the mother of the new survivors.</td>
</tr>
</table>
<p>Creating new survivors this way is very simple. This JSON, for
example, would create two new male survivors:</p>
<code>{"male": 2, "settlement_id": "5a1485164af5ca67035bea03"}</code>
<p>A successful <b>POST</b> to this route always returns a list of
serialized survivors (i.e. the ones that were created), so if
you are creating more than four or five survivors, this route is
a.) going to take a couple/few seconds to come back to you and b.)
is going to drop a pile of JSON on your head. YHBW.</p>
<p>NB: this route <i>does not</i> support random sex assignment.</p>
        """,
    },
}

settlement_management = {
    "settlement_get_settlement_id": {
        "name": "/settlement/get/&lt;settlement_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": """\
<p> Retrieve a serialized version of the settlement associated
with &lt;settlement_id&gt; (to include all related user and game
assets, including survivors).</p>
<p><b>Important!</b> Depending on the number of expansions, survivors,
users, etc. involved in a settlement/campaign, this one can take a
long time to come back (over 2.5 seconds on Production hardware).
YHBW</p>
	""",
    },
    "settlement_get_summary_settlement_id": {
        "name": "/settlement/get_summary/&lt;settlement_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": """\
<p>Get a nice, dashboard-friendly summary of a settlement's info.</p>
<p>This route is optimized for speedy returns, e.g. the kind you want when
showing a user a list of their settlements.</p>
        """,
    },
    "settlement_get_campaign_settlement_id": {
        "name": "/settlement/get_campaign/&lt;settlement_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": """\
<p>Retrieve a serialized version of the settlement where the
<code>user_assets</code> element includes the <code>groups</code>
list, among other things, and is intended to be used in creating
'campaign' type views.</p>
<p>Much like the big <code>get</code> route for settlements, this one
can take a while to come back, e.g. two or more seconds for a normal
settlement. YHBW.</p>
        """,
    },
    "settlement_get_sheet_settlement_id": {
        "name": "/settlement/get_sheet/&lt;settlement_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": """\
<p>A convenience endpoint that only returns the settlement's <code>sheet</code>
element, i.e. the dictionary of assets it owns.</p>
        """,
    },
    "settlement_get_game_assets_settlement_id": {
        "name": "/settlement/get_game_assets/&lt;settlement_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": """\
<p>A convenience endpoint that only returns the serialized settlement's <code>
game_assets</code> element, i.e. the JSON representation of the game assets
(gear, events, locations, etc.) required to represent the settlement. </p>
        """,
    },
    "settlement_get_event_log_settlement_id": {
        "name": "/settlement/get_event_log/&lt;settlement_id&gt;",
	"subsection": "settlement_component_gets",
        "desc": """\
<p><b>GET</b> this end point to retrieve all settlement event log
entries (in a giant hunk of JSON) in <u>reverse chronological
order</u>, i.e. latest first, oldest last.</p>
<p>PROTIP: For higher LY settlements this can be a really huge
list and take a long time to return: if you're a front-end
developer, definitely consider loading this one AFTER you have
rendered the rest of your view.</p>
<p>Another way to optimize  here is to include a filter key/value
pair in your <b>POST</b> body to limit your results. Some of the
accepted filter params will decrease the time it takes for your
requested lines to come back from the API:
<table class="embedded_table">
<tr><th>key</th><th>value type</th><th>scope</th>
<tr>
    <td>lines</td>
    <td>arbitrary int</td>
    <td class="text">Limit the return to the last <code>lines</code>-worth of lines: <code>{lines: 1
0}</code>. Note that this <u>does not</u> make the query or the return time better or faster for settlements with large event logs.</td>
</tr>
<tr>
    <td>ly</td>
    <td>arbitrary int</td>
    <td class="text">
        Limit the return to event log lines created <u>during</u> an arbitrary Lantern Year, e.g. <code>{ly: 9}</code>.<br/>
        Note:
        <ul class="embedded">
            <li>This will always return <i>something</i> and you'll get an empty list back for Lantern Years with no events.</li>
            <li>This param triggers a performance-optimized query and will return faster than a general call to the endpoint with no params.</li>
        </ul>
</tr>
<tr>
    <td>get_lines_after</td>
    <td>event log OID</td>
    <td class="text">Limit the return to event log lines created <u>after</u> an event log OID: <cod
e>{get_lines_after: "5a0370b54af5ca4306829050"}</code></td>
</tr>
<tr>
    <td>survivor_id</td>
    <td>arbitrary survivor's OID</td>
    <td class="text">Limit the return to event log lines that are tagged with a survivor OID: <code>
{survivor_id: "5a0123b54af1ca42945716283"}</code></td>
</tr>
</table>
<p><b>Important!</b> Though the API will accept multiple filter
params at this endpoint, <b>POST</b>ing more than one of the
above can cause...unexpected output. YHBW.</p>
        """,
    },
    "settlement_get_storage_settlement_id": {
        "name": " /settlement/get_storage/&lt;settlement_id&gt;",
	"methods": ['GET','OPTIONS'],
	"subsection": "settlement_component_gets",
        "desc": """\
<p>Hit this route to get representations of the settlement's storage.</p>
<p>What you get back is an array with two dictionaries, one for resources
and one for gear:</p>
<pre><code>[
    {
        "storage_type": "resources",
        "total":0,
        "name":"Resource",
        "locations": [
            {
                "bgcolor":"B1FB17",
                "handle":"basic_resources",
                "name":"Basic Resources",
                "collection": [
                    {
                        "handle":"_question_marks",
                        "name":"???",
                        "rules":[],
                        "consumable_keywords": ["fish","consumable","flower"],
                        "type_pretty": "Resources",
                        "keywords": ["organ","hide","bone","consumable"],
                        "desc":"You have no idea what monster bit this is. Can be used as a bone, organ, or hide!",
                        "type":"resources",
                        "sub_type":"basic_resources",
                        "quantity":0,"flippers":false
                    },
                    ...
                ],
                ...
            },
    },
], </pre></code>
<p>This JSON is optimized for representation via AngularJS, i.e. iteration over
nested lists, etc.</p>
<p>Each dictionary in the main array has an array called <code>locations</code>,
which is a list of dictionaries where each dict represents a location within the
settlement.</p>
<p>Each location dictionary has an array called <code>collection</code> which is
a list of dictionaries where each dictionary is a piece of gear or a resource.</p>
<p>The attributes of the dictionaries within the <code>collection</code> array
include the <code>desc</code>, <code>quantity</code>, etc. of an individual
game asset (piece of gear or resource or whatever).</p>
        """,
    },
    "zz_settlement_abandon_settlement_id": {
        "name": "/settlement/abandon/&lt;settlement_id&gt;",
        'deprecated': True,
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>As of January 2021, this route is deprecated. Please use the"
            "<code>set_attribute</code> route (<b>POST</b> "
            "<code>abandoned</code> as the <code>value</code>) instead.</p>"
        ),
    },
    "settlement_remove_settlement_id": {
        "name": "/settlement/remove/&lt;settlement_id&gt;",
        "methods": ["POST", "OPTIONS"],
        "desc": """\
<p><b>POST</b> (not <b>GET</b>) to this route to mark the settlement as
removed.</p>
<p>Once marked as removed, settlements are queued up by the API for removal
from the database: the next time the maintenance process runs, it will check
the timestap of the mark as removed event and purge the settlement
(and all survivors) from the database.</p>
<p><b>This cannot be undone.</b></p>
        """,
    },




	#
	#	settlement SET attributes
	#
    "settlement_set_custom_url_settlement_id": {
        "name": "/settlement/set_custom_url/&lt;settlement_id&gt;",
        "methods": ["POST", "OPTIONS"],
        "subsection": "settlement_set_attribute",
        "desc": (
            '<p><b>POST</b> an URL fragment to reserve it as the custom '
            'locator for a settlement.</p>'
            '<p>All incoming values are forced to lowercase.</p>'
            '<p>URLs are evaluated by the API, which returns HTTP 422 if '
            "it doesn't like whatever you're trying to set."
        ),
        'examples': [
            "{url: 'the_black_lantern'}",
            "{url: 'deadrock'}",
        ],
    },
    "settlement_set_attribute_settlement_id": {
        "name": "/settlement/set_attribute/&lt;settlement_id&gt;",
        "methods": ["POST", "OPTIONS"],
        "subsection": "settlement_set_attribute",
        "desc": (
            "<p><b>POST</b> some JSON containing <code>attribute</code> and "
            "a <code>value</code> keys where 'attribute' is the Settlement "
            "attribute you want to set and and 'value' is what you want to set "
            "it to.</p>"
        ),
        'examples': [
            "{attribute: 'survival_limit', value: 3}",
            "{attribute: 'abandoned', value: true}",
            "{attribute: 'abandoned', value: 'UNSET'}",
        ],
    },

    "settlement_set_name_settlement_id": {
        "name": "/settlement/set_name/&lt;settlement_id&gt;",
        "subsection": "settlement_set_attribute",
        "desc": """\
<p><b>POST</b> some JSON whose body contains the key 'name' and whatever the
new name is going to be as that key's value to change the settlement's
name:</p>
<code>{'name': 'The Black Lantern'}</code>
<p><b>Important!</b> Submitting an empty string will cause the API to
default the settlement's name to "UNKNOWN". There are no technical
reasons (e.g. limitations) for this, but it breaks the display in most
client apps, so null/empty names are forbidden.</p>
        """,
    },
    "settlement_set_inspirational_statue_settlement_id": {
        "name": "/settlement/set_inspirational_statue/&lt;settlement_id&gt;",
        "subsection": "settlement_set_attribute",
        "desc": """\
<p>Set the settlement's <code>inspirational_statue</code> attrib
by <b>POST</b>ing a Fighting Art handle to this route:</p>
<code>{'handle': 'leader'}</code>
<p>This route will actually check out the handle and barf on you
if you try to <b>POST</b> an unrecognized FA handle to it. YHBW.</p>
	""",
    },
    "settlement_set_lantern_research_level_settlement_id": {
        "name": "/settlement/set_lantern_research_level/&lt;settlement_id&gt;",
        "subsection": "settlement_set_attribute",
        "desc": """\
<p>Set the Settlement's Lantern Research Level with some basic
JSON:</p>
<code>{'value': 3}</code>
<p>This route is preferably to a generic attribute setting route
becuase it a.) ignores values over 5 and b.) forces the attrib,
which is not part of the standard data motel, to exist if it does
not.</p>
<p>Definitely use this instead of <code>set_attribute</code>.</p>
	""",
    },
    "settlement_update_set_lost_settlements_settlement_id": {
        "name": "/settlement/set_lost_settlements/&lt;settlement_id&gt;",
        "subsection": "settlement_set_attribute",
        "desc": """\
<p>Use this route to set a settlement's Lost Settlements total.</p>
<p><b>POST</b> some JSON containing the new value to set it to:</p>
<code>{"value": 2}</code>
<p>The above code would set the settlement's Lost Settlements total
to two; negative numbers will default to zero. </p>
	""",
    },


	#
	#	settlement UPDATE attributes
	#

    "settlement_update_attribute_settlement_id": {
        "name": "/settlement/update_attribute/&lt;settlement_id&gt;",
        "subsection": "settlement_update_attribute",
        "desc": """\
<p><b>POST</b> some JSON containing an 'attribute' and a 'modifier'
key where 'attribute' is an integer settlement attrib and 'mofier' is
how much you want to increment it by:</p>
<code>{'attribute': 'death_count', 'modifier': -1}</code>
<p> This route also supports incrementing the <code>survival_limit
</code> and <code>death_count</code> routes.</p>
	""",
    },
    "settlement_update_population_settlement_id": {
        "name": "/settlement/update_population/&lt;settlement_id&gt;",
        "subsection": "settlement_update_attribute",
        "desc": """\
<p><b>POST</b> some JSON containing the key 'modifier' whose value is
an integer that you want to add to the settlement's population
number.<p>
<p>This works basically identically to the <code>update_attribute</code>
route, so considering using that route instead. </p>
<p>For example, this JSON would add two to the settlement's
population number:</p>
<code>{'modifier': 2}</code>
<p><b>POST</b> negative numbers to decrease.</p>
<p><b>Important!</b> Settlement population can never go below zero,
so any 'modifier' values that would cause this simply cause the
total to become zero.</p>\
	""",
    },
    "settlement_replace_game_assets_settlement_id": {
        "name": "/settlement/replace_game_assets/&lt;settlement_id&gt;",
        "subsection": "settlement_update_attribute",
        "desc": """\
<p>This route functions nearly identically to the other update-type routes in
this subsection, except for one crucial difference: it works on list-type
attributes of the settlement (whereas the others mostly work on string or
integer type attributes).</p>
<p>This route accepts a list of <code>handles</code> and a <code>type</code>
of game asset and then evalutes the settlement's current handles of that type,
removing and adding as necessary in order to bring the settlement's list in sync
with the incoming list. </p>
<p>Your POST body needs to define the attribute <code>type</code>
you're trying to update, as well as provide a list of handles
that represent the settlement's current asset list:</p>
<pre><code>{
    "type": "locations",
    "handles": [
        "lantern_hoard","bonesmith","organ_grinder"
    ]
}</code></pre>
<p>Finally, a couple of tips/warnings on this route:<ul>
    <li class="plain">The <code>handles</code> list/array is handled by the API as if it were a set, i.e. duplicates are silently ignored.</li>
    <li class="plain">If any part of the update fails (i.e. individual add or remove operations), the whole update will fail and <u>no changes to the settlement will be saved</u>.</li>
    <li class="plain">This route does not support Location or Innovation levels! (Use <code>set_location_level</code> or <code>set_innovation_level</code> for that.)</li>
</ul></p>
	""",
    },
    "settlement_update_endeavor_tokens_settlement_id": {
        "name": "/settlement/update_endeavor_tokens/&lt;settlement_id&gt;",
        "subsection": "settlement_update_attribute",
        "desc": """\
<p>Use this route to change a settlement's endeavor token count.</p>
<p><b>POST</b> some JSON containing the number to modify by:</p>
<code>{"modifier": 2}</code>
<p>The above code would add two to the settlement's current total,
whereas the code below would decrement by one:</p>
<code>{"modifier": -1}</code>
	""",
    },
    "settlement_update_toggle_strain_milestone_settlement_id": {
        "name": "/settlement/toggle_strain_milestone/&lt;settlement_id&gt;",
        "subsection": "settlement_update_attribute",
        'deprecated': True,
        "desc": '<p>Use <code>set_strain_milestones</code> instead.</p>',
    },
    "settlement_set_strain_milestones_settlement_id": {
        "name": "/settlement/set_strain_milestones/&lt;settlement_id&gt;",
        "subsection": "settlement_update_attribute",
        "desc": """\
<p><b>POST</b> a list of Strain Milestones to update the settlement's list of
unlocked Strain Milestones.</p>
<code>{'strain_milestones': ['plot_twist', 'somatotropin_surge']}</code>
	""",
    },
    "settlement_set_patterns_settlement_id": {
        "name": "/settlement/set_patterns/&lt;settlement_id&gt;",
        "subsection": "settlement_update_attribute",
        "desc": """\
<p><b>POST</b> a list of pattern gear handles to update the settlement's
available patterns.</p>
<code>{'patterns': ['teleric_eye_tac', 'grim_muffler']}</code>
<p>This endpoint is the only way to manage this attribute. Adding and removing
is logged atomically in the settlement event log.</p>
	""",
    },


	#
	#	bulk survivor management
	#

    "settlement_update_survivors_settlement_id": {
        "name": "/settlement/update_survivors/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_survivors",
        "desc": """\
<p>Use this route to update a specific group of survivors, e.g.
Departing survivors.</p>
<p><b>POST</b> some JSON including the type of survivors to include,
the attribute to modify, and the modifier:</p>
<code>{include: 'departing', attribute: 'Insanity', modifier: 1}</code>
<p><b>Important!</b> This route currently only supports the
<code>include</code> value 'departing' and will error/fail/400 on
literally anything else.</p>\
	""",
    },


	#
	#	settlement: manage expansions
	#

    "settlement_update_add_expansions_settlement_id": {
        "name": "/settlement/add_expansions/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_expansions",
        "desc": """\
<p>Add expansions to a settlement by <b>POST</b>ing a list of expansion handles.
The body of your post should be a JSON-style list:</p>
<code>{'expansions': ['beta_challenge_scenarios','dragon_king']}</code>
<p>
Note that this route not only updates the settlement sheet, but also
adds/removes timeline events, updates the settlement's available game
assets (e.g. items, locations, etc.).
</p>
	""",
    },
    "settlement_update_rm_expansions_settlement_id": {
        "name": "/settlement/rm_expansions/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_expansions",
        "desc": """\
<p>Remove expansions from a settlement by <b>POST</b>ing a list of
expansion handles. The body of your post should be a JSON-style
list:</p>
<code>{'expansions': ['manhunter','gorm','spidicules']}</code>
<p>
Note that this route not only updates the settlement sheet, but also
adds/removes timeline events, updates the settlement's available game
assets (e.g. items, locations, etc.).
</p>
<p><b>Important!</b> We're all adults here, and the KDM API will
<i>not</i> stop you from removing expansion handles for expansions
that are required by your settlement's campaign. If you want to
prevent users from doing this, that's got to be part of your UI/UX
considerations.</p>
	""",
    },


	#
	#	settlement: manage monsters
	#
    "settlement_set_current_quarry_settlement_id": {
        "name": "/settlement/set_current_quarry/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_monsters",
        "desc": """\
<p>This route sets the settlement's 'current_quarry' attribute,
which is the monster that the settlement's Departing Survivors are
currently hunting.</p><p><b>POST</b> some simple JSON containing a monster
name (do not use handles for this):</p>
<code>{'current_quarry': 'White Lion Lvl 2'}</code>
<p>...or, the monster is unique:</p>
<code>{'current_quarry': 'Watcher'}</code>
<p><b>Important!</b> You're typically going to want to pull monster
names from the settlements' <code>game_assets -> defeated_monsters</code>
list (which is a list of monster names created for the settlement
based on expansion content, etc.)</p>
	""",
    },
    "settlement_add_defeated_monster_settlement_id": {
        "name": "/settlement/add_defeated_monster/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_monsters",
        "desc": """\
<p><b>POST</b> a 'monster' string to this route to add it to the
settlement's list of defeated monsters:</p>
<code>{'monster': 'White Lion (First Story)}</code> or
<code>{'monster': 'Flower Knight Lvl 1'}</code>
<p><b>Important!</b> Watch the strings on this one and try to avoid
free text: if the API cannot parse the monster name and match it to
a known monster type/name, this will fail.</p>
	""",
    },
    "settlement_rm_defeated_monster_settlement_id": {
        "name": "/settlement/rm_defeated_monster/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_monsters",
        "desc": """\
<p><b>POST</b> a 'monster' string to this route to remove it from the
settlement's list of defeated monsters, i.e. the <code>sheet.defeated_monsters</code>
array/list: </p>
<code>{'monster': 'Manhunter Lvl 4'}</code>
<p>Attempts to remove strings that do NOT exist in the list will
not fail (i.e. they will be ignored and fail 'gracefully').</p>
	""",
    },
    "settlement_add_monster_settlement_id": {
        "name": "/settlement/add_monster/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_monsters",
        "desc": """\
<P>Use this route to add quarry or nemesis type monsters to the
settlement. <b>POST</b> some JSON containing the handle of the monster to
add it:</p>
<code>{'handle': 'flower_knight'}</code>
<p>The API will determine whether the monster is a nemesis or a quarry
and add it to the appropriate list. For nemesis monsters, use the
<code>/settlement/update_nemesis_levels</code> route (below) to manage
the checked/completed levels for that nemesis.</p>
<p>Make sure to check the settlement JSON <code>game_assets.monsters</code>
and use the correct handle for the desired monster.</p>
	""",
    },
    "settlement_rm_monster_settlement_id": {
        "name": "/settlement/rm_monster/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_monsters",
        "desc": """\
<p><b>POST</b> some JSON containing a quarry or nemesis type monster handle
to remove it from the settlement's list:</p>
<code>{'handle': 'sunstalker'}</code>
<p>The API will determine whether the monster is a quarry or a nemesis.
When a nemesis monster is removed, its level detail is also removed.</p>
	""",
    },
    "settlement_update_nemesis_levels_settlement_id": {
        "name": "/settlement/update_nemesis_levels/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_monsters",
        "desc": """\
<p>Use this method to update the Settlement sheet's <code>nemesis_encounters</code>
dictionary, i.e. to indicate that a nemesis encounter has occurred.</p>
<p>A typical dictionary might look like this:</p>
<code>        "nemesis_encounters": {"slenderman": [], "butcher": [1,2]}</code>
<p>In this example, the settlement has (somehow) encountered a
a level 1 Butcher, but has not yet encountered a Slenderman.</p>
<p>To update the dictionary, <b>POST</b> some JSON that includes the
nemesis monster's handle and the levels that are complete.</p>
<p><b>POST</b> this JSON to reset/undo/remove Butcher encounters:<p>
<code>{"handle": "butcher", "levels": []}</code>
<p><b>POST</b> this JSON to record an encounter with a level 1 Manhunter:</p>
<code>{"handle": "manhunter", "levels": [1]}</code>
	""",
    },
    "settlement_set_milestones_settlement_id": {
        "name": "/settlement/set_milestones/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_principles",
        "desc": (
            "<p><b>POST</b> some JSON containing the list of the settlement's "
            "milestone handles to update the settlement record.</p>"
            "<p>PROTIP: a list of the settlement's available milestones can be "
            "found in the "
            "<code>settlement.game_assets.milestones_options</code> that comes "
            "down from the API with the settlement data.</p>"

        ),
        'examples': [
            "{'milestone_story_events': ['pop_15', 'game_over', 'first_death']}",
            "{'milestone_story_events': ['first_child']}",
        ],
    },
    "zz_settlement_add_milestone_settlement_id": {
        'deprecated': True,
        "name": "/settlement/add_milestone/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_principles",
        "desc": '<p>Use <code>set_milestones</code> instead.</p>'
    },
    "zz_settlement_rm_milestone_settlement_id": {
        'deprecated': True,
        "name": "/settlement/rm_milestone/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_principles",
        "desc": '<p>Use <code>set_milestones</code> instead.</p>'
    },
    "settlement_set_principle_settlement_id": {
        "name": "/settlement/set_principle/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_principles",
        "desc": """\
<p><b>POST</b> some JSON to this route to set or unset a settlement principle.
Request the handle of the <code>principle</code> and the election you want to
make:</p>
<pre><code>
{
    principle: 'conviction',
    election: 'romantic',
}</code></pre>
<p>This route has a couple of unusual behaviors to note:</p>
	<ul>
    <li class="plain">It requires both keys (i.e. you will get a 400 back if you
    <b>POST</b> any JSON that does not include both).</li>
    <li class="plain">It will accept a Boolean for 'election', because this is how
    you 'un-set' a principle.</li>
	</ul>
<p> To un-set a principle, simply post the principle handle and set the
 <code>election</code> key to 'false':</p>
<code>{principle: 'new_life', election: false}</code>
<p> <b>Important!</b> Adding principles to (or removing them from) a
settlement automatically modifies all current survivors, in many
cases. If you've got survivor info up on the screen when you set a principle,
be sure to refresh any survivor info after <b>POST</b>ing JSON to this route!
</p>\
	""",
    },


	#
	#	location controls
	#

    "settlement_add_location_settlement_id": {
        "name": "/settlement/add_location/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_locations",
        "desc": """\
<p> <b>POST</b> a location <code>handle</code> to this route to add
it to the settlement's Locations:</p>
<code>{'handle': 'bone_smith'}</code>
	""",
    },
    "settlement_rm_location_settlement_id": {
        "name": "/settlement/rm_location/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_locations",
        "desc": """\
<p>This is basically the reverse of <code>add_location</code>
and works nearly identically. <b>POST</b> a JSON representation of a
Location handle to remove it from the settlement's list:</p>
<code>{'handle': 'barber_surgeon'}</code>
	""",
    },
    "settlement_set_location_level_settlement_id": {
        "name": "/settlement/set_location_level/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_locations",
        "desc": """\
<p>For Locations that have a level (e.g. the People of the
Sun's 'Sacred Pool'), you may set the Location's level by posting
the <code>handle</code> of the location and the desired level:</p>
<code>{'handle': 'sacred_pool', 'level': 2}</code>
	""",
    },


	#
	#	innovation controls
	#

    "settlement_get_innovation_deck_settlement_id": {
        "name": "/settlement/get_innovation_deck/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_innovations",
        "desc": """\
<p>Retrieve the settlement's current innovation deck as an array of asset names
by default.</p>
<p>Alternately, you can <b>POST</b> the parameter
<code>return_type: "dict"</code> to this endpoint to get a hash of innovations
(representing the settlement's Innovation Deck) back from this endpoint.</p>
<p>In the hash, innovation assets are sorted by their name (i.e. <i>not</i>
 by their handle):<p>
<pre><code>{
    "albedo": {
        "handle": "albedo",
        "name": "Albedo",
        "consequences": [
            "citrinitas"
        ],
        "endeavors": [
            "gorm_albedo"
        ],
        "expansion": "gorm",
        "type_pretty": "Innovations",
        "sub_type_pretty": "Expansion",
        "type": "innovations",
        "sub_type": "expansion",
        "innovation_type": "science"
    },
    "bed": {
        "handle": "bed",
        "name": "Bed",
        "type": "innovations",
        "endeavors": [
            "bed_rest"
        ],
        "type_pretty": "Innovations",
        "sub_type_pretty": "Innovation",
        "survival_limit": 1,
        "sub_type": "innovation",
        "innovation_type": "home"
    },
    ...
    "symposium": {
        "handle": "symposium",
        "name": "Symposium",
        "consequences": [
            "nightmare_training",
            "storytelling"
        ],
        "type": "innovations",
        "settlement_buff": "When a survivor innovates, draw an additional 2 Innovation Cards to choose from.",
        "type_pretty": "Innovations",
        "sub_type_pretty": "Innovation",
        "survival_limit": 1,
        "sub_type": "innovation",
        "innovation_type": "education"
    }
}
</code></pre>
	""",
    },
    "settlement_add_innovation_settlement_id": {
        "name": "/settlement/add_innovation/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_innovations",
        "desc": """\
 <p> <b>POST</b> an Innovation <code>handle</code> to this route to add
it to the settlement's Innovations:</p>
<code>{'handle': 'hovel'}</code>
<p>...or:</p><code>{'handle': 'mastery_club'}</code>
<p><b>Important!</b> As far as the API is concerned, Principles (e.g.
'Graves', 'Survival of the Fittest', etc. <u>are not innovations</u>
and you <u>will</u> break the website if you try to add a principle
as if it were an innovation.</p>
<p>Use <code>set_principle</code> (below) instead.</p>
	""",
    },
    "settlement_rm_innovation_settlement_id": {
        "name": "/settlement/rm_innovation/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_innovations",
        "desc": """\
<p>This is basically the reverse of <code>add_innovation</code>
and works nearly identically. <b>POST</b> a JSON representation of an
Innovation handle to remove it from the settlement's list:</p>
<code>{'handle': 'mastery_club'}</code>
	""",
    },
    "settlement_set_innovation_level_settlement_id": {
        "name": "/settlement/set_innovation_level/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_innovations",
        "desc": """\
<p>For Innovations that have a level (e.g. the Slenderman's 'Dark
Water Research'), you may set the Innovation's level by posting
the <code>handle</code> of the innovation and the level:</p>
<code>{'handle': 'dark_water_research', 'level': 2}</code>
	""",
    },


	#
	#	timeline!
	#

    "settlement_get_timeline_settlement_id": {
        "name": "/settlement/get_timeline/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_timeline",
        "methods": ['GET'],
        "desc": """\
<p>Hit this endpoint to get a JSON representation of the
settlement's timeline.</p>
<p>This is read-only and optimized for performance, so you'll
get a timeline MUCH faster using this route than one of the
routes that pulls down the whole settlement.</p>
	""",
    },
    "settlement_add_lantern_years_settlement_id": {
        "name": "/settlement/add_lantern_years/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_timeline",
        'methods': ['POST','OPTIONS'],
        "desc": """\
<p><b>POST</b> a number (int) of years to add to the settlement's
Timeline:</p>
<code>{years: 5}</code>
<p><b>NB:</b> Timelines are capped at 50 LYs. If you try to add
a number of years that would take you above 50 LYs, you'll get a
400 back.</p>
	""",
    },
    "settlement_set_current_lantern_year_settlement_id": {
        "name": "/settlement/set_current_lantern_year/&lt;settlement_id&gt;",
        "subsection": "settlement_manage_timeline",
        'methods': ['POST','OPTIONS'],
        "desc": """\
<p>To set the settlement's current LY, <b>POST</b> an int to this
endpoint:</p>
<code>{ly: 3}</code>
	""",
    },
    'settlement_set_lantern_year': {
        'name': '/settlement/set_lantern_year/&lt;settlement_id&gt;',
        'methods': ['POST','OPTIONS'],
        'subsection': 'settlement_manage_timeline',
        'desc': """\
            <p>Use this endpoint to compeltely overwrite a lantern year.</p>
            <p>Requires the <code>ly</code> param, which should be a
            whole lantern year represented as JSON, e.g:
<pre><code>
{
    'year': 1,
    'story_event': [
        {'handle': 'core_returning_survivors'}
    ],
    'settlement_event': [
        {'handle': 'core_first_day'}
    ]
}
</pre></code>
        </p>
        """,
    },
    "zz_settlement_replace_lantern_year_settlement_id": {
        "name": "/settlement/replace_lantern_year/&lt;settlement_id&gt;",
        'deprecated': True,
        "subsection": "settlement_manage_timeline",
        "desc": '<p>Use <code>set_lantern_year</code> instead.</p>'
    },


	#
	#	settlement admins
	#

    "settlement_add_admin_settlement_id": {
        "name": "/settlement/add_admin/&lt;settlement_id&gt;",
        "subsection": "settlement_admin_permissions",
	"methods": ["POST","OPTIONS"],
        'deprecated': True,
        "desc": '<p>Use <code>add_settlement_admin</code> instead.</p>'
    },
    "settlement_rm_admin_settlement_id": {
        "name": "/settlement/rm_admin/&lt;settlement_id&gt;",
        "subsection": "settlement_admin_permissions",
	"methods": ["POST","OPTIONS"],
        'deprecated': True,
        "desc": '<p>Use <code>rm_settlement_admin</code> instead.'
    },


	#
	#	settlement notes
	#

    "settlement_add_note_settlement_id": {
        "name": "/settlement/add_note/&lt;settlement_id&gt;",
        "subsection": "settlement_notes_management",
	"methods": ["POST","OPTIONS"],
        "desc": """\
<p>Since any player in a game is allowed to create settlement
notes, the JSON required by this endpoint must include a user's
OID.</p>
<p>This endpoint supports the following key/value pairs:</p>
<table class="embedded_table">
    <tr><th>key</th><th><b>R</b>/O</th><th>value</th></tr>
    <tr>
        <td class="small_key">author_id</td>
        <td class="type"><b>R</b></type>
        <td class="value">The creator's OID as a string.</td>
    </tr>
    <tr>
        <td class="small_key">note</td>
        <td class="type"><b>R</b></type>
        <td class="value">The note as a string. We accept HTML here, so if you want to display this back to your users as HTML, you can do that.</td>
    </tr>
    <tr>
        <td class="small_key">author</td>
        <td class="type">O</type>
        <td class="value">The creator's login, e.g. <code>demo@kdm-manager.com</code>, as a string. Best practice is to NOT include this, unless you really know what you're doing.</td>
    </tr>
    <tr>
        <td class="small_key">lantern_year</td>
        <td class="type">O</type>
        <td class="value">The Lantern Year the note was created. Defaults to the current LY if not specified.</td>
    </tr>
</table>
<p>For example, to add a new note to a settlement, your <b>POST</b>
body will, at a minimum, look something like this:</p>
<code>
{
    author_id: "5a26eb1a4af5ca786d1ed548",
    note: "Nobody expects the Spanish Inquisition!"
}
</code>
<p><b>Important!</b> This route returns the OID of the
newly-created note:</p>
<code>{"note_oid": {"$oid": "5a2812d94af5ca03ef7db6c6"}}</code>
<p>...which can then be used to remove the note, if necessary
(see <code>rm_note</code> below).</p>
	""",
    },
    "settlement_rm_note_settlement_id": {
        "name": "/settlement/rm_note/&lt;settlement_id&gt;",
        "subsection": "settlement_notes_management",
	"methods": ["POST","OPTIONS"],
        "desc": """\
<p><b>POST</b> the OID of a settlement note to remove it.</p>
<code>{_id: "5a26eb894af5ca786d1ed558"}</code>
<p>As long as you get a 200 back from this one, the note has
been removed. If you get a non-200 status (literally anything other
than a 200), something went wrong. </p>
	""",
    },
}

survivor_management = {
    "survivor_get": {
        "name": "/survivor/get/&lt;survivor_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": (
            '<p>Retrieves a JSON representation of the survivor with OID '
            '<i>&lt;survivor_id&gt;</i>.</p>'
            '<p>As with other <code>GET</code> type routes, this one returns '
            "a lot of info, but what you typically want is in the "
            '<code>sheet</code> element:</p>'
            """<pre><code>{
  "meta": {...},
  "sheet": {
    "_id": {
      "$oid": "5febfb74d174525f6eca199b"
    },
    "email": "toconnell@thelaborinvain.com",
    "born_in_ly": 0,
    "created_on": {
      "$date": 1609279252167
    },
    "created_by": {
      "$oid": "5fad50306515930c165b006f"
    },
    "settlement": {
      "$oid": "5febfb73d174525f6eca1998"
    },
    "sex": "M",
    "hunt_xp": 3,
    ...
  },
  "notes": [...],
  "survival_actions": [
      {
          "name": "Dodge",
          "available": true,
          "sort_order": 0,
          "title_tip": "'Dodge' is available by default.",
          "handle": "dodge",
          "sub_type": "survival_action",
          "type": "survival_actions",
          "type_pretty": "Survival Actions",
          "sub_type_pretty": "Survival Action",
          "selector_text": "Dodge"
      },
      ...
  ],
  ...
}</code></pre>"""
	),
    },
    "survivor_get_lineage": {
        "name": "/survivor/get_lineage/&lt;survivor_id&gt;",
        "methods": ["GET", "OPTIONS"],
        "desc": (
            '<p>This endpoint returns non-game-related data about a '
            'survivor, including their complete event log, i.e. the log '
            'of changes and updates to the survivor.</p>'
            '<p>The JSON that comes back from this endpoint <i>does not</i> '
            "include the survivor's OID, so be careful with your local scope "
            'when iterating through lists of survivors and calling this '
            'endpoint.</p>'
        ),
    },
    "zz_survivor_get_survival_actions": {
        "name": "/survivor/get_survival_actions/&lt;survivor_id&gt;",
        'deprecated': True,
        "methods": ["GET", "OPTIONS"],
        "desc": (
            '<p>Please use the <code>survival_actions</code> element returned '
            'by the <code>/survivor/get/&lt;survivor_id&gt;</code> instead.</p>'
        ),
    },

    # survivor shset
    "survivor_reset_attribute_details": {
        "name": "/survivor/reset_attribute_details/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["GET", "POST", "OPTIONS"],
        "desc": (
            "<p><b>GET</b> or <b>POST</b> to this endpoint to remove all "
            "gear and token effects from a survivor's attributes.</p>"
        )
    },
    "survivor_reset_damage": {
        "name": "/survivor/reset_damage/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["GET", "POST", "OPTIONS"],
        "desc": (
            "<p>Hit this endpoint to reset all damage locations.</p>"
        )
    },
    "zz_survivor_toggle_damage": {
        "name": "/survivor/toggle_damage/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        'deprecated': True,
        "desc": (
            '<p><b>POST</b> a damage location to this endpoint to toggle it on '
            'or off.</p>'
            '<p>This endpoint is deprecated. Use <code>set_attribute</code> '
            'instead (and <b>POST</b> a Boolean).</p>'
        ),
        'examples': [
            "{'location': 'brain_damage_light'}",
            "{'location': 'waist_damage_heavy'}",
        ],
    },
    "survivor_set_abilities_and_impairments": {
        "name": "/survivor/set_abilities_and_impairments/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        'desc': (
            "<p>Set the survivor's <code>abilities_and_impairments</code> list,"
            " automatically logging add/remove operations required to sync the "
            "existing list with the incoming one.</p>"
        ),
        'examples': [
            '{value: ["bitter_frenzy", "cancerous_illness", "tinker"]}'
        ],
    },
    "survivor_set_attribute": {
        "name": "/survivor/set_attribute/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p><b>Important!</b> As with the Settlement record, this is "
            "pretty much where you want to start with updates/edits for the "
            "survivor record <i>before</i> looking into using specialty "
            "routes.</p>"
            "<p>Basically, try this one first, and if it doesn get the result "
            "you want, then look at other endpoints.</p>"
            "<p>For this endpoint, you want to <b>POST</b> some JSON that "
            "includes both <code>attribute</code> and <code>value</code> keys, "
            "with an appropriate type value for <code>value</code>.</p>"
            "<p>You can use this one to update pretty much any attribute of "
            "the survivor sheet, including damage, and it is essentially the "
            "same as the <code>set_many_attributes</code> route (except for "
            "how it only does one attribute at a time).</p> "
            "<p>Refer to the following table for damage 'attributes':</p><table>"
            '<tr><th></th><th><div class="kd checkbox"></div></th><th><div class="kd checkbox heavy"></div></th></tr>'
            '<tr><td>brain</td><td>brain_damage_light</td><td></td>'
            '<tr><td class="kdm_manager_font">b</td><td></td><td>head_damage_heavy</td>'
            '<tr><td class="kdm_manager_font">d</td><td>arms_damage_light</td><td>arms_damage_heavy</td>'
            '<tr><td class="kdm_manager_font">c</td><td>body_damage_light</td><td>body_damage_heavy</td>'
            '<tr><td class="kdm_manager_font">e</td><td>waist_damage_light</td><td>waist_damage_heavy</td>'
            '<tr><td class="kdm_manager_font">f</td><td>legs_damage_light</td><td>legs_damage_heavy</td>'
            '</table>'
            '<p><b>Important!</b> For updating attributes that are lists of '
            'game assets, please use <code>replace_game_assets</code>.</p>.'
        ),
        'examples': [
            '{attribute: "abilities_and_impairments", value: ["crystal_skin", "dead_inside", "prepared"]}',
            '{attribute: "survival", value: 3}',
            '{attribute: "Head", value: 1}',
            '{attribute: "Understanding", value: 2}',
            '{attribute: "Luck", value: -3}',
            '{attribute: "brain_damage_light", value: true}',
            '{attribute: "legs_damage_heavy", value: false}',
            '{attribute: "Movement", value: 4}',
            '{attribute: "hunt_xp", value: 6}',
            '{attribute: "bleeding_tokens", value: 2}',
        ],
    },
    "survivor_set_attribute_detail": {
        "name": "/survivor/set_attribute_detail/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            '<p>This is the way to add attribute tokens to a survivor -OR- to '
            'update their attributes to reflect equipped gear.</p>'
            '<p><b>POST</b> some JSON reflecting the attribute and the tokens '
            "and/or gear adjustment using the 'detail' key.</p>"
            '<p>The examples below show how to add a +1 movement token, '
            'a -1 luck token and a +2 speed bonus from gear.</p>'
        ),
        'examples': [
            '{attribute: "Movement", detail: "tokens", value: 1}',
            '{attribute: "Luck", detail: "tokens", value: -1}',
            '{attribute: "Speed", detail: "gear", value: 2}',
        ],
    },
    "survivor_set_name": {
        "name": "/survivor/set_name/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p><b>POST</b> a 'name' value to this endpoint to change the "
            "survivor's name:</p><code>{name: 'Hungry Basalt'}</code>"
        )
    },
    "zz_survivor_set_sex": {
        "name": "/survivor/set_sex/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        'deprecated': True,
        "methods": ["POST", "OPTIONS"],
        "desc": '<p>Use the <code>set_attribute</code> route instead.</p>',
    },
    "zz_survivor_set_survival": {
        "name": "/survivor/set_survival/&lt;survivor_id&gt;",
        'deprecated': True,
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": '<p>Use the <code>set_attribute</code> route instead.</p>',
    },
    "survivor_set_affinities": {
        "name": "/survivor/set_affinities/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>This supersedes both <code>set_affinity</code>, and "
            "<code>update_affinities</code>, which are both deprecated in "
            "API releases higher than 1.50.n.</p>"
            "<p>The idea here is to <b>POST</b> some JSON containing one or "
            "all of the following keys: <code>red</code>, <code>green</code> "
            "or <code>blue</code>, and for each of those keys to have an "
            "integer value, e.g.:</p>"
            "<code>{red: 1, green: 0, blue:4}</code>"
            "<p>For convenience/laziness-sake, the API allows you to zero out "
            "an affinity by <i>not</i> setting a value for it.</p>"
            "<p><b>POST</b> <code>{red: 1, blue: 3}</code>, for example, to "
            "set he survivor's red affinities to 1, their blue affinities to "
            "three and their green affinities to zero.</p>"
        ),
        'examples': [
            '{red: 3, blue:1}',
            '{green: 4, red: 1}',
            '{blue: 0}'
        ],
    },
    "zz_survivor_set_bleeding_tokens": {
        "name": "/survivor/set_bleeding_tokens/&lt;survivor_id&gt;",
        'deprecated': True,
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": '<p>Use the <code>set_attribute</code> route instead.</p>',
    },
    "survivor_set_status_flag": {
        "name": "/survivor/set_status_flag/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>The API allows survivors to be 'flagged' with a status, which "
            "is an attribute that always evaluates to Boolean true if it "
            "exits, but which is <b>never set to Boolean false</b>.</p>"
            "<p>(This may see odd, but as a design pattern, it has its uses as "
            "an unambigious indicator of status: allowing these types of "
            "statuses to be false would result in potentially ambigious double "
            "negatives, etc.)</p>"
            "<p>To set a flag, simply <b>POST</b> it to this end point:</p>"
            "<code>{flag: 'cannot_consume'}</code>"
            "<p>To un-set a flag, <b>POST</b> the flag and the "
            "<code>unset</code> key:</p>"
            "<code>{flag: 'cannot_spend_survival', unset: true}</code>."
            "<p>Alternately, post the 'value' of Boolean false.</p>"
            "<p>Supported flags include:</p><table>"
            "<tr><td>cannot_activate_two_handed_weapons</td></tr>"
            "<tr><td>cannot_activate_two_plus_str_gear</td></tr>"
            "<tr><td>cannot_consume</td></tr>"
            "<tr><td>cannot_be_nominated_for_intimacy</td></tr>"
            "<tr><td>cannot_gain_bleeding_tokens</td></tr>"
            "<tr><td>cannot_spend_survival</td></tr>"
            "<tr><td>cannot_use_fighting_arts</td></tr>"
            "<tr><td>departing</td></tr>"
            "<tr><td>skip_next_hunt</td></tr>"
            "</table>"
        ),
        'examples': [
            '{flag: "cannot_spend_survival"}',
            '{flag: "cannot_consume", "value": false}',
            '{flag: "departing", "unset": true}',
            '{flag: "cannot_gain_bleeding_tokens"}'
        ],
    },
    "survivor_set_retired": {
        "name": "/survivor/set_retired/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>Takes a Boolean object as the value for a key called "
            "<code>retired</code>. Rejects anything else.</p>"
        ),
        'examples': [
            '{retired: true}',
            '{retired: false}',
        ],
    },
    "survivor_set_sword_oath": {
        "name": "/survivor/set_sword_oath/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>Starting with release 1.44.307, which adds support for the "
            "<b>Echoes of Death 3</b> expansion and the <i>Sword Oath</i> "
            "Fighting Art, the API can also track the sword that a survivor "
            "nominates as well as the number of wounds.</p>"
            "<p>Just <b>POST</b> any valid gear handle and the number of "
            "wounds to this endpoint:</p>"
        ),
        'examples': [
            "<code>{sword: 'bone_blade', wounds: 3}</code>",
        ],
    },
    "survivor_set_fighting_art_level": {
        "name": "/survivor/set_fighting_art_level/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>For Fighting Arts that support a level, such as the <i>Silk "
            "Surgeon</i> FA from <b>Spidicules</b>.</p>"
            "<p><b>POST</b> a Fighting Art handle and a list of which levels "
            "the survivor has.</p>"
            "<p><code>levels</code> should be a list of integers.</p>"
            "<p>(Supersedes the long-deprecated "
            "<code>toggle_fighting_arts_level</code> endpoint, which should "
            "no longer be used as of Jan 2022.)</p>"
        ),
        'examples': [
            "<code>{handle: 'silk_surgeon', levels: [0,1]}</code>",
            "<code>{handle: 'silk_surgeon', levels: [0,3,2]}</code>",
        ],
    },
    "survivor_toggle_sotf_reroll": {
        "name": "/survivor/toggle_sotf_reroll/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["GET", "POST", "OPTIONS"],
        "desc": (
            "<p>Hit this end point to toggle the survivor record's"
            "<code>sotf_reroll</code> attribute.</p>"
            "<p>If the record does not have this attribute, accessing this "
            "endpoint will create it and set it to <code>true</code>.</p>"
            "<p><b>Warning!<b></p> This attribute, since it is only used with "
            "certain campaign content, is <b>not</b> part of the survivor data "
            "model and <b>cannot</b> be toggled using the "
            "<code>toggle_boolean</code> endpoint!</p>"
        ),
    },
    "survivor_set_weak_spot": {
        "name": "/survivor/set_weak_spot/&lt;survivor_id&gt;",
        "subsection": "survivor_sheet",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p><b>POST</b> JSON defining a <code>'weak_spot'</code> value to "
            "this endpoint to set the survivor's weak spot.</p>"
            "<p>Set the value to 'UNSET' to remove a weak spot.</p>"
            "<p>Important!</p> Values supported by this endpoint are survivor "
            "hit locations, which <u>are capitalized</u> in our data model.</p>"
        ),
        'examples': [
            "<code>{weak_spot: 'Head'}</code>",
            "<code>{weak_spot: 'UNSET'}</code>",
        ],
    },
    # deprecated
    "zz_toggle_status_flag": {
        "name": "/survivor/toggle_status_flag/&lt;survivor_id&gt;",
        'deprecated': True,
        "methods": ["GET", "OPTIONS"],
        "subsection": "survivor_sheet",
        "desc": (
            '<p>Please use the <code>set_status_flag</code> route instead.</p>'
        ),
    },
    "zz_survivor_set_affinity": {
        "name": "/survivor/set_affinity/&lt;survivor_id&gt;",
        'deprecated': True,
        "methods": ["GET", "OPTIONS"],
        "subsection": "survivor_sheet",
        "desc": (
            '<p>Please use the <code>set_affinities</code> route instead.</p>'
        ),
    },
    "zz_survivor_update_affinities": {
        "name": "/survivor/update_affinities/&lt;survivor_id&gt;",
        'deprecated': True,
        "methods": ["GET", "OPTIONS"],
        "subsection": "survivor_sheet",
        "desc": (
            '<p>Please use the <code>set_affinities</code> route instead.</p>'
        ),
    },

    # survivor gear management
    "add_cursed_item": {
        "name": "/survivor/add_cursed_item/&lt;survivor_id&gt;",
        "subsection": "survivor_gear_management",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            '<p><b>POST</b> some JSON that includes a gear handle to add it to '
            "the survivor's list of cursed items.</p>"
        ),
        'examples': [
            "<code>{handle: 'thunder_maul'}</code>",
        ],
    },
    "rm_cursed_item": {
        "name": "/survivor/rm_cursed_item/&lt;survivor_id&gt;",
        "subsection": "survivor_gear_management",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>The reverse of the previous method. <b>POST</b> a gear handle "
            "to remove it.</p>"
        ),
        'examples': [
            "<code>{handle: 'blue_lantern'}</code>",
        ],
    },
    "set_gear_grid": {
        "name": "/survivor/set_gear_grid/&lt;survivor_id&gt;",
        "subsection": "survivor_gear_management",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            '<p><b>POST</b> an array named <code>gear_grid</code> that '
            'includes between one (1) and nine (9) key/value pairs '
            'where the key is a gear grid location and the value is a '
            'gear handle:</p>'
            """<pre><code>{'gear_grid': {
    'top_left': 'bone_blade',    'top_middle': 'bone_blade',    'top_right': 'bone_blade',
    'middle_left': 'bone_blade', 'middle_middle': 'bone_blade', 'middle_right': 'bone_blade',
    'bottom_left': 'bone_blade', 'bottom_middle': 'bone_blade', 'bottom_right': 'bone_blade',
    }
}</code></pre>"""
            '<p>Yes, I am aware that the central location is named '
            '"middle_middle": you laugh now, but you will thank me '
            'when you are able to programmatically iterate the table '
            'in one or two lines of code.</p>'
        ),
        'examples': [
            "<code>{top_left: 'bone_blade', 'top_middle': 'rawhide_headband'}</code>",
            "<code>{middle_middle: 'rawhide_vest', 'bottom_right': 'brain_mint', bottom_left: 'lantern_greaves'}</code>",
        ],
    },

    # notes
    "add_note": {
        "name": "/survivor/add_note/&lt;survivor_id&gt;",
        "subsection": "survivor_notes_management",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<b>POST</b> an array named <code>note</code> to this route that "
            "includes the following key/value pairs:"
            "<table><tr>"
            "<th>key</th><th>req/optional</th><th>type</th><th>note</th>"
            "</tr>"
            "<tr><td>note</td><td>R</td><td>str</td>"
            "<td>HTML is OK.</td></tr>"
            "<tr><td>pinned</td><td>O</td><td>bool</td><td></td></tr>"
            "</table>"
        )
    },
    "update_note": {
        "name": "/survivor/update_note/&lt;survivor_id&gt;",
        "subsection": "survivor_notes_management",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<b>POST</b> a note (in JSON format) back to this endpoint "
            "to update it. Note JSON that does not include the <i>_id</i>, "
            "attribute will be rejected!"
        )
    },
    "rm_note": {
        "name": "/survivor/rm_note/&lt;survivor_id&gt;",
        "subsection": "survivor_notes_management",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<b>POST</b> a note's OID to this endpoint to remove it: "
            "<code>{_id: 5fbe989f6515932455f4c5da}</code>."
        )
    },

    # survivor admin
    "survivor_set_color_scheme": {
        "name": "/survivor/set_color_scheme/&lt;survivor_id&gt;",
        "methods": ["POST", "OPTIONS"],
        "subsection": "survivor_admin",
        "desc": (
            "<p><b>POST</b> a <code>color_scheme</code> handle to this "
            "endpoint to set the Survivor Sheet attribute of the same name.</p>"
            "<p>There are couple of places where you can get a list of "
            "available color scheme handles:</p>"
        ),
        "examples": [
            "{color_scheme: 'TK'}"
        ],
    },
    "add_favorite": {
        "name": "/survivor/add_favorite/&lt;survivor_id&gt;",
        "subsection": "survivor_admin",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            '<p>The API takes a bit of an unusual approach to making a '
            "survivor a 'favorite' or starred survivor due to the fact that "
            "users can remove settlements (i.e. the parent record of a "
            "survivor record). Rather than having the User record contain a "
            "list of favorite survivors, we actually make a list of users on "
            "the survivor who have made the survivor one of their favorites."
            "</p><p>To add a user's OID to the survivor's list of users who "
            "have starred it, use the <code>user_email</code> key and an "
            "OID."
        ),
        'examples': [
            "{user_email: 'toconnell@thelaborinvain.com'}"
        ]
    },
    "rm_favorite": {
        "name": "/survivor/rm_favorite/&lt;survivor_id&gt;",
        "subsection": "survivor_admin",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>This is effectively the reverse of the "
            "<code>add_favorite</code> endpoint (above):</p>"
        ),
        'examples': [
            "{user_email: 'toconnell@thelaborinvain.com'}"
        ]
    },
    "survivor_set_email": {
        "name": "/survivor/set_email/&lt;survivor_id&gt;",
        "methods": ["POST", "OPTIONS"],
        "subsection": "survivor_admin",
        "desc": (
            "<p>Sets the survivor's <code>email</code> attribute, which "
            "determines the 'owner' of the survivor, from an access and "
            "permissions perspective.</p>"
            "<p><b>Important!</b> The API allows the creator of a survivor "
            "and it's owner (as determined by the <code>email</code> "
            "attribute) to modify it. Anyone else gets a 403.</p>"
        ),
        "examples": [
            "{email: 'toconnell@thelaborinvain.com'}"
        ],
    },
    "survivor_remove": {
        "name": "/survivor/remove/&lt;survivor_id&gt;",
        "subsection": "survivor_admin",
        "methods": ["GET", "POST", "OPTIONS"],
        "desc": (
            "<p>Removes the survivor.</p>"
        ),
    },

    # survivor relationships
    "survivor_set_parent": {
        "name": "/survivor/set_parent/&lt;survivor_id&gt;",
        "subsection": "survivor_relationships",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p>In order to set a survivor parent, you have to <b>POST</b> the "
            "<code>role</code> of the parent, as well as the OID of the "
            "parent.</p>"
            "<p>Possible <code>role</code> values are <code>father</code> and "
            "<code>mother</code>, all lower-case, exactly as they're printed "
            "here.</p>."
            "<p><b>POST</b>ing any other <code>role</code> values or an "
            "invalid OID (of the parent) will get you a 400 back.</p>"
        ),
        'examples': [
            "{role: 'father', oid: '60020d77ea3701e3ef793a6f'}",
            "{role: 'mother', oid: '51gea3596f57b836f182f691'}"
        ]
    },
    "survivor_set_partner": {
        "name": "/survivor/set_partner/&lt;survivor_id&gt;",
        "subsection": "survivor_relationships",
        "methods": ["POST", "OPTIONS"],
        "desc": (
            "<p><b>POST</b> a key/value pair where the value is the OID of "
            "the partner:</p>"
            "<code>{partner_id: '89gea3596f57b836f182fabc'}</code>"
            "<P>Finally, this end point supports a 'magic' value: if you use "
            "the string <code>UNSET</code> (all caps) as the value for the "
            "<code>partner_id</code>, this will cause the API To remove the "
            "<code>partner_id</code> attribute from the survivor compeltely "
            "(i.e. it will no longer be in the JSON of the serialized "
            "survivor record.</p>"
        ),
        'examples': [
            "{partner_id: '60020d77ea3701e3ef793a6f'}"
        ]
    },
}
