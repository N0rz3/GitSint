import requests
import json
import random
import os
import time
import argparse
from tqdm import tqdm
from modules import git_src, repos, archived, mirrors, templates, type, languages_stats, friends, omniscient, organizations, sniffer, forks
import utils


class Core:
    def maincore():
        global DEBUG
        os.system("cls && title GitSint v0.0.5 By Norze " if os.name == "nt" else "clear")
        banner = f"""
 _____ _  _____  ____  _  _      _____ 
/  __// \/__ __\/ ___\/ \/ \  /|/__ __\\
| |  _| |  / \  |    \| || |\ ||  / \  
| |_//| |  | |  \___ || || | \||  | |  
\____\\\_/  \_/  \____/\_/\_/  \|  \_/  
                                       
BY 🦊 Norze (GitSint v0.0.5){utils.Black}
🔥 subscribe to my github account !{utils.Reset}                                                                                                            
                                                                                           """

        print(banner)

        # command for launch
        parser = argparse.ArgumentParser(description='Find account information')
        parser.add_argument('username', help='<username>')
        parser.add_argument('--JSON', action='store_true', help='Export the data in JSON format')

        args = parser.parse_args()
        ps = args.username

        # ps = pseudo

        time.sleep(2)
        response = requests.get(utils.api_user(ps))

        if response.status_code == 200:
            """
            Main code core 
            """
            DEBUG = True
            print(f"\n\nDebug : {DEBUG}")
            data = json.loads(response.text)

            fork = forks.search(ps)
            source = git_src.source(ps)
            reposs = repos.repo(ps)
            archive = archived.arch(ps)
            miros = mirrors.miro(ps)
            temp = templates.temp(ps)

            for i in tqdm(range(int(9e6))):
                pass
            print(utils.Reset + f"""\n        
{utils.Yellow}[!] 🔍 Profile github scraped !

{utils.Light_Red}> ACCOUNT
-------------------------------------

{utils.Light_Green}> {utils.Reset}Identifiers:
Username: {data['login']}
Name: {data['name']}
ID: {data['id']}

{utils.Light_Green}> {utils.Reset}Social:
Twitter: @{data['twitter_username']}

{utils.Light_Green}> {utils.Reset}Details:
Location: {data['location']}
Biography: {data['bio']}

{utils.Light_Green}> {utils.Reset}Avatar:
{data['avatar_url']}

{utils.Light_Green}> {utils.Reset}Status:
Site Admin: {data['site_admin']}
Type: {data['type']}
{type.types(ps)}
Hireable: {data['hireable']}

{utils.Light_Green}> {utils.Reset}Stats:
Public repos: {data['public_repos']}
Followers: {data['followers']}
Following: {data['following']}
Gists: {data['public_gists']}

{utils.Light_Green}> {utils.Reset}Account
Account created: {data['created_at'].replace("-", "/").replace("T", " ").replace("Z", "")} 🌐 (UTC)
Last account update: {data['updated_at'].replace("-", "/").replace("T", " ").replace("Z", "")} 🌐 (UTC)\n""")

            for i in tqdm(range(int(9e6))):
                pass
            print(f"""
{utils.Light_Red}> REPOSITORIES STATS
-------------------------------------{utils.Reset}

{utils.Light_Green}[+] {reposs} repositories ({source} source{'s' if int(source) > 1 else ''}, {fork} fork{'s' if int(fork) > 1 else ''}, {archive} archived, {miros} mirror{'s' if int(miros) > 1 else ''}, {temp} template{'s' if int(temp) > 1 else ''}){utils.Reset}
  """)
            languages_stats.percentage(ps)

            print("\n\n")
            for i in tqdm(range(int(9e6))):
                pass
            organizations.orgz(username=ps)
            friends.close_friends(target_username=ps)

            variant = ps.replace("0", "o").replace("3", "e").replace("1", "i").replace(" ", "").replace("4", "a").replace("9", "").replace("5", "").replace("6", "").replace(" ", "").replace("7", "").replace("8", "")
            variation = ps.replace("c", "s").replace(" ", "").replace("3", "").replace("0", "o").replace("off", "") + "y"

            if data['name'] != None:
                va = ", " + data['name'].replace("0", "o").replace("3", "e").replace("1", "i").replace(" ", "").replace("4", "a").replace("9", "").replace("5", "").replace("6", "").replace(" ", "").replace("7", "").replace("8", "").upper()
            if data['name'] == None:
                va = ""
            if data['twitter_username'] != None:
                tw = f"'{data['twitter_username']}',"
            if data['twitter_username'] == None:
                tw = ""

            if data['name'] is not None:
                na = f"'{data['name']}'"
            if data['name'] == None:
                na = ""

            for i in tqdm(range(int(9e6))):
                pass
            print(f"""\n
{utils.Light_Red}> HIDDEN IDENTITY
-------------------------------------{utils.Reset}

[~] Possibles usernames variations -> {variation}, {variant}{va}
""")
            omniscient.commit.spoof(username=ps)
            if sniffer.name(ps):
                name = sniffer.name(ps).replace("@protonmail.ch", "").replace("@gmail.com", "").replace("@outlook.com", "").replace("@foxmail.com", "").replace("@hotmail.com", "").replace("@protonmail.com", "")
            else:
                name = ""
            print(f"""
{sniffer.search(ps)}
[~] History of names used :""")
            omniscient.commit(username=ps)
            print(f"""
[~] The target uses these names [{tw} {na}, '{data['login']}', '{name}']\n""")

            if name != "":
                print(f"""
Email that corresponds to the target => {sniffer.name(ps)}          
             """)
            {sniffer.mails(ps)}
            print(f"""
[~] Potentials emails were generated from the nickname and variations !

[?] {data['login'] + "@" + random.choice(utils.domain_list)} -> @{data['login']}
[?] {ps + "@" + random.choice(utils.domain_list)} -> @{ps}
[?] {ps.replace(" ", "").upper() + "@" + random.choice(utils.domain_list)} -> @{ps}
[?] {ps.replace(" ", "").upper().replace("3", "e").replace("1", "i").replace("8", "B").replace("0", "o") + "@" + random.choice(utils.domain_list)} -> @{ps}
[?] {ps + ps + "@" + random.choice(utils.domain_list)} -> @{ps}
{sniffer.mail(ps)}
  """)
            if data['name'] != None:
                print(f"""[?] {data['name'] + data['name'] + "@" + random.choice(utils.domain_list)} -> @{data['name']}
[?] {data['login'] + data['name'] + "@" + random.choice(utils.domain_list)} -> @{data['login']}
[?] {data['name'] + "@" + random.choice(utils.domain_list)} -> @{data['name']}
[?] {data['name'].replace("e", "3").replace("i", "1").replace("E", "3").replace("I", "1").replace(" ", "").replace("A", "4").replace("a", "4").replace("b", "8").replace("B", "8") + "@" + random.choice(utils.domain_list)} -> @{data['name']}
  """)
            if data['twitter_username'] != None:
                print(f"""[?] {data['twitter_username'] + "@" + random.choice(utils.domain_list)} -> @{data['twitter_username']}""")

            print(utils.Reset + "[?] = maybe, [~] = several, [-] = not, [+] = good")

        else:
            DEBUG = False
            print(f"{utils.Light_Red}Debug : {DEBUG}")

        if args.JSON:
            path = "export/reports.json"
            database = f"""
            "login": "{data['login']}",
            "name": "{data['name']}",
            "id": "{data['id']}",
            "avatar": "{data['avatar_url']}",
            "twitter": "{data['twitter_username']}",
            "email": "{sniffer.name(ps)}",

            "location": "{data['location']}",
            "biography": "{data['bio']}",

            "public_repos": "{data["public_repos"]}",
            "followers": "{data['followers']}",
            "following": "{data['following']}",

            "account_created": "{data['created_at'].replace("-", "/").replace("T", " ").replace("Z", "")}",
            "last_profile_update": "{data['updated_at'].replace("-", "/").replace("T", " ").replace("Z", "")}",

            "company": "{data['company']}"
        """
            json_form = """[\n      {""" + "\n" + database + "\n" + """      }\n]"""
            with open(path, "w+", encoding="utf-8")as file:
                file.write(json_form)

                print(f"""
{utils.Light_Green} [+] Export finish in the path : {path} !""")
                exit()

        else:
          print()

        exit()
        

if __name__ == "__main__":
    Core.maincore()
