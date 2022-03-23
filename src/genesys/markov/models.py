from genesys.model.keyed import MarkovChain
from v3.models.model import Model


class Street(Model):
    def __init__(self, name, **fields):
        super().__init__(**fields)
        self.name = name

    def __repr__(self):
        return "ул. {}".format(self.name)


class StreetChain(MarkovChain):
    def street(self):
        return Street(str(self))
