pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi-app-auto-jenkins"
        CONTAINER_NAME = "fastapi-container"
    }

    stages {

        stage('Docker Build') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                docker stop %CONTAINER_NAME% || exit 0
                docker rm %CONTAINER_NAME% || exit 0
                docker run -d -p 8000:8000 --name %CONTAINER_NAME% %IMAGE_NAME%
                '''
            }
        }
    }
}