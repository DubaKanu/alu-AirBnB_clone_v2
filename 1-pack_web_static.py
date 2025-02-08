#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from web_static folder
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive of web_static directory"""
    try:
        # Ensure the versions directory exists
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Create the archive filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        # Run the tar command to create the archive
        print("Packing web_static to {}".format(archive_path))
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path if os.path.exists(archive_path) else None
    except Exception:
        return None
