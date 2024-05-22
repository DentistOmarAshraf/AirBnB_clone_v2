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

    if not result.failed:
        full_path = f"versions/web_static_{x}.tgz"
        return (full_path)


def do_deploy(archive_path=None):
    """
    do_deploy - deploy archeived files
    """
    if not archive_path or not os.path.isfile(archive_path):
        return False

    loc = False
    func = run
    ip_address = os.popen("curl -s ifconfig.me").read()
    if ip_address in env.hosts:
        loc = True
        func = local

    base_name = os.path.basename(archive_path)
    wout_exet = os.path.splitext(base_name)[0]

    if not loc:
        put(archive_path, "/tmp/", local)
    else:
        local("cp {} /tmp/".format(archive_path))

    func("mkdir -p /data/web_static/releases/{}/"
         .format(wout_exet))
    func("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
         .format(base_name, wout_exet))
    func("rm /tmp/{}"
         .format(base_name))

    str_1 = "/data/web_static/releases/"
    str_2 = f"{wout_exet}"
    str_3 = "/web_static/*.html"

    func(f"chmod ugo+x {str_1}{str_2}{str_3}")
    func(f"chmod g-w {str_1}{str_2}{str_3}")
    func(f"mv {str_1}{str_2}/web_static/* {str_1}{str_2}/")
    func(f"rm -rf {str_1}{str_2}/web_static")
    func("rm -rf /data/web_static/current")
    func(f"ln -s {str_1}{str_2} /data/web_static/current")

if __name__ == "__main__":
    path = execute(do_pack)
    execute(do_deploy, archive_path=path["<local-only>"])
