pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages {
        stage("Unit test"){
            steps {
                sh "python3 -m unittest"
            }
        }
    }
}