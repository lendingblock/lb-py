

class Component:

    def __init__(self, cli, base=None):
        self.cli = cli
        self.base = base or self.__class__.__name__.lower()
