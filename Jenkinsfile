pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Shreya-Singh08/employee-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t employee-app:v1 .'
            }
        }

        stage('Docker Images') {
            steps {
                bat 'docker images'
            }
        }

    }
}