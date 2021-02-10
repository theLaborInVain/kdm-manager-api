#!/usr/bin/env bash

SUPERVISORCTL=`which supervisorctl`

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
    pip install -r requirements.txt | grep -v 'already satisfied' 
    pip freeze $1 | while read x; do echo -e " * $x"; done
    echo -e
    echo -e "Flask server:"
}

deploy() {

    OPERATION=$1

    if [[ $EUID -ne 0 ]]; then
       echo -e "\n\tThis operation must be performed by root!\n"
       exit 1
    fi

    $SUPERVISORCTL $OPERATION kdm-manager-api
    $SUPERVISORCTL $OPERATION kdm-manager-api-world-daemon

}

case "$1" in
    status)
        deploy $1
        ;;
    start)
        echo -e "Starting API server..."
        deploy $1
        ;;
    stop)
        echo -e "Stopping API server..."
        deploy $1
        ;;
    restart)
        echo -e "Restarting API server..."
        deploy $1
        ;;
    dev)
        start_venv development
        python api.py
        ;;
    *)
        echo "Usage: $NAME {status|start|stop|restart|dev}" >&2
        exit 3
esac
