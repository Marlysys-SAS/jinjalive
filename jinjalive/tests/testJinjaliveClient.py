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

from jinjalive.console.cli import main
import os
import sys
import unittest


TESTDATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class TestJinjaliveClient(unittest.TestCase):
    '''
    This testcase is used to test the 'jinjalive' command line client in various conditions.
    '''

    def test_010_success_client(self):
        '''
        Test client success if correct context and template files
        '''
        sys.argv = ['jinjalive', '--noverbose', '-cf', '%s/sample_context.yaml' % TESTDATA_DIR, '-tf', '%s/sample_template_success.tpl' % TESTDATA_DIR, '-of', '/tmp/jinjalive.out']
        main()

    def test_020_missing_context_parameter(self):
        '''
        Test client failure if context parameter is missing
        '''
        sys.argv = ['jinjalive', '-tf', '%s/sample_template_success.tpl' % TESTDATA_DIR, '-of', '/tmp/jinjalive.out']
        with self.assertRaises(SystemExit):
            main()

    def test_030_missing_template_parameter(self):
        '''
        Test client failure if template parameter is missing
        '''
        sys.argv = ['jinjalive', '-cf', '%s/sample_context.yaml' % TESTDATA_DIR, '-of', '/tmp/jinjalive.out']
        with self.assertRaises(SystemExit):
            main()

    def test_040_missing_output_parameter(self):
        '''
        Test client failure if output parameter is missing
        '''
        sys.argv = ['jinjalive', '-cf', '%s/sample_context.yaml' % TESTDATA_DIR, '-tf', '%s/sample_template_success.tpl' % TESTDATA_DIR]
        with self.assertRaises(SystemExit):
            main()

    def test_050_context_file_not_found(self):
        '''
        Test client failure when context file is not found
        '''
        sys.argv = ['jinjalive', '-cf', '%s/sample_context_not_found.yaml' % TESTDATA_DIR, '-tf', '%s/sample_template_success.tpl' % TESTDATA_DIR, '-of', '/tmp/jinjalive.out']
        with self.assertRaises(SystemExit):
            main()

    def test_060_template_file_not_found(self):
        '''
        Test client failure when template file is not found
        '''
        sys.argv = ['jinjalive', '-cf', '%s/sample_context.yaml' % TESTDATA_DIR, '-tf', '%s/sample_template_not_found.tpl' % TESTDATA_DIR, '-of', '/tmp/jinjalive.out']
        with self.assertRaises(SystemExit):
            main()
