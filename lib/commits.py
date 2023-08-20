from .Requests import Requests       

class Email:
    async def search(user):

        r = await Requests(f"https://api.github.com/users/{user}/events").get()
        events = r.json()

        emails = []

        for event in events:
            if event["type"] == "PushEvent":
                commits = event["payload"]["commits"]
                for commit in commits:
                    author = commit["author"]
                    email = author.get("email")
                    username = author.get("name")
                    if email and "@users.noreply.github.com" not in email:
                        if (email, username) not in emails:
                            emails.append((email, username))

        result = {
            'count': len(emails),  
            'emails': []           
        }

        for email, username in emails:
            result['emails'].append({
                'name': username,
                'email': email
            })

        if result['count'] > 0:
            return result
        else:
            return {
                'message': 'Email(s) not found in commits for the given user'
            }

    async def resolv_email(user):
        count = 0
        email = None  

        r = await Requests(f"https://api.github.com/users/{user}/events").get()
        events = r.json()

        for event in events:
            if event["type"] == "PushEvent":
                commits = event["payload"]["commits"]
                for commit in commits:
                    author = commit["author"]
                    current_email = author.get("email")
                    username = author.get("name")
                    if current_email and "@users.noreply.github.com" not in current_email and username == user:
                        count += 1
                        email = current_email 

        result = {
            'count': count,  
            'email': email          
        }

        if result['count'] > 0:
            return result
        elif result['count'] == 0:
            return {
                'email': 'None@nop'
            }

class Name:
    async def history(user):
        response = await Requests("https://api.github.com/users/{}/events".format(user)).get()

        pseudos = {}

        data = response.json()

        for commit in data:
            if commit["type"] == "PushEvent":
                commits = commit["payload"]["commits"]
                for c in commits:
                    pseudo = c["author"]["name"]
                    if pseudo in pseudos:
                        pseudos[pseudo] += 1
                    else:
                        pseudos[pseudo] = 1

        if len(pseudos) > 0:
            gateau = {
                'message': 'History of usernames found in commits'
            }
            listt = []
            for pseudo, count in pseudos.items():
                d = {
                    'name': pseudo,
                    'count': count
                }
                listt.append(d)
            gateau['names'] = listt
            return gateau

        else:
            return {
                'message': f'{user} has not had several names',
                'names':{
                    'name': None,
                    'count': 0
                }
            }