import requests
import utils

class orgz:
    def __init__(self, username : str) -> str:
        """
        Verify all organizations linked to the account
        """

        self.username = username

        url = utils.api_orgs(username)


        response = requests.get(url)

        organizations = response.json()

        if len(organizations) > 0:
            print(f"\n{utils.Light_Red}> ORGANIZATIONS\n-------------------------------------{utils.Reset}")
            print(utils.Light_Green + f"[+] {len(organizations)} organization{'s' if len(organizations) > 1 else ''} found !{utils.Reset}")
            for organization in organizations:
                org =  organization['login']
                org_url = f"https://api.github.com/orgs/{org}"

                responses = requests.get(org_url)
                orgza = responses.json()

                print("\nName : " + str(orgza['name']) if orgza['name'] is not None else "Not found")
                print("Email : " + str(orgza['email']) if orgza['email'] is not None else "Not found")
                print("Description : " + str(orgza['description']) if orgza['description'] is not None else "Not found")
                print("Website : " + str(orgza['blog']) if orgza['blog'] is not None else "Not found")
                print("GitHub page : " + str(orgza['html_url']) if orgza['html_url'] is not None else "Not found")
                print("\nDomain name -> " + str(orgza['blog'].replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")) if orgza['blog'] is not None else "Not found" )
        else:
            print("\n[-] No organization(s) found.")
