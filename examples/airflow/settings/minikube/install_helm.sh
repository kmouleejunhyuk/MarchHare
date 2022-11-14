
#install helm
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
bash get_helm.sh

#install airflow via helm
helm repo add airflow-stable https://airflow-helm.github.io/charts