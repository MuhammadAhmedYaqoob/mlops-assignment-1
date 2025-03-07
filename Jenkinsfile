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
        always {
            emailext body: 'Pipeline is accomplished.', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }
    }
}
