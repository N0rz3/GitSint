RED = "\033[31m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
PURPLE = "\033[38;2;171;130;255m"

def italic(text):
    ITALIC = "\033[3m" + text + "\033[0m"
    return ITALIC