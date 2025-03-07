pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/MuhammadAhmedYaqoob/mlops-assignment-1.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("MuhammadAhmedYaqoob/mlops-assignment-1:${env.BUILD_ID}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'mlops-assignment1') {
                        // Ensure dockerImage is accessible here; if needed, declare it at a higher scope
                        def dockerImage = docker.build("MuhammadAhmedYaqoob/mlops-assignment-1:${env.BUILD_ID}")
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
