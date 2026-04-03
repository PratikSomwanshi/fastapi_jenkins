pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi-app-auto-jenkins"
    }

    stages {


        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true

                docker run -d -p 8000:8000 \
                  --name $IMAGE_NAME
                '''
            }
        }
    }
}