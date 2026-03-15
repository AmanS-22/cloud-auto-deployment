pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AmanS-22/cloud-auto-deployment.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                pip3 install flask --break-system-packages
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd /var/lib/jenkins/workspace/cloud-auto-deploy

                echo "Stopping old app..."
                pkill -f app.py || true
                sleep 2

                echo "Starting new app..."
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
