#!/bin/zsh
# install guide: https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/
# install as master node

# requirements: Homebrew & zsh & sudo & kubelet & kubectl
    # add 
    # autoload -Uz compinit; \n compinit
    # to ~/.zshrc

brew install kubectl

source <(kubectl completion zsh)

brew install minikube
brew install --cask docker
kubectl cluster-info dump

# after this:
    # run docker desktop(or run docker by systemctl)
    # kubectl cluster-info
    # add alias kubectl="minikube kubectl --"
    # minikube start
    # minikube webserver
