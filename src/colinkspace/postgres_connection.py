import psycopg2

from src.utils.main import parse_config_file


class PostgresConnection:
    def __init__(self, postgres_config = None):
        if postgres_config is None:
            postgres_config = parse_config_file()["POSTGRES"]
        self._postgres_config = postgres_config
        self.conn = self.connect_to_db()
    
    def connect_to_db(self):
        postgres_config = self._postgres_config
        conn = psycopg2.connect(
            host=postgres_config["HOST"],
            port=postgres_config["PORT"],
            user=postgres_config["USER"],
            password=postgres_config["PASSWORD"],
            database=postgres_config["DATABASE"]
        )
        return conn

    def execute_sql(self, query: str, data: list):
        cur = self.conn.cursor()
        cur.execute(query, data)
        self.conn.commit()
        cur.close()

    def process_frontend_input():
        pass
