"""

    No blueprints in this app! All the routes happen in this module.

    Some major changes in the 1.0.0 release:

        - the request_broker.py module is no more!
        - admin is a module in apps/ now, and has its own methods

"""

# stdlib
import json

# json/bson/oid
from bson.objectid import ObjectId
from bson import json_util

# flask!
import flask
import flask_jwt_extended

#
#   app imports
#
#from api.models import users, settlements, names

#   app module imports
from app import admin, API, assets, docs, utils, world
from app.models import names, users
from app.utils import crossdomain

#import world



#
#   browser-facing endpoints, e.g. stat, documentation, etc..
#

#       stat (supersedes deprecated settings routes)

@API.route("/stat")
@crossdomain(origin=['*'])
def stat_api():
    """ This is basically a ping. Returns the generic API meta data dict
    as JSON. """
    return flask.Response(
        response=json.dumps(utils.api_meta, default=json_util.default),
        status=200,
        mimetype="application/json"
    )

@API.route("/robots.txt")
def robots():
    """ The default return for accessing https://api.kdm-manager.com (or
    equivalent endpoint), which gets you the API docs. """
    return flask.send_file("static/html/robots.txt")




#   Notifications

@API.route("/get/notifications", methods=["GET", "OPTIONS"])
@crossdomain(origin=['*'])
def get_notifications():
    """ Retrieves notifications created by the admins via the panel (below).
    This is is a public route, i.e. requires no authorization. """
    return admin.notifications.get_webapp_alerts()


#
#      ADMIN PANEL
#

@API.route("/admin")
@API.basicAuth.login_required
def panel():
    """ Gets the admin panel. Requires basicAuth. """
    return flask.render_template(
        '/admin_panel/_main.html',
        user = json.dumps(flask.request.User.user, default=json_util.default),
        api_key = utils.settings.get('keys','api_key'),
    )


@API.route("/admin/get/<resource>", methods=["GET", "OPTIONS"])
@API.basicAuth.login_required
def admin_view(resource):
    """ Retrieves admin panel resources as JSON. """
    return admin.get_data(resource)


@API.route("/admin/notifications/<method>", methods=["POST"])
@API.basicAuth.login_required
def admin_notifications(method):
    """ Creates a new admin type asset. Requires basicAuth."""
    return admin.get_notifications(method)


@API.route("/admin/user_asset/<action>", methods=['POST'])
@API.basicAuth.login_required
def admin_get_user(action):
    """ Gets a user by email; login must be included in the POST. Calls the
    response method of the User Object associated with <action>. """

    utils.check_api_key()

    user_login = flask.request.get_json().get('login', None)
    user_record = utils.mdb.users.find_one({'login': user_login})

    # die if we can't find the user record in MDB
    if user_login is None or user_record is None:
        return utils.http_404

    user_object = assets.get_user_asset('user', user_record['_id'])
    if isinstance(user_object, flask.Response):
        return user_object
    return user_object.request_response(action)


@API.route("/admin/releases/<action>", methods=['POST','GET','OPTIONS'])
@API.basicAuth.login_required
def admin_releases(action):
    """ How we work with releases. POST a dict with an 'action' value
    to take that action. """
    return admin.releases.do(action)


#
#   documentation
#

@API.route("/")
def index():
    """ The default return for accessing https://api.kdm-manager.com (or
    equivalent endpoint), which gets you the API docs. """
    return flask.send_file("static/html/docs.html")

@API.route("/changelog")
@API.route("/changelog.json")
@API.route("/change_log")
@API.route("/change_log.json")
def dump_change_log():
    """ Dumps the change log. """
    return admin.releases.do('dump')


@API.route("/docs/<action>/<render_type>")
def render_documentation(action, render_type=None):
    """ These routes get you various representations of the contents of the
    docs module.

    For now, the supported 'action' list includes only the following::

        - get: this basically retrieves all extant documentation
        - get_documented_endpoints: calls this method of the docs object,
            which basically returns a set of the currently documented
            endpoints
        - get_sections: returns all sections defined in docs.sections

    The only supported 'render_type' is 'json' (case-insensitive).

    """

    response = utils.http_404           # default response

    render_type = render_type.upper()   # case-insensitive: json/JSON

    docs_object = docs.DocumentationObject()

    if action == 'get':
        if render_type == 'JSON':
            j = json.dumps(
                docs_object.render_as_json(),
                default=json_util.default
            )
            response = flask.Response(
                response=j,
                status=200,
                mimetype="application/json"
            )
    elif action == 'get_documented_endpoints':
        output = docs_object.get_documented_endpoints()
        if render_type == 'JSON':
            response = flask.Response(
                response=json.dumps(output),
                status=200,
                mimetype="application/json"
            )
        elif render_type == 'TEXT':
            response = flask.Response(
                response="\n".join(output),
                status=200,
                mimetype="application/json"
            )
    elif action == 'get_sections':
        if render_type == 'JSON':
            j = json.dumps(
                docs_object.dump_sections(),
                default=json_util.default
            )
            response = flask.Response(
                response=j,
                status=200,
                mimetype="application/json"
            )

    return response



#   WORLD

@API.route("/world")
@crossdomain(origin=['*'], headers='Content-Type')
def world_json():
    """ Renders the world data (from the world module) in JSON. """

    world_object = world.World()

    output = {"world_daemon": {'msg': 'DEPRECATED'}}
    output.update(world_object.list(dict))

    response = flask.Response(
        response=json.dumps(output, default=json_util.default),
        status=200,
        mimetype="application/json"
    )
    return response



#   game asset lookups

@API.route("/game_asset")
@API.route("/game_assets")  # as a courtesy/concession
@crossdomain(origin=['*'])
def list_game_assets():
    """ Dumps a list of all available game assets (does not include meta and
    webapp asset modules. """
    return flask.Response(
        response=json.dumps(
            assets.list(game_assets=True),
            default=json_util.default
        ),
        status=200,
        mimetype="application/json"
    )

@API.route("/game_asset/<asset_type>", methods=API.default_methods)
@API.route("/game_assets/<asset_type>", methods=API.default_methods)
@crossdomain(origin=['*'])
def lookup_asset(asset_type):
    """ Looks up game asset collection assets. Or, if you GET it, dumps the
    initialized asset module's assets dictionary. """

    if asset_type not in assets.list():
        return flask.Response(
            response="/game_asset/%s is not a supported endpoint!" % asset_type,
            status=404,
        )

    return assets.get_game_asset(asset_type)


#
#   UI/UX Helpers
#

@API.route("/get_random_names/<count>")
@crossdomain(origin=['*'], headers='Content-Type')
def get_random_names(count):
    """ Rapid-fire random name generator for FIRST names. """
    names_object = names.Assets()
    return flask.Response(
        response=json.dumps(
            names_object.get_random_names(int(count)),
            default=json_util.default
        ),
        status=200,
        mimetype="application/json"
    )

@API.route("/get_random_surnames/<count>")
@crossdomain(origin=['*'], headers='Content-Type')
def get_random_surnames(count):
    """ Rapid-fire random name generator for LAST names. """
    names_object = names.Assets()
    return flask.Response(
        response=json.dumps(
            names_object.get_random_surnames(int(count)),
            default=json_util.default
        ),
        status=200,
        mimetype="application/json"
    )


#
#   User creation and auth
#

@API.route("/login", methods=["POST", "OPTIONS"])
@crossdomain(origin=['*'])
def get_token(check_pw=True, user_id=False):
    """ Tries to get credentials from the request headers. Fails verbosely."""

    user_object = None

    if check_pw:
        if flask.request.json is None:
            return flask.Response(
                response="JSON payload missing from /login request!",
                status=422
            )
        user_object = users.authenticate(
            flask.request.json.get("username", None),
            flask.request.json.get("password", None)
        )
    else:
        user_object = users.User(_id=user_id)

    if user_object is None:
        return utils.http_401

    tok = {
        "_id": str(user_object.user["_id"]),
        'access_token': flask_jwt_extended.create_access_token(
            identity=user_object.jsonize()
        ),
    }

    return flask.Response(
        response=json.dumps(tok),
        status=200,
        mimetype="application/json"
    )


@API.route("/reset_password/<action>", methods=["POST", "OPTIONS"])
@crossdomain(origin=['*'])
def reset_password(action):
    """ Routes for requesting and performing a password reset. """
    setattr(flask.request, 'action', action)
    if action == 'request_code':
        return users.initiate_password_reset()
    elif action == 'reset':
        return users.reset_password()

    err_msg = "'%s' is not a valid action for this route." % action

    return flask.Response(response=err_msg, status=422)



#
#   private routes - past here, you've got to authenticate
#

@API.route("/authorization/<action>", methods=["POST", "GET", "OPTIONS"])
@crossdomain(origin=['*'])
def refresh_auth(action):
    """ Uses the 'Authorization' block in the request header to return a fresh
    token for a user. """

    # first, drop GETs trying to do a refresh: we don't play that shit
    if action == 'refresh' and flask.request.method == 'GET':
        return utils.http_405

    setattr(flask.request, 'action', action)

    # check the headers; API key first, then user-level auth
    utils.check_api_key()
    if not "Authorization" in flask.request.headers:
        return utils.http_401
    else:
        auth = flask.request.headers["Authorization"]

    if action == "refresh":
        user = users.refresh_authorization(auth)
        if user is not None:
            return get_token(check_pw=False, user_id=user["_id"])
        return utils.http_401
    elif action == "check":
        return users.check_authorization(auth)

    # if we strike out, we're obviously not authorized:
    return utils.http_402


@API.route("/new/<asset_type>", methods=["POST", "OPTIONS"])
@crossdomain(origin=['*'])
def new_asset(asset_type):
    """ Uses the 'Authorization' block of the header and POSTed params to create
    a new settlement. """

    utils.check_api_key()

    setattr(flask.request, 'action', 'new')

    # first, check to see if this is a request to make a new user. If it is, we
    #   don't try to pull the user from the token b/c it doesn't exist yet.
    #   Instead, initialize a user obj w/ no _id to call User.new()
    if asset_type == 'user':
        user_object = users.User()
        output = user_object.serialize('create_new')
        output["Authorization"] = {
            'access_token': flask_jwt_extended.create_access_token(
                identity=user_object.jsonize()
            ),
            "_id": str(user_object.user["_id"]),
        }
        return flask.Response(
            response=json.dumps(output, default=json_util.default),
            status=200,
            mimetype="application/json"
        )

    # otherwise, if we're creating any other type of user asset, do it using
    #   the generic method in the app/assets/__init__.py module
    flask.request.collection = asset_type
    flask.request.User = users.token_to_object(flask.request, strict=False)

    return assets.new_user_asset(asset_type)


@API.route("/<collection>/<action>/<asset_id>", methods=API.default_methods)
@crossdomain(origin=['*'])
def collection_action(collection, action, asset_id):
    """ This is our major method for retrieving and updating settlements.

    This is also one of our so-called 'private' routes, so you can't do this
    stuff without an authenticated user.
    """

    # fail anything without a valid OID right now, rather than spinning up a lot
    #   of machinery only to fail the request later
    if not ObjectId.is_valid(asset_id):
        err_msg = 'The /%s/%s/ route requires a valid Object ID!'
        return flask.Response(
            response=err_msg % (collection, action),
            status=400
        )

    utils.check_api_key()

    # update the request object
    flask.request.collection = collection
    setattr(flask.request, 'action', action)
    flask.request.User = users.token_to_object(flask.request, strict=False)

    asset_object = assets.get_user_asset(collection, asset_id)

    if isinstance(asset_object, flask.Response):
        return asset_object

    return asset_object.request_response(action)


@API.route("/avatar/get/<image_oid>", methods=["GET"])
@crossdomain(origin=['*'])
def serve_avatar_image(image_oid):
    """ Retrieves a survivor avatar from the GridFS system, sort of like a
    webserver would. Note to self: replace this with some kind of webserver
    functionality."""
    avatar = utils.GridfsImage(image_oid)
    return avatar.render_response()


#
#   DEV SECTION! These routes are not used in production (because the webserver
#       does them). YHBW
#

@API.route('/static/<sub_dir>/<path:path>')
def route_to_static(path, sub_dir):
    """ Generic /static/* endpoints served here."""
    return flask.send_from_directory('static/%s' % sub_dir, path)

@API.route("/favicon.ico")
def favicon():
    """ So you can see Logan's pretty logo in your dev environment."""
    return flask.send_file("static/media/images/favicon.png")
