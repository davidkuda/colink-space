import random
from pprint import pprint
import json

from hacker_news_scraper.hacker_news_scraper import HackerNewsScraper


PATH_HN_LINKS_CSV = "data/hacker_news_links.csv"
PATH_USERS_CSV = "data/users.csv"


def main():
    generate_random_users()
    # create_hacker_news_links_csv_file()
    # write_app_data_files(100)


def generate_random_users(number: int = 10) -> None:
    """Generates :arg:number random user data and writes to "data/users.csv"."""
    first_names = read_lines_of_file('data/first_names.txt')
    last_names = read_lines_of_file('data/last_names.txt')
    email_providers = ['protonmail.com', 'pm.me', 'gmail.com', 'bluewin.ch', 'gmx.ch']

    with open(PATH_USERS_CSV, 'w') as file:
        header = 'id,name,email\n'
        file.write(header)
        
        for i in range(number):
            first_name = random.choice(first_names).strip()
            last_name = random.choice(last_names).strip()
            name = f'{first_name} {last_name}'.strip()
            email = f'{first_name.lower()}.{last_name.lower()}@{random.choice(email_providers)}'

            data = [
                str(i),
                name,
                email
            ]
            
            line = ",".join(data) + "\n"

            file.write(line)


def create_hacker_news_links_csv_file(days: int = 20):
    """Parse hacker news and write links to a "data/hacker_news_links.csv"."""
    links = HackerNewsScraper.main(days)
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
    """Writes sample app data (json like dict) to "data/app_links/{filename}.json".
    
    100 files are 0.4mb in size. 1'000'000 files are 400 mb in size.
    
    Args:
        iterations (int): Define how many files that should be created.
    """
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
    """Opens a file and returns all lines as list."""
    with open(path, "r") as file:
        lines = file.readlines()
    return lines


if __name__ == "__main__":
    main()
