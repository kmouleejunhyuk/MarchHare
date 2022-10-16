# install guide: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
# install as master node

# requirements: bash 4.1+ & sudo

sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl

# kubelet, kubeadm, kubectl 1.22.6 버전 설치
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt install kubeadm kubectl kubelet
sudo apt-mark hold kubelet kubeadm kubectl

#minikube 설치
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start

# monitoring
# minikube dashboard -p profile --url -> opens url(8080)
# kubectl proxy --address='0.0.0.0' --disable-filter=true -> opens proxy(8001)
# in Local(labtop): ssh -L 12345:localhost:8001 user@remote-ip
# connect to: http://localhost:12345/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/pod?namespace=default