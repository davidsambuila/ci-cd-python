pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ci-cd-python-app"
        CONTAINER_NAME = "ci-cd-python-container"
    }

    stages {
        stage('Clonar código') {
            steps {
                git branch: 'main', url: 'https://github.com/davidsambuila/ci-cd-python.git'
            }
        }

        stage('Build imagem Docker') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Parar e remover container existente') {
            steps {
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Rodar container Docker') {
            steps {
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${DOCKER_IMAGE}"
            }
        }

        stage('Testar API (exemplo)') {
            steps {
                sh 'curl -s http://localhost:5000 || echo "API não respondeu"'
            }
        }
    }
}
