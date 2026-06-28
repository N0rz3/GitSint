<h1 align="center" id="title">🔎🐈 G i t S i n t</h1>

![](assets/logo.jpg)
[![python version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)](https://www.python.org/downloads/)
[![license](https://img.shields.io/badge/License-GNU-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.fr.html)

# **😇 About GitSint**
> 🕵️ GitSint (v2) is an OSINT tool for investigations on the GitHub platform.
> The tool mostly works with GitHub APIs.

**Features of script**
- fully async
- asynchrone scraping 
- menu in cli format (commands)

**GitSint extracts various information like**
- login
- name
- email
- id
- biography
- location
- avatar (+ upload)
- followers
- following
- repos
- gists
- date of creation/update
- X (Twitter)
- blog
- organizations
- potentials friends
- similar names
- emails related
- names related
- names used
- email to account

👀 **The information found by GitSint is presented in the form of a tree structure for better navigation.**
![](assets/gitsintt.png)

## **🎉What's new ?**

- Fully asynchrone system
- Completely redone design
- Find all email adress in commits 
- Find all usernames in commits
- Added email-based account tracking.
- Information searches from an organization
- Light mode => account tracking by email (works with GitHub API)
- Avatar upload
- Search for similar names


## **📦 Installation**

- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads) ⚠️ **Necessary for the proper functioning of GitSint**

```
$ git clone https://github.com/N0rz3/GitSint.git
$ cd ./GitSint
$ pip install -r requirements.txt
```

## **🎲 Usage**

```
usage: gitsint.py [-h] [-u [USERNAME]] [-o [ORGANIZATION]] [-e [EMAIL]] [-f [FRIENDS]] [-l] [-a [AVATAR]]
                  [-s [SIMILAR]]

options:
  -h, --help            show this help message and exit
  -u, --username [USERNAME]
                        searches all public information by username
  -o, --organization [ORGANIZATION]
                        searches all public information by organization
  -e, --email [EMAIL]   search for an account by email
  -f, --friends [FRIENDS]
                        search for potential friends by username
  -l, --light           light mode with option '-e' (search account by email with API)
  -a, --avatar [AVATAR]
                        download profile picture (avatar) by username
  -s, --similar [SIMILAR]
                        search for similar names by username
```

### 🐧 Some examples of usage
- `$ python3 gitsint.py -u username`
- `$ python3 gitsint.py -o orga`
- `$ python3 gitsint.py -e email@email.com`🦾 Recommended for a **100%** accurate result.
- `$ python3 gitsint.py -l -e email@email.com` ✨ The 'light' mode is far less efficient than the 'email' module; it works using the GitHub API.

## 🌞 More

###  🛡️ Protection

If you don't want to display your email address in the commits and leave it private, you just have to go to 

**settings -> emails**  
and tick these two parameters

![](assets/protection.png)

*I invite you to read this guide which will explain how to protect your personal data on GitHub. [(DOC)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)*

### **🗿 Contributions**
Make a [pull requests](https://github.com/N0rz3/GitSint/pulls) with all the details needed to contribute of the cat work 😺

### **✔️ / ❌ Rules**

**this tool was designed for educational purposes only and is not intended for any mischievous use, I am not responsible for its use.**

### **📜 License**

**This project is [License GPL v3](https://www.gnu.org/licenses/gpl-3.0.fr.html) be sure to follow all rules 👍**

### **💖 Thanks**
- If you like what i do please subscribe 💖. And if you find this tool is useful don't forget to star 🌟
- This tool is inspired by [GitFive](https://github.com/mxrch/GitFive) made by [mxrch](https://github.com/mxrch)

**💶 Support me 👇**

<a href="https://www.buymeacoffee.com/norze" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50" ></a> 
