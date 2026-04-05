pipeline {
 agent any
 environment {
 DOCKER_IMAGE = " yourdockerhubusername/java-app:latest"   # INPUT REQUIRED (your DockerHub username)
 }
 stages {
 stage('Clone Repository') {
 steps {
 git branch: 'main',                                      # INPUT REQUIRED if your branch name is different
 url: 'https://github.com/your-reponame/simple-java-app.git'  # INPUT REQUIRED (your GitHub repo link)
 }
 }
 stage('Build with Maven') {
 steps {
 bat 'mvn clean package'
 }
 }
 stage('Build Docker Image') {
 steps {
 bat "docker build -t %DOCKER_IMAGE% ."
 }
 }
 stage('Push to DockerHub') {
 steps {
 withCredentials([usernamePassword(
 credentialsId: 'dockerhub-creds',                         # INPUT REQUIRED (Jenkins credential ID)
 usernameVariable: 'DOCKER_USER',
 passwordVariable: 'DOCKER_PASS'
 )]) {
 bat """
 docker login -u %DOCKER_USER% -p %DOCKER_PASS%
 docker push %DOCKER_IMAGE%
 """
 }
 }
 }
 stage('Deploy to Kubernetes') {
 steps {
 bat 'kubectl apply -f deployment.yaml'                    # INPUT REQUIRED if your YAML file name/path differs
 }
 }
 }
 post {
 success {
 echo 'CI/CD Pipeline executed successfully!'
 }
 failure {
 echo 'Pipeline failed. Please check logs.'
 }
 }
}
