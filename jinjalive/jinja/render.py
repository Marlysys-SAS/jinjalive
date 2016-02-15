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

from __future__ import unicode_literals

from jinja2.environment import Environment
from jinja2.runtime import StrictUndefined


def jinja_render(context, template):
    """
    Render a given template with the given context, using Jinja2.
    """
    jinja_environment = Environment(undefined=StrictUndefined,
                                    lstrip_blocks=True,
                                    trim_blocks=True,
                                    extensions=['jinja2.ext.loopcontrols',
                                                'jinja2.ext.with_',
                                                'jinja2.ext.autoescape'])
    jinja_template = jinja_environment.from_string(template)
    return jinja_template.render(context)
