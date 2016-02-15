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
# Testing: 04a_test_context_file_not_found.sh
# ###########################################
'
# Test jinjalive failure if missing context file.
#
# Generate output file given a context file and a template file
# Here, the context file is not existing.
#  
#  Run : ./04a_test_context_file_not_found.sh
#
########################################################

# Check and source virtualenvwrapper.sh file
source `which virtualenvwrapper.sh` || { echo 'ERROR: virtualenvwrapper.sh not found. Exiting.'; exit 1; }

# Work on virtual environment
set +e
workon jinjalive

# Launch test
jinjalive -cf sample_context_unexisting.yaml -tf sample_template_success.tpl -of sample_output.out
RETVAL=$?
[ $RETVAL -eq 0 ] && echo Failure: Test 'missing context file' should raise an Exception, but no exception raised
[ $RETVAL -ne 0 ] && echo Success: Test 'missing context file' raised an Exception and error code is not 0
set -e
