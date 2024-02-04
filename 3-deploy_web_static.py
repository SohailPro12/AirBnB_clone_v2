#!/usr/bin/python3
# Fabric script that generates a .tgz archive
# from the contents of the web_static folder
from datetime import datetime
from fabric.api import local, put, run, env
from os.path import exists
env.hosts = ['54.87.205.91', '54.87.240.9']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """distributes archive remotely"""
    if exists(archive_path) is False:
        return False
    try:
        """Extract Filename and No Extension"""
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        """Prepare Path and Upload Archive"""
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        """Create Release Directory and Extract Archive"""
        run('mkdir -p {}{}/'.format(path, name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, name))
        """Clean Up Temporary Files"""
        run('rm /tmp/{}'.format(file_name))
        """Move Web Static Content and Remove Original Folder"""
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        run('rm -rf {}{}/web_static'.format(path, name))
        """Remove Old Current Link and Create New Symbolic Link"""
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, name))
        return True
    except Exception as e:
        return False


def deploy():
    """full deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
