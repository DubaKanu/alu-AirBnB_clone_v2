#!/usr/bin/env bash
# Sets up the web servers for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update -y
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create/recreate the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
CONFIG_FILE="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" $CONFIG_FILE; then
    sudo sed -i "/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" $CONFIG_FILE
fi

# Restart Nginx to apply changes
sudo service nginx restart

exit 0
