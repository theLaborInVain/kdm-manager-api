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
**Neither the [https://kdm-manager.com](https://kdm-manager.com) service nor any of the software utilized by that ser
vice (including the API deployed at [https://thewatcher.io](https://thewatcher.io) are developed, authorized, support
ed by or affiliated with Kingdom Death or Adam Poots Games, LLC.**

For more information, please refer to [the 'About' section of the project's development blog](http://kdm-manager.blog
spot.com/p/credits-and-acknowledgements.html).


## Licensing and permission
The MIT license (LICENSE.md) covers application and API code in this repository, but it does not and cannot cover the
 game assets (in the `/v2/api.thewatcher.io/api/assets` folder), which are the sole property of Kingdom Death.



# Installation instructions

Install host dependencies:

    # apt-get -y update
    # apt-get -y install python3 python3-venv python3-dev supervisor nginx git

Clone the repo.

Install app dependencies:

    $ cd kdm-manager-api
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ deactivate


## Run

Run the dev server from the root of the project directory:

    $ cd kdm-manager-api
    $ ./server.sh dev

Assuming everything went according to plan with pip, this should start listening
on 0.0.0.0:8021 and responding to requests.


## Deploy

In order to deploy, **perform the steps above under `Install` first**, then
navigate to the project's root directory and run the `install.sh` script as
the root user:

    # cd kdm-manager-api
    # ./install.sh

The `install.sh` script will reload both nginx and `supervisord`, at which point
the API should be running on 127.0.0.0:8020 and nginx should be listening for
requests for https://downtime.kdm-manager.com, https://kdm-manager.com, etc.


