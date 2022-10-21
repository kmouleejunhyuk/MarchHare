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

