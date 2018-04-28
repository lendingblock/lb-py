import requests

from .orders import Orders
from .loans import Loans


API_URL = 'https://api.lendingblock.com/v1'


class Lendingblock:

    def __init__(self, url=None, session=None):
        self.session = session or requests.Session()
        self.orders = Orders(self)
        self.loans = Loans(self)
        self.api_url = url or API_URL

    def url(self, path=None):
        url = self.api_url
        return '%s/%s' % (url, path) if path else url
