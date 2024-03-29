# The KDM API
The API used by [https://kdm-manager.com](https://kdm-manager.com) and related
[Kingdom Death: Monster](https://kingdomdeath.com) utilities.

* Webapp: [Flask](http://flask.pocoo.org/) + [AngularJS](https://angularjs.org/) (1.754)
* Webserver: [NGINX](https://www.nginx.com/) + [Gunicorn](http://gunicorn.org/)


# Important!

**Neither the code stored in this repository nor the code deployed at
[https://api.kdm-manager.com](https://api.kdm-manager.com)) are authorized,
developed, supported by or otherwise affiliated with Kingdom Death or Adam 
Poots Games, LLC.**


# About

Please read the information below before cloning or forking this repository.


## Licensing and permission
The KDM API is developed and maintained by [The Labor in Vain](https://thelaborinvain.com)
and the code in this repository is available under the terms of the MIT license
(i.e. `LICENSE` in the project root directory).

This license covers application code in this repository only. The license 
**does not and cannot** pertain to the game assets (in the `/app/assets` 
folder), which are __the sole property of Adam Poots Games, LLC.__ and which
are presented here without authorization.


## Issues
Please use
[GitHub's Issues utility](https://github.com/theLaborInVain/kdm-manager-api/issues)
to report issues to the repository maintainer.


# Installation instructions

Install host dependencies:

    # apt-get -y update
    # apt-get -y install python3 python3-venv python3-dev supervisor nginx git mongodb

Navigate to your home and clone the repo:

    $ cd 
    $ git clone https://github.com/theLaborInVain/kdm-manager-api.git


## Run

**Important!** The API server will not start without a file called
`settings_private.cfg` in the project's root directory. This file is _not_
included in the distribution, and you will have to create it manually.

Run the dev server from the root of the project directory:

    $ cd kdm-manager-api
    $ ./server.sh

Assuming everything went according to plan, this should start listening
on 0.0.0.0:8013 and responding to requests.


## Deploy

**Important!** At the time of the 1.0.0 release of the API, the install files
still have some hard-coded paths, e.g. `/home/toconnell` and similar. Deploying
the API as a different user will require the modification of these files!

In order to deploy, **perform the steps above under _Installation instructions_
 first**, then navigate to the project's root directory and run the `install.sh`
script as the root user:

    # cd kdm-manager-api
    # ./install.sh

The `install.sh` script will reload both nginx and `supervisord`, at which point
the API should be running on 127.0.0.1:8013 and nginx should be listening for
requests for https://api.kdm-manager.com

(Modify the /deploy/nginx.conf file to change this.)


## System administration

If you do choose to deploy the API, you'll probably want to rotate the logs (in
the application's `logs/` folder).

The API comes with a simple _logrotate_ configuration file, and using it with
your crontab is probably the most convenient way:

    #30 2 * * * /usr/sbin/logrotate -s /home/toconnell/logrotate/status /home/toconnell/kdm-manager-api/deploy/logrotate.conf > /dev/null 2>&1

(Obviously, you will need to create a 'logrotate' directory before this will run.)
