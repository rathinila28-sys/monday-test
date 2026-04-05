pipeline {
 agent any
 tools {
 maven 'M3'                         # INPUT REQUIRED (must match Maven name configured in Jenkins)
 }
 stages {
 stage('Checkout Git') {
 steps {
 git branch: 'main',                # INPUT REQUIRED if your repo uses a different branch
 url: '<your-repository-url>'       # INPUT REQUIRED (your GitHub repository link)
 }
 }
 stage('Build and Test') {
 steps {
 bat 'mvn clean test'
 }
 }
 }
}
