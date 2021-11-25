import datetime
from pprint import pprint

import requests
from bs4 import BeautifulSoup


class HackerNewsScraper:
    """Each page on Hacker News has 30 links. This class represents such a page."""
    
    RESULTS_PER_PAGE = 30

    @staticmethod
    def main(days: int = 5):
        """Yields top 30 Hacker News links for every day since today - days.
        
        Args:
            days (int): How many days to go back.
        
        Yields:
            data (List[dict]):
                data = {
                    "link": link,
                    "description": description,
                    "score": score,
                    "date": date
                }
        """
        today = datetime.date.today()
        one_day = datetime.timedelta(1)
        yesterday = today - one_day

        for day in reversed(range(days)):
            delta = datetime.timedelta(day)
            date = today - delta
            hacker_news_page = HackerNewsScraper(date)
            links = hacker_news_page.scrape_links()
            yield from links


    def __init__(self, date: str = None):
        if date is None:
            date = datetime.date.today().__str__
        self.page_url = f"https://news.ycombinator.com/front?day={date}"
        self._page_content = requests.get(self.page_url).content
        self._soup = BeautifulSoup(self._page_content, "html.parser")
 
    def scrape_links(self):
        things = self._get_things()
        scores = self._get_scores()
        
        if len(things) != len(scores):
            print("Different num of things and scores!")
        
        date = self._get_date()
        links = []
        for i in range(self.RESULTS_PER_PAGE):
            thing = things[i]
            link_element = thing.find(class_="titlelink")
            link = link_element.get("href")
            description = link_element.string
            score = int(scores[i].string.split()[0])
            
            data = {
                "link": link,
                "description": description,
                "score": score,
                "date": date
            }
            
            links.append(data)
        
        return links

    def _get_date(self) -> str:
        """The date is the first word in the title."""
        date: str = self._soup.title.string.split()[0]
        return date
     
    def _get_things(self):
        """A link on HN is stored in an element with the class "athing"."""
        things = self._soup.find_all(class_="athing")
        return things
        
    def _get_scores(self):
        """The score of a link is stored in an element with the class "score"."""
        scores = self._soup.find_all(class_="score")
        return scores


if __name__ == "__main__":
    for links in HackerNewsScraper.main():
        pprint(links)
