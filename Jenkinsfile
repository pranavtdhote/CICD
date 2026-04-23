pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main' , url: 'https://github.com/pranavtdhote/event-registration-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t event-registration-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 event-registration-app'
            }
        }

        stage('Test Application') {
            steps {
                sh 'echo "Application Deployed Successfully"'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop event-registration-app || true
                docker rm event-registration-app || true
                docker run -d -p 5000:5000 --name event-registration-app event-registration-app
                '''
            }
        }
    }
}
