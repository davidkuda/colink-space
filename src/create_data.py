import random
from pprint import pprint
import json

from hacker_news_scraper.hacker_news_scraper import HackerNewsScraper


PATH_HN_LINKS_CSV = "data/hacker_news_links.csv"
PATH_USERS_CSV = "data/users.csv"


def create_hacker_news_links():
    """Parse hacker news and write links to a csv file."""
    links = HackerNewsScraper.main(20)
        
    path = PATH_HN_LINKS_CSV
    with open(path, "w") as file:
        header = "date,link,title,score\n"
        file.write(header)

        for data in links:
            date = data["date"]
            link = data["link"]
            description = data["description"]
            score = str(data["score"])
            line = ",".join([date, link, description, score]) + "\n"
            file.write(line)


def write_app_data_files(iterations: int) -> None:
    """Writes sample app data (json like dict) to a json file."""
    for iteration in range(iterations):
        data = create_app_links_data()
        data.update({"id": str(iteration)})
        data_as_json_str = json.dumps(data)

        file_name = f"app_data_{iteration}"
        file_path = f"data/app_links/{file_name}.json"

        with open(file_path, "w") as new_json_file:
            new_json_file.write(data_as_json_str)


def create_app_links_data() -> dict:
    """Generate sample links that will be written to the app database."""
    date, link, description = get_random_hn_link()
    data = {
        "user_id": get_random_user_id(),
        "date": date,
        "link": link,
        "description": description
    }
    return data


def get_random_user_id():
    users = read_lines_of_file(PATH_USERS_CSV)
    random_user = random.choice(users)
    id = random_user.split(",")[0]
    return id



def get_random_hn_link():
    """Get a random link from the hackernews links csv."""
    hn_links = read_lines_of_file(PATH_HN_LINKS_CSV)
    line = random.choice(hn_links).split(",")
    date = line[0]
    link = line[1]
    description = line[2]
    return date, link, description


def read_lines_of_file(path: str):
    with open(path, "r") as file:
        lines = file.readlines()
    return lines


if __name__ == "__main__":
    write_app_data_files(10)
