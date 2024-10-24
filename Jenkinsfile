pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git 'https://github.com/abhishek0083/DevopsMiniProject1.git' // Change to your repository
            }
        }
       
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    bat 'docker build -t my-ecommerce-website .'
                }
            }
        }
        
        stage('Deploy Home Page') {
            steps {
                script {
                    // Deploy the Home page
                    bat 'docker stop my-ecommerce-home || exit 0'
                    bat 'docker rm my-ecommerce-home || exit 0'
                    bat 'docker run -d --name my-ecommerce-home -p 8081:80 my-ecommerce-website'
                }
            }
        }
        stage('Deploy About Page') {
            steps {
                script {
                    // Deploy the About page
                    bat 'docker stop my-ecommerce-about || exit 0'
                    bat 'docker rm my-ecommerce-about || exit 0'
                    bat 'docker run -d --name my-ecommerce-about -p 8082:80 my-ecommerce-website'
                }
            }
        }
        stage('Deploy Products Page') {
            steps {
                script {
                    // Deploy the Products page
                    bat 'docker stop my-ecommerce-products || exit 0'
                    bat 'docker rm my-ecommerce-products || exit 0'
                    bat 'docker run -d --name my-ecommerce-products -p 8083:80 my-ecommerce-website'
                }
            }
        }
        stage('Deploy Contact Page') {
            steps {
                script {
                    // Deploy the Contact page
                    bat 'docker stop my-ecommerce-contact || exit 0'
                    bat 'docker rm my-ecommerce-contact || exit 0'
                    bat 'docker run -d --name my-ecommerce-contact -p 8084:80 my-ecommerce-website'
                }
            }
        }
    }
    post {
        success {
            echo 'Deployment was successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
