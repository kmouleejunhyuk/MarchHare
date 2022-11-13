** example how-to(based on linux) **  
1. install minikube by running bash `./minikube/install_ubuntu.sh`
2. modify airflow.extraVolumeMounts in examples/settings/airflow/airflow_helm.yaml
3. install helm by running bash `./minikube/install_helm.sh`
4. set cluster and install airflow by running `bash run_airflow.sh`