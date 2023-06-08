import requests
import utils

def search(ps: str) -> str:
    """
    Function that loops through commits to find an email

    List of functions:
     - added commits
     - email recovery
    """

    r = requests.get(utils.api_commits(ps))
    events = r.json()

    emails = []

    print(f"\n[+] Commit sniffing...")
    for event in events:
        if event["type"] == "PushEvent":
            commits = event["payload"]["commits"]
            for commit in commits:
                author = commit["author"]
                email = author["email"]
                username = author["name"]
                if "@users.noreply.github.com" not in email:
                    if (email, username) not in emails:
                        emails.append((email, username))
    if emails:
        if len(emails) == 1:
            print("[+] Email found in commits !\n")
            for email, username in emails:
                print(f"{utils.Light_Green}[+] [Email found in commits] {email} -> @{ps}{utils.Reset}")

        else:
            print("[+] Emails found in commits !\n")
            print("[~] Several email options :")
            for email, username in emails:
                print(f" - {username}, {email}")
    else:
        print("[-] Email not found in commits.")


def name(ps: str) -> str:

    r = requests.get(utils.api_commits(ps))
    events = r.json()

    emails = []

    for event in events:
        if event["type"] == "PushEvent":
            commits = event["payload"]["commits"]
            for commit in commits:
                author = commit["author"]
                email = author["email"]
                username = author["name"]
                if "@users.noreply.github.com" not in email:
                    if (email, username) not in emails:
                        emails.append((email, username))

    if len(emails) == 1:
        for email, username in emails:
            emaile = email

        return emaile
    else:
        emaile = ""


def mail(ps: str) -> str:

    r = requests.get(utils.api_commits(ps))
    events = r.json()

    emails = []

    for event in events:
        if event["type"] == "PushEvent":
            commits = event["payload"]["commits"]
            for commit in commits:
                author = commit["author"]
                email = author["email"]
                username = author["name"]
                if "@users.noreply.github.com" not in email:
                    if (email, username) not in emails:
                        emails.append((email, username))

    if len(emails) == 1:
        for email, username in emails:
            emaile = f"{utils.Light_Green}[!] [Target email find] {email} -> @{username}{utils.Reset}"

            return emaile
    else:
        emaile = ""
        return emaile


def mails(ps: str) -> str:
    r = requests.get(utils.api_commits(ps))
    events = r.json()

    emails = []

    for event in events:
        if event["type"] == "PushEvent":
            commits = event["payload"]["commits"]
            for commit in commits:
                author = commit["author"]
                email = author["email"]
                username = author["name"]
                if "@users.noreply.github.com" not in email:
                    if (email, username) not in emails:
                        emails.append((email, username))

    if len(emails) != 1:
        for email, username in emails:
            print(f"\nEmail that corresponds to the target => {email}\n\n")
    else:
        print("[-] The target does not have an email linked to their account.")
