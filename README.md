Ganglia API
===========

The Ganglia API is a small standalone python application that takes XML data from
a number of Ganglia gmetad processes and presents a RESTful JSON API of the most
recently received data.

This is designed to be part of our wider monitoring and metrics framework.

What's that you say?
--------------------

The ganglia gmetad API leaves something to be desired, especially if you are running
a large number of gmetad processes.  This finds all of the gmetad processes, then
polls each one of them in turn, keeping the latest results in memory.

We make it easy to query the latest data searching by environment, host, metric name.

Requirements and assumptions
----------------------------

You'll need python 2.6 and tornado (we use 2.2.1) available to run this server.

The code assumes you are on the same server as the gmetad configuration, which is
stored under /etc/ganglia using filenames of the form gmetad-*-*.conf - the first
match being interpreted as the environment and the second as the service.

We also assume that /var/log/ganglia-api.log is writable and we can create 
/var/run/ganglia-api.pid to record the PID.

That being the case you should be able to run the python app on the command line
and it will listen by default on port 8080. 

The API
-------

There is currently one API endpoint at http://localhost:8080/ganglia/api/v1/metrics

You can filter using the following fields:
 - environment
 - service
 - metric
 - group
 - host
 - cluster

e.g.
http://localhost:8080/ganglia/api/v1/metrics?environment=PROD&metric=load_one

Which will return you the most recent one minute load values for every host in PROD
as JSON.

The following is some example output:

	{
	    "response": {
	        "localTime": "2012-10-01T18:22:20.866758", 
	        "metrics": [
	            {
	                "age": "89", 
	                "cluster": "oradb_dc1", 
	                "dataUrl": "http://ganglia.guprod.gnl:8080/ganglia/api/v1/metrics?&environment=PROD&cluster=oradb_dc1&host=oradb04&metric=load_one&service=R2", 
	                "description": "One minute load average", 
	                "environment": "PROD", 
	                "graphUrl": "http://ganglia.gul3.gnl/ganglia-PROD-R2/graph.php?&ti=One%20Minute%20Load%20Average&c=oradb_dc1&r=1day&v=0&h=oradb04&vl=%20&z=default&m=load_one", 
	                "group": "load", 
	                "host": "oradb04", 
	                "id": "prod.r2.oradb_dc1.oradb04.load.load_one", 
	                "instance": "", 
	                "metric": "load_one", 
	                "service": "R2", 
	                "tags": [
	                    "os:Linux", 
	                    "datacentre:dc1", 
	                    "virtual:physical"
	                ], 
	                "title": "One Minute Load Average", 
	                "type": "both", 
	                "units": " ", 
	                "value": "12.57"
	            },
	            {
	                "age": "93", 
	                "cluster": "resmac_dc1", 
	                "dataUrl": "http://ganglia.guprod.gnl:8080/ganglia/api/v1/metrics?&environment=PROD&cluster=resmac_dc1&host=resmac01&metric=load_one&service=R2", 
	                "description": "One minute load average", 
	                "environment": "PROD", 
	                "graphUrl": "http://ganglia.gul3.gnl/ganglia-PROD-R2/graph.php?&ti=One%20Minute%20Load%20Average&c=resmac_dc1&r=1day&v=0&h=resmac01&vl=%20&z=default&m=load_one", 
	                "group": "load", 
	                "host": "resmac01", 
	                "id": "prod.r2.resmac_dc1.resmac01.load.load_one", 
	                "instance": "", 
	                "metric": "load_one", 
	                "service": "R2", 
	                "tags": [
	                    "os:Linux", 
	                    "datacentre:dc1", 
	                    "virtual:physical"
	                ], 
	                "title": "One Minute Load Average", 
	                "type": "both", 
	                "units": " ", 
	                "value": "3.04"
	            },

	... SNIP ...

	            {
	                "cluster": "oradb_dc1", 
	                "dataUrl": "http://ganglia.guprod.gnl:8080/ganglia/api/v1/metrics?&environment=PROD&cluster=oradb_dc1&metric=load_one&service=R2", 
	                "description": "One minute load average", 
	                "environment": "PROD", 
	                "graphUrl": "http://ganglia.gul3.gnl/ganglia-PROD-R2/graph.php?&ti=One%20Minute%20Load%20Average&c=oradb_dc1&r=1day&v=0&vl=%20&z=default&m=load_one", 
	                "group": "load", 
	                "id": "prod.r2.oradb_dc1.load.load_one", 
	                "instance": "", 
	                "metric": "load_one", 
	                "num": "1", 
	                "service": "R2", 
	                "sum": "11.09", 
	                "title": "One Minute Load Average", 
	                "type": "both", 
	                "units": " "
	            }, 
	            {
	                "cluster": "resmac_dc1", 
	                "dataUrl": "http://ganglia.guprod.gnl:8080/ganglia/api/v1/metrics?&environment=PROD&cluster=resmac_dc1&metric=load_one&service=R2", 
	                "description": "One minute load average", 
	                "environment": "PROD", 
	                "graphUrl": "http://ganglia.gul3.gnl/ganglia-PROD-R2/graph.php?&ti=One%20Minute%20Load%20Average&c=resmac_dc1&r=1day&v=0&vl=%20&z=default&m=load_one", 
	                "group": "load", 
	                "id": "prod.r2.resmac_dc1.load.load_one", 
	                "instance": "", 
	                "metric": "load_one", 
	                "num": "4", 
	                "service": "R2", 
	                "sum": "6.57", 
	                "title": "One Minute Load Average", 
	                "type": "both", 
	                "units": " "
	            }

	... SNIP ...

	        ], 
	        "status": "ok", 
	        "time": "0.069", 
	        "total": 46
	    }
	}

