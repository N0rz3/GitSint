import time
import shutil
import subprocess
import tempfile
from pathlib import Path
import os
import stat
from bs4 import BeautifulSoup
from lib.Requests import *

class Text_Manager:
    def __init__(self, text: str, time: int=3) -> None:
        self.text = text
        self.time = time

    # all colors used
    RED = "\033[31m"
    WHITE = "\033[0m"
    GREEN = "\033[38;2;0;201;87m"
    PURPLE = "\033[38;2;171;130;255m"
    BLACK = "\033[38;2;89;89;89m"
    CYAN = "\033[36m"

    def italic(self):
        ITALIC = "\033[3m" + self.text + "\033[0m"
        return ITALIC

    def no_letters(self):
        digits = "".join(filter(str.isdigit, self.text))
        return digits

    def Tprint(self):
        print(self.text, end="", flush=True)
        time.sleep(self.time)
        print("\r" + " " * (len(self.text) + 1) + "\r", end="", flush=True)

class Keys:
    def __init__(self, target: str) -> None:
        self.targ = target

    async def key_recoverer(self):
        r = await Requests(url=f"https://github.com/{self.targ}.keys").get()

        lines = r.text.strip().split('\n')

        if lines:
            ssh_rsa_count = sum("ssh-rsa" in line for line in lines)
            return ssh_rsa_count

        else:
            pass

class Credentials:
    def __init__(self, username:str, token:str) -> None:
        self.u = username
        self.t = token

    async def check_token(self):
        api_test_valid = "https://api.github.com/octocat"  

        headers = {
            'Authorization': f'Bearer {self.t}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

        r = await Requests(api_test_valid, headers=headers).get()
        status = r.status_code

        status_dict = {
            200: '[+] Token valid.',
            401: '[-] Token not valid please try creating one again.',
            403: '[-] Rate limit try again later...'
        }

        for key, value in status_dict.items():
            if key == status:
                if key != 200:
                    exit("\n" + value)
                else:
                    print("\n" + value)
                    break

    async def check_scopes(self):
        await self.check_token()

        api = "https://api.github.com"

        headers = {"Authorization": f"token {self.t}"}

        r = await Requests(url=api, headers=headers).get()
 
        oauth_scopes = r.headers.get("x-oauth-scopes", "")
        oauth_scopes = str(oauth_scopes).split(",")
        oauth_scopes = [scope.strip() for scope in oauth_scopes]

        scopes_list = [
            'repo',
            'delete_repo',
            'user:email'
        ]

        print("\n[+] 🎯 The scopes presents => " + ', '.join(oauth_scopes))
        if all(scope in oauth_scopes for scope in scopes_list):
            print("[+] 🎯 The scopes (repo, delete_repo, user:email) are present in the token.")

        else:
            exit("[-] 🎯 The scopes (repo, delete_repo, user:email) are not present in the token.")

class GitEngine:
    async def get_all_repositories(user):
        repos = []
        page = 1

        while True:
            r = await Requests(f"https://api.github.com/users/{user}/repos?per_page=100&page={page}").get()
            data = r.json()

            if not isinstance(data, list) or not data:
                break

            repos.extend(data)

            if len(data) < 100:
                break

            page += 1
        return repos

    def clone_repository(url):
        temp_dir = tempfile.mkdtemp(
            prefix="repo_",
            dir=TMP_DIR
        )

        try:
            cmd = ["git", "clone", "--quiet"]
            cmd += ["--depth", "1"]
            cmd += [url, temp_dir]

            subprocess.run(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )

            return temp_dir

        except Exception:
            shutil.rmtree(temp_dir, ignore_errors=True)
            return None

    def extract_history(repo_path):
        try:
            result = subprocess.check_output(
                [
                    "git",
                    "-C",
                    repo_path,
                    "log",
                    "--all",
                    "--format=%an|%ae"
                ],
                text=True,
                stderr=subprocess.DEVNULL
            )
            return result.splitlines()

        except Exception:
            return []

        finally:
            shutil.rmtree(repo_path, ignore_errors=True)

async def name_find(username: str):
    url = f"https://github.com/{username}"

    req = await Requests(url).get()

    soup = BeautifulSoup(req.text, 'html.parser')
    name = soup.find("span", {"class": "p-name vcard-fullname d-block overflow-hidden"})

    if name != None:
        _name = name.text.strip()
        if _name != '':
            return _name
        else:
            return None
    else:
        return None

TMP_DIR = Path(tempfile.gettempdir()) / "trackx"
TMP_DIR.mkdir(parents=True, exist_ok=True)

def change_permissions(path):
    if not path.exists():
        return

    for root, dirs, files in os.walk(path):
        for d in dirs:
            try:
                os.chmod(os.path.join(root, d), stat.S_IWRITE)
            except Exception:
                pass

        for f in files:
            try:
                os.chmod(os.path.join(root, f), stat.S_IWRITE)
            except Exception:
                pass

def delete_tmp_dir():
    if not TMP_DIR.exists():
        return

    change_permissions(TMP_DIR)
    shutil.rmtree(TMP_DIR, ignore_errors=True)
