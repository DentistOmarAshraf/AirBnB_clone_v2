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
    if not archive_path or not os.path.isfile(archive_path):
        return False

    base_name = os.path.basename(archive_path)
    wout_exet = os.path.splitext(base_name)[0]
    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/{}/"
        .format(wout_exet))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(base_name, wout_exet))
    run("rm /tmp/{}"
        .format(base_name))
    with cd("/data/web_static/releases/"):
        run("chmod ugo+x {}/web_static/*.html"
            .format(wout_exet))
        run("chmod g-w {}/web_static/*.html"
            .format(wout_exet))
        run("mv {}/web_static/* {}/"
            .format(wout_exet, wout_exet))
        run("rm -rf {}/web_static"
            .format(wout_exet))
    run("rm -fr /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(wout_exet))
    print
