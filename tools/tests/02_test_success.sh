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
# Testing: 02_test_success.sh
# ###########################################
'
# Test jinjalive success
#
# Generate output file given a context file and a template file
# No missing variables
#  
#  Run : ./02_test_success.sh
#
########################################################

# Check and source virtualenvwrapper.sh file
source `which virtualenvwrapper.sh` || { echo 'ERROR: virtualenvwrapper.sh not found. Exiting.'; exit 1; }

# Work on virtual environment
set +e
workon jinjalive
set -e

# Launch test
rm -Rf outputfile.out
jinjalive -cf sample_context.yaml -tf sample_template_success.tpl -of sample_output.out
RETVAL=$?
set +e
[ $RETVAL -eq 0 ] && echo Success: Test 'success' succeeded
[ $RETVAL -ne 0 ] && echo Failure: Test 'success' failed
set -e