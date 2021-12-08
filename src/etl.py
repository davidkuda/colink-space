import datetime
import random

from colinkspace.postgres_connection import PostgresConnection
from colinkspace.backend import write_new_users, write_new_post
from colinkspace.data_quality_checker import DataQualityChecker
from utils.generate_mock_data import generate_random_users
from utils.utils import read_users_from_csv
from hacker_news_scraper.hacker_news_scraper import HackerNewsScraper


def main():
    # settings:
    number_of_random_users = 10
    days = 3
    posts_per_user = 3

    pg = PostgresConnection()
    generate_random_users(number_of_random_users)
    pg.init_tables()
    users = read_users_from_csv()

    write_new_users(users)
    DataQualityChecker.check_users_exist()

    spaces_and_owners = pg.execute_sql("SELECT space_id, user_id FROM space_owners;")

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
                write_new_post(post_data)

    DataQualityChecker.check_posts_of_user()


if __name__ == "__main__":
    main()
