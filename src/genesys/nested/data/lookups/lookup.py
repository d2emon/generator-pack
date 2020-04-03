from genesys.nested.models import Model


class Lookup:
    def __init__(self, *values):
        self.values = values

    def lookup(self):
        class LookupGenerator(Model.BaseFactory):
            default = self.values

        return LookupGenerator
