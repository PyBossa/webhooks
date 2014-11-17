# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2014 Daniel Lombraña González
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

import enki
import json
import settings

def basic(**kwargs):
    """A basic analyzer."""
    e = enki.Enki(endpoint=settings.endpoint,
                  api_key=settings.api_key,
                  app_short_name=kwargs['app_short_name'])
    e.get_tasks(task_id=kwargs['task_id'])
    e.get_task_runs()
    print e.tasks
    print "Enki initaliated"
    for t in e.tasks: # pragma: no cover
        desc = e.task_runs_df[t.id]['info'].describe()
        print "The top answer for task.id %s is %s" % (t.id, desc['top'])
    with open('./static/results.json', 'w') as f:
        f.write(json.dumps(kwargs))
    return "OK"
