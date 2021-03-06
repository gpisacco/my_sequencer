#!/bin/bash
cd /var/data/my_sequencer
# virtualenv creation
mkdir local
cd local
virtualenv env
source env/bin/activate
pip install -r ../requirements.txt

# let www-data user access the site
sudo chown -R  www-data /var/data/my_sequencer

cd ../scripts
# nginx config
sudo cp my_sequencer /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

# nginx config
sudo cp my_sequencer.ini /etc/uwsgi/apps-enabled/
sudo service mongodb start
sleep 10
sudo service uwsgi start
sudo service nginx start
tail -f /var/log/lastlog #ugly way to avoid configuring supervidord
