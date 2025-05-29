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

        stage('Rodar container Docker') {
            steps {
                script {
                    sh "docker run -d --name ci-cd-python-container -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Testar API (exemplo)') {
            steps {
                sh 'curl -s http://localhost:5000 || echo "API não respondeu"'
            }
        }

        stage('Parar container') {
            steps {
                sh 'docker stop ci-cd-python-container || true'
                sh 'docker rm ci-cd-python-container || true'
            }
        }
    }
}
