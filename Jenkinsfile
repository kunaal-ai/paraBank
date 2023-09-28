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
            mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "PASS CI: Project name -> ${env.JOB_NAME}", to: "kunaal.qaengineer@gmail.com";  

        }
        failure {
            mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "kunaal.qaengineer@gmail.com";  

        }
    }
}   