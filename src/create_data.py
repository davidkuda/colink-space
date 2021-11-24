from pprint import pprint

from hacker_news_scraper.hacker_news_scraper import HackerNewsScraper


def create_links():
    links = HackerNewsScraper.main(20)
        
    path = "data/links.csv"
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


def write_links_to_csv_file(path: str):
    pass


if __name__ == "__main__":
    create_links()
    