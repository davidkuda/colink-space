import datetime
import random
from pprint import pprint

from colinkspace.postgres_connection import PostgresConnection
from colinkspace.backend import write_new_users
from utils.generate_mock_data import generate_random_users
from hacker_news_scraper.hacker_news_scraper import HackerNewsScraper


def main():
    pg = PostgresConnection()
    generate_random_users(10)
    pg.init_tables()
    users = read_users_from_csv()
    write_new_users(users)

    spaces_and_owners = pg.execute_sql("SELECT * FROM space_owners;")

    days = 3
    posts_per_user = 3

    for day in reversed(range(days)):
        today = datetime.date.today()
        delta = datetime.timedelta(day)
        date = today - delta
        hacker_news_data = HackerNewsScraper(date).links

        for space_and_owner in spaces_and_owners:
            for i in range(posts_per_user):
                random_hn_link = random.choice(hacker_news_data)
                post_data = {
                    "link": random_hn_link["link"],
                    "description": random_hn_link["description"],
                    "date": date,
                    "space_id": space_and_owner[0],
                    "user_id": space_and_owner[1],
                }
                pprint(post_data)

    # join and see which user has most shares
    # join and see which links was shared most


def read_users_from_csv():
    PATH_USERS_CSV = "data/users.csv"
    users = []
    with open(PATH_USERS_CSV, "r") as file:
        headers = file.readline()
        for line in file:
            name, email = line.strip().split(",")
            users.append({"name": name, "email": email})
    return users


if __name__ == "__main__":
    main()
