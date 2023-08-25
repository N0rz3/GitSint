from .Requests import Requests
from .objects import TempPrint
from .text import *
import uuid

class Light:
    async def hunt(email):
        api = "https://api.github.com/search/users?q={}".format(email)

        r = await Requests(api).get()
        TempPrint("[~] GitHub account tracking...").Tprint()

        if r.status_code == 200:
            try:
                items = r.json()['items']
                if not items:
                    print("[-] Email provided seems to not have a github account.")
                    exit()

                name = items[0]['login']

                TempPrint(f"{GREEN}[+] Account found !{WHITE}").Tprint()
                print(f"[+] Username => {name}")
                exit()

            except (KeyError, ValueError):
                print("[-] JSON parsing error.")
                exit()


class Basic:
    async def create_repo(token):
        repo = str(uuid.uuid1())

        headers = {
            'authorization': f'token {token}'
        }

        data = {
            'name': repo,
            'private': True
        }

        r = await Requests("https://api.github.com/user/repos", headers=headers, json=data).post()

        if r.status_code == 201:
            TempPrint("[+] Creation of repo...").Tprint()
            success = True
        
        return success, repo
  
    async def commit(token, user, email):
        success, repo = await Basic.create_repo(token)

        if success:
            headers = {
                "authorization": f'token {token}'
            }

            data = {
                "message": "commit",
                "committer": {
                    "name": "GitSint",
                    "email": email
                },
                "content": "R2l0U2ludA=="
            }

            response = await Requests(f"https://api.github.com/repos/{user}/{repo}/contents/gitsint.txt", headers=headers, json=data).put()
            if response.status_code == 201:
                success = True

            return success, repo
        
        else:
            exit()

    async def push(token, user, email):
            success, repo = await Basic.commit(token, user, email)

            if success:
                headers = {
                    'authorization': f'token {token}'
                }

                TempPrint("[+] Pushing...").Tprint()
                r = await Requests(f"https://api.github.com/repos/{user}/{repo}/commits", headers=headers).get()

                try:
                            TempPrint(f"{GREEN}[+] Account found !{WHITE}").Tprint()
                            name = "\n[+] Username => " + r.json()[0]['author']['login']
                except (KeyError, ValueError):
                            name = "\n[-] Push error." # rare result

                print(name)

                return repo

            else:
                exit("\n[!] Commit error.")

    async def delete(token, user, email):
        repos = await Basic.push(token, user, email)

        headers = {
            'authorization': f'token {token}'
        }

        r = await Requests(f"https://api.github.com/repos/{user}/{repos}", headers=headers).delete()

        if r.status_code == 204:
            print(italic("[+] Repo deleted."))
        else:
            print("[-] Error while deleting the repo.")

#################################################################################

    def login():
        name = input("\n[?] Please enter your username: ")

        print(italic(f"\n-> {BLACK}https://github.com/settings/tokens (check the options of repo, delete_repo, user:email){WHITE}"))
        token = input("[?] Please enter your token: ")

        with open("creads.txt", "w") as file:
            file.write("Name:" + name + "\n" + "Token:" + token)
            exit(f"{GREEN}[+] Creads saved!{WHITE}")       

    async def launch(email):
        try:
            with open("creads.txt", "r") as file:
                reads = file.read().split('\n')

            user = None
            token = None

            for read in reads:
                if "Name:" in read:
                    user = read.split(':')[1].strip()
                elif "Token:" in read:
                    token = read.split(':')[1].strip()

            if user and token:
                await Basic.delete(token, user, email)
            else:
                print("[-] Username and/or token not found in the file.")

        except FileNotFoundError:
            print("[-] Please log in.")