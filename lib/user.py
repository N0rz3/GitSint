from .commits import *
from .friends import *
from .profile import *
from .text import *
from .gitlab import user_test_in_gitlab
from .hunterio import Hunter
from .secondary_account import search2

async def trackx(user):
    profile = await user_infos.profile_scraping(user)
    profile = profile['profile']
    repos = await user_infos.scrap_repos(user)
    orgs = await user_infos.org(user)
    friends = await track(user)
    email_search = await Email.search(user)
    username_history = await Name.history(user)
    num_contributors = await user_infos.contributions(user)
    gitlab = await user_test_in_gitlab(user)
    email_target = await Email.resolv_email(user)
    company = await Hunter.find_domain(user)
    second = await search2(user)

    print(f"{RED}{user}{WHITE}")
    print(f"├──Profile")
    print(f"│  ├──Name: {profile['name']}")
    print(f"│  ├──Id: {profile['id']}")
    print(f"│  ├──Bio: {profile['biography']}")
    print(f"│  ├──Location: {profile['location']}")
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
    print(f"│")
    print(f"├──Date")
    print(f"│  ├──Creation date: {profile['creation_date'].replace('-', '/').replace('T', ' ').replace('Z', '')} 🌐 (UTC)")
    print(f"│  └──Update date: {profile['update_date'].replace('-', '/').replace('T', ' ').replace('Z', '')} 🌐 (UTC)")
    print(f"│")
    print(f"├──Social")
    print(f"│  ├──X (Twitter): {profile['x']}")
    print(f"│  └──GitLab")
    print(f"│     └──Name: {gitlab['name']}")
    print(f"│")
    print(f"├──URL")
    print(f"│  ├──Blog: {profile['blog']}")
    print(f"│  └──{company['message']}")
    print(f"│")
    print(f"├──Organization(s)")
    for org in orgs.get('organization', []):
        print(f"│  ├──Name: {org['name']}")
    print(f"│")
    print(f"├──Friend(s)")
    for friend in friends['friends']:
        if friend['name'] != "":   
            print(f"│  ├──{friend['name']}")
    print(f"│")
    print(f"├──Contributions")
    print(f"│  └──{num_contributors} contributions in the last year")
    print(f"│")
    print(f"├──Commits")
    print(f"│  └──Emails")
    if 'count' in email_search:
        print(f"│     └──Count: {email_search['count']}")
        if email_search['count'] > 0 and 'emails' in email_search:
            for email_data in email_search['emails']:
                print(f"│        ├──Name: {email_data['name']}")
                print(f"│        │  └──Email: {email_data['email']}")
    print(f"│")
    print(f"│  └──Name(s) History")
    if second['count'] > 0 and 'names' in second:
        print(f"│     ├──Potentials secondary account(s)")
        print(f"│     │  └──Count: {second['count']}")
        for second_data in second['names']:
            print(f"│     │     ├──Name: {second_data}")
    
    print(f"│     ├──Names used: {gitlab['name']}, {profile['name']}, {profile['x']}, {email_target['email'].split('@')[0]}")
    if 'message' in username_history:
        print(f"│     └──{username_history['message']}")
        if 'has not had several names' in username_history['message']:
            exit()

        if 'names' in username_history:
            if username_history['message'] == "No names found in commits.":
                exit()
            for name_data in username_history['names']:
                print(f"│        ├──Name: {name_data['name']} (found in {name_data['count']} commit{'s' if name_data['count'] > 1 else ''})")
