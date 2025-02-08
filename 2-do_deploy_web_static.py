#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""
from fabric.api import env, put, run
import os

# Define the web servers
env.hosts = ['3.80.204.65', '3.80.117.108']

def do_deploy(archive_path):
    """Deploys an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]  # Extract filename
        folder_name = file_name.split(".")[0]  # Remove extension
        release_path = "/data/web_static/releases/{}/".format(folder_name)

        # Upload archive to /tmp/
        put(archive_path, "/tmp/{}".format(file_name))

        # Create the directory on the remote server
        run("mkdir -p {}".format(release_path))

        # Extract the archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_path))

        # Remove the uploaded archive
        run("rm /tmp/{}".format(file_name))

        # Move contents from extracted folder
        run("mv {}/web_static/* {}".format(release_path, release_path))

        # Remove the now-empty web_static folder
        run("rm -rf {}/web_static".format(release_path))

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True
    except:
        return False
