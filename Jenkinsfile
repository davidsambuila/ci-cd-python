pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ci-cd-python-app"
    }

    stages {
        stage('Clonar código') {
            steps {
                git 'https://github.com/davidsambuila/ci-cd-python.git'
            }
        }

        stage('Build imagem Docker') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }


        }

        stage('Run Tests') {
            steps {
                // Usa PYTHONPATH para que o pytest encontre o pacote `app`
                sh "docker exec ${CONTAINER_NAME} sh -c 'PYTHONPATH=. pytest tests/'"
            }
        }

        stage('Testar API (exemplo)') {
            steps {
                sh 'curl -s http://localhost:5000 || echo "API não respondeu"'
            }
        }
    }
}
