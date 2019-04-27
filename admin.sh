#!/bin/bash

pushd /home/toconnell/kdm-manager-api
source venv/bin/activate
export PYTHONPATH="`pwd`"

PYTHON_PATH=`which python`
PYTHON_VERS=`python --version`
echo -e " * interpreter: $PYTHON_PATH ($PYTHON_VERS)"
echo -e " *  PYTHONPATH: $PYTHONPATH"

python app/admin $@ 
