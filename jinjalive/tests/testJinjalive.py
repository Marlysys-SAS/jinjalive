# -*- coding: utf-8 -*-
#
# Copyright 201​6​ ​Marlysys
#
# Licensed under the Apache License, Version 2.0 (the 'License'); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from jinjalive.console.cli import JinjaLive
from jinjalive.console.cli import main
import os
import sys
import unittest

from jinja2.exceptions import UndefinedError


TESTDATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class TestJinjalive(unittest.TestCase):

    def test_010_success(self):
        '''
        Test success with correct context and template files.
        '''
        JinjaLive().process('%s/sample_context.yaml' % TESTDATA_DIR, '%s/sample_template_success.tpl' % TESTDATA_DIR, '/tmp/toto')

    def test_020_missing_variable(self):
        '''
        Test failure with correct context but missing variable in template file.
        '''
        with self.assertRaises(UndefinedError):
            JinjaLive().process('%s/sample_context.yaml' % TESTDATA_DIR, '%s/sample_template_missing_variables_1.tpl' % TESTDATA_DIR, '/tmp/toto')

    def test_030_missing_variable(self):
        '''
        Test failure with correct context but missing variable in template file.
        '''
        with self.assertRaises(UndefinedError):
            JinjaLive().process('%s/sample_context.yaml' % TESTDATA_DIR, '%s/sample_template_missing_variables_2.tpl' % TESTDATA_DIR, '/tmp/toto')

    def test_040_context_file_not_found(self):
        '''
        Test failure with context file not found.
        '''
        with self.assertRaises(IOError):
            JinjaLive().process('%s/sample_context_not_found.yaml' % TESTDATA_DIR, '%s/sample_template_success.tpl' % TESTDATA_DIR, '/tmp/toto')

    def test_050_template_file_not_found(self):
        '''
        Test failure with template file not found.
        '''
        with self.assertRaises(IOError):
            JinjaLive().process('%s/sample_context.yaml' % TESTDATA_DIR, '%s/sample_template_not_found.tpl' % TESTDATA_DIR, '/tmp/toto')

    def test_060_missing_context_parameter(self):
        '''
        Test failure with context parameter missing.
        '''
        sys.argv = ['jinjalive', '-tf', '%s/sample_template_success.tpl' % TESTDATA_DIR, '-of', '/tmp/toto']
        with self.assertRaises(SystemExit):
            main()

    def test_070_missing_template_parameter(self):
        '''
        Test failure with template parameter missing.
        '''
        sys.argv = ['jinjalive', '-cf', '%s/sample_context.yaml' % TESTDATA_DIR, '-of', '/tmp/toto']
        with self.assertRaises(SystemExit):
            main()

    def test_080_missing_output_parameter(self):
        '''
        Test failure with output parameter missing.
        '''
        sys.argv = ['jinjalive', '-cf', '%s/sample_context.yaml' % TESTDATA_DIR, '-tf', '%s/sample_template_success.tpl' % TESTDATA_DIR]
        with self.assertRaises(SystemExit):
            main()

    def test_090_success_client(self):
        '''
        Test success client with all parameters.
        '''
        sys.argv = ['jinjalive', '--noverbose', '-cf', '%s/sample_context.yaml' % TESTDATA_DIR, '-tf', '%s/sample_template_success.tpl' % TESTDATA_DIR, '-of', '/tmp/toto']
        main()
