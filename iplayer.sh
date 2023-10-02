#!/bin/bash

#get_iplayer --pvr && pipenv run flexget -c files/flexget/config_sorter.yml execute && rclone move /var/data/ gstorag    e:/Plex/ -vvv

docker pull barwell/get-iplayer:latest
cd /home/ben/GitHub/ansible-seedbox-env
docker run -v $(pwd)/files/get_iplayer:/data/config -v /mnt/data/completed/TV:/data/output barwell/get-iplayer --pvr
pipenv run flexget -c files/flexget/config_sorter.yml execute
#rclone move /var/data/ gstorage:/Plex/ -vvv
rsync -avhe ssh /var/data/TV/ bhcopeland@192.168.0.242:/mnt/media/TV/
