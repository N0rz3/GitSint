import requests
from bs4 import BeautifulSoup
import utils

class close_friends:
    def __init__(self, target_username: str) -> str:

        self.target_username = target_username

        print("\n\n[~] Analyze potential(s) friend(s)...")
        followers_url = f"https://github.com/{target_username}?tab=followers"

        following_url = f"https://github.com/{target_username}?tab=following"

        def extract_usernames(url):
            usernames = []
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            for user in soup.find_all("span", {"class": "Link--primary"}):
                usernames.append(user.text.strip())
            return usernames

        followers_usernames = []
        page_num = 1
        while True:
            url = f"{followers_url}&page={page_num}"
            usernames = extract_usernames(url)
            if len(usernames) == 0:
                break
            followers_usernames.extend(usernames)
            page_num += 1

        following_usernames = []
        page_num = 1
        while True:
            url = f"{following_url}&page={page_num}"
            usernames = extract_usernames(url)
            if len(usernames) == 0:
                break
            following_usernames.extend(usernames)
            page_num += 1

        common_usernames = list(set(followers_usernames) & set(following_usernames))

        if len(common_usernames) != 0:
            print(f"\n{utils.Light_Red}> FRIENDS\n-------------------------------------{utils.Reset}")
            print(f"{utils.Light_Green}\n[+] {len(common_usernames) - 1} potential{'s' if len(common_usernames) - 1 > 1 else ''} friend{'s' if len(common_usernames) > 1 else ''} found !{utils.Reset}\n")
            print(f"Friend{'s' if len(common_usernames) > 1 else ''} list :")
            for username in common_usernames:
                print(f" - {username}")

        else:
            print("\n[-] No potential friend(s) were found.")