#!/bin/bash

# this files only pull the lastest version
cd /var/data/my_sequencer
git pull
/bin/bash /var/data/my_sequencer/scripts/install.sh
