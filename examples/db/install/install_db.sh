kubectl apply -f pv-volume.yaml
kubectl apply -f pv-claim.yaml
helm install --set primary.persistence.existingClaim="db-pvc" --set volumePermissions.enabled=true database my-repo/postgresql