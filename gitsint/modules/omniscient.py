import requests, time
import utils

class xrai:
    def __init__(self, username: str):

        self.username = username

        url = utils.api_commits(username)

        response = requests.get(url)

        if response.status_code != 200:
            print("Error")
            exit()

        pseudos = {}

        data = response.json()

        for commit in data:
            if commit["type"] == "PushEvent":
                commits = commit["payload"]["commits"]
                for c in commits:
                    pseudo = c["author"]["name"]
                    if pseudo in pseudos:
                        pseudos[pseudo] += 1
                    else:
                        pseudos[pseudo] = 1

        if len(pseudos) > 0:
            print(f"\n[OMINISCIENT] Related name{'s' if len(pseudo) > 1 else ''} to account :")
            for pseudo, count in pseudos.items():
                print(f" - {pseudo} (found in {count} commit{'s' if count > 1 else ''})")
        else:
            print("[-] There is no username linked to the account.")



    def spoof(username: str) -> str:
        target_username = username

        url = utils.api_searchs(target_username)

        response = requests.get(url)

        if response.ok:
            users = response.json()["items"]
            num_users = len(users)

            print("[OMINISCIENT] Spoofing...")
            time.sleep(1)
            if num_users != 1:
                print(f"{utils.Light_Green}\n[OMINISCIENT] [+] User{'s' if num_users > 1 else ''} were found with the same name as the target account !{utils.Reset}\n")
                for user in users:
                    username = user["login"]
                    if username != target_username and target_username in username:
                        print(f"- {username}")
            else:
                print("[-] There is no user with the same username.")
        else:
            print(f"Error : {response.status_code}")