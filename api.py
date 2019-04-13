from app import api

if __name__ == '__main__':
    api.run(
        host="0.0.0.0",
        port=api.settings.get('server','port'),
        ssl_context='adhoc'
    )
