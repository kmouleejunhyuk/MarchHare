minikube start --driver='docker' --profile='airflow' --kubernetes-version='stable' --nodes 3
helm install airflow airflow-stable/airflow --namespace default --values ./airflow_helm.yaml 

# monitoring minikube
# minikube dashboard -p profile --url -> opens url(8080)
# in Local(labtop): ssh -L 12345:localhost:8080 user@remote-ip -> airflow dashboard
# in Local(labtop): ssh -L 11111:localhost:nnnn user@remote-ip -> minikube dashboard
# connect to: http://localhost:11111/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/pod?namespace=default
# connect to: http://localhost:12345