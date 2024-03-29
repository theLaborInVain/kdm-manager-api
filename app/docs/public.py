"""

    These are the public endpoints that we document for the API. Nothing here
    requires JWT or other credentials to access.

"""


#
#   dashboard-related endpoints first
#

dashboard = {
    "stat": {
	"name": "/stat",
        "methods": ["GET"],
	"desc": (
            '<p>Returns basic information about the API.<p>'
            "<p>This can be used as a sort of 'ping' to test it if it's alive "
            "or as quick way to get the current version, etc.</p>"
	),
    },
    "stat": {
	"name": "/check_api_key",
        "methods": ["GET", "OPTIONS"],
	"desc": (
            "<p>Evaluates incoming request heders 'API-Key' value and returns "
            "200 if the incoming API key is known by the API.</p>"
            "<p>Otherwise, returns a 403.</p>"
        ),
    },
    "world": {
	"name": "/world",
        "methods": ["GET"],
	"desc": (
            '<p> Retrieve a JSON representation of aggregate/world stats.</p>'
	),
    },
}


#
#   game asset retrieval/lookup endpoints
#

game_asset_lookups = {
    'aaa_kingdom_death': {
        'name': '/kingdom_death',
        "methods": ["GET"],
        'desc': (
            '<p>Hit this endpoint to retrieve a JSON representation of every '
            '<i>Monster</i> game asset that the API tracks.</p>'
            '<p>While the other public routes (below) in this section allow '
            'more targeted asset retrieval, this endpoint, which is optimized '
            'for speed, just dumps <i>everything</i>.</p>'
            '<p><b>Important!</b> This endpoint dumps game assets at the '
            'HEAD revision of the game, typically the latest release published '
            'by Kingdom Death.</p>'
            '<p>To get the current HEAD revision, simply <code>/stat</code> '
            'the API.</p>'
        ),
    },
    'game_asset': {
        'name': '/game_asset',
        "methods": ["GET"],
        'desc': '<p>Returns a list of available game asset modules.</p>',
    },
    'game_asset_abilities_and_impairments': {
        'name': '/game_asset/abilities_and_impairments',
        'desc': 'Returns a JSON representation of known A&I assets.',
    },
    "game_asset_campaigns": {
        "name": "/game_asset/campaigns",
        "desc": """\
<p>Accepts a <code>name</code> or <code>handle</code> parameter included in the body
of the request (which should be JSON) and returns a JSON
representation of a campaign asset:</p>
<code>{"name": "People of the Lantern"}</code>
<p>...gets you back something like this:</p>
<code>{"handle": "people_of_the_lantern","milestones":
["first_child", "first_death", "pop_15", "innovations_5",
"game_over" ], "saviors": "1.3.1", "name": "People of the Lantern",
"default": true, "principles": ["new_life", "death", "society",
"conviction"], "always_available": { "location": ["Lantern
Hoard"], "innovation": ["Language"]},"nemesis_monsters": [
"butcher", "kings_man","the_hand","watcher"],"quarries": [
"white_lion","screaming_antelope","phoenix", "beast_of_sorrow",
"great_golden_cat", "mad_steed", "golden_eyed_king"],"type":
"campaign_definition"}</code>
<p>This also works with handles, e.g.:</p>
<code>{"handle": "people_of_the_stars"}</code>
<p>Like all lookup routes, if you <b>GET</b> this endpoint,
the API will return the definitions of all assets.</p>
        """,
    },
    'game_asset_cursed_items': {
        'name': '/game_asset/cursed_items',
        'desc': """\
<p>Returns a JSON representation of all known cursed items.</p>
<p>This is basically a lookup dictionary where the handles/keys correspond
to handles in the <code>gear</code> asset collection, but the values contain
references/hooks that can be used to look up curse effects.</p>
<p>This is a transitional method and will eventually be deprecated.</p>
        """,
    },
    'game_asset_disorders': {
        'name': '/game_asset/disorders',
        'desc': """\
<p>Returns a JSON representation of all known disorders.</p>
        """,
    },
    'game_asset_endeavors': {
        'name': '/game_asset/endeavors',
        'desc': """\
<p>Endeavors are a complex asset and their attributes are irregular.</p>
<p>At a minimum, a JSON representation of an endeavor includes its name and its
cost:</p>
<pre><code>
    'bloodletting_breathing_a_vein': {
        'name': 'Breathing a Vein',
        'cost': 1,
    },
</code></pre>
<p>Others include information that can be used to determine if a particular
endeavor is available. These will typically reference other asset handles:</p>
<pre><code>
    'build_skinnery': {
        'name': 'Build',
        'desc': 'Skinnery',
        'cost': 1,
        'class': 'available_endeavors_build',
        'hide_if_location_exists': 'skinnery',
    },
</code></pre>
<p>Finally, watch out for some odd, not-totally-conventional or predictable
handle names when working with Endeavor assets, e.g.
<code>subterranean_agriculture_2_build_wet_resin_crafter</code>. We err on
the side of being over-descriptive with these handles to avoid ambiguity.</p>
        """,
    },
    'game_asset_events': {
        'name': '/game_asset/events',
        'desc': """\
<p>Returns a JSON representation of all known story and settlement events.</p>
        """,
    },
    "game_asset_expansions": {
        "name": "/game_asset/expansions",
        "desc": """\
<p><b>POST</b> a <code>name</code> or <code>handle</code> to this endpoint
to get a particular expansion's asset definition.</p>
<p>For example, if you <b>POST</b> this:</p>
<code>{handle: "gorm"}</code>
<p>You'll get back a nice hunk of JSON definiting the asset:</p>
<pre><code>{
    "ui": {
        "pretty_category": "Quarry"
    },
    'maximum_intro_ly': 1,
    'late_intro_event': 'gorm_approaching_storm',
    "quarries": [
        "gorm"
    ],
    "name": "Gorm",
    "always_available": {
        "location": [
            "Gormery",
            "Gormchymist"
        ],
        "innovation": [
            "Nigredo"
        ]
    },
    "released": {
        "$date": 1457913600000
    },
    "type_pretty": "Expansion",
    "timeline_add": [
        {
            "handle": "gorm_approaching_storm",
            "type": "story_event",
            "ly": 1
        },
        {
            "handle": "gorm_gorm_climate",
            "type": "settlement_event",
            "name": "Gorm Climate",
            "ly": 2
        }
    ],
    "handle": "gorm",
    "type": "expansion",
    "sub_type": "expansion",
    "flair": {
        "color": "EAE40A",
        "bgcolor": "958C83"
    }
}</code></pre>
<p>This route also supports lookups via <code>name</code> values,
e.g. <code>{name: "Flower Knight"}</code> or similar.</p>
<p>If you <b>GET</b> this route, it will return the definitions
for all supported expansion content as a dictionary/hash.</p>
        """,
    },
    'game_asset_fighting_arts': {
        'name': '/game_asset/fighting_arts',
        'desc': """\
<p>Returns a JSON representation of all known Fighting Arts.</p>
        """,
    },
    "game_asset_gear": {
        "name": "/game_asset/gear",
        "desc": """\
<p><b>POST</b> a <code>name</code> or <code>handle</code> to this endpoint
to do gear lookups:</p>
<code>{handle: "lantern_halberd"}</code>
<p>...gets you back a JSON representation of the asset:</p>
<pre><code>{
    "handle": "lantern_halberd",
    "name": "Lantern Halberd",
    "rules": [
        "Reach 2",
        "Irreplaceable",
        "Unique"
    ],
    "type_pretty": "Gear",
    "keywords": [
        "weapon",
        "melee",
        "two-handed",
        "spear",
        "other"
    ],
    "type": "gear",
    "sub_type": "rare_gear",
    "desc": "After attacking, if standing, you may move up to 2 spaces directly away from the monster."
}</code></pre>
<p>This route also supports <code>name</code> lookups, e.g. <code>
{name: "Vespertine Bow"}</code>, etc.</p>
<p><b>GET</b> this endpoint to dump all gear.</p>
        """,
    },
    'game_asset_innovations': {
        'name': '/game_asset/innovations',
        'desc': '<p>Returns a JSON representation of all Innovations.</p>',
    },
    'game_asset_locations': {
        'name': '/game_asset/locations',
        'desc': """\
<p>Pay attention to the <code>type</code> and <code>sub_type</code>
attributes of Settlement Location dictionaries: many of them are 'pseudo'
locations meant to facilite gear organization, etc. and you typically will not
want to show a user a list of all of these assets in a tracker app.</p>
        """,
    },
    "game_asset_monsters": {
        "name": "/game_asset/monsters",
        "desc": """\
<p>
    Accepts a "name" or "handle" parameter in the <b>POST</b> body and
    returns a JSON representation of a monster type game asset.
    For example, <b>POST</b>ing to /monster with JSON such as this:
</p>
<code>{"name": "White Lion Lvl. 1"}</code>
<p>...returns JSON like this: </p>
<code>{"comment": "Lvl. 1", "handle": "white_lion", "name":
"White Lion", "level": 1, "levels": 3, "sort_order": 0, "type":
"quarry"}</code>
<p>Or, with a handle:</p>
<code>{"handle": "manhunter"}</code>
<p>...you get:</p>
<pre><code>{
    "handle": "manhunter",
    "name": "Manhunter",
    "levels": 4,
    "sort_order": 103,
    "type": "nemesis",
    "selectable": false,
    "misspellings": ["THE MANHUNTER", "MAN HUNTER"],
}</code></pre>
<p>Like all lookup routes, if you <b>GET</b> this endpoint,
the API will return the definitions of all assets.</p>
        """,
    },
    'game_asset_resources': {
        'name': '/game_asset/resources',
        'desc': '<p>Returns a JSON representation of all known resources.</p>',
    },
    'game_asset_strain_milestones': {
        'name': '/game_asset/strain_milestones',
        'desc': '<p>Returns a JSON representation of all Strain Milestones.</p>'
    },
    'game_asset_survival_actions': {
        'name': '/game_asset/survival_actions',
        'desc': '<p>Returns a JSON representation of all Survival Actions.</p>'
    },

    'zz_game_asset_settlements': {
        'name': '/game_asset/settlements',
        'deprecated': True,
        'desc': (
            '<p>Starting February 2021, this endpoint is deprecated.</p>'
        ),
    },
}


user_creation_and_auth = {
    "new_user": {
        "name": "/new/user",
        "key": True,
        "desc": """\
<p>Include the valid email address and password in the JSON body of your
<b>POST</b> to create a new user:</p>
<code>{'username': 'demo@kdm-manager.com', 'password': 'tehH4x0r'}</code>
<p> If you get a 200 back from the API, the user was created without
issue. Otherwise, this route produces some pretty explicit feedback when it
returns anything other than a 200.</p>\
""",
    },
    "login": {
        "name": "/login",
        "desc": """\
<p>
    The KD:M API uses JSON Web Tokens (<a
    href="https://jwt.io/">https://jwt.io</a>) to manage user
    sessions and user authentication.
</p>
<p>
    <b>POST</b> to this route with JSON containing user credentials in
    the body of the request to get a token:</p>
    <code>{"username": "demo@kdm-manager.com", "password": "l33th4x0r"}</code>
    <p>...if your credential checks out, you get a token and the the
    the user's ID (see below for working with users) back. Easy!</p>\
	""",
    },
}

password_reset = {
    "reset_password_request_code": {
        "name": "/reset_password/request_code",
        "desc": """\
<p> Resetting a password is a two-part process: first, you request a recovery
code by posting a registered user's email address to this route. This emails
your user with a URL that they can use to reset their password. <p>
<p> To request a recovery code, simply <b>POST</b> some JSON containting the
email of the user:</p>
<code>{'username': 'demo@kdm-manager.com'}</code>
<p>If this comes back 200, then the user has been emailed. Otherwise, if you
get a non-200 response, it'll have specific reasons why it did not work.</p>
<p>Additionally, if you want to handle the password reset in your own app
(the default app is https://kdm-manager.com), which you probably do, just
include the <code>app_url</code> attribute in your post:</p>
<code>
    {'username': 'demo@kdm-manager.com',
    'app_url': 'https://my-badass-kdm-app.com'}
</code>
<p>Assuming that the user email is legint, <b>POST</b>ing this value will
cause the email that the user receives to include your URL:</p>
<code><pre>
Hello demo@kdm-manager.com!

 You are receiving this message because https://my-badass-kdm-app.com recieved
a password reset request for your user, demo@kdm-manager.com.

 If you did not initiate a password reset request, please ignore this email
and continue to use your existing/current credentials: they will not be
altered in any way!

 If you made this request and would like to reset your password, please sign
https://my-badass-kdm-app.com?recover_password=True&recovery_code=MC9AU4I4NFYKJ3TWPLWVPHX29N2U08
</pre></code>
<p>From here, you would parse the user's request to your (badass) app, get their
email address and the password they want to use, and then use the
<code>/reset_password/reset</code> endpoint (below) to finish the job.</p>
<p><b>PROTIP:</b> the recovery URL that the API generates for the email
starts at the question mark, so you can put in whatever endpoint you need on
your own app, e.g. "https://my-badass-kdm-app/reset_password" or similar.
Just be careful not to use a trailing slash!</p>\
        """,
    },
    "reset_password_reset": {
        "name": "/reset_password/reset",
        "desc": """\
<p> Before you <b>POST</b> to this route, you need a recovery code.<p>
<p>Once you have it, include it with the user's email and <b>new</b> password in
the body of your request:</p>
<code>{'username': 'demo@kdm-manager.com', 'password': 's3cr3tP4ss',
'recovery_code': '9FH3BKSNFI37FB476ZHABNDOWHEUSYAB234'}</code>
<p>If your post comes back with a 200, then the user's password has been changed
to the password you <b>POST</b>ed, and you can use it to log them in.</p>
        """,
    },
}

ui_ux_helpers = {
    "get_random_names": {
        "name": "/get_random_names/&lt;count&gt;",
        "methods": ["GET"],
        "desc": """\
<p>Returns <code>count</code> random names for each possible survivor sex.</p>
<p><b>Important!</b>This method DOES NOT accept <b>POST</b>-type requests and
<code>count</code> must be an integer!</p>
<p>Output looks like this:</p>
                <pre><code>{
    "M": [
        "Fingal",
        "Pelagius",
        "Stark"
    ],
    "F": [
        "Hope",
        "Moana",
        "Rasha"
    ]
}
</code></pre>
        """,
    },
    "get_random_surnames": {
        "name": "/get_random_surnames/&lt;count&gt;",
        "methods": ["GET"],
        "desc": """\
<p>Returns <code>count</code> random surnames.</p>
<p>Output is just an array of strings:</p>
<pre><code>[
    "Skyhunter",
    "Darkhunter",
    "Stormson",
    "Butcher",
    "Hammerheart"
]</code></pre>
<p><b>Important!</b>This method DOES NOT accept <b>POST</b>-type
requests and <code>count</code> must be an integer!</p>\
        """,
    },
}
