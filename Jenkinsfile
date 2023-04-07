pipeline {
  agent any
  stages {
    stage('set the environment') {
      steps {
        sh 'kubectl apply -f ./kubernetes-ingress/ingress_all_requirements.yaml'
      }
    }
    stage('set the deployment') {
      steps {
        sh 'kubectl apply -f ./kubernetes-ingress/Deployment.yaml'
        sh 'kubectl apply -f ./kubernetes-ingress/service.yaml'
      }
    }
    stage('set ingress') {
      steps {
        sh 'kubectl apply -f ./kubernetes-ingress/ingress.yaml'
      }
    }  
}
}