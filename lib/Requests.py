import httpx

class Requests:
    def __init__(self, 
                url: str,
                headers=None,
                data=None,
                params=None,
                json=None):
        self.url = url
        self.head = headers
        self.data = data
        self.params = params
        self.json = json

    async def get(self):
        try:
            async with httpx.AsyncClient() as client:
                requests = await client.get(url=self.url, headers=self.head, params=self.params)

                return requests

        except httpx.HTTPError:
            return()
        
    async def post(self):
        try:
            async with httpx.AsyncClient() as client:
                requests = await client.post(url=self.url, headers=self.head, params=self.params, json=self.json)

                return requests
            
        except httpx.HTTPError:
            return()
            
    async def put(self):
        try:
            async with httpx.AsyncClient() as client:
                requests = await client.put(url=self.url, headers=self.head, params=self.params, json=self.json)

                return requests
            
        except httpx.HTTPError:
            return()
            
    async def delete(self):
        try:
            async with httpx.AsyncClient() as client:
                requests = await client.delete(url=self.url, headers=self.head, params=self.params)

                return requests

        except httpx.HTTPError:
            return()
