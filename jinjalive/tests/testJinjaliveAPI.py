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

from jinjalive.console.cli import JinjaLive
import os
import unittest

from jinja2.exceptions import UndefinedError


TESTDATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class TestJinjaliveAPi(unittest.TestCase):
    '''
    This testcase is used to test the JinjaLive API in various conditions.
    '''

    def test_010_success(self):
        '''
        Test API success if correct context and template files
        '''
        JinjaLive().process('%s/sample_context.yaml' % TESTDATA_DIR, '%s/sample_template_success.tpl' % TESTDATA_DIR, '/tmp/jinjalive.out')

    def test_020_missing_variable(self):
        '''
        Test API if UndefinedError is raised when correct context but missing variable used in template file
        '''
        with self.assertRaises(UndefinedError):
            JinjaLive().process('%s/sample_context.yaml' % TESTDATA_DIR, '%s/sample_template_missing_variables_1.tpl' % TESTDATA_DIR, '/tmp/jinjalive.out')

    def test_030_missing_variable(self):
        '''
        Test API if UndefinedError is raised when correct context but missing variable used in template file
        '''
        with self.assertRaises(UndefinedError):
            JinjaLive().process('%s/sample_context.yaml' % TESTDATA_DIR, '%s/sample_template_missing_variables_2.tpl' % TESTDATA_DIR, '/tmp/jinjalive.out')

    def test_040_context_file_not_found(self):
        '''
        Test API if UndefinedError is raised when context file is not found
        '''
        with self.assertRaises(IOError):
            JinjaLive().process('%s/sample_context_not_found.yaml' % TESTDATA_DIR, '%s/sample_template_success.tpl' % TESTDATA_DIR, '/tmp/jinjalive.out')

    def test_050_template_file_not_found(self):
        '''
        Test API if UndefinedError is raised when template file is not found
        '''
        with self.assertRaises(IOError):
            JinjaLive().process('%s/sample_context.yaml' % TESTDATA_DIR, '%s/sample_template_not_found.tpl' % TESTDATA_DIR, '/tmp/jinjalive.out')
