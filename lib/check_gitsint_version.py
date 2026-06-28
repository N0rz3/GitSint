from .utils.utils import Text_Manager as TM
from .Requests import Requests
import json

class Version:
    def version():
        with open('config.json', 'r') as json_file:
            j = json.load(json_file)

            v = j['version']
            return v

    async def check_update():
        v = Version.version()

        r = await Requests("https://raw.githubusercontent.com/N0rz3/GitSint/master/config.json").get()

        file = json.load(r)
        v_ = file['version']

        if v != v_:
            print(f"🙀 You are not up to date, the {TM.PURPLE}{v_}{TM.WHITE} version is available !")
            print(f"🐱 You are advised to reinstall the tool ({TM.CYAN}{TM('https://github.com/N0rz3/GitSint').italic()}{TM.WHITE})\n")

        else:
            print(f"🔥 Your are up to date !\n")
