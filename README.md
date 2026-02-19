pipeline {
    agent any
    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello World', description: 'Enter a message')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DARRURUSUPRAJA/exp1.git'
            }
        }
        stage('Print Parameter') {
            steps {
                echo "The message is: ${params.MESSAGE}"
            }
        }
        stage('Execute BAT') {
            steps {
                bat "echo Hello from Jenkins"
            }
        }
    }
}
