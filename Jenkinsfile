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
        stage('Deploy') {
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
                    git branch: 'master', url: 'https://github.com/your/repo.git'
                    sh "sed -i 's/imageTag:.*/imageTag: ${env.BUILD_NUMBER}/' /values.yaml"
                    git add: '.', comment: "Update Helm chart image tag to ${env.BUILD_NUMBER}"
                    git push
                }
            }
        }
    }
}
