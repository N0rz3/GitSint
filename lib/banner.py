from .text import *
import json

with open('config.json') as file:
    version = json.load(file)['version']

banner = f"""{RED}
    |\__/,|   (`\\
  _.|o o  |_   ) )
-(((---(((----------------------  
 / _] |_   _/' _/| |  \| |_   _| 
| [/\ | | | `._`.| | | ' | | |   
 \__/_| |_| |___/|_|_|\__| |_|   {PURPLE}{italic(f"GitSint v{version} 🐙")}{RED}
     
          {WHITE}BY Norze
  GitHub {RED}OSINT{WHITE} tool made with 💖
"""
