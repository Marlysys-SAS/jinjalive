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

from jinjalive.jinja.render import jinja_render
import json
import traceback

from flask import Flask, render_template, request
from flask_bower import Bower
from flask_cache import Cache
import yaml


# Flask application
app = Flask(__name__)

# Flask-Bower extension
app.config['BOWER_COMPONENTS_ROOT'] = 'static/bower'
Bower(app)

# Flask-Cache extension
cache = Cache(app, config={'CACHE_TYPE': 'null'})


@app.route("/", methods=['GET'])
@cache.cached(timeout=3600)
def index():
    """
    JinjaLive web application home page.
    """
    return render_template('index.html')


@app.route('/render', methods=['POST'])
@cache.cached(timeout=3600)
def render():
    """

    """
    try:
        # Get POST data
        params = request.get_json()
        template = params['template'].replace("\t", " " * 4)
        raw_context = params['context']
        showwhitespaces = params.get('showwhitespaces', False)

        # Load context, first try with JSON, if it fails, try YAML
        try:
            context = json.loads(raw_context)
        except:
            context = yaml.safe_load(raw_context)

        # Render the template with variables
        output = jinja_render(context, template)

        # HTML-ize the output
        if showwhitespaces:
            output = output.replace(' ', '•')

        # Return rendered template, with a 200 status code
        return output, 200
    except Exception, e:
        traceback.print_exc()
        # Return error message, with a 500 status code
        return str(e), 500


def main():
    app.debug = True
    app.run(host='0.0.0.0', port=8888)

if __name__ == "__main__":
    main()
