from rich.progress import *
from .commits import *
from .friends import *
from .profile import *
from .utils.utils import Text_Manager as TM
from .names_resembling import search2
from .utils.utils import Keys

async def trackx(user):

    RED = TM.RED
    WHITE = TM.WHITE

    modules = [
        ("profile", "Profile scraping", user_infos.profile_scraping),
        ("repos", "Repositories scraping", user_infos.scrap_repos),
        ("orgs", "Organizations scraping", user_infos.org),
        ("friends", "Friends scraping", track),
        ("emails", "Commits analyzing", Email.search),
        ("history", "Username history analyzing", Name.history),
        ("similar", "Similar names searching", search2),
        ("keys", "SSH Keys scraping", lambda u: Keys(u).key_recoverer()),
    ]

    results = {}

    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]{task.fields[module]}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
        transient=True,  
    ) as progress:

        task = progress.add_task(
            "🐈‍⬛ GitSint",
            total=len(modules),
            module="Starting..."
        )

        for key, label, func in modules:

            progress.update(task, module=f"🐙 {label}...")

            results[key] = await func(user)

            progress.advance(task)

    profile = results["profile"]["profile"]
    repos = results["repos"]
    orgs = results["orgs"]
    friends = results["friends"]
    email_search = results["emails"]
    username_history = results["history"]
    second = results["similar"]
    ssh_keys = results["keys"]

    print(f"{RED}{user}{WHITE}")
    print(f"├──Profile")
    print(f"│  ├──Name: {profile['name']}")
    print(f"│  ├──Id: {profile['id']}")
    if profile['biography']:
        print(f"│  ├──Bio: {profile['biography']}")
    else:pass
    if profile['location']:
        print(f"│  ├──Location: {profile['location']}")
    else: pass
    print(f"│  ├──Avatar: {profile['avatar']}")
    print(f"│  ├──Followers: {profile['followers']}")
    print(f"│  └──Following: {profile['following']}")
    print(f"│")
    print(f"├──Stats")
    print(f"│  └───Repostitories")
    print(f"│      └──Public repos: {repos['public_repos']}")
    print(f"│         ├──Sources: {repos['sources']}")
    print(f"│         ├──Forks: {repos['forks']}")
    print(f"│         ├──Archived: {repos['archived']}")
    print(f"│         ├──Mirrors: {repos['mirrors']}")
    print(f"│         └──Templates: {repos['templates']}")
    print(f"│")
    print(f"├──Gists")
    print(f"│  └──Gists: {profile['gists']}")
    print(f"|")
    print(f"├──Keys")
    print(f"│  └──SSH Keys: {ssh_keys}")
    print(f"│")
    print(f"├──Date")
    print(f"│  ├──Creation date: {profile['creation_date'].replace('-', '/').replace('T', ' ').replace('Z', '')} 🌐 (UTC)")
    print(f"│  └──Update date: {profile['update_date'].replace('-', '/').replace('T', ' ').replace('Z', '')} 🌐 (UTC)")
    print(f"│")
    if profile['x']:
        print(f"├──Social")
        print(f"│  └──X (Twitter): @{profile['x']}")
    else:pass
    print(f"│")
    if profile['blog'] != '':
        print(f"├──URL")
        print(f"│  └──Blog: {profile['blog']}")
    else:pass
    print(f"│")
    if orgs.get('organization'):
        print("├──Organization(s)")
        for org in orgs.get('organization', []):
            print(f"│  ├──Name: {org['name']}")
        print("│")
    print(f"│")
    print(f"├──Friend(s)")
    for friend in friends['friends']:
        if friend['name'] != "":   
            print(f"│  ├──{friend['name']}")
    print(f"│")
    print(f"├──Commits")
    print(f"│  ├──Emails")
    if 'count' in email_search:
        print(f"│  │  └──Count: {email_search['count']}")
        if email_search['count'] > 0 and 'emails' in email_search:
            for email_data in email_search['emails']:
                print(f"│  │    ├──Name: {email_data['name']}")
                if email_data['name'].lower() in {user.lower(), profile["name"].lower(), profile['x']}:
                    print(f"│  │    │  └──Email: {email_data['email']} {TM.PURPLE}(🙀 TARGET'S EMAIL){TM.WHITE}")
                else:
                    print(f"│  │    │  └──Email: {email_data['email']}")
    print(f"│  │")
    print(f"│  └──Name(s) History")
    if second['count'] > 0 and 'names' in second:
        print(f"│     ├──Names resembling")
        print(f"│     │  └──Count: {second['count']}")
        for second_data in second['names']:
            print(f"│     │     ├──Name: {second_data}")
    
    print(f"│     │")
    if 'message' in username_history:
        print(f"│     └──{username_history['message']}")
        if 'has not had several names' in username_history['message']:
            exit()

        if 'names' in username_history:
            if username_history['message'] == "No names found in commits.":
                exit()
            for name_data in username_history['names']:
                print(f"│        ├──Name: {name_data['name']} (found in {name_data['count']} commit{'s' if name_data['count'] > 1 else ''})")
