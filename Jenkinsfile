@Library("Shareit") _
pipeline {
    agent {label "vinod"}

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
                    echo "Hello-World"
                    docker_push("flask-app","latest","vshnvanand")
                    echo "World gone"
                }
            }
        }    
        stage('deploy') {
            steps {
                script{
                    docker_compose() 
                }
            }
        }
    }
}
