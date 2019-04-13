#!/usr/bin/env bash

start_venv() {
    echo -e "\nVirtual Envrionment:"

    # 1.) start the generic venv of the app
    source venv/bin/activate

    # 2.) export env variables for our server
    export FLASK_ENV=$1

    # 3.) confirm to the CLI for the user
    PYTHON_PATH=`which python`
    PYTHON_VERS=`python --version`
    echo -e " * $PYTHON_PATH"
    echo -e " * Python $PYTHON_VERS"
    echo -e " * FLASK_ENV=$FLASK_ENV"
    echo -e "\nPIP:"
    pip freeze $1 | while read x; do echo -e " * $x"; done
    echo -e
    echo -e "Flask server:"
}

case "$1" in
    dev)
        start_venv development
        python api.py
        ;;
    *)
        echo "Usage: $NAME {dev}" >&2
        exit 3
esac
