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

from flask import render_template
import logging

LOG = logging.getLogger(__name__)

from rhoci.jobs import bp  # noqa


@bp.route('/index')
@bp.route('/')
def index():
    """All jobs."""
    return render_template('jobs/index.html')


@bp.route('/builds')
def builds():
    """All builds."""
    return render_template('builds/index.html')


@bp.route('/tests')
def tests():
    """All tests."""
    return render_template('tests/index.html')


@bp.route('/<name>')
def job(name):
    """Specific job summary."""
    print(name)
    return render_template('job/summary.html')
