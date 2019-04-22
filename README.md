# The KDM API
The API used by [https://kdm-manager.com](https://kdm-manager.com) and related
[Kingdom Death: Monster](https://kingdomdeath.com) utilities.

* Webapp: [Flask](http://flask.pocoo.org/) + [AngularJS](https://angularjs.org/) (1.754)
* Webserver: [NGINX](https://www.nginx.com/) + [Gunicorn](http://gunicorn.org/)

# Important Information!

Please read the information below before cloning or forking this repository.

## About
The KDM API is developed and maintained exclusively by 
[The Labor in Vain](https://thelaborinvain.com).


## Issues
Please use
[GitHub's Issues utility](https://github.com/theLaborInVain/kdm-manager-api/issues)
to report issues to the repository maintainer.


## Intellectual property
**Neither the [https://kdm-manager.com](https://kdm-manager.com) service nor any
of the software utilized by that service (including the API deployed at
[https://api.kdm-manager.com](https://api.kdm-manager.com)) are developed,
authorized, supported by or affiliated with Kingdom Death or Adam Poots Games,
LLC.**

For more information, please refer to
[the 'About' section of the project's development blog](http://kdm-manager.blogspot.com/p/credits-and-acknowledgements.html).


## Licensing and permission
The MIT license (`LICENSE` in the project root directory) covers application and
API code in this repository, but it does not and cannot cover the game assets
 (in the `/app/assets` folder), which are the sole property of Kingdom Death.



# Installation instructions

Install host dependencies:

    # apt-get -y update
    # apt-get -y install python3 python3-venv python3-dev supervisor nginx git mongodb

Navigate to your home and clone the repo:

    $ cd 
    $ git clone https://github.com/theLaborInVain/kdm-manager-api.git

Install app dependencies:

    $ cd kdm-manager-api
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ deactivate


## Run

The API server will not start without a file called `settings_private.cfg` in
the project's root directory.

Run the dev server from the root of the project directory:

    $ cd kdm-manager-api
    $ ./server.sh dev

Assuming everything went according to plan with pip, this should start listening
on 0.0.0.0:8013 and responding to requests.


## Deploy

**Important!** At the time of the 1.0.0 release of the API, the install files
have some hard-coded paths, e.g. `/home/toconnell` and similar. Deploying the
API as a different user will require the modification of these files!

In order to deploy, **perform the steps above under _Installation instructions_
 first**, then navigate to the project's root directory and run the `install.sh`
script as the root user:

    # cd kdm-manager-api
    # ./install.sh

The `install.sh` script will reload both nginx and `supervisord`, at which point
the API should be running on 127.0.0.1:8013 and nginx should be listening for
requests for https://api.kdm-manager.com

From there, run `server.sh` as root to manage deployment operations, e.g. start,
stop, restart, etc.

## System administration

If you do choose to deploy the API, you'll probably want to rotate the logs (in
the application's `logs/` folder).

The API comes with a simple _logrotate_ configuration file, and using it with
your crontab is probably the most convenient way:

    #30 2 * * * /usr/sbin/logrotate /home/toconnell/kdm-manager-api/deploy/logrotate.conf > /dev/null 2>&1
