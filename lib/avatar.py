from .utils.utils import Text_Manager
from .Requests import Requests
import os

BLACK = Text_Manager.BLACK

class Avatar_Scraper:
    def __init__(self, name: str) -> None:
        self.name = name

    async def scraper(self):
        api = f"https://api.github.com/users/{self.name}"

        req = await Requests(url=api).get()
    
        self.avatar = req.json()['avatar_url'] 

    async def downloader(self):
        await self.scraper()

        directory = "avatars"
        if not os.path.exists(directory):
            os.makedirs(directory)

        PATH = os.path.join(directory, f"{self.name}.jpg")

        avatar_response = await Requests(url=self.avatar).get()

        if avatar_response.status_code == 200:
            avatar_content = avatar_response.content

            with open(PATH, "wb") as file:
                file.write(avatar_content)
                PATH = os.path.abspath(PATH)

                print(f"[+] ✍️ Profile picture saved at: {Text_Manager(BLACK + PATH).italic()}")
        else:
            print(f"[-] Failed to download profile picture. Status Code: {avatar_response.status_code}")
