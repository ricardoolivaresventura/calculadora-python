pipeline {
    agent any
     triggers {
        pollSCM('*****')
    }
    stages {
        stage("Unit test"){
            steps {
                sh "python -m unittest"
            }
        }
    }
}