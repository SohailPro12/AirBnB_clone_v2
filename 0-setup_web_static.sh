#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Install Nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Creat the necessarily folders and the index.html
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Hello there!" | sudo tee /data/web_static/releases/test/index.html

# a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give the ownership
sudo chown -hR ubuntu:ubuntu /data/

# configure nginx and restart it
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
