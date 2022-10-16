# install guide: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
# install as master node

# requirements: kubectl & bash 4.1+
    # add 
    # autoload -Uz compinit; \n compinit
    # to ~/.zshrc

    # install kubectl
    # curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    # sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl



curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start