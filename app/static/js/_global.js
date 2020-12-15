"use strict";

//  public/vanilla JS functions and non-angular stuff
function sleep (time) {return new Promise((resolve) => setTimeout(resolve, time));}

//  the app starts here!
var myApp = angular.module('apiUtils', ['ngAnimate']);

// avoid clashes with jinja2
myApp.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{a');
    $interpolateProvider.endSymbol('a}');
}]);

myApp.filter('trustedHTML', function($sce) {return $sce.trustAsHtml;});

myApp.controller('globalController', function($scope, $http, $interval, $q, $timeout) {


    // inject some date calc methods into the root scope
    $scope.now = new Date();
    $scope.getAge = function(birthday){ //only does days for now
        var birthday = new Date(birthday);
        var age = $scope.now - birthday;
        return Math.round(age / (1000 * 60 * 60 * 24));
    };


	//
    // re-usable UI/UX methods
	//
    $scope.loadURL = function(destination) {
        // allows us to use ng-click to re-direct to URLs
        window.location = destination;
    };

    $scope.exportThis = function(ngEvent) {
        // use's $event from ng-click to get the current element's innerHTML
        // and set that as the value of 'target' (which should be a variable
        // or something similar).

        if (ngEvent === undefined) {
            console.error('exportThis(): required $event as first arg');
        }
        return ngEvent.target.innerHTML;
    }


    $scope.getElement = function(elementId) {
        try {
            var element = document.getElementById(elementId);
        } catch(err) {
            console.error(err);
            throw 'Could not find element: ' + elementId;
        };
        if (element === undefined || element === null) {
            var err = "No element with ID value";
            throw err;
        } else {
            return element
        };
        throw 'ngShowHide encountered an error!';
    }

    //
    //  ngShow/ngHide/ngShowHide ; this is real similar to kdmManager.js
    //

	$scope.ngVisible = {};
    $scope.ngHiddenClass = "hidden";
    $scope.ngVisibleclass = "visible";

    $scope.ngShow = function(elementId) {
        $scope.ngVisible[elementId] = true;
        $timeout (
            function() {
                var element = $scope.getElement(elementId);
                element.classList.remove($scope.ngHiddenClass);
                element.classList.add($scope.ngVisibleClass);
            }
        );
    };

    $scope.ngHide = function(elementId) {
        $scope.ngVisible[elementId] = false;
        $timeout (
            function() {
                var element = $scope.getElement(elementId);
                element.classList.remove($scope.ngVisibleClass);
                element.classList.add($scope.ngHiddenClass);
            }
        );
    };

    $scope.ngShowHide = function(elementId) {
        // a toggle wrapper for ngShow and ngHide that uses ngVisible to
        // determine which function to run
        if (!$scope.ngVisible[elementId]) {
            $scope.ngShow(elementId);
        } else {
            $scope.ngHide(elementId);
        };
    };

    $scope.setFocus = function(elementId) {
        var element = document.getElementById(elementId);
        if (element === null) {
            console.error("Element '" + elementId + "' is null!");
        };
        element.focus();
    };


    //
    //  API methods used by all apps
    //

    $scope.initializeReleasesData = function() {

        $scope.apiData.releases = {}
        $scope.apiData.releases.all = null;
        $scope.apiData.releases.current = null;
        $scope.apiData.releases.upcoming = null;
        $scope.apiData.releases.platforms = null;

    }


    $scope.setReleases = function() {
        // sets the releases element, which is ALL releases

        $scope.initializeReleasesData();

        var endpoints = ['platforms', 'all', 'current', 'upcoming'];
        var promises = [];

        for (var i = 0; i < endpoints.length; i++) {
            var endpoint = endpoints[i];
            var reqURL = '/releases/' + endpoint;
            console.time(reqURL);
            var promise = $http.get(reqURL);
            promises.push(promise);
        };

        $q.all(promises).then(
            function(result){
                for (var i = 0; i < result.length; i++){
                    var r = result[i];
                    var endpoint = r.config.url.split('/').pop()
                    $scope.apiData.releases[endpoint] = r.data;
                    console.timeEnd(r.config.url);
                };
            }
        ).catch(
            function(result){
                $scope.apiData.releases = undefined;
				console.error(result.data);
				console.error(result);
			}
		);
	};


    // misc. API methods
    $scope.setStatApi = function() {
        // sets the apiData.stat dictionary, which is just /stat output
        var req_url = '/stat';
        console.time(req_url);
        $http({
            method: 'GET',
            url: req_url,
            headers: {
                'API-Key': $scope.api_key
            }
        }).then(
            function successCallback(response) {
                $scope.apiData.stat = response.data.meta;
                console.timeEnd(req_url)
            }, function errorCallback(response) {
                console.error(response);
                console.timeEnd(req_url);
            }
        )
    };
        

    $scope.init = function() {
        console.info('Initializing global apiUtils controller...');

        // initialize some hashes in the global $scope
        $scope.apiData = {
            releases: null,
        };
        $scope.scratch = {};

        // do some fancier stuff
        $scope.setStatApi();

    }
    $scope.init();

});
