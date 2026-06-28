import asyncio
from lib.utils.utils import GitEngine, delete_tmp_dir
from lib.Requests import *

MAX_CONCURRENT_REPOS = 5
_HISTORY_CACHE = {}

async def get_history(user):
    if user in _HISTORY_CACHE:
        return _HISTORY_CACHE[user]

    data = await collect_history(user)

    _HISTORY_CACHE[user] = data

    return data

async def collect_history(user):
    repos = await GitEngine.get_all_repositories(user)

    emails = {}
    usernames = {}

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REPOS)

    async def process_repo(repo):
        async with semaphore:
            if repo.get("fork"):
                return

            url = repo.get("clone_url")

            if not url:
                return

            repo_path = await asyncio.to_thread(GitEngine.clone_repository, url)

            if not repo_path:
                return

            history = await asyncio.to_thread(GitEngine.extract_history, repo_path)

            for line in history:
                if "|" not in line:
                    continue

                name, email = line.split("|", 1)

                name = name.strip()
                email = email.strip()

                if name:
                    usernames[name] = usernames.get(name, 0) + 1

                if email and "@users.noreply.github.com" not in email:

                    if email not in emails:
                        emails[email] = {
                            "name": name,
                            "count": 1
                        }
                    else:
                        emails[email]["count"] += 1

    await asyncio.gather(*(process_repo(repo) for repo in repos))
    
    await asyncio.sleep(0.2)
    delete_tmp_dir()

    return emails, usernames

class Email:
    async def search(user):

        emails, _ = await get_history(user)

        result = {
            "count": len(emails),
            "emails": []
        }

        for email, data in sorted(
            emails.items(),
            key=lambda x: x[1]["count"],
            reverse=True
        ):

            result["emails"].append({
                "name": data["name"],
                "email": email,
                "count": data["count"]
            })

        return result if result["count"] > 0 else {
            "message": "Email(s) not found."
        }

class Name:
    async def history(user):

        _, usernames = await get_history(user)

        if not usernames:
            return {
                "message": "No names found in commits.",
                "names": [{"name": None, "count": 0}]
            }

        return {
            "message": "History of usernames found in commits",
            "names": [
                {"name": n, "count": c}
                for n, c in sorted(
                    usernames.items(),
                    key=lambda x: x[1],
                    reverse=True
                )
            ]
        }
