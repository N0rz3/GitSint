from utils.text import *
from .Requests import Requests
import json

class Version:
    def version():
        with open('config.json', 'r') as json_file:
            j = json.load(json_file)

            v = j['version']

            print(f"[+] Your version is: " + v)

            return v

    async def check_update():
        v = Version.version()

        r = await Requests("https://raw.githubusercontent.com/N0rz3/GitSint/master/config.json").get()

        file = json.load(r)
        v_ = file['version']

        if v != v_:
            print(f"\n[-] Your version isn't up to date")
            print(f"[~] You are advised to reinstall the tool\n=> https://github.com/N0rz3/GitSint")

        else:
            print(italic(f"\n[+] Your version is up to date"))
