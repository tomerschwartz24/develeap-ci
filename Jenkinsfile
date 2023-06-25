 
pipeline {
    agent any
     environment {
 
    AWS_ACCOUNT_ID="384005890259"
    AWS_DEFAULT_REGION="eu-central-1" 
    IMAGE_REPO_NAME="counter-service"
    IMAGE_TAG="latest"
    REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
 }
    stages {
        
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository'
                checkout scm
            }
        }

        stage('Build') {
            steps {
            script {
                dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}" 
                //ecr login 
            }
              
            }
        }
        
        
        stage('Deploy to ECR') {
            steps {
            script {
                
                sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"

                    
                }
            }
        }
    } 
}
