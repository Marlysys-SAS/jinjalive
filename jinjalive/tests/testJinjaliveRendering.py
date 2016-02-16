# -*- coding: utf-8 -*-
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

from jinjalive.jinja.render import jinja_render
import os
import unittest
import uuid


TESTDATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class TestJinjaliveRendering(unittest.TestCase):
    '''
    This testcase is used to test the Jinja rendering in various conditions.
    '''

    def test_010_simple_variable(self):
        '''
        Test Jinja rendering success for a simple variable
        '''
        random_uuid = str(uuid.uuid4())
        context = {'uuid': random_uuid}
        template = "UUID={{ uuid }}"
        output = jinja_render(context, template)
        self.assertIn(random_uuid, output)

    def test_020_list_variable_join(self):
        '''
        Test Jinja rendering success for a list variable (join)
        '''
        random_uuids = [str(uuid.uuid4()) for _ in range(10)]
        context = {'uuids': random_uuids}
        template = "UUIDS={{ uuids|join(' ') }}"
        output = jinja_render(context, template)
        for random_uuid in random_uuids:
            self.assertIn(random_uuid, output)

    def test_030_list_variable_for(self):
        '''
        Test Jinja rendering success for a list variable (for loop)
        '''
        random_uuids = [str(uuid.uuid4()) for _ in range(10)]
        context = {'uuids': random_uuids}
        template = "{% for uuid in uuids %}{{ uuid }}{% endfor %}"
        output = jinja_render(context, template)
        for random_uuid in random_uuids:
            self.assertIn(random_uuid, output)

    def test_040_nested_variable(self):
        '''
        Test Jinja rendering success for a nested variable
        '''
        random_uuids = [str(uuid.uuid4()) for _ in range(10)]
        context = {'host': {'uuids': random_uuids}}
        template = "{% for uuid in host.uuids %}{{ uuid }}{% endfor %}"
        output = jinja_render(context, template)
        for random_uuid in random_uuids:
            self.assertIn(random_uuid, output)
