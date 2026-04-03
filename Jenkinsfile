pipeline{

    agent any

    environment {
        IMAGE_NAME = "fastapi-app"
        CONTAINER_NAME = "fastapi-container"
    }

    stages{
        stage("Build"){
            steps{
                sh 'echo "Hello World from Build $IMAGE_NAME"'
            }
        }

        stage("Test"){
            steps{
                sh 'echo "Hello World from Test"'
            }
        }

        stage("Deploy"){
            steps{
                sh 'echo "Hello World from Deploy"'
            }
        }
    }
}