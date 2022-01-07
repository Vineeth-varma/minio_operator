#! /bin/bash
sudo docker rmi flaskproject:latest
sudo docker rmi eccs-docker-registry.ericsson.com:5000/flaskproject:v1
sudo docker build -t flaskproject:v1 .
sudo docker tag flaskproject:v1 eccs-docker-registry.ericsson.com:5000/flaskproject:v1
sudo docker push eccs-docker-registry.ericsson.com:5000/flaskproject:v1
