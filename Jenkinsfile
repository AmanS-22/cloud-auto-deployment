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
            echo "Stopping old app FORCEFULLY..."
            pkill -9 -f "python3 app.py" || true
            sleep 2
    
            echo "Cleaning deployment directory..."
            rm -rf /var/lib/jenkins/flask-app
            mkdir -p /var/lib/jenkins/flask-app
    
            echo "Copying latest code..."
            cp -r $WORKSPACE/* /var/lib/jenkins/flask-app/
    
            echo "Starting NEW app..."
            cd /var/lib/jenkins/flask-app
            nohup python3 app.py > app.log 2>&1 &
    
            echo "Deployment completed!"
            '''
        }
    }
    }
}
