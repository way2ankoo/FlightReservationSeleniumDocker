pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                sh "docker build -t=way2ankoo/selenium ."
            }
        }
        stage('Push Image') {
            environment {
                DOCKER_HUB = credentials('dockerhub-creds')
            }
            steps {
                sh 'docker login -u ${DOCKER_HUB_USR} -p ${DOCKER_HUB_PSW}'
                sh "docker push way2ankoo/selenium-docker"
            }
        }
    }

    post {
        always {
            sh "docker logout"
        }
    }
}