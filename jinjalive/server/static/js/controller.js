/*
# Copyright 201​6​ ​Marlysys
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
*/
'use strict';

app.controller("JinjaLiveCtrl", function($scope, $http, FileSaver, Blob,
		localStorageService, $uibModal, $hotkey) {

	// Sample template and context
	$scope.template = default_template;
	$scope.context = default_context;

	// CodeMirror options
	$scope.templateEditorOptions = {
		lineNumbers : true,
		lineWrapping : false,
		autofocus : true,
		mode : "jinja2"
	};
	$scope.contextEditorOptions = {
		lineNumbers : true,
		lineWrapping : false,
		mode : "yaml",
	};

	// Watch changes
	$scope.$watch("template + context + showwhitespaces", function() {
		$scope.render();
	})
		
	// Render template with context through POST on server
	$scope.render = function() {
		var data = {
			template : $scope.template,
			context : $scope.context,
			showwhitespaces : $scope.showwhitespaces,
		};
		$http.post(SCRIPT_ROOT + '/render', data).then(function successCallback(response) {
			$scope.output = response.data;
			$('.alert-danger').hide();
			$('.alert-success').show();
		}, function errorCallback(response) {
			$scope.error = response.data;
			$('.alert-success').hide();
			$('.alert-danger').show();
		});
	};

	// Download template
	$scope.downloadTemplate = function() {
		var data = new Blob([ $scope.template ], {
			type : 'text/plain;charset=utf-8'
		});
		FileSaver.saveAs(data, 'jinjalive.template.txt');
	};

	// Storage
	$scope.saveDefault = function() {
		localStorageService.set('Sample Jinja', {
			template : $scope.template,
			context : $scope.context
		});
	};
	$scope.saveDefault();
	$scope.entries = localStorageService.keys();
	$scope.load = function(entry_name) {
		var entry = localStorageService.get(entry_name);
		$scope.template = entry.template;
		$scope.context = entry.context;
	};
	$scope.clear = function(entry) {
		localStorageService.remove(entry);
		$scope.entries = localStorageService.keys();
	};

	// Save modal
	$scope.save = function() {
		var modalInstance = $uibModal.open({
			templateUrl : 'saveEntry.html',
			controller : 'saveEntryCtrl',
			resolve : {
				entries : function() {
					return $scope.entries;
				}
			}
		});
		modalInstance.result.then(function(entry_name) {
			localStorageService.set(entry_name, {
				template : $scope.template,
				context : $scope.context
			});
			$scope.entries = localStorageService.keys();
		});
	};
	
	// Catch Ctrl-S to save
	$hotkey.bind('Ctrl + S', function() {
		$scope.save();
	});
	
});

app.controller('saveEntryCtrl', function($scope, $uibModalInstance, entries) {

	$scope.entries = angular.copy(entries);
	$scope.entries.splice($scope.entries.indexOf("Sample Jinja"), 1);

	$scope.ok = function(entry) {
		if (typeof entry !== 'undefined')
			$scope.entry_name = entry;
		$uibModalInstance.close($scope.entry_name);
	};

	$scope.cancel = function() {
		$uibModalInstance.dismiss('cancel');
	};
});
