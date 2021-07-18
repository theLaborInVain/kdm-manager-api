#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
pushd $SCRIPTPATH/.. > /dev/null

source venv/bin/activate
export FLASK_ENV=production
venv/bin/gunicorn -b localhost:8013 -w 4 app:API
