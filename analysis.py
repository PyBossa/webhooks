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
    for t in e.tasks:
        desc = e.task_runs_df[t.id]['info'].describe()
        print "The top answer for task.id %s is %s" % (t.id, desc['top'])
    with open('./static/results.json', 'w') as f:
        f.write(json.dumps(kwargs))
