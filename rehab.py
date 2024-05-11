#!/usr/bin/python3

from fabric.api import *


env.user = "ubuntu"
env.hosts = ['54.174.46.224', '54.146.95.95']
env.key_file = "/home/vagrant/.ssh/id_rsa.pub"

def rehab():
    try:
        sudo("rm -r /data/")
    except:
        pass
    sudo("/home/ubuntu/AirBnB_clone_v2/./rehab.sh")
    sudo("nginx -s reload")
    sudo("/home/ubuntu/AirBnB_clone_v2/./0-setup_web_static.sh")
