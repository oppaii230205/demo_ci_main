pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.10"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/oppaii230205/demo_ci_main'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 --version
                python3 -m venv venv
                . venv/bin/activate
                python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                pip install ruff pytest coverage
                '''
            }
        }

        stage('Lint with Ruff') {
            steps {
                // Giống continue-on-error của GitHub Actions
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh '''
                    . venv/bin/activate
                    ruff check . --output-format=github --target-version=py310
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                coverage run -m pytest -v -s
                '''
            }
        }

        stage('Coverage Report') {
            steps {
                sh '''
                . venv/bin/activate
                coverage report -m
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'Build SUCCESS'
        }
        failure {
            echo 'Build FAILED'
        }
    }
}