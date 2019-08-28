'use strict'; 


var myApp = angular.module('adminPanel', []);

// avoid clashes with jinja2
myApp.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);

myApp.filter('trustedHTML', function($sce) {return $sce.trustAsHtml;});

myApp.controller('globalController', function($scope, $http, $interval) {


    $scope.scratch = {};

    $scope.now = new Date();
    $scope.getAge = function(birthday){ //only does days for now
        var birthday = new Date(birthday);
        var age = $scope.now - birthday;
        return Math.round(age / (1000 * 60 * 60 * 24));
    };

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
                console.timeEnd(jwt_req_url)
                return undefined;
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

    $scope.showHide = function(e_id) {
        var e = document.getElementById(e_id);
        var hide_class = "hidden";
        var visible_class = "visible";
        if (e === null) {console.error("showHide('" + e_id + "') -> No element with ID value '" + e_id + "' found on the page!"); return false}
        if (e.classList.contains(hide_class)) {
            e.classList.remove(hide_class);
            e.classList.add(visible_class);
        } else {
            e.classList.add(hide_class);
            e.classList.remove(visible_class)
        };
    };

    $scope.showSpinner = function(id) {
        $("#" + id).fadeIn(3000);
    };
    $scope.hideSpinner = function(id) {
        $("#" + id).fadeOut(3000);
    };

    $scope.seconds_since_last_refresh = 0;
    $scope.updateCounter = function() {
        $scope.seconds_since_last_refresh++; 
    };
    $interval($scope.updateCounter, 1000);

    $scope.getRecentSettlements = function() {
//        console.warn('[RECENT SETTLEMENTS] Getting recent settlements...');
        $http.get('game_asset/campaigns').then(
            function(result){$scope.campaign_assets = result.data;},
            function(result){console.error('Could not retrieve campaign asset definitions!');}
        );
        $http.get('game_asset/expansions').then(
            function(result){$scope.expansion_assets = result.data;},
            function(result){console.error('Could not retrieve expansion asset definitions!');}
        );

        $scope.retrievingSettlements = true;
        $scope.showSpinner('recentSettlementsSpinner'); 
        $http.get('admin/get/settlement_data').then(function(result){
            $scope.settlements = result.data;
            $scope.hideSpinner('recentSettlementsSpinner');
            $scope.retrievingSettlements = false;
//            console.warn('[RECENT SETTLEMENTS] Got recent settlements!');
        });
    };

    setInterval( function init() {
        
        $scope.showSpinner('spinner');
        $http.get('stat').then(function(result){$scope.settings = result.data;});
        $http.get('https://api.github.com/repos/theLaborInVain/kdm-manager-api').then(function(result){$scope.github = result.data;});

        if ($scope.retrievingSettlements != true){
            $scope.getRecentSettlements();
        };

        $scope.showSpinner('userSpinner');
        $scope.scratch.get_user_data_failure = false;
        $http.get('admin/get/user_data').then(
            function(result){$scope.users = result.data; $scope.hideSpinner('userSpinner')},
            function(result){
                console.error('Could not retrieve recent user data!');
                console.error(result);
                $scope.hideSpinner('userSpinner');
                $scope.scratch.get_user_data_failure = true;
                $scope.scratch.get_user_data_failure_msg = result.data;
                $scope.users = undefined;
            }
        );
        $http.get('admin/get/logs').then(function(result){$scope.logs = result.data;});

        $http.get('world').then(function(result){
            $scope.world = result.data;
            $scope.hideSpinner('spinner');
            $scope.refreshed = new Date();
            $scope.seconds_since_last_refresh = 0;
//            console.log("[MAIN] Refreshed main view!");
            });

        return init;
        }(),
    120000
    )




    $scope.copyToClipboard = function(text) {
        window.prompt("Copy User OID to clipboard:", text);
    };

    // initialize

//    window.setInterval($scope.initialize(), 5000);


});

myApp.controller('alertsController', function($scope, $http) {

    $scope.scratch = {
        initializing_panel: true,
    };

    $scope.getWebappAlerts = function() {
        $scope.scratch.initializing_panel = true;
        console.time('getWebappAlerts()');
        $http.get('/get/notifications').then(
            function(result){
                $scope.webappAlerts = result.data;
                console.timeEnd('getWebappAlerts()');
                $scope.scratch.initializing_panel = false;
            },
            function(result){console.error('Could not retrieve webapp alerts!');}
        );
    };

    // initialize
    $scope.newAlert = {
        expiration: 'next_release',
        type: 'kpi',
        title: null,
        body: null,
        created_by: $scope.user._id.$oid,
    }

    // methods

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
        $http.post("/admin/notifications/expire", a).then(function(result){
            a.expiration = 'NOW';
            console.warn(result);
            $scope.getWebappAlerts();
        });
    };


    // run the alerts panel init job at intervals
    setInterval( function init() {
        console.info('Initializing alerts panel...');

        if ($scope.user._id === undefined) {
            console.error("Admin user '" + $scope.user.login + "' _id is undefined!");
            console.warn($scope.user);
        };

        $scope.getWebappAlerts();

        return init;
        }(),
    120000
    )
})

myApp.controller('userAdminController', function($scope, $http) {

    $scope.scratch = {
    };

    $scope.closeWorkWithUser = function() {
        delete $scope.workWithUser;
    };

    $scope.getUser = function() {
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
        $scope.workWithUser = undefined;


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
                window.alert(userLogin + ' subscription level updated!');
                $scope.scratch.searchUserEmail = userLogin;
                $scope.getUser()
            }, function errorCallback(response) {
                console.error(response);
                window.alert(response.data);
                console.timeEnd(timerName);
        		$scope.scratch.showLoader = false;
            }
        );
        


    };

    $scope.init = function() {
        console.info('Initializing userAdminController...')
    };

    $scope.init();

})
