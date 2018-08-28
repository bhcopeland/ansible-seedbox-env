import os
import subprocess
import shlex

path_to_watch = '/mnt/data/completed/TV'
get_iplayer = '/home/bhcopeland/.get_iplayer/pvr'

tv_shows = [f for f in os.listdir (get_iplayer)]
for show in tv_shows:
    print(show)
    p = subprocess.Popen("get_iplayer --pvr " + show, shell=True, stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    p_status = p.wait()
    print output
    for file in os.listdir(path_to_watch):
        if file.endswith(".mp4"):
            print(file)
            f = subprocess.Popen("/opt/flexget/venv/bin/flexget --cron -c /opt/flexget/config_sorter.yml execute", shell=True, stdout=subprocess.PIPE)
            (output, err) = f.communicate()
            f_status = f.wait()
            print output
	    r = subprocess.Popen("flock -n /tmp/.rlock_lock rclone move /var/data/ gstorage:/Plex/ -vvv", shell=True, stdout=subprocess.PIPE)
	    (output, err) = r.communicate()
            r_status = r.wait()
            print output
