import requests
from bs4 import BeautifulSoup

def repo(ps: str = "user") -> str:
    """
    Web scraping function
    """
    url = requests.get(f"https://github.com/{ps}?tab=repositories")
    url_src = BeautifulSoup(url.text, "html.parser")
    repos = url_src.find("span", {"class": "Counter"}).attrs["title"]

    return repos