#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
Execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    Compresses the 'web_static' folder into a .tgz archive.
    The archive is stored in the 'versions/' directory.
    Returns the archive path if successful, otherwise None.
    """
    try:
        # Ensure the 'versions' directory exists
        if not os.path.exists("versions"):
            local('mkdir -p versions')

        # Generate timestamp for archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = 'versions/web_static_{}.tgz'.format(timestamp)

        # Create the archive
        result = local('tar -cvzf {} web_static'.format(archive_path))

        # Return archive path if successful, otherwise None
        return archive_path if result.succeeded else None

    except Exception:
        return None

