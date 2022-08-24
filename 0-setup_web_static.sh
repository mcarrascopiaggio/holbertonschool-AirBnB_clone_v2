#!/usr/bin/env bash
# Prepare your web servers
# install Nginx if it not already installed
# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/releases/ if it doesn’t already exist
# Create the folder /data/web_static/shared/ if it doesn’t already exist
# Create the folder /data/web_static/releases/test/ if it doesn’t already exis
# https://linux.die.net/man/1/mkdir -> mkdir -p no error if existing, 
# Create a fake HTML file /data/web_static/releases/test/index.html
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
# https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/
# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive.
# https://askubuntu.com/questions/6723/change-folder-permissions-and-ownership
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# Don’t forget to restart Nginx after updating the configuration
sudo apt update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo chmod 777 /data/web_static/releases/test/index.html
sudo echo "Hello All!" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "56i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
