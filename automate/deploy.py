import os
import subprocess
import shlex

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

path_downloaded = '/mnt/data/completed/TV'
get_iplayer = '/home/ben/.get_iplayer/pvr'
path_completed = '/var/data/TV'

def upgrade_iplayer():
    u = subprocess.Popen("sudo apt install get-iplayer -y", shell=True, stdout=subprocess.PIPE)
    (output, err) = u.communicate()
    u_status = u.wait()

def run_flexget():
    f = subprocess.Popen("venv/bin/flexget -c files/flexget/config_sorter.yml execute", shell=True, stdout=subprocess.PIPE)
    (output, err) = f.communicate()
    f_status = f.wait()
    return output

def run_rclone():
    r = subprocess.Popen("/usr/bin/flock -n /tmp/.rlock_lock rclone move /var/data/ gstorage:/Plex/ -vvv", shell=True, stdout=subprocess.PIPE)
    (output, err) = r.communicate()
    r_status = r.wait()

def run_iplayer():
    p = subprocess.Popen("/usr/bin/get_iplayer --pvr " + show, shell=True, stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    p_status = p.wait()

tv_shows = [f for f in os.listdir (get_iplayer)]
for files in os.listdir(path_downloaded):
   run_flexget()
#   print("Flexget", output)
for show in tv_shows:
   print(show)
   run_iplayer()
#   for file_com in os.listdir(path_completed):
#       sub = path_completed + '/' + file_com
#       for file_coms in os.listdir(sub):
#           run_rclone()
       # if files.endswith(".mp4"):
    #      print("rclone", output)

run_rclone()
