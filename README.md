# **📌 GitSint Osint (__G.S.A.__) - 🔍 Github Scraper Accounts**

![gitsint](https://user-images.githubusercontent.com/123885505/234362710-b2c1de45-ea76-4f2d-a8d6-21ba8a66a9f3.jpg)


## **🕵️‍♂️ Find all traces left by a user !**


__Find information using open-source intelligence (OSINT) on a Github account.__


## 🛠️ Requirements / Launch

- [Python 3](https://www.python.org/downloads/release/python-370/)

```sh
>> git clone https://github.com/N0rz3/GitSint.git
>> cd GitSint\gitsint
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






During the launch there will be marked `DEBUG` if the debug is __**True**__ it is that the request to the API went well otherwise the debug will be __**False**__ which means that there was an error during the query as:
- A debit limit (if there have already been requests made before in a short period of time)

- The account does not exist (spelling error)


## 🧾 **Summary**

With GitSint you can find:
- the names used
- name variations
- the names linked to the account
- the emails linked to the account
- the personal email of the account
and many more things...


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

## **🧑 Tester**

 Tool tester on 😸 [BlueRed](https://github.com/CSM-BlueRed)
