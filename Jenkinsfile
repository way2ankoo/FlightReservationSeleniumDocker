pipeline {
    agent any

    stages {
        stage('Stage-1') {
            steps {
                echo 'Hello World'
                echo "Number = ${NUMBER}"
            }
        }
        stage('Stage-2') {
            environment {
                NUMBER = 6
            }
            steps {
                echo 'firse Hello World'
                echo "Number = ${NUMBER}"
            }
        }
        stage('Stage-3') {
            steps {
                echo 'firse Hello World firse'
                echo "Number = $(NUMBER)"
            }
        }
    }
    post{
        always{
            echo 'doing cleanup'
        }
    }
}