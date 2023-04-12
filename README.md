# Certificate-maker-py-app-deployed-on-k8s-ingress-deployment
a python application deployed on Kubernetes ingress deployment to help user to create a certificate as it takes the name of the certified , organization and head signature then it creates the certificate for you

commands to run the project

1- kubectl apply -f kubernetes-ingress/ingress_all_requirements.yaml

2- kubectl apply -f kubernetes-ingress/Deployment.yaml

3- kubectl apply -f kubernetes-ingress/service.yaml

4- kubectl apply -f kubernetes-ingress/ingress.yaml

