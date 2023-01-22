# run psql install script
cd MarchHare/examples/db/install
helm repo add bitnami https://charts.bitnami.com/bitnami
bash install_db.sh
pip install -r MarchHare/examples/db/requirements.txt

# after connecting psql client, setup base database and job_meta table
(easy to execute in manual. scripting is hard)
bash MarchHare/examples/db/run_client.sh
(in postgres=# session)
CREATE DATABASE base;
CREATE TABLE IF NOT EXISTS job_meta (
	jobhash serial PRIMARY KEY,
	metric VARCHAR ( 50 ) UNIQUE NOT NULL,
	input VARCHAR ( 50 ) UNIQUE NOT NULL,
	output VARCHAR ( 255 ) UNIQUE NOT NULL,
	start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP  NOT NULL,
    node VARCHAR ( 50 ) NOT NULL
);
(exit session with ctrl_D)

# after setup, user can use db_util
export PYTHONPATH=$<path_to_marchhare/examples/db folder>:$PYTHONPATH
python -c "import db_util"

# useful informations
To accuire postgresql password, run command below
- kubectl get secret --namespace default database-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d

To accuire postgresql ip, run command below
- kubectl get pod database-postgresql-0 --template '{{.status.podIP}}'

