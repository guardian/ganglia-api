Ganglia API v2
==============

The Ganglia API is a small standalone python application that takes XML data from
a number of Ganglia gmetad processes and presents a RESTful JSON API of the most
recently received data.

This is designed to be part of our wider monitoring and metrics framework.

What's that you say?
--------------------

The ganglia gmetad XML API leaves something to be desired, especially if you are running
a large number of gmetad processes.  This finds all of the gmetad processes, then
polls each one of them in turn, keeping the latest results in memory.

We make it easy to query the latest data searching by environment, grid, cluster, host,
group or metric name.

Requirements and assumptions
----------------------------

You'll need python 2.7 and tornado (we use 4.3) available to run this server.

The code assumes you are on the same server as the gmetad configuration, which is
stored under /etc/ganglia using filenames of the form `gmetad-*.conf` - the asterisk
being interpreted as the environment.

**Ganglia Gmetad Example Configuration Files**

```
gmetad-PROD.conf   # => xml_port 8651, interactive_port 8652
gmetad-STAGE.conf  # => xml_port 8751, interactive_port 8752
gmetad-DEV.conf    # => xml_port 8851, interactive_port 8852
```

We also assume that /var/log/ganglia-api.log is writable and we can create 
/var/run/ganglia-api.pid to record the PID.

That being the case you should be able to run the python app on the command line
and it will listen by default on port 8080. 

### Setup

	virtualenv ve
	source ve/bin/activate
	pip install -r requirements.txt

Edit `ganglia_api.py` to import dev_settings rather than settings.

	python ganglia/ganglia_api.py

The API should now be running on port 8080.

The API
-------

There is currently one API endpoint at http://localhost:8080/ganglia/api/v2/metrics

You can filter using the following fields:
 - environment
 - grid
 - cluster
 - host
 - group
 - metric

e.g.
http://localhost:8080/ganglia/api/v2/metrics?environment=PROD&metric=load_one

Which will return you the most recent one minute load values for every host in PROD
as JSON.

The following is some example output:

    {
        "metrics": [
            {
                "cluster": "webdc1",
                "dataUrl": "http://ganglia-api.example.com:8080/ganglia/api/v2/metrics?&environment=PROD&cluster=webdc1&host=vagrant-ubuntu-trusty-64&grid=web&metric=load_one",
                "description": "One minute load average",
                "environment": "PROD",
                "graphUrl": "http://vagrant-ubuntu-trusty-64/ganglia/graph.php?&ti=One%20Minute%20Load%20Average&c=webdc1&r=1day&v=0&h=vagrant-ubuntu-trusty-64&vl=%20&z=default&m=load_one",
                "grid": "web",
                "group": "load",
                "host": "vagrant-ubuntu-trusty-64",
                "id": "prod.web.webdc1.vagrant-ubuntu-trusty-64.load.load_one",
                "instance": "",
                "metric": "load_one",
                "sampleTime": "2016-06-17T13:47:35.000Z",
                "tags": [
                    "foo",
                    "bar",
                    "baz"
                ],
                "title": "One Minute Load Average",
                "type": "gauge",
                "units": " ",
                "value": 0.0
            }
        ],
        "status": "ok",
        "time": "0.000",
        "total": 1
    }

License
-------

    Ganglia API v1 and v2
    Copyright 2012-2013,2016 Guardian News & Media

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
