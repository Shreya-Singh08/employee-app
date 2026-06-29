pipeline {

    agent any

    environment {
        IMAGE_NAME = "shreyasingh08/employee-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    tools {
        sonarQube 'SonarScanner'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Shreya-Singh08/employee-app.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat """
                    sonar-scanner ^
                    -Dsonar.projectKey=employee-app ^
                    -Dsonar.projectName=employee-app ^
                    -Dsonar.sources=. ^
                    -Dsonar.python.version=3
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat "kubectl apply -f kubernetes/deployment.yaml"
                bat "kubectl apply -f kubernetes/service.yaml"
                bat "kubectl apply -f kubernetes/configmap.yaml"
                bat "kubectl apply -f kubernetes/secret.yaml"
            }
        }

        stage('Verify Deployment') {
            steps {
                bat "kubectl get pods"
                bat "kubectl get deployments"
                bat "kubectl get svc"
            }
        }
    }

    post {

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }

        always {
            cleanWs()
        }
    }
}