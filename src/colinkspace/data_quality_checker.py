from . postgres_connection import PostgresConnection


class DataQualityChecker:
    @staticmethod    
    def check_users_exist():
        pg = PostgresConnection()
        query = "SELECT COUNT(user_id) FROM users"
        users_count = pg.execute_sql(query)[0][0]
        if users_count == 0:
            print("WARNING: No users found!")
        else:
            print("Quality check passed: There are users in the database.")

    @staticmethod
    def check_posts_of_user():
        pg = PostgresConnection()
        user_id = pg.execute_sql("SELECT user_id FROM users LIMIT 1;")[0][0]
        posts = pg.execute_sql(f"SELECT * FROM posts WHERE user_id = '{user_id}';")
        if len(posts) < 1:
            print("WARNING: Users have no posts!")
        else:
            print("Quality check passed: Users have posts.")
