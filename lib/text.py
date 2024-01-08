RED = "\033[31m"
WHITE = "\033[0m"
GREEN = "\033[38;2;0;201;87m"
PURPLE = "\033[38;2;171;130;255m"
BLACK = "\033[38;2;89;89;89m"

def italic(text):
    ITALIC = "\033[3m" + text + "\033[0m"
    return ITALIC
