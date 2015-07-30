#!/bin/bash

curl -O https://raw.githubusercontent.com/gpisacco/my_sequencer/master/scripts/Dockerfile
docker build -t sequence .
docker run -d -p 8085:80 sequence
sleep 30
curl http://localhost:8085/value/po_number
