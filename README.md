# CI  Repo for Web Applicatiton

## Description 
This repository contain all the necessary resources in order to build and deploy an application into AWS ECR

## Repo Content 
* Jenkinsfile to build and deploy the application to aws ECR (from my home jenkins lab) 

* Python web application (counter-service.py) including the requirements.txt

* Dockerfile to build the application and create a docker image out of it. 

### Jenkins Pipeline <br>
- The pipeline  checkouts the repository. <br>
- builds the application. <br>
- pushes the docker image to ECR with the BUILD_NUMBER of jenkins + latest tag. <br>
- Additionally the pipeline will check out the infra repo and update the application helm chart image.tag to the same build number the docker image have.

### Counter-service application
- Python application that checks the number of HTTP GET requests and "announce" them.