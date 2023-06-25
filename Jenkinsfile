 
pipeline {
    agent any
    stages {
        
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t 384005890259.dkr.ecr.eu-central-1.amazonaws.com/counter-service:counter -f Dockerfile .'
            }
        }
        
        stage('Deploy to ECR') {
            steps {
            script {
                        docker.withRegistry('384005890259.dkr.ecr.eu-central-1.amazonaws.com/counter-service', 'ecr:eu-central-1:aws-creds') {
                    app.push("${env.BUILD_NUMBER}")
                    app.push("latest")
                    }
                }
            }
        }
    } 
}
