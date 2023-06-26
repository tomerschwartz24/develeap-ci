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
                script {
                    app = docker.build("counter-service")
                }
            }
        }
        stage('Push Image to ECR') {
            steps {
            script {
                docker.withRegistry('https://384005890259.dkr.ecr.eu-central-1.amazonaws.com/counter-service', 'ecr:eu-central-1:aws-creds') {
                    app.push("${env.BUILD_NUMBER}")
                    app.push("latest")
                }
            }
        }
    }
    stage('Update Helm Chart') {
        steps {
            script {
                try {
                    build job: 'mock-app-helm-ci'
                } catch (Exception e) {
                    // Handle the failure gracefully
                    echo "Failed to update Helm Chart: ${e.getMessage()}"
                }
            }
        }
    }
}
}
