#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive
"""
from fabric.api import env
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy
import os

# Define the web servers
env.hosts = ['3.80.204.65', '3.80.117.108']

def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
