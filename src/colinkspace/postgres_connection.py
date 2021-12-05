import psycopg2

from utils.utils import parse_config_file


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

    def execute_sql(self, query: str):
        cur = self.conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        self.conn.commit()
        cur.close()

    def process_new_post_from_frontend(post_data: dict):
        """Writes data from the frontend to the database.
        
        Expected input:
        
            {
                "user_id": "625",
                "space_id": "890",
                "date": "2021-11-06",
                "link": "https://blog.racket-lang.org/2021/11/racket-v8-3.html",
                "description": "Racket v8.3"
            }
        
        Write the data to two relational tables:
            links:
                Fetch meta data from link such as title and description 
                and store in database
            posts: Every user is generating a post
        """
        query = f"""
        INSERT INTO posts
        
        """
