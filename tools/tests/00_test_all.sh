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

# Init environment
./01_init_env.sh

#######################################################
# Testing: Rendering success
# This section will perform the following functions:
# - Generate output file from well-formed and existing context and template files.
########################################################
./02_test_success.sh

#######################################################
# Testing: Failures missing variables
# This section will perform the following functions:
# - Try to generate output from an incomplete context file (plain variables).
# - Try to generate output from an incomplete context file (loop variables).
########################################################
./03a_test_missing_variables.sh
./03b_test_missing_variables.sh

#######################################################
# Testing: Failures file not found
# This section will perform the following functions:
# - Try to generate output with an unexisting context file path.
# - Try to generate output with an unexisting template file path.
########################################################
./04a_test_context_file_not_found.sh
./04b_test_template_file_not_found.sh

#######################################################
# Testing: Failures missing parameters
# This section will perform the following functions:
# - Try to generate output with command line context file parameter missing.
# - Try to generate output with command line template file parameter missing.
# - Try to generate output with command line output file parameter missing.
########################################################
./05a_test_context_file_parameter_missing.sh
./05b_test_template_file_parameter_missing.sh
./05c_test_output_file_parameter_missing.sh