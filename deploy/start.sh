#!/bin/bash

pushd /home/toconnell/kdm-manager-api
source venv/bin/activate
export FLASK_ENV=production
venv/bin/gunicorn -b localhost:8013 -w 4 app:api
