pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        PATH = "/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin"
    }

    stages {
        stage('Checkout') {
            steps {

                git branch: 'main', url: 'https://github.com/nishant141114/jenkins-test-2.git'
            }
        }
        stage('Package Lambda') {
            steps {
                // Create the deployment package
                sh 'zip lambda_function.zip main.py'
            }
        }
        stage('Terraform Init') {
            steps {
                // new code ehdcbejfd hbd j
                sh '/opt/homebrew/bin/terraform init'
            }
        }
        stage('Terraform Apply') {
            steps {
                // Apply the Terraform configuration
                sh '/opt/homebrew/bin/terraform apply -auto-approve'
            }
        }
    }
    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
