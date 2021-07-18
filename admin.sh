#!/bin/bash

#
#   This initializes the venv that the API runs in and passes all arguments from
#   STDIN to the __main__ namespace of the admin module (under apps).
#
#   Which, to put it another way, is to say that you should go check out that
#   module if you're interested in manual, CLI administration of the API.
#

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
pushd $SCRIPTPATH > /dev/null

source venv/bin/activate
export PYTHONPATH="`pwd`"

PYTHON_PATH=`which python`
PYTHON_VERS=`python --version`
echo -e " * interpreter: $PYTHON_PATH ($PYTHON_VERS)"
echo -e " *  PYTHONPATH: $PYTHONPATH"

python $SCRIPTPATH/app/admin $@ 
