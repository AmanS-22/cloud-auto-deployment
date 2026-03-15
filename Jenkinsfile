pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/AmanS-22/cloud-auto-deployment.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building application'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests'
            }
        }

stage('Deploy') {
    steps {
        sh '''
        cd /var/lib/jenkins/workspace/cloud-auto-deploy

        echo "Stopping old app if running..."
        pkill -f app.py || true

        echo "Starting new app..."
        nohup python3 app.py > app.log 2>&1 &
        '''
    }
}
    }
}
