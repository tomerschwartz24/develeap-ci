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
        stage('Push to ECR') {
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
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[credentialsId: 'github-ATOKEN', url: 'git@github.com:tomerschwartz24/mock-app-infra.git', refspec: '+refs/heads/*:refs/remotes/origin/*']]])
                    sh """
                    git checkout main
                       """
                }
            }
        }
    }
}
