'use strict';

myApp.controller('apiDocumentationController', function($scope, $http) {

    $scope.init = function() {

        console.info('Initializing apiDocumentationController...');

        $http.get('/docs/get').then(
            function(result){
                $scope.docs = result.data;
            }
        );
        $http.get('/docs/sections').then(
            function(result){
                $scope.section_lookup = result.data;
            }
        );
    };

    $scope.init();


    $scope.objectKeys = Object.keys;

    $scope.toggleAboutBlock = function(){
        var e = document.getElementById('aboutBlock');
        e.classList.toggle('closed');
    };

    $scope.toggleNav = function(){
        document.getElementById("christianSideNav").classList.toggle('nav_open');
        document.getElementById("container").classList.toggle('nav_open');
    };

    $scope.scrollTo = function(target_element){
        var target = document.getElementById(target_element);
        target.scrollIntoView({behavior: 'smooth', block: 'nearest', inline: 'start'});
    };

});
