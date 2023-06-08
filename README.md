# **📌 GitSint Osint (__G.S.A.__) - 🔍 Github Scraper Accounts**

![gitsint](https://user-images.githubusercontent.com/123885505/234362710-b2c1de45-ea76-4f2d-a8d6-21ba8a66a9f3.jpg)
![GitHub](https://img.shields.io/github/license/bellingcat/octosuite?style=flat)
![Python minimum version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)

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
```
                                       
 _____ _  _____  ____  _  _      _____ 
/  __// \/__ __\/ ___\/ \/ \  /|/__ __\
| |  _| |  / \  |    \| || |\ ||  / \  
| |_//| |  | |  \___ || || | \||  | |  
\____\\_/  \_/  \____/\_/\_/  \|  \_/  

BY 🦊 Norze (GitSint v0.0.5)
🔥 subscribe to my github account !

usage: gitsint.py [-h] <github username>
```


### **📚 Example input:**
```sh
python gitsint.py N0rz3
```


### **📚 Example output:**
```
                                      
 _____ _  _____  ____  _  _      _____ 
/  __// \/__ __\/ ___\/ \/ \  /|/__ __\
| |  _| |  / \  |    \| || |\ ||  / \  
| |_//| |  | |  \___ || || | \||  | |  
\____\\_/  \_/  \____/\_/\_/  \|  \_/  

BY 🦊 Norze (GitSint v0.0.5)
🔥 subscribe to my github account !


Debug : True


> ACCOUNT                                                                                  
-------------------------------------                                                      
                                                                                           
> Identifiers:                                                                             
Username: N0rz3                                                                            
Name: Norze                                                                                
ID: 123885505                                                                              
                                                                                           
> Social:                                                                                  
Twitter: @None                                                                             
                                                                                           
> Details:                                                                                 
Location: France                                                                           
Biography: hello my name is norze  and I am 13 years, I develop mainly in python           
                                                                                           
> Avatar:                                                                                  
https://avatars.githubusercontent.com/u/123885505?v=4                                      
                                                                                           
> Status:                                                                                  
Site Admin: False                                                                          
Type: User                                                                                 
Highlights : null                                                                          
Hireable: None                                                                             
                                                                                           
> Stats:                                                                                   
Public repos: 7                                                                            
Followers: 12                                                                              
Following: 5                                                                               
Gists: 0                                                                                   
                                                                                           
> Account                                                                                  
Account created: 2023/01/29 15:04:08 🌐 (UTC)                                               
Last account update: 2023/06/01 19:37:48 🌐 (UTC)                                           


> REPOSITORIES STATS                                                    
-------------------------------------                                   
                                                                        
[+] 7 repositories (7 sources, 0 fork, 0 archived, 0 mirror, 0 template)
                                                                        
[+] Language stats :                                                    
 - Python (100.0%)     


[-] No organization(s) found.               

[~] Analyze potential(s) friend(s)...         
                                              
> FRIENDS                                     
-------------------------------------         
                                              
[+] ?? potentials friends found !              
                                              
Friends list :                                                                         
 - ....                                 
 - ....                                 


> HIDDEN IDENTITY                                             
-------------------------------------                         
                                                              
[~] Possibles usernames variations -> Norzy, Norze, NORZE     
                                                              
[+] Spoofing...                                               
[-] There is no user with the same username.                  
                                                              
[+] Commit sniffing...                                        
[-] Email not found in commits.                               
                                                              
None                                                          
[~] History of names used :                                   
                                                              
[+] Related names to account :                                
 - Norze (found in 29 commits)                                
                                                              
[~] The target uses these names [ 'Norze', 'N0rz3', '']     



[~] Potentials emails were generated from the nickname and variations !

[?] N0rz3@github.com -> @N0rz3
[?] N0rz3@hotmail.com -> @N0rz3
[?] N0RZ3@yahoo.com -> @N0rz3
[?] NoRZe@gmail.com -> @N0rz3
[?] N0rz3N0rz3@icloud.com -> @N0rz3
[?] NorzeNorze@yandex.com -> @Norze
[?] N0rz3Norze@protonmail.com -> @N0rz3
[?] Norze@hotmail.com -> @Norze
[?] Norz3@icloud.com -> @Norze
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
