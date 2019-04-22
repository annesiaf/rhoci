# Copyright 2019 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from __future__ import absolute_import

from rhoci.common.config import Config
from rhoci.database import Database
from rhoci.db.enconders import MongoJSONEncoder, ObjectIdConverter

from flask import Flask


def create_app():
    # Create application
    app = Flask(__name__)
    app.json_encoder = MongoJSONEncoder
    app.url_map.converters['objectid'] = ObjectIdConverter
    app.config['custom'] = Config().config

    Database.initialize()

    register_blueprints(app)

    return app


def register_blueprints(app):

    from rhoci.main import bp as main_bp
    app.register_blueprint(main_bp)

    from rhoci.DFG import bp as DFG_bp
    app.register_blueprint(DFG_bp, url_prefix='/DFG')

    from rhoci.jobs import bp as jobs_bp
    app.register_blueprint(jobs_bp, url_prefix='/jobs')

    from rhoci.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
