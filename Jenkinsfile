pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/pranavtdhote/CICD.git'
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

                # Safe cleanup (no errors)
                docker ps -q --filter "publish=5000" | xargs -r docker stop || true
                docker ps -aq --filter "publish=5000" | xargs -r docker rm || true

                docker run -d -p 5000:5000 --name event-registration-app event-registration-app
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                echo "Running Advanced Test Cases..."

                BASE_URL="http://host.docker.internal:5000"

                # -------------------------------
                # Smart Wait (instead of sleep)
                # -------------------------------
                for i in {1..10}
                do
                    curl -s $BASE_URL && break
                    echo "Waiting for app..."
                    sleep 2
                done

                # -------------------------------
                # Test Case 1: App Reachable
                # -------------------------------
                curl -f $BASE_URL || { echo "App not reachable"; exit 1; }

                # -------------------------------
                # Test Case 2: Status Code
                # -------------------------------
                STATUS=$(curl -o /dev/null -s -w "%{http_code}" $BASE_URL)
                [ "$STATUS" -eq 200 ] || { echo "Wrong status: $STATUS"; exit 1; }

                # -------------------------------
                # Test Case 3: Content Check
                # -------------------------------
                curl -s $BASE_URL | grep -i "event" || {
                    echo "Content check failed"
                    exit 1
                }

                # -------------------------------
                # Test Case 4: Container Running
                # -------------------------------
                docker ps | grep event-registration-app || {
                    echo "Container not running"
                    exit 1
                }

                echo "All Tests Passed ✅"
                '''
            }
        }
    }

    post {
        success {
            echo 'Build SUCCESS: Application deployed and tested successfully!'
        }
        failure {
            echo 'Build FAILED: Check logs for errors.'
        }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}