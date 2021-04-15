myApp.controller('adminPanelController', function($scope, $http, $interval) {

    // the "last refreshed" counter
    $scope.seconds_since_last_refresh = 0;
    $scope.updateCounter = function() {
        $scope.seconds_since_last_refresh++; 
    };
    $interval($scope.updateCounter, 1000);

    // ui/ux helpers
    $scope.copyToClipboard = function(text) {
        window.prompt("Copy User OID to clipboard:", text);
    };

    // DEPRECATED - replace this with flask 
	$scope.setUserJWT = function() {
		// sets $scope.user.jwt to a valid JWToken
		if ($scope.user.plaintext_password === undefined) {
			console.error('Admin user password is not set!')
		};

		var jwt_req_url = 'login';
		console.time(jwt_req_url);
        var jwt_promise = $http({
            method: 'POST',
            url: jwt_req_url,
            data: {
                'username': $scope.user.login,
                'password': $scope.user.plaintext_password,
            },
            headers: {
				'API-Key': $scope.api_key,
            },
        })

        jwt_promise.then(
            function successCallback(response) {
                $scope.user.jwt = response.data.access_token;
                console.log('JWT set for ' + $scope.user.login);
                console.timeEnd(jwt_req_url)
            }, function errorCallback(response) {
                console.error(response);
                console.timeEnd(jwt_req_url);
                $scope.ngShowHide('adminPasswordInputError');
                var err = response.status + " - " + response.data
                document.getElementById('adminPasswordInputErrorMsg').innerHTML = err;
            }
        );
	}

    $scope.getEventLog = function(settlement) {
		// make sure we've got a fresh token
		$scope.setUserJWT();

        settlement.event_log = [
            {event: 'Retrieving settlement Event Log as ' + $scope.user.login + '...'}
        ]

        var event_log_req_url = '/settlement/get_event_log/' + settlement._id.$oid;
		var event_log_promise = $http({
			method: 'POST',
			url: event_log_req_url,
			headers: {
				'API-Key': $scope.api_key,
				'Content-Type': undefined,
				'Authorization': $scope.user.jwt,
			},
		})
        event_log_promise.then(function(result){
            settlement.event_log = result.data;
        });

    };


    // DEPRECATE THIS
    // DEPRECATE THIS
    $scope.showHide = function(e_id) {
        console.warn('showHide() is deprecated! Use ngShowHide().');
        $scope.ngShowHide(e_id);
    };
    // DEPRECATE THIS
    // DEPRECATE THIS



    //
    //  Alerts
    //

    $scope.getWebappAlerts = function() {
        var funcName = 'getWebappAlerts()';
        $scope.scratch.initializing_panel = true;
        console.time(funcName);
        $http.get('/get/notifications').then(
            function(result){
                $scope.webappAlerts = result.data;
                console.timeEnd(funcName);
                $scope.scratch.initializing_panel = false;
            },
            function(result){console.error('Could not retrieve webapp alerts!');}
        );
    };

    // initialize the newAlert "worksheet"
    $scope.newAlert = {
        expiration: 'next_release',
        type: 'kpi',
        title: null,
        body: null,
        created_by: $scope.user._id.$oid,
    }

    $scope.createAlert = function() {
        console.warn($scope.newAlert);
        $http.post("/admin/notifications/new", $scope.newAlert).then(function(result){
            console.warn(result);
            $scope.getWebappAlerts();
            $scope.newAlert.title = null;
            $scope.newAlert.body = null;
            $scope.showHide('createNewAlert');
        });
    };

    $scope.expireAlert = function(a) {
        // expire an alert in the API; reload alerts from API
        $http.post("/admin/notifications/expire", a).then(function(result){
            a.expiration = 'NOW';
            $scope.getWebappAlerts();
        });
    };


    $scope.getRecentUsers = function() {
        $scope.users = undefined; 
        $http.get('admin/get/user_data').then(
            function(result){
                $scope.users = result.data;
            },
            function(result){
                console.error('Could not retrieve recent user data!');
                console.error(result);
                $scope.hideSpinner('userSpinner');
                $scope.scratch.get_user_data_failure = true;
                $scope.scratch.get_user_data_failure_msg = result.data;
                $scope.users = undefined;
            }
        );
    };


    //
    // general init
    //

    setInterval( function init() {
       
        $scope.getWebappAlerts();

        $scope.ngVisible.mainSpinner = true
        $http.get('stat').then(function(result){$scope.settings = result.data;});
        $http.get('https://api.github.com/repos/theLaborInVain/kdm-manager-api').then(function(result){$scope.github = result.data;});


        $scope.scratch.get_user_data_failure = false;

        $scope.getRecentUsers();

        $http.get('admin/get/logs').then(function(result){$scope.logs = result.data;});

        $http.get('world').then(function(result){
            $scope.world = result.data;
            $scope.ngVisible.mainSpinner = false;
            $scope.refreshed = new Date();
            $scope.seconds_since_last_refresh = 0;
//            console.log("[MAIN] Refreshed main view!");
            });

        return init;
        }(),
    120000
    )

});


//
// RELEASES!
//
myApp.controller('releasesController', function($scope, $rootScope, $http) {

    // this controller is used by elements that do not share scope in the
    // actual HTML/DOM, so use $rootScope for any elements shared between
    // the controllers!

    // init method
    $scope.init = function() {
        console.info('Initializing releasesController...');
        $rootScope.releasesObject = {
            showLoader: true,
        };
        $scope.setReleases();
    };

    //
    // methods for working on a release
    //
    $scope.getEditingRelease = function() {
        // a laziness method to get the release that we're editing on back
        // in the webapp
        return $rootScope.releasesObject.editingRelease;
    };

    $scope.toggleSection = function(sectionName) {
        // toggles a section in or out of the active post's sections
        var post = $scope.getEditingRelease();
        var sectionIndex = post.sections.indexOf(sectionName);
        if (sectionIndex === -1) {
            post.sections.push(sectionName)
        } else {
            post.sections.splice(sectionIndex,1)
        }
        $scope.updateRelease();
    };

    $scope.addItemToSection = function(sectionName) {
        // adds a new item to the release's 'items' list; an item is a dict
        // that we add arbitrary items to

        // first, if we're initializing, do that
        var post = $scope.getEditingRelease();
        if (post.items === null) {
            post.items = [];
        };

        // now, push the new item
        var currentItemCount = post.items.length;
        post.items.push(
            {
                'section': sectionName,
                'sort': currentItemCount +1,
                'body': '',
                'feature': false,
                'details': []
            }
        );

        // auto-increment the patch version
        post.version.patch++;

        // finally, change focus to the new item
        var newItemId = post._id.$oid + '_item_' + currentItemCount;
        sleep(400).then(() => {
            $scope.setFocus(newItemId);
        });
    };

    $scope.initializeFeatureDetail = function(item) {
        console.warn('initializing feature detail!');
        var post = $scope.getEditingRelease();

        // first time we open a feature, we need to create a detail for it
        // and fiddle the version numbers
        if (item.details.length === 0) {
            console.warn('Initializing feature item details!');
            $scope.addDetailToItem(item);

            // now, increment the minor version (since this is a feature now)
            // and decrement the patch, since this is no longer an enhancement
            post.version.minor++;
            post.version.patch--;
        };

    };

    $scope.addDetailToItem = function(item) {
        var post = $scope.getEditingRelease();

        // push the new detail
        var currentDetailCount = item.details.length;
        item.details.push(
            {
                'body': '',
            }
        );

        // auto-increment the patch version
        post.version.patch++;

        // finally, change focus to the new detail
        var newDetailId = 'item_' + item.sort + '_detail_' + currentDetailCount;
        sleep(400).then(() => {
            $scope.setFocus(newDetailId);
        });
    }

    $scope.updateAlink = function() {
        $scope.scratch.alink = '<a href="' + $scope.scratch.alink_URL + '">' + $scope.scratch.alink_text + '</a>'
    }

    $scope.createNewRelease = function(platformName, userLogin) {

        $rootScope.releasesObject.showLoader = true;

        var reqURL = '/admin/releases/new';
        var postData = {
            'platform': platformName,
            'login': userLogin,
        }

        console.time(reqURL);

        $http.post(reqURL, postData).then(
            function(result){
                console.timeEnd(reqURL);
                console.warn('Created new release for ' + platformName);
                $scope.setReleases();
                $rootScope.releasesObject.showLoader = false;
                $rootScope.releasesObject.editingRelease = result.data;
            },
            function(result){
                console.error('Failed to create new release! ' + reqURL);
                console.error(result);
            }
        );
    };

    $scope.updateRelease = function(action) {
        // updates a release via POST
        if (action === undefined) {
            action = 'update'
        };

        var reqURL = '/admin/releases/' + action;
        var releaseData = $scope.releasesObject.editingRelease

        $rootScope.releasesObject.showLoader = true;
        console.time(reqURL);

        $http.post(reqURL, releaseData).then(
            function(result){
                console.timeEnd(reqURL);
                console.warn(action + 'd release ' + releaseData._id.$oid);
                $rootScope.releasesObject.editingRelease = result.data;
                $rootScope.releasesObject.showLoader = false;
                $scope.setReleases();
            },
            function(result){
                console.error('Failed to update release!');
                console.error(result);
            }
        );
        
    }

});


myApp.controller('apiDocumentationEditorController', function($scope, $http) {

    $scope.init = function() {
        console.info('Initializing API documentation editor...');
        $scope.setUndocumentedMethods();
    };

    $scope.setUndocumentedMethods = function() {
        // sets $scope.apiUndocumentedMethods
        $scope.apiUndocumentedMethods = undefined

        var reqURL = '/docs/get_undocumented_methods';

        console.time(reqURL);

        $http.get(reqURL).then(
            function(result){
                console.timeEnd(reqURL);
                $scope.apiUndocumentedMethods = result.data;
            },
            function(result){
                console.error('Failed to retrieve undocumented methods from API!');
                console.error(result);
            }
        );
    };

    $scope.init();

});


myApp.controller('userAdminController', function($scope, $http) {

    $scope.scratch = {
    };

    $scope.closeWorkWithUser = function() {
        delete $scope.workWithUser;
        $scope.getRecentUsers();
    };

    $scope.getUser = function() {
        $scope.workWithUser = undefined; 
        var userLogin = $scope.scratch.searchUserEmail;

        // blank out the search and show the spinner
        $scope.scratch.searchUserEmail = undefined;
        $scope.scratch.showLoader = true;

        console.warn("Attempting to retrieve '" + userLogin + "' from API...")

        var timerName = 'getUser(' + userLogin + ')'
		console.time(timerName);

        var user_promise = $http({
            method: 'POST',
            url: '/admin/user_asset/get',
            data: {
            	'login': userLogin,
            },
            headers: {
                'API-Key': $scope.api_key,
            },
        })

		user_promise.then(
            function successCallback(response) {
                $scope.workWithUser = response.data
                console.timeEnd(timerName);
        		$scope.scratch.showLoader = false;
            }, function errorCallback(response) {
                console.error(response);
                console.timeEnd(timerName);
				$scope.workWithUser = {'user': {'login': null}};
        		$scope.scratch.showLoader = false;
            }
        );

    };

    $scope.setSubscriptionLevel = function(userObject, subscriptionObject) {
        var userLogin = userObject.user.login;
        var currentSubscriptionLevel = userObject.user.subscriber.level;
        var targetSubscriptionLevel = subscriptionObject.level;
        var targetSubscriptionDesc = subscriptionObject.desc;

        // sanity check; die if we fail
        if (currentSubscriptionLevel === targetSubscriptionLevel) {
            console.error(userLogin + ' subscription level is already ' + targetSubscriptionLevel);
            return false;
        };
    
        // get ready to do it
        console.warn('Setting ' + userLogin + ' subscriber level to ' +
            targetSubscriptionLevel + ' (' + targetSubscriptionDesc + ').'
        );

        $scope.scratch.showLoader = true;

        var timerName = 'setSubscriptionLevel(' + userLogin + ')'
        console.time(timerName);

        var subscriber_promise = $http({
            method: 'POST',
            url: '/admin/user_asset/set_subscriber_level',
            data: {
                'login': userLogin,
                'level': targetSubscriptionLevel,
            },
            headers: {
                'API-Key': $scope.api_key,
            },
        })

		subscriber_promise.then(
            function successCallback(response) {
                console.timeEnd(timerName);
                userObject.user.subscriber.level = targetSubscriptionLevel;
        		$scope.scratch.showLoader = false;
            }, function errorCallback(response) {
                console.error(response);
                console.timeEnd(timerName);
        		$scope.scratch.showLoader = false;
            }
        );


    };

    $scope.toggleVerifiedEmail = function(userObject) {
        // turns the user's 'verified_email' attrib on or off

        var startingValue = userObject.verified_email;
        var newValue = true;

        if (startingValue) {
            newValue = false;
        }

        var reqURL = '/user/set_verified_email/' + userObject._id.$oid
        console.time(reqURL);

        var promise = $http({
            method: 'POST',
            url: reqURL,
            data: {'value': newValue},
            headers: {
                'API-Key': $scope.api_key,
				'Authorization': $scope.user.jwt,
            },
        });

		promise.then(
            function successCallback(response) {
                console.timeEnd(reqURL);
                userObject.verified_email = newValue;
            }, function errorCallback(response) {
                console.error(response);
                console.timeEnd(reqURL);
            }
        );


    };

    $scope.exportUser = function(userLogin) {
        // hits the /admin/user_asset/export end point and posts a login
        // to it; gets the pickle back

        var form = document.createElement("form");
        form.method = "POST";
        form.action = "/admin/user_asset/export";
        var a_input = document.createElement("input");
        a_input.name = 'login';
        a_input.value =  userLogin;
        form.appendChild(a_input);
        document.body.appendChild(form);
        form.submit();

    };


})
