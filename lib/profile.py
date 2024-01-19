from bs4 import BeautifulSoup
from .Requests import Requests
from .utils.utils import *
        
class user_infos:
    types = ['fork', 'source', 'archived', 'mirror', 'template']
    list = []
    
    BASE_URL = "https://github.com"

    async def scrap_repos(user):
        for type in user_infos.types:
            response = await Requests(f"{user_infos.BASE_URL}/{user}?tab=repositories&q=&type={type}&language=&sort=").get()
            soup = BeautifulSoup(response.content, 'html.parser')
            count = soup.find("div", {"class": "user-repo-search-results-summary TableObject-item TableObject-item--primary v-align-top"}).findAll("strong")
            count = count[0].text.strip()

            user_infos.list.append(count)
                
        return {
                'public_repos': int(user_infos.list[1]) + int(user_infos.list[0]) + int(user_infos.list[2]) + int(user_infos.list[3]) + int(user_infos.list[4]),
                'sources': user_infos.list[1],
                'forks': user_infos.list[0],
                'archived': user_infos.list[2],
                'mirrors': user_infos.list[3],
                'templates': user_infos.list[4]
            }


    async def profile_scraping(user):
        profile_url = await Requests(user_infos.BASE_URL + f"/{user}").get()

        soup = BeautifulSoup(profile_url.content, 'html.parser')

        name = soup.find("span", {"class": "p-name vcard-fullname d-block overflow-hidden"})
        name = name.text.strip()
        if name == "":
            name = None
        else:
            name = name

        api = f"https://api.github.com/users/{user}"

        req = await Requests(api).get()

        json_data = req.json()  

        id = json_data['id']
        location = json_data['location']
        company = json_data['company']
        blog = json_data['blog']
        bio = json_data['bio']
        x = json_data['twitter_username']
        gists = json_data['public_gists']
        creation = json_data['created_at']
        update = json_data['updated_at']
        followers = json_data['followers']  
        following = json_data['following']
        avatar = json_data['avatar_url']  

        return {
            'profile': {
                'name': name,
                'id': id,
                'location': location,
                'company': company,
                'blog': blog,
                'biography': bio,
                'x': x,
                'gists': gists,
                'creation_date': creation,
                'update_date': update,
                'followers': followers,
                'following': following,
                'avatar': avatar
            }
        }


    async def org(user):
        org_list = []

        api = f"https://api.github.com/users/{user}/orgs"

        r = await Requests(api).get()

        if r and r.text and "{" in r.text:
            orgs = r.json()

            for org in orgs:
                name = org['login']
                org_data = {
                    'name': name
                }
                org_list.append(org_data)

            data = {
                'organization': org_list
            }

            return data

        else:
            data = {
                'message': 'Has no related organizations'
            }
            return data
        
    async def contributions(user):
        url = "https://github.com/{}".format(user)

        r = await Requests(url).get()

        soup = BeautifulSoup(r.text, "html.parser")

        contribut = soup.find('h2', {'class': 'f4 text-normal mb-2'})
        contribut = contribut.text.strip()

        numbers = Text_Manager(text=contribut).no_letters()
        return numbers
