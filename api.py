"""

    This starts the API application. DO NOT make this file executable or attempt
    to execute it outside of the context of a virtual environment.

"""

from app import API

if __name__ == '__main__':
    print(' * KDM API version %s' % API.config['VERSION'])
    API.run(
        host="0.0.0.0",
        port=API.config['PORT'],
        ssl_context = (
            API.config['DEV_SSL_CERT'],
            API.config['DEV_SSL_KEY']
        ),
    )
