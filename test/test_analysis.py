# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2015 SciFabric LTD.
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa. If not, see <http://www.gnu.org/licenses/>.
"""
App package for testing PyBossa application.

This exports:
    - Test the app

"""
import json
import enki
from base import Test
from analysis import basic
from mock import patch, Mock


class TestApp(Test):

    """Class for Testing the PyBossa application."""


    def test_basic(self):
        """Test basic method works."""
        with patch('enki.Enki', autospec=True):
            enki_mock = enki.Enki(endpoint='server',
                                  api_key='api',
                                  project_short_name='project')
            enki_mock.tasks = []
            res = basic(**self.payload)
            assert enki_mock.get_tasks.called
            assert enki_mock.get_task_runs.called
            assert res == 'OK', res
