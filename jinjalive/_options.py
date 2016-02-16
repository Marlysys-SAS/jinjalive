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

from oslo_config import cfg

cli_opts = [
    cfg.StrOpt('context_filename',
               short='cf',
               required=True,
               help='The YAML context filename (containing your variables).'),
    cfg.StrOpt('template_filename',
               short='tf',
               required=True,
               help='The Jinja template file to render.'),
    cfg.StrOpt('output_filename',
               short='of',
               required=True,
               help='The rendered output file path.'),
]
