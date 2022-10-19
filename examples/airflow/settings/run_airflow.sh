minikube start --driver='docker' --profile='airflow-demo'  --cni='calico' --kubernetes-version='stable' --nodes 3 
helm install airflow airflow-stable/airflow --namespace default --values ./airflow_helm.yaml 

# monitoring minikube
# minikube dashboard -p profile --url -> opens url(8080)
# kubectl proxy --address='0.0.0.0' --disable-filter=true -> opens proxy(8001)
# in Local(labtop): ssh -L 12345:localhost:8001 user@remote-ip
# connect to: http://localhost:12345/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/pod?namespace=default