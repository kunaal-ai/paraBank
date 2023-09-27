pipeline {
    agent any

    triggers {
        cron('H/15 * * * *')
    }

    stages {
        stage ('build') {
            steps {
                echo "Hello Devops Engineers"
            }
        }
        stage ('test') {
            steps {
                echo "Hello Devops Engineers"
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
