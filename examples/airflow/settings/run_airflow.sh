minikube start --driver='docker' --profile='airflow' --kubernetes-version='stable' --nodes 3
helm install airflow airflow-stable/airflow --namespace default --values ./airflow/airflow_helm.yaml 

kubectl port-forward svc/airflow-web 8080:8080 --namespace default

# monitoring minikube
# in remote(linux server), run another terminal and run: minikube dashboard -p profile --url -> opens url(8080)
# in Local(labtop): ssh -L 12345:localhost:8080 user@remote-ip -> airflow dashboard
# in Local(labtop): ssh -L 11111:localhost:nnnn user@remote-ip -> minikube dashboard, nnnn is minikube dashboard port by random
# connect to: http://localhost:11111/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/pod?namespace=default
# connect to: http://localhost:12345