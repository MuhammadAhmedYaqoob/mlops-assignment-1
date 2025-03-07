pipeline {
    agent any
    environment {
        IMAGE_NAME = "muhammadahmedyaqoob/mlops-assignment-1:${env.BUILD_ID}"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/MuhammadAhmedYaqoob/mlops-assignment-1.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build(IMAGE_NAME)
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'mlops-assignment1') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
    post {
        success {
            emailext subject: "Deployment Successful",
                     body: "The deployment of your application was successful.",
                     to: 'ahmedyaqoobbusiness@gmail.com'
        }
        failure {
            emailext subject: "Deployment Failed",
                     body: "The deployment encountered issues. Please check Jenkins logs.",
                     to: 'ahmedyaqoobbusiness@gmail.com'
        }
    }
}
