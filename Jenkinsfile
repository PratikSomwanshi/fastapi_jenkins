pipeline {
    agent any

    stages {

        stage('Build & Deploy with Compose') {
            steps {
                bat '''
                docker compose down
                docker compose up -d --build
                '''
            }
        }

    }
}