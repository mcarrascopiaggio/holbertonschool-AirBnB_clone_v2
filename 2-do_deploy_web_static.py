#!/usr/bin/python3
"""
Fabric script that distributes an archive
to your web servers, using the function do_deploy
"""

from fabric.api import local, put, env, run
from os import path
env.hosts = ['54.87.154.255', '54.172.224.147']
env.user = "ubuntu"


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
