from typing import List

from . import postgres_connection
from utils.utils import create_random_uuid


def main():
    pass


def write_new_users(data: List[dict]) -> None:
    """Write new user to database.
    
    Args:
        data (List[dict]): A list of dicts with user data.
            expected format:
                {
                    "name": "foo",
                    "email": "bar@gmx.ch"
                }
    """
    pg = postgres_connection.PostgresConnection()
    cur = pg.conn.cursor()

    for user in data:
        
        # First check if email exists already
        table = "users"
        value = user["name"]
        query = f"SELECT exists (SELECT 1 FROM {table} WHERE name = '{value}' LIMIT 1);"    
        cur.execute(query)
        user_exists = cur.fetchone()[0]
        if user_exists:
            print("email was already registered, skipping")
            continue
        
        # Write to "users" table
        user_uuid = create_random_uuid()
        query = """
        INSERT INTO users (user_id, name, email)
        VALUES ((%s), (%s), (%s));
        """
        cur.execute(query, (user_uuid, user["name"], user["email"]))

        # Create a new default space for user
        space_uuid = create_random_uuid()
        query = """
        INSERT INTO users (user_id, name, email)
        VALUES ((%s), (%s), (%s));
        """
        cur.execute(query, (space_uuid, f'{user["name"]}\'s Personal Space', "2021-12-05"))

        # Make the user owner of the space
        query = "INSERT INTO space_owners (user_id, space_id) VALUES ((%s), (%s))"
        cur.execute(query, (user_uuid, space_uuid))

        # Commit transaction
        pg.conn.commit()
    
    cur.close()
    pg.conn.close()
