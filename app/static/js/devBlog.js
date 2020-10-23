"use strict";

myApp.controller('devBlogController', function($scope, $http) {

    $scope.init = function() {
        console.info("Initializing devBlogController...");
    };

    $scope.init();

    $scope.buttonRepeaterFilter = function(release) {
        // use this with an ng-repeat filter pass to filter on scratch
        //  values
        if ($scope.scratch.platformFilter === undefined) {
            return release
        } else if ($scope.scratch.platformFilter === release.platform) {
            return release
        }
    }

    $scope.setReleaseObject = function(release_oid) {
        // iterates $scope.apiData.releases.all and tries to use one of the
        //  releases to set $scope.releaseObject
        for (var i = 0; i < $scope.apiData.releases.all.length ; i++) {
            var release = $scope.apiData.releases.all[i];
            if (release._id.$oid === release_oid) {
                console.warn(release);
                $scope.releaseObject = release;
                return true;
            }
        };
    };

});
