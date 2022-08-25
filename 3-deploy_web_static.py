#!/usr/bin/python3
"""
Fabric script that distributes an archive
to your web servers, using the function do_deploy
"""

from fabric.api import local, put, env, run
from os import path
from datetime import datetime
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
        file_name = archive_path.split('/')[1]
        file_name_noext = archive_path.split('/')[1].split('.')[0]
        to_path = '/data/web_static/releases/' + file_name_noext
        up_path = '/tmp/' + file_name
        put(archive_path, up_path)
        run('mkdir -p ' + to_path)
        run('tar -xzf ' + up_path + ' -C ' + to_path)
        run('rm ' + up_path)
        run('mv ' + to_path + '/web_static/* ' + to_path + '/')
        run('rm -rf ' + to_path + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s ' + to_path + ' /data/web_static/current')
        return True
    except Exception:
        return False

def deploy():
"""
creates and distributes an archive to your web servers
"""
route = do_pack()
    if route is None:
        return False
    dep = do_deploy(route)
    if dep is False:
        return False
    return dep
