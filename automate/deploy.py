import os
import subprocess
import shlex

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

path_downloaded = '/mnt/data/completed/TV'
get_iplayer = '/home/bhcopeland/.get_iplayer/pvr'
path_completed = '/var/data/TV'

tv_shows = [f for f in os.listdir (get_iplayer)]
for show in tv_shows:
    print(show)
    p = subprocess.Popen("get_iplayer --pvr " + show, shell=True, stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    p_status = p.wait()
    print output
    for file_com in os.listdir(path_completed):
        sub = path_completed + '/' + file_com
        for file_coms in os.listdir(sub):
            r = subprocess.Popen("flock -n /tmp/.rlock_lock rclone move /var/data/ gstorage:/Plex/ -vvv", shell=True, stdout=subprocess.PIPE)
	    (output, err) = r.communicate()
	    r_status = r.wait()
            print("rclone", output)
    for files in os.listdir(path_downloaded):
        if files.endswith(".mp4"):
            f = subprocess.Popen("/opt/flexget/venv/bin/flexget -c /opt/flexget/config_sorter.yml execute", shell=True, stdout=subprocess.PIPE)
            (output, err) = f.communicate()
            f_status = f.wait()
            print("Flexget", output)
