#!/bin/bash

#run the test scripts
cd /var/data/my_sequencer
source local/env/bin/activate
export CONFIG=../config/test.conf
py.test -v -s api/test_my_sequencer.py