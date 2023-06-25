# CI  Repo for Web Applicatiton

## Description 
This repository contain all the necessary resources in order to build and deploy an application into AWS ECR

## Repo Content 
* Jenkinsfile to build and deploy the application to aws ECR (from my home jenkins lab) 
- 

* Python web application (dev-ci.py) including the requirements.txt

* Dockerfile to build the application and create an image out of it

* Kubernetes manifests
 - both manifests are deployed under tomer-candidate namespace 
 - deployment.yaml  which labels the application and the containers.image to my ECR 
 - service.yaml to create a service of type loadbalancer and expose the application to the world