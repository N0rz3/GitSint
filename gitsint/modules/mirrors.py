from bs4 import BeautifulSoup
import requests

def miro(ps: str = "user") -> str: 
    """
    Web scraping function
    """
    url = requests.get(f"https://github.com/{ps}?tab=repositories&q=&type=mirror&language=&sort=")
    
    url_src = BeautifulSoup(url.text, "html.parser")
    url_body = url_src.find("div", {"class": "user-repo-search-results-summary TableObject-item TableObject-item--primary v-align-top"}).findAll("strong")
    url_body = url_body[0].text.strip()

    return url_body