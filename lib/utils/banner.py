from .utils import Text_Manager
import json

RED = Text_Manager.RED
PURPLE = Text_Manager.PURPLE
WHITE = Text_Manager.WHITE

with open('config.json') as file:
    version = json.load(file)['version']

banner = f"""{RED}
    |\__/,|   (`\\
  _.|o o  |_   ) )
-(((---(((----------------------  
 / _] |_   _/' _/| |  \| |_   _| 
| [/\ | | | `._`.| | | ' | | |   
 \__/_| |_| |___/|_|_|\__| |_|   {PURPLE}{Text_Manager(text=f"GitSint v{version} 🐙").italic()}{RED}
     
          {WHITE}BY Norze
  GitHub {RED}OSINT{WHITE} tool made with 💖
"""
