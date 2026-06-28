from .Requests import Requests
from .utils.utils import Text_Manager as TM
from .utils.utils import Credentials
from .utils.utils import name_find
from .user import trackx
import uuid
import os

BLACK = TM.BLACK
WHITE = TM.WHITE

class Hunt_lightmod:
    async def hunt(email):
        api = "https://api.github.com/search/users?q={}".format(email)

        r = await Requests(api).get()
        TM("[~] 🎭 GitHub account tracking...").Tprint()

        if r.status_code == 200:
            try:
                items = r.json()['items']
                if not items:
                    exit(f"[-] 😔 {email} has not GitHub account.")

                username = items[0]['login']
                name = await name_find(username)

                if name:
                    print(f"[+] 🤙 Username => {username} ({name})")
                
                else:
                    print(f"[+] 🤙 Username => {username}")

                print()
                await trackx(username)

            except (KeyError, ValueError):
                exit("[-] JSON parsing error.")

class Hunt:
    def __init__(self, target: str) -> None:
        self.token = None
        self.user = None
        self.name = None
        self.succes = bool
        self.username = None
        self.repo = str(uuid.uuid1())
        self.email = target

    async def create_repo(self):
        self.success = False

        headers = {
            'authorization': f'token {self.token}'
        }

        data = {
            'name': self.repo,
            'private': True
        }

        r = await Requests("https://api.github.com/user/repos", headers=headers, json=data).post()

        if r.status_code == 201:
            TM("[+] 🎭 Creation of repo...").Tprint()  # creation private repo
            self.success = True

    async def commit(self):
        await self.create_repo()

        if self.success:
            headers = {
                "authorization": f'token {self.token}'
            }

            data = {
                "message": "commit",
                "committer": {
                    "name": "GitSint",
                    "email": self.email
                },
                "content": "R2l0U2ludA=="
            }

            TM("[+] 🎭 Spoofing...").Tprint()  # spoofing commit with the email provided in the data
            response = await Requests(f"https://api.github.com/repos/{self.user}/{self.repo}/contents/gitsint.txt", headers=headers, json=data).put()
            if response.status_code == 201:
                self.success = True

        else:
            exit()

    async def push(self):
        await self.commit()

        if self.success:
            headers = {
                'authorization': f'token {self.token}'
            }

            TM("[+] 🎭 Pushing...").Tprint()  # data push (email) of the falsified commit
            r = await Requests(f"https://api.github.com/repos/{self.user}/{self.repo}/commits", headers=headers).get()

            self.username = r.json()[0]['author']

            if not self.username:
                print(f"\n[-] 😔 {self.email} has not GitHub account.")

            else:
                name = await name_find(self.username['login'])

                if name:
                    print(f"\n[+] 🤙 Username => {self.username['login']} ({name})")

                else:
                    print(f"\n[+] 🤙 Username => {self.username['login']}")

        else:
            print("\n[!] Commit error.")

    async def delete(self):
        await self.push()

        headers = {
            'authorization': f'token {self.token}'
        }

        r = await Requests(f"https://api.github.com/repos/{self.user}/{self.repo}", headers=headers).delete()

        if r.status_code == 204:
            print(TM(f"[+] Repo deleted.").italic())  # delete private repo
        else:
            print("[-] Error while deleting the repo.")

        if self.username:
            print()
            await trackx(self.username['login'])
        else:
            pass

#######################################################################################

    async def login(self):
        self.name = None
        self.token = None

        while not self.name:
            self.name = input("\n[?] 🐱 Please enter your username (recommended to use this option with a secondary account): ")

        print(f"\n{BLACK}-> https://github.com/settings/tokens (check scopes of : repo, delete_repo, user:email){WHITE}")
        while not self.token:
            self.token = input("[?] 🔑 Please enter your token: ")

        await Credentials(username=self.name, token=self.token).check_scopes()

        with open("creds.txt", "w") as file:
            file.write(f"Name:{self.name}\nToken:{self.token}")
            path = os.path.abspath("creds.txt")

            print("\n[+] ✍️ Credentials saved!")

            print(TM(f"[+] Credentials path => {path}").italic())

    async def launch(self):
        try:
            with open("creds.txt", "r") as file:
                reads = file.read().splitlines()

            for read in reads:
                if "Name:" in read:
                    self.user = read.split(':')[1].strip()
                elif "Token:" in read:
                    self.token = read.split(':')[1].strip()

            if self.user and self.token:
                r = await Requests("https://api.github.com/octocat", headers={'Authorization': f'Bearer {self.token}','X-GitHub-Api-Version': '2022-11-28'}).get()
                if r.status_code == 200:
                    await self.delete()

                else:
                    print("[-] Token not valid please try creating one again.")
                    print("-> You have to log in / re-log in")

                    await self.login()

            else:
                print("[-] Credentials not found in file.")
                print("-> You have to log in / re-log in")

                await self.login()

        except FileNotFoundError:
            print("[-] Credentials file not found.")
            print("-> You have to log in / re-log in")

            await self.login()
