from abc import ABC
from typing import List


class Component(ABC):
    def __init__(self, cli, base=None):
        self.cli = cli
        self.base = base or self.__class__.__name__.lower()

    def url(self, path: str = None):
        if path and path.startswith('/'):
            path = path[1:]
        return f'{self.base}/{path}' if path else self.base


class ReadComponent(Component, ABC):

    async def get(self, id: str, **kwargs) -> dict:
        url = self.url(id)
        return await self.cli.execute(url, **kwargs)

    async def get_list(self, query: dict = None, **kwargs) -> List[dict]:
        url = self.url()
        return await self.cli.execute(url, params=query, **kwargs)


class CrudComponent(ReadComponent, ABC):

    async def create(self, data: dict, **kwargs) -> dict:
        url = self.url()
        return await self.cli.execute(url, 'POST', json=data, **kwargs)

    async def delete(self, id: str, **kwargs):
        url = self.url(id)
        return await self.cli.execute(url, 'DELETE', **kwargs)
