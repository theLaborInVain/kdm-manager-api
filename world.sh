#!/bin/bash

#
#   works like admin.sh, except it has daemon modes
#

pushd /home/toconnell/kdm-manager-api > /dev/null 2>&1
source venv/bin/activate
export PYTHONPATH="`pwd`"

python app/world $@ 
