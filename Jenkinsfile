pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ci-cd-python-app"
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

        stage('Subir com Docker Compose') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }

        stage('Testar API (exemplo)') {
            steps {
                sh 'curl -s http://localhost:5000 || echo "API não respondeu"'
            }
        }
    }
}
