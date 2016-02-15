#!/bin/bash -e
#
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

echo '
# ###########################################
# Testing: 05b_test_template_file_parameter_missing.sh
# ###########################################
'
# Test jinjalive failure if missing template file parameter.
#
# Generate output file given a context file and a template file
# Here, the template file parameter is not given.
#  
#  Run : ./05b_test_template_file_parameter_missing.sh
#
########################################################

# Check and source virtualenvwrapper.sh file
source `which virtualenvwrapper.sh` || { echo 'ERROR: virtualenvwrapper.sh not found. Exiting.'; exit 1; }

# Work on virtual environment
set +e
workon jinjalive

# Launch test
jinjalive -cf sample_context.yaml -of sample_output.out
RETVAL=$?
[ $RETVAL -eq 0 ] && echo Failure: Test 'missing template file parameter' should raise an Exception, but no exception raised
[ $RETVAL -ne 0 ] && echo Success: Test 'missing template file parameter' error code is not 0
set -e
