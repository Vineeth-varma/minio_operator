#! /bin/bash

sudo echo "minio ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers

Mount_data_folder=$(mount -l | grep 'type ext4' | awk '{ print $3}')
sudo chown minio:minio $Mount_data_folder

sudo echo "export PATH=$PATH"| sudo tee -a /home/minio/.bashrc
source /home/minio/.bashrc

export FLASK_APP=/home/minio/flask-basic-auth/index.py
flask run -h 0.0.0.0  &

while true
do
  sleep 60 
done
