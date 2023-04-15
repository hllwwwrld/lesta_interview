import psycopg2


class Connections:
    def __init__(self, config):
        # connection to postgres db and creating cursor
        # connection based on given_config
        self.conn_db = psycopg2.connect(database=config.get('db_conn', 'database'),
                                        user=config.get('db_conn', 'user'),
                                        password=config.get('db_conn', 'password'),
                                        host=config.get('db_conn', 'host'),
                                        port=config.get('db_conn', 'port'))
        self.cursor = self.conn_db.cursor()
