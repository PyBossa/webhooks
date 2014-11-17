[![Build
Status](https://travis-ci.org/PyBossa/webhooks.svg)](https://travis-ci.org/PyBossa/webhooks)
[![Coverage Status](https://img.shields.io/coveralls/PyBossa/webhooks.svg)](https://coveralls.io/r/PyBossa/webhooks?branch=master)
## Analyzing your PyBossa project in real-time

This very simple web module shows how you can easily analyze your PyBossa
project in real-time.

PyBossa supports webhooks, notifying via an HTTP POST request the task that has
been completed by the volunteers or users. The POST sends basically the
following data:

```JSON
{'fired_at':,
 'app_short_name': 'project-slug',
 'app_id': 1,
 'task_id': 1,
 'event': 'task_completed'} 
```

The PyBossa server sends all the required information to analyze the results of
the contributions of the volunteers for a given task using
[Enki](https://github.com/PyBossa/enki).

While the main purpose of this project is to do the analysis of the results,
you can customize and fork this project to do many more things like:

 * Post to Twitter that your project has completed a task.
 * Upload the results to your DropBox folder by writing the results in a file.
 * etc.

In this specific version, the **analysis** module only shows how you can easily 
get the most voted option for an image pattern recognition project.

## Installation

To install the project all you need is run the following command (we recommend
you to use a virtual environment):

```bash
pip install -r requirements.txt
```

Now, copy the settings.py.template file to: **settings.py** and fill in the
information. Once you are done with this file, you'll be ready to run the
server.

## Running the server

Now that you've the required libraries installed, running the server is as
simple as this:

```bash
python app.py
```

## Configuring background jobs

By default, this project has disabled the creation of queues in your system. If
you expect to have lots of contributions in your project, we recommend you to
enable them.

To support queues you will need to install in your machine a Redis server.
Then, change the flag: **enable_background_jobs** to True in your settings.py
file, and restart the server. 

*Note*: if you are already running a Redis server and queues, you can customize
the name of your queue in the settings file. Check out the config variable:
**queue_name**.

### Running the background jobs

Now that you have the project running background jobs, you need to process
them. This is very simple, in another terminal run the following command:

```bash
rqworker mywebhooks
```

*NOTE*: If you've changed the name of the queue, please, update the previous
command with your new queue name. That's all! Enjoy!!!

## LICENSE

See COPYING file.
