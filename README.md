# **📌 GitSint Osint (__G.S.A.__) - 🔍 Github Scraper Accounts**

![gitsint](https://user-images.githubusercontent.com/123885505/234362710-b2c1de45-ea76-4f2d-a8d6-21ba8a66a9f3.jpg)


## **🕵️‍♂️ Find all traces left by a user !**


__Find information using open-source intelligence (OSINT) on a Github account.__


## 🛠️ Requirements / Launch

- [Python 3](https://www.python.org/downloads/release/python-370/)

```sh
>> git clone https://github.com/N0rz3/GitSint.git
>> cd GitSint/gitsint
>> pip install -r requirements.txt
>> python main.py
```


- Details : 
```yaml
usage: python gitsint.py [-h / --help] [-u / --username <username>]


options: 
   -h, --help        show this help message and exit
   -u, --username    <username>

```


### **📚 Example :**
```sh
python gitsint.py -u N0rz3
```
https://user-images.githubusercontent.com/123885505/234613439-bf4c7bb4-349a-4dba-881d-e21cefa06ec7.mp4





**Have fun ! 🥰💕**

During the launch there will be marked `DEBUG` if the debug is __**True**__ it is that the request to the API went well otherwise the debug will be __**False**__ which means that there was an error during the query as:
- A debit limit (if there have already been requests made before in a short period of time)

- The account does not exist (spelling error)


## 🧾 **Summary**

Main features :

 - Used names
 - Related names
 - Name history
 - Pseudo variations
 - Potential friends
 - Related organizations
 - Personal email
 - Related emails
 - Potential emails generated with found names
 - Commit analysis
 - Main account information (bio, creation/modification date, name, location) if available
 - Accounts with the same or similar pseudonym
 - Potential duplicate accounts
 - JSON export

Optimization:

 - No need for a key to use the tool.

Default:

- Rate limiting due to APIs used ? Change your IP thanks to VPN or Proxy.

GitSint mainly uses APIs but also web scraping using the BeautifulSoup 4 library.

Export of the main information in JSON format:
```json
[
    {
        "login": "example",
        "name": "examples",
        "id": "10000000",
        "avatar": "avatar.url/url",
        "twitter": "example@twitter",
        "email": "example@example.com"
    }
]
```



## **✔️/❌ Rules**

**Disclaimer**

This tool was built solely for educational purposes, and I am not responsible for its use.

Using this tool in a paid service is strictly prohibited.
Please use it only for personal investigation purposes or open-source projects.

__**⚠️ DO NOT USE FOR MALICIOUS PURPOSES  ⚠️**__ 



## **📝 License**

[GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.fr.html)


## **👋🏻 Socials**

- 😺 My github -> N0rz3
- 🤖 My discord -> NORZE#9666

Do you like what I offer as content ?
Subscribe to my GitHub account for more tools and programs ! 😉



## **💳 Credits**

- ✏️ Inspiration : gitfive by [mxrch](https://github.com/mxrch)
- 🖼️ Original logo : [orginal logo](https://dribbble.com/shots/16062020-3D-GitHub-Logo)
- 🖼️ Custom logo : me 🤗
- 👨‍💻 Source code : me 🤗
