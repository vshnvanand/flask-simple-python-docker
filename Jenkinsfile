@Library("Shareit") _
pipeline {
    agent {label "babu"}

    stages {
        stage('cloning') {
            steps {
               script{
                   clone("https://github.com/vshnvanand/flask-simple-python-docker.git","main")
               }
            }
        }
        stage('build') {
            steps {
                script{
                    docker_build("flask-app","latest","vshnvanand")
                }
            }
        }
        stage('push'){
            steps {
                script{
                    
                    docker_push("flask-app","latest","vshnvanand")
                    
                }
            }
        }    
        stage('deploy') {
            steps {
                script{
                    docker_compose() 
                    echo "sab khatam everything done gone"
                }
            }
        }
    }
}
