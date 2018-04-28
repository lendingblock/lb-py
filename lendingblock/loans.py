from .component import Component


class Loans(Component):

    def get(self, id):
        url = self.cli.url('%s/%s' % (self.base, id))
        return self.request('GET', url)
