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

# Check and source virtualenvwrapper.sh file
source `which virtualenvwrapper.sh` || { echo 'ERROR: virtualenvwrapper.sh not found. Exiting.'; exit 1; }

# Recreate clean virtual environment
rmvirtualenv jinjalive
set +e
mkvirtualenv --clear jinjalive
set -e
pip install -U pip setuptools
pip install -r ../../requirements.txt
pip install -r ../../test-requirements.txt


# Launch setup.py to generate console scripts.
cd ../..
python setup.py develop
cd -