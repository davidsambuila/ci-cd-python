"""
---

### 8. `jenkins_pipeline.groovy` (exemplo básico para Jenkins Pipeline)

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/seu_usuario/seu_repositorio.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-mysql-app .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-mysql-app flask-mysql-app'
            }
        }
    }
}

"""