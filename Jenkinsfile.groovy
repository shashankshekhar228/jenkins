pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/shashankshekhar228/jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x addition.py"
                sh "python3 addition.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "chmod u+x test1.py"
                sh "python3 test1.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "chmod u+x test2.py"
                sh "python3 test2.py"
            }
        }
    } 
}