from .Requests import Requests
from .objects import TempPrint
from .text import *


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