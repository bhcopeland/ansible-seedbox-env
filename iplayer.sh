#!/bin/bash

#get_iplayer --pvr && pipenv run flexget -c files/flexget/config_sorter.yml execute && rclone move /var/data/ gstorag    e:/Plex/ -vvv


docker run -v $(pwd)/files/get_iplayer:/data/config -v /mnt/data/completed/TV:/data/output barwell/get-iplayer --pvr && pipenv run flexget -c files/flexget/config_sorter.yml execute && rclone move /var/data/ gstorage:/Plex/ -vvv
