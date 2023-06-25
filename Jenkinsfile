 
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
            }
              //  sh 'docker build -t 384005890259.dkr.ecr.eu-central-1.amazonaws.com/counter-service:counter -f Dockerfile .'
            }
        }
        
        stage('Deploy to ECR') {
            steps {
            script {
                docker.withRegistry('https://384005890259.dkr.ecr.eu-central-1.amazonaws.com/counter-service', 'ecr:eu-central-1:aws-creds')
                sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"

                    
                }
            }
        }
    } 
}
