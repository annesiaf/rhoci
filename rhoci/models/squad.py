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

from rhoci.database import Database


class Squad(object):

    def __init__(self, name, DFG, components):
        self.name = name
        self.DFG = DFG
        self.components = components

    def save_to_db(self):
        if not Database.find_one("squads", {"name": self.name}):
            Database.insert(collection='squads',
                            data=self.json())

    def json(self):
        return {
            'name': self.name,
            'components': self.components,
        }
