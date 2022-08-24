#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
https://www.hostinger.es/tutoriales/como-usar-comando-tar-linux
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """do_pack function"""
    local("mkdir -p versions")
    now = datetime.now()
    name = "versions/web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    try:
        local("tar -czvf " + name + " web_static")
        return name
    except Exception:
        return None
