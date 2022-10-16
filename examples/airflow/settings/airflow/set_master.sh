
#you need cluster named default
export AIRFLOW_NAME="airflow-cluster"
export AIRFLOW_NAMESPACE="default"

## install using helm 3
helm install \
  "$AIRFLOW_NAME" \
  airflow-stable/airflow \
  --namespace "$AIRFLOW_NAMESPACE" \
  --values ./airflow_helm.yaml

kubectl port-forward svc/${AIRFLOW_NAME}-web 8080:8080 --namespace $AIRFLOW_NAMESPACE
