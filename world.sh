#!/bin/bash

#
#   works like admin.sh, except it has daemon modes
#

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
pushd $SCRIPTPATH > /dev/null

source venv/bin/activate
export PYTHONPATH="`pwd`"

python app/world $@ 
