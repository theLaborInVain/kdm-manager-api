#!/usr/bin/env bash

#
#   This script allows the server to be started in 'development' mode.
#   If you want to deploy the API in a production context, check the files
#   in the /deploy folder and use supervisord.
#

start_venv() {
    echo -e "\nVirtual Envrionment:"

    # 1.) start the generic venv of the app
    source venv/bin/activate

    # 2.) export env variables for our server
    export FLASK_ENV='development'

    # 3.) confirm to the CLI for the user
    PYTHON_PATH=`which python`
    PYTHON_VERS=`python --version`
    echo -e " * $PYTHON_PATH"
    echo -e " * Python $PYTHON_VERS"
    echo -e " * FLASK_ENV=$FLASK_ENV"
    echo -e "\nPIP:"
    pip install -r requirements.txt | grep -v 'already satisfied' 
    pip freeze $1 | while read x; do echo -e " * $x"; done
    echo -e
    echo -e "Flask server:"
}

start_venv
python api.py
