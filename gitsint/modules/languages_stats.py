import requests
import utils

def percentage(ps: str) -> str:
    response = requests.get(utils.api_repos(ps))
    repos = response.json()

    total_bytes = 0
    language_bytes = {}

    for repo in repos:
        language = repo["language"]
        if language is not None:
            bytes = repo["size"]
            total_bytes += bytes
            if language in language_bytes:
                language_bytes[language] += bytes
            else:
                language_bytes[language] = bytes

    print(f"[+] Language{'s' if len(language_bytes) > 1 else ''} stats :")
    for language in language_bytes:
        percentage = (language_bytes[language] / total_bytes) * 100
        result = f" - {language} ({percentage:.1f}%)"

        print(result)