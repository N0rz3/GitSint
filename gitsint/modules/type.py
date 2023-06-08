from bs4 import BeautifulSoup
import requests

def types(ps: str = "user") -> str: 
    """
    Web scraping function
    """
    url = requests.get(f"https://github.com/{ps}")
    
    url_src = BeautifulSoup(url.text, "html.parser")
    url_body = url_src.find("span", title="Label: Pro")

    if url_body != None:
        url_body = url_body.text.strip()
        urlb = f"Highlights : {url_body} "
    elif url_body == None:
        urlb = "Highlights : null"
    

    return urlb