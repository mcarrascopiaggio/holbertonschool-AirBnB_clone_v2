#!/usr/bin/python3
"""
Fabric script that distributes an archive
to your web servers, using the function do_deploy
"""

from fabric.api import local, put, env, run
from os import path
env.hosts = ['54.87.154.255', '54.172.224.147']
env.user = "ubuntu"

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

def do_deploy(archive_path):
    """function to distribute an archive to web server"""
    if not (path.exists(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        name = archive_path.split('/')[1].split('.')[0]
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
            .format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except:
        return False
