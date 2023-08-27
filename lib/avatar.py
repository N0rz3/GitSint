from .text import *
from .Requests import Requests
import os

async def scraper(name):
    api = f"https://api.github.com/users/{name}"

    req = await Requests(api).get()
   
    avatar = req.json()['avatar_url'] 
    return name, avatar 


async def downloader(name):
    name, avatar_url = await scraper(name)
    name_file = f"avatar_{name}.jpg"
    
    avatar_text = await Requests(avatar_url).get()
    avatar_text = avatar_text.content

    with open(name_file, "wb") as file:
        file.write(avatar_text)
        PATH = os.path.abspath(name_file)

        print(f"[+] Profile picture saved at: {italic(BLACK + PATH)}")