#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo -e "\n\tThis script must be run as root!\n" 
   exit 1
fi


SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
pushd $SCRIPTPATH > /dev/null


install() {
    echo -e " Creating symlinks:"
    ln -v -s $SCRIPTPATH/deploy/supervisor.conf /etc/supervisor/conf.d/kdm-manager-api.conf
    ln -v -s $SCRIPTPATH/deploy/world_supervisor.conf /etc/supervisor/conf.d/kdm-manager-api-world-daemon.conf
    ln -v -s $SCRIPTPATH/deploy/nginx.conf /etc/nginx/sites-enabled/kdm-manager-api
    echo -e "\n Reloading services:"
    /etc/init.d/nginx reload
    supervisorctl reload
    sleep 5
    tail /var/log/supervisor/supervisord.log
    echo -e ""
    netstat -anp |grep "0.0.0.0"
    echo -e "\n Done!\n"
}



read -sn 1 -p "
 Press any key to create links to $SCRIPTPATH/deploy files...
";echo

install
