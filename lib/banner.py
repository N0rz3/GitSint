from .text import *

banner = f"""{RED}
    |\__/,|   (`\\
  _.|o o  |_   ) )
-(((---(((----------------------  
 / _] |_   _/' _/| |  \| |_   _| 
| [/\ | | | `._`.| | | ' | | |   
 \__/_| |_| |___/|_|_|\__| |_|   {PURPLE}{italic("GitSint v2.2.1 🐙")}{RED}
     
          {WHITE}BY Norze
  GitHub {RED}OSINT{WHITE} tool made with 💖
"""

banner2 = f"""{RED}
    |\__/,|   (`\\
  _.|o o  |_   ) )
-(((---(((----------------------  
 / _] |_   _/' _/| |  \| |_   _| 
| [/\ | | | `._`.| | | ' | | |   
 \__/_| |_| |___/|_|_|\__| |_|   {PURPLE}{italic("GitSint v2.2.1 🐙")}{RED}
     
          {WHITE}BY Norze
  GitHub {RED}OSINT{WHITE} tool made with 💖

𝕩  X.com: @norze15
☕ Donations: https://www.buymeacoffee.com/norze


usage: gitsint.py [-h] [-u [USERNAME]] [-o [ORGANIZATION]] [-e [EMAIL]] [-f [FRIENDS]] [-l] [-a [AVATAR]]

options:
usage: gitsint.py [-h] [-u [USERNAME]] [-o [ORGANIZATION]] [-e [EMAIL]] [-f [FRIENDS]] [-a [AVATAR]] [-s [SEARCH]] 
                  [-l]

options:
  -h, --help            show this help message and exit
  -u [USERNAME], --username [USERNAME]
                        searches all public information by username
  -o [ORGANIZATION], --organization [ORGANIZATION]
                        searches all public information by organization
  -e [EMAIL], --email [EMAIL]
                        search for an account by email
  -f [FRIENDS], --friends [FRIENDS]
                        search for potential friends by username
  -a [AVATAR], --avatar [AVATAR]
                        download profile picture (avatar) by username
  -s [SEARCH], --search [SEARCH]
                        search potential secondary account(s) by username
  -l, --light           light mode with option '-e'
"""
