from .component import Component


class Orders(Component):

    def create(self, *args, **kwargs):
        payload = dict(*args, **kwargs)
        return self.request('POST', json=payload)
