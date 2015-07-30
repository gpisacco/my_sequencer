Sequencer
-------------

The API is simple, to install the docker container run :

.. code-block:: console

    $ curl -sSL https://raw.githubusercontent.com/gpisacco/my_sequencer/master/scripts/base.sh | sh

All you need to bring the API online is to create a docker container
it  gets the code from git , deploys it and runs a small curl script
(the computer needs to have docker installed)

To run the test scripts :

.. code-block:: console

    $ docker exec <container_id> /var/data/my_sequencer/scripts/run_test.sh

Features
--------
* Set a sequencer number
* Retrieve the sequence number

Notes
--------
* All the services (mongodb,nginx and uwsgi) are running in the same container due to time restrictions
* Unit tests and production uses different databases , they are configured via an env varable