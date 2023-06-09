from colorama import *

"""
Domain's list
- mail (gmail, yahoo.fr, etc...)
- website (.fr, .com, .xyz)
"""

domain_list = ["gmail.com","outlook.com","protonmail.com","yahoo.com","mail.com","yandex.com", "icloud.com", "hotmail.com", "github.com"]

domains = [".com", ".xyz", ".fr", ".eu"]


"""
API's list
- only github
"""
def api_user(ps: str) -> None:
    api_user = f"https://api.github.com/users/{ps}"

    return api_user

def api_commits(ps: str) -> None:
    api_commits = f"https://api.github.com/users/{ps}/events"

    return api_commits

def api_orgs(ps: str) -> None:
    api_orgs = f"https://api.github.com/users/{ps}/orgs"

    return api_orgs

def api_events(ps: str) -> None:
    api_events = f"https://api.github.com/users/{ps}/events/public"

    return api_events

def api_searchs(ps: str) -> None:
    api_searchs = f"https://api.github.com/search/users?q={ps}"

    return api_searchs

def api_repos(ps: str) -> None:
    api_repos = f"https://api.github.com/users/{ps}/repos"

    return api_repos



Black = Fore.BLACK
Light_Red = Fore.LIGHTRED_EX
Reset = Fore.RESET
Light_Green = Fore.LIGHTGREEN_EX
Light_Purple = Fore.LIGHTMAGENTA_EX
Yellow = Fore.YELLOW
