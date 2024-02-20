#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-pip
sudo pip install --no-cache-dir -r requirements.txt
sudo apt install docker -y
sudo systemctl start docker
#sudo usermod -aG sudo $USER
#sudo usermod -aG docker $USER
sudo systemctl restart docker
sudo apt install docker-compose -y
sudo apt install unzip
wget https://github.com/SergeiLomachenko/app/raw/main/app.zip
unzip app.zip -d app/
cd app/app/
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose restart
