import time
from lib.Requests import *

class Text_Manager:
    def __init__(self, text: str, time: int=3) -> None:
        self.text = text
        self.time = time

    # all colors used
    RED = "\033[31m"
    WHITE = "\033[0m"
    GREEN = "\033[38;2;0;201;87m"
    PURPLE = "\033[38;2;171;130;255m"
    BLACK = "\033[38;2;89;89;89m"

    def italic(self):
        ITALIC = "\033[3m" + self.text + "\033[0m"
        return ITALIC

    def no_letters(self):
        digits = "".join(filter(str.isdigit, self.text))
        return digits

    def Tprint(self):
        print(self.text, end="", flush=True)
        time.sleep(self.time)
        print("\r" + " " * (len(self.text) + 1) + "\r", end="", flush=True)

class Keys:
    def __init__(self, target: str) -> None:
        self.targ = target
        # self.keys_lister: list[str]

    async def key_recoverer(self):
        r = await Requests(url=f"https://github.com/{self.targ}.keys").get()

        lines = r.text.strip().split('\n')

        if lines:
            ssh_rsa_count = sum("ssh-rsa" in line for line in lines)
            return ssh_rsa_count

        else:
            pass
