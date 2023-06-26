pipeline {
    agent any
    stages {
        stage('Pre-check') {
            steps {
                script {
                    // Check if the change is in the source repository
                    def sourceRepoChange = false
                    def sourceRepoUrl = 'https://github.com/tomerschwartz24/mock-app/'
                    def pipelineRepoUrl = 'git@github.com:tomerschwartz24/mock-app-infra.git'
                    
                    for (change in currentBuild.changeSets) {
                        for (commit in change) {
                            if (commit.url.startsWith(sourceRepoUrl)) {
                                sourceRepoChange = true
                                break
                            }
                        }
                    }
                    
                    if (!sourceRepoChange) {
                        echo 'Change was triggered via Update Helm Chart. Stopping the build.'
                        currentBuild.result = 'ABORTED'
                        return
                    }
                }
            }
        }
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
                    yq eval   '.image.tag = "${env.BUILD_NUMBER}"' -i counter-app-helm/values.yaml
                    git add counter-app-helm/values.yaml
                    git commit counter-app-helm/values.yaml -m " Updated counter-app Helm chart image tag to \${BUILD_NUMBER} "
                    git push --set-upstream origin main
                       """
                }
            }
        }
    }
}
