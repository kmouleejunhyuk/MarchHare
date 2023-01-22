# run psql install script
cd MarchHare/examples/db/install
bash install_db.sh

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



