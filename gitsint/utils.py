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
def api_user(ps: str) -> str:
    api_user = f"https://api.github.com/users/{ps}"

    return api_user

def api_commits(ps: str) -> str:
    api_commits = f"https://api.github.com/users/{ps}/events"

    return api_commits

def api_orgs(ps: str) -> str:
    api_orgs = f"https://api.github.com/users/{ps}/orgs"

    return api_orgs

def api_events(ps: str) -> str:
    api_events = f"https://api.github.com/users/{ps}/events/public"

    return api_events

def api_searchs(ps: str) -> str:
    api_searchs = f"https://api.github.com/search/users?q={ps}"

    return api_searchs

def api_repos(ps: str) -> str:
    api_repos = f"https://api.github.com/users/{ps}/repos"

    return api_repos



# List all colors used

"""
Colors palette used -> https://www.webucator.com/article/python-color-constants-module/
Color rgb example (205,102,0) => Functional rgb color in python scripts example (\033[38;2;205;102;0m)
"""

Black = "\033[38;2;0;0;0m"
Light_Red = "\033[38;2;255;48;48m"
Reset = '\033[38;2;255;255;255m'
Light_Green = "\033[38;2;193;255;193m"
Light_Purple = "\033[38;2;191;62;255m"
Yellow = "\033[38;2;255;255;0m"
