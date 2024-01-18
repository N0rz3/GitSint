from .Requests import Requests
from utils.text import *

async def organizations_scraping(org):
    api = "https://api.github.com/orgs/{}".format(org)

    r = await Requests(api).get()
    
    try:
        data = {
            'name': r.json()['name'],
            'location': r.json()['location'],
            'url': r.json()['blog'],
            'email': r.json()['email'],
            'verified': r.json()['is_verified'],
            'followers': r.json()['followers'],
            'following': r.json()['following'],
            'creation': r.json()['created_at'].replace("-", "/").replace("T", " ").replace("Z", ""),
            'update': r.json()['updated_at'].replace("-", "/").replace("T", " ").replace("Z", "")
        }

        members_api = "https://api.github.com/orgs/{}/public_members".format(org)

        req = await Requests(members_api).get()

        members = req.json()

        member_list = []

        for member in members:
            member_data = {
                'login': member['login']
            }
            member_list.append(member_data)

        data['members'] = member_list

        return data
    
    except KeyError:
        exit("[-] Organization provided does not exist.")

async def print_organization_info(org):
    org_data = await organizations_scraping(org=org)

    print(RED + org_data['name'] + WHITE)
    print(f"├──URL:", org_data['url'])
    print(f"├──Location:", org_data['location'])
    print(f"├──Email:", org_data['email'])
    print(f"├──Verified:", org_data['verified'])
    print(f"├──Followers:", org_data['followers'])
    print(f"├──Following:", org_data['following'])
    print(f"├──Creation Date:", org_data['creation'] + " 🌐 (UTC)")
    print(f"├──Last Update:", org_data['update'] + " 🌐 (UTC)")
    print(f"├──Member(s)")
    for member in org_data['members']:
        print(f"    ├──{member['login']}")
