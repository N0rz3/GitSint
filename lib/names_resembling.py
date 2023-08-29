from .Requests import Requests
from bs4 import BeautifulSoup

# patch note n°2
# fix {AttributeError: 'NoneType' object has no attribute 'text'}

async def search(user):
    api = "https://api.github.com/search/users?q={}".format(user)

    r = await Requests(api).get()

    if r.status_code == 200:
            try:
                items = r.json()['items']
                if not items:
                    print(f"[-] No result for {user}.")
                    exit()

                else:
                    count = 0
                    for item in items:
                        _login = item['login'] 

                        if _login != user:
                            count += 1     

                            url = f"https://github.com/{_login}"

                            _r = await Requests(url).get()

                            soup = BeautifulSoup(_r.text, 'html.parser')
                            name = soup.find("span", {"class": "p-name vcard-fullname d-block overflow-hidden"})
                            if name != None:
                                _name = name.text.strip()

                                if _name != '':
                                    print(f"[+] 🙉 {_login} ({_name})")

                                else:
                                    print(f"[+] 🙉 {_login}")
                            else:
                                print(f"[+] 🙉 {_login}")

                    if count == 0:
                        print(f"[-] No result for {user}.")

            except (KeyError, ValueError):
                print("[-] JSON parsing error.")
                exit()


async def search2(user):
    api = "https://api.github.com/search/users?q={}".format(user)

    r = await Requests(api).get()

    if r.status_code == 200:
        count = 0
        names = []

        try:
            items = r.json().get('items', [])
            if not items:
                return {
                    "count": count,
                    "names": f"No result for {user}."
                }

            for item in items:
                _login = item['login']

                if _login != user:
                    url = item['url']
                    _api = await Requests(url).get()
                    _name = _api.json().get('name', '')

                    if _name:
                        count += 1
                        names.append(f"{_login} ({_name})")
                    else:
                        count += 1
                        names.append(f"{_login}")

            return {
                "count": count,
                "names": names
            }

        except (KeyError, ValueError):
            return {
                "count": False,
                "names": "JSON parsing error."
            }
