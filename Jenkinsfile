pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main' , url: 'https://github.com/pranavtdhote/CICD.git'
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
                sh '''
                echo "Running Advanced Test Cases..."

                # Wait for app to start
                sleep 10

                BASE_URL="http://localhost:5000"

                # -------------------------------
                # Test Case 1: Application is reachable
                # -------------------------------
                curl -f $BASE_URL || { echo "App not reachable"; exit 1; }

                # -------------------------------
                # Test Case 2: Check HTTP Status Code
                # -------------------------------
                STATUS=$(curl -o /dev/null -s -w "%{http_code}" $BASE_URL)
                if [ "$STATUS" -ne 200 ]; then
                    echo "Failed: Expected 200, got $STATUS"
                    exit 1
                fi

                # -------------------------------
                # Test Case 3: Response Content Check
                # -------------------------------
                RESPONSE=$(curl -s $BASE_URL)
                echo "$RESPONSE" | grep -i "event" || {
                    echo "Failed: Expected keyword not found in response"
                    exit 1
                }

                # -------------------------------
                # Test Case 4: Port Check
                # -------------------------------
                netstat -tuln | grep 5000 || {
                    echo "Failed: Port 5000 not active"
                    exit 1
                }

                # -------------------------------
                # Test Case 5: Container Running Check
                # -------------------------------
                docker ps | grep event-registration-app || {
                    echo "Failed: Container not running"
                    exit 1
                }

                # -------------------------------
                # Test Case 6: API Endpoint Test (if exists)
                # -------------------------------
                curl -f $BASE_URL/api || echo "API endpoint not found (optional)"

                echo "All Advanced Test Cases Passed ✅"
                '''
            }
        }

    post {
        success {
            echo '✅ Build SUCCESS: Application deployed and tested successfully!'
        }
        failure {
            echo '❌ Build FAILED: Check logs for errors.'
        }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}