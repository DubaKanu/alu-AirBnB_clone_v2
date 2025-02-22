#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Update and install Nginx if not installed
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create required directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
echo "Hello, this is a test HTML file." | sudo tee /data/web_static/releases/test/index.html

# Remove any existing symbolic link and create a new one
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from /data/web_static/current/
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

