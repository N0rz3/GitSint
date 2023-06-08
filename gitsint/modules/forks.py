import requests
from bs4 import BeautifulSoup

def search(ps: str) -> str:
    forks = requests.get(f"https://github.com/{ps}?tab=repositories&q=&type=fork&language=&sort=")


    forks_src = BeautifulSoup(forks.text, "html.parser")
    info = forks_src.find("div", {"class": "user-repo-search-results-summary TableObject-item TableObject-item--primary v-align-top"}).findAll("strong")
    info = info[0].text.strip()

    return info