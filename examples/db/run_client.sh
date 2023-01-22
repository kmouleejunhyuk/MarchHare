export POSTGRES_PASSWORD=$(kubectl get secret --namespace default database-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)

export POSTGRES_IP=$(kubectl get pod database-postgresql-0 --template '{{.status.podIP}}')

kubectl run base-postgresql-client --rm --tty -i --restart='Never' --namespace default --image docker.io/bitnami/postgresql:15.1.0-debian-11-r12 --env="PGPASSWORD=$POSTGRES_PASSWORD" --command -- psql --host $POSTGRES_IP -U postgres -d postgres -p 5432

