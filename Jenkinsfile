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
                echo "Stopping old Flask server..."
                pkill -f "python3 app.py" || true
        
                echo "Preparing deployment folder..."
                rm -rf ~/flask-app
                mkdir -p ~/flask-app
        
                echo "Copying new code..."
                cp -r * ~/flask-app
        
                echo "Starting new Flask server..."
                cd ~/flask-app
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
