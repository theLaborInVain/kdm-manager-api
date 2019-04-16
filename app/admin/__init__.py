"""

    This is the admin module. LOTS going on here:

        - command line administration methods
        - API methods for getting administrative info

"""

# local imports
from app import utils
from app.admin import notifications


def get_data(resource=None):
    """ Retrieves various types of admin panel data. If the requester wants
	something we don't have, raise a 422 """

    if resource == 'user_data':
        return panel.get_user_data()
    elif resource == 'settlement_data':
        return panel.get_settlement_data()
    elif resource == 'logs':
        return panel.serialize_system_logs()
    elif resource == 'webapp_alerts':
        return notifications.get_webapp_alerts()

    return utils.InvalidUsage("Admin resource '%s' does not exist!", status=400)
