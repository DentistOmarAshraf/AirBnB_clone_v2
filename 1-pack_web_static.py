#!/usr/bin/python3
"""
Using Fabric to archive webstatic file
"""

from fabric.api import *
from datetime import datetime


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
