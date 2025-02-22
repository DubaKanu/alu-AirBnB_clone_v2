#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers.
"""

from fabric.api import put, run, env
from os.path import exists

# List of web server IPs
env.hosts = ['3.80.204.65', '75.101.241.129']


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers.
    Returns True if successful, otherwise False.
    """
    if not exists(archive_path):
        return False

    try:
        # Extract file name and directory name from archive_path
        file_n = archive_path.split("/")[-1]  # Extract filename
        no_ext = file_n.split(".")[0]  # Remove file extension
        path = "/data/web_static/releases/"

        # Upload the archive to /tmp/ on the server
        put(archive_path, "/tmp/")

        # Create the release directory
        run("mkdir -p {}{}/".format(path, no_ext))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C {}{}/".format(file_n, path, no_ext))

        # Remove the uploaded archive
        run("rm /tmp/{}".format(file_n))

        # Move the contents from extracted folder
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))

        # Remove the now-empty web_static folder
        run("rm -rf {}{}/web_static".format(path, no_ext))

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))

        return True

    except Exception:
        return False

