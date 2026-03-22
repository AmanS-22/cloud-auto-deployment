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
                echo "Stopping old app..."
                pkill -f "python3 app.py" || true

                echo "Preparing deployment directory..."
                rm -rf /var/lib/jenkins/flask-app
                mkdir -p /var/lib/jenkins/flask-app

                echo "Copying latest code..."
                cp -r $WORKSPACE/* /var/lib/jenkins/flask-app/

                echo "Starting app..."
                cd /var/lib/jenkins/flask-app
                nohup python3 app.py > app.log 2>&1 &

                echo "Deployment done!"
                '''
            }
        }
    }
}
