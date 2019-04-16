"""

    This starts the API application. DO NOT make this file executable or attempt
    to execute it outside of the context of a virtual environment.

"""

from app import API

if __name__ == '__main__':
    API.run(
        host="0.0.0.0",
        port=API.settings.get('server', 'port'),
        ssl_context='adhoc'
    )
