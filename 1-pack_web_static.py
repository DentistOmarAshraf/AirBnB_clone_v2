#!/usr/bin/env python3
"""
Using Fabric to archive webstatic file
"""

from fabric.api import *


def do_pack():
    """
    do_pack - order to create archive of web_static folder
    """
    with hide("running", "output"):
        full_date = local("stat -c '%y' web_static", capture=True).stdout

    # here x to change date format from (year-month-day)
    # to (yearmonthday)
    x = ""
    for i in full_date:
        if i == '.':
            break
        if i.isnumeric():
            x = x + i
    
    print(f"Packing web_static to versions/web_static_{x}.tgz")
    with hide('running', 'output'):
        local("mkdir -p versions")
    local(f"tar -cvzf versions/web_static_{x}.tgz web_static")
