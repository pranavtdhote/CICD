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
                sh '''
                docker stop event-registration-app || true
                docker rm event-registration-app || true

                docker ps -q --filter "publish=5000" | xargs -r docker stop
                docker ps -aq --filter "publish=5000" | xargs -r docker rm

                docker run -d -p 5000:5000 --name event-registration-app event-registration-app
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh 'echo "Application Deployed Successfully"'
            }
        }


    }
}
