from .Requests import Requests
from bs4 import BeautifulSoup

async def user_test_in_gitlab(user):
    url = "https://gitlab.com/{}".format(user)

    r = await Requests(url).get()

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        name = soup.find("h1", class_="gl-heading-1 gl-line-height-1 gl-mr-2 gl-my-0!")

        return {
            'name': name.text.strip()
        }

    else:
        return {
            'name': None
        }
