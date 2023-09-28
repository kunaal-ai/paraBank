pipeline {
    agent any
    triggers {
        cron('H/60 * * * *')
    }
    stages {
        stage ('checkout') {
            steps {
                echo "********   Checkout *********"
                git branch: 'main', url: 'https://github.com/kunaal-ai/paraBank.git'
                
            }
        }
        stage ('build') {
            steps {
                echo "*******  BUILD  **********"
                sh 'pip3 install -r requirements.txt'  
            }
        }
        stage ('test') {
            steps {
                echo "*********  TEST  ***********"
                
                script {
                    withCredentials([string(credentialsId: 'paraSoftUIPass', variable: 'PASSWORD')]) {
                        sh "PASSWORD=$PASSWORD python3 -m pytest tests"
                    }
                }    
            }
        }
    }

    post {
        always { 
            echo 'I will always say Hello again!'
        }
        success {
            echo 'I will say Hello only if job is success'
        }
        failure {
            echo 'I will say Hello only if job is failure'
        }
    }
}   