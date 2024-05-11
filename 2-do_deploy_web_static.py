#!/usr/bin/python3
"""
Using Fabric to archive webstatic file
"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['54.174.46.224', '54.146.95.95']


def do_pack():
    """
    do_pack - order to create archive of web_static folder
    """
    date = datetime.now()
    x = date.strftime("%Y%m%d%H%M%S")
    print(f"Packing web_static to versions/web_static_{x}.tgz")
    with hide("running", "output"):
        local("mkdir -p versions")
    local(f"tar -cvzf versions/web_static_{x}.tgz web_static")


def do_deploy(archive_path=None):
    """
    do_deploy - deploy archeived files
    """
    if not archive_path or  not os.path.isfile(archive_path):
        return False

    base_name = os.path.basename(archive_path)
    wout_exet = os.path.splitext(base_name)[0]
    put(archive_path, "/tmp/")
    run(f"mkdir -p /data/web_static/releases/{wout_exet}")
    run(f"tar -xzf /tmp/{base_name} -C /data/web_static/releases/{wout_exet}")
    run(f"rm /tmp/{base_name}")
    x = f"/data/web_static/releases/{wout_exet}/web_static/"
    run(f"mv {x}/* /data/web_static/releases/{wout_exet}")
    run(f"rm -fr {x}")
    run("rm -fr /data/web_static/current")
    symb_link = "/data/web_static/current"
    run(f"ln -s /data/web_static/releases/{wout_exet} {symb_link}")
    run("sudo service nginx reload")
    print("New version deployed!")
