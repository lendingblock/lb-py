import aiohttp

from .orders import Orders
from .loans import Loans


API_URL = 'https://api.lendingblock.com/v1'


class Lendingblock:

    def __init__(self, url=None, session=None, token=None):
        self.session = session
        self.token = token
        self.orders = Orders(self)
        self.loans = Loans(self)
        self.api_url = url or API_URL

    def url(self, path=None):
        url = self.api_url
        if path and path.startswith('/'):
            path = path[1:]
        return f'{url}/{path}' if path else url

    async def close(self):
        if self.session:
            await self.session.close()

    async def execute(self, path, method=None, headers=None, **kw):
        if not self.session:
            self.session = aiohttp.ClientSession()
        if self.token:
            headers = headers or {}
            headers['X-Lendingblock-Api-Key'] = self.token
        method = method or 'GET'
        headers = headers or {}
        headers['Accept'] = 'application/json, text/*; q=0.5'
        print(self.url(path))
        response = await self.session.request(
            method, self.url(path), headers=headers, **kw
        )
        return await response.json()
