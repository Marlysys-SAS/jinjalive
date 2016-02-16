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

from datetime import datetime
from jinjalive._options import cli_opts
from jinjalive.jinja.render import jinja_render
import os
import sys

from oslo_config import cfg
from oslo_log import log
import yaml


CONF = cfg.CONF
CONF.register_cli_opts(cli_opts)

# Register log options
LOG = log.getLogger(__name__)
log.register_options(CONF)


class JinjaLive(object):

    '''
    JinjaLive implementation.
    '''

    def process(self, context_filename, template_filename, output_filename):
        '''
        The function executed by the main method.

        :param context_filename: Path of the context file, containing your variables.
        :type context_filename: str
        :param template_filename: Path of the Jinja template to be rendered.
        :type template_filename: str
        :param output_filename: Path of the rendered output file.
        :type output_filename: str

        :raises IOError: raised if given context or template file is not found.
        :raises UndefinedError: raised if a variable is used in the template file but is not defined in the context file.
        '''
        # Start time (for duration display)
        start_time = datetime.now()

        # Check if context file exists
        if not os.path.exists(context_filename):
            raise IOError("Context file '%s' not found. Please check parameters." % os.path.abspath(context_filename))

        # Check if template file exists
        if not os.path.exists(template_filename):
            raise IOError("Template file '%s' not found. Please check parameters." % os.path.abspath(template_filename))

        # Display summary
        LOG.info("YAML context file:     %s" % os.path.abspath(context_filename))
        LOG.info("Jinja template file:   %s" % os.path.abspath(template_filename))

        # Loading context dictionary from YAML file
        with open(context_filename, 'r') as yaml_file:
            context = yaml.load(yaml_file.read())

        # Read the template as a string
        with open(template_filename, 'r') as template:
            template = template.read()

        # Render output
        rendered_output = jinja_render(context, template)
        LOG.info("%s OUTPUT %s" % ("-" * 36, "-" * 36))
        for line in rendered_output.splitlines():
            LOG.info(line)

        # Write rendered string in output file
        with open(output_filename, 'wb') as output_file:
            output_file.write(rendered_output)

        LOG.info("-" * 80)
        LOG.info("Generation duration:   %s" % (datetime.now() - start_time))
        LOG.info("Generated output file: %s" % os.path.abspath(output_filename))


def main():
    '''
    The entry point either called by the code at the bottom of the file or by the generated command line tool 'jinja_renderer'.

    Initializes the oslo config from command line parameters and call the main JinjaRenderer class.

    Exists with error code if an error occurs.
    '''
    # Parse command line argument as part of CONF.
    try:
        CONF(sys.argv[1:])
    except cfg.RequiredOptError as e:
        LOG.error(str(e))
        CONF.print_help()
        sys.exit(2)

    CONF.log_level = log.INFO

    # Setup log from configuration
    log.setup(CONF, 'jinjalive')

    try:
        JinjaLive().process(CONF.context_filename, CONF.template_filename, CONF.output_filename)
    except Exception as e:
        LOG.error(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
