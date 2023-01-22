import psycopg2
from loguru import logger
NOCONN_MSG = "no connection exists in this session"


class dbsession(object):
    def __init__(self):
        self.conn = None

    def get_conn_info(self):
        assert self.conn is not None, NOCONN_MSG
        # create a cursor
        cur = self.conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        cur.close()

    def connect(self, password: str, ip: str, user: str, dbname: str, verbose: bool = False) -> None:
        assert self.conn is None, "Connection with this session already exists"
        try:
            conn = psycopg2.connect(
                host=ip,
                database=dbname,
                user=user,
                password=password)

            self.conn = conn
            logger.info("DB connected")

            if verbose:
                self.get_conn_info()

        except (Exception, psycopg2.DatabaseError) as e:
            logger.error("DB not connected")
            logger.error(e)
            self.connected = False

    def disconnect(self) -> None:
        assert self.conn is not None, NOCONN_MSG
        self.conn.close()
        self.conn = None
        logger.info("Connection disabled")

    def insert_job_info(self, jobinfos, table_name="job_info") -> list:
        '''
        jobinfo: list of [(metric, input, output, start_time, end_time, node)...]
        '''
        assert self.conn is not None, NOCONN_MSG
        conn = self.conn

        try:
            cur = conn.cursor()
            infostring = ','.join(jobinfos)
            sql = f"INSERT INTO {table_name} VALUES({infostring}) RETURNING jobhash;"

            jobhash = cur.execute(sql)
            conn.commit()
            cur.close()
            return jobhash

        except (Exception, psycopg2.DatabaseError) as error:
            logger.info(error)
            return None

    def exec(self, sql):
        assert self.conn is not None, NOCONN_MSG
        conn = self.conn

        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            logger.info(error)
