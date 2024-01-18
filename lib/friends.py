from .Requests import Requests
from utils.text import *
from utils.Print import *
from bs4 import BeautifulSoup

async def extract_usernames(url):
    usernames = []
    response = await Requests(url).get()
    soup = BeautifulSoup(response.text, "html.parser")
    for user in soup.find_all("span", {"class": "Link--primary"}):
        usernames.append(user.text.strip())
    return usernames

async def track(user):
    followers_url = f"https://github.com/{user}?tab=followers"
    following_url = f"https://github.com/{user}?tab=following"

    followers_usernames = await extract_all_usernames(followers_url)
    following_usernames = await extract_all_usernames(following_url)

    common_usernames = list(set(followers_usernames) & set(following_usernames))

    data = {
        'message': f'Potential friends found ({len(common_usernames) - 1}).',
        'friends': [{'name': username} for username in common_usernames if username.lower() != user.lower()]
    }

    return data

async def extract_all_usernames(url):
    usernames = []
    page_num = 1
    while True:
        page_url = f"{url}&page={page_num}"
        extracted_usernames = await extract_usernames(page_url)
        if len(extracted_usernames) == 0:
            break
        usernames.extend(extracted_usernames)
        page_num += 1
    return usernames

async def output(user):
    TempPrint("[+] Analyzing followers and followings...").Tprint()
    friends = await track(user)

    print(f"{RED}{user}{WHITE}")
    print(f"└──{friends['message']}")

    for friend in friends['friends']:
        if friend['name'] != "":   
            print(f"   ├──{friend['name']}")
