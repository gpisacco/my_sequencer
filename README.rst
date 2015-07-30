Sequencer
-------------

The API is simple, to install the docker container run :

.. code-block:: console

    $ curl -O https://raw.githubusercontent.com/gpisacco/my_sequencer/master/scripts/Dockerfile
    $ docker build -t sequence .
    $ docker run -d -p 8085:80 sequence
    $ sleep 30
    $ curl http://localhost:8085/value/po_number

All you need to bring the API online is to create a docker container
it even gets the code from git and deploys it

To run the test scripts :

.. code-block:: console

    $ docker exec <container_id> /var/data/my_sequencer/scripts/run_test.sh

Features
--------
* Set a sequencer number
* Retrieve the sequence number