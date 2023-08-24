from .Requests import Requests
from .profile import user_infos
  
class Hunter:
    async def find_domain(user):
        infos = await user_infos.profile_scraping(user=user)
        company = infos['profile']['company']

        if company != None:
            params = {
                'query': str(company).lower()
            }

            r = await Requests("https://hunter.io/v2/domains-suggestion", params=params).get()

            if '"data": []' in r.text:
                domain = None

                return {
                    'message': f'Company: {company}'
                }
              
            else:
                count = 0
                datas= r.json()['data']

                for data in datas:
                    name = data['name']

                    if str(name).lower() == str(company).lower():
                        count += 1
                        domain = data['domain']
                        break
                    
                    else:
                        continue

                if count > 0:
                    return {
                        'message': f'Company: {company} - (Hunter.io) {company} => {domain}'
                    }
                
                else:
                    return {
                        'message': f'Company: {company}'
                }
        else:
            return {
                    'message': f'{user} is not connected to any company.'
                }
