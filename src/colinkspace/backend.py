from typing import List

from linkpreview import link_preview

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


def write_new_post(data: dict):
    """Write a post from a user to database.
    
    Args:
        data (dict):
            {
                "link": "str",
                "description": "str",
                "date": "yyyy-mm-dd",
                "space_id": "uuid",
                "user_id": "uuid"
            }
    """
    pg = postgres_connection.PostgresConnection()
    cur = pg.conn.cursor()

    # check if link is already in db
    link = data["link"]
    query = f"SELECT link_id FROM links WHERE url = '{data['link']}';"
    cur.execute(query)
    
    link_uuid = cur.fetchone()
    
    if link_uuid is None:
        link_uuid = create_random_uuid()
        # parse link
        preview = link_preview(link)

        # write link
        query = f"""
        INSERT INTO links 
        (link_id, url, title, description, image_url)
        VALUES ((%s), (%s), (%s), (%s), (%s))"""
        cur.execute(query, (link_uuid, link, preview.title, 
                            preview.description, preview.image))
    
    # Write post
    post_uuid = create_random_uuid()

    query = """
    INSERT INTO posts (
        post_id,
        link_id,
        space_id,
        user_id,
        description,
        date
    )
    VALUES ((%s), (%s), (%s), (%s), (%s), (%s))
    """
    
    cur.execute(query, (
        post_uuid,
        link_uuid,
        data["space_id"],
        data["user_id"],
        data["description"],
        data["date"]
    ))
