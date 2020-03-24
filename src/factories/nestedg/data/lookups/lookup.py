from nestedg.model import Model


class Lookup:
    def __init__(self, *values):
        self.values = values

    def lookup(self):
        class LookupGenerator(Model.BaseGenerator):
            default = self.values

        return LookupGenerator
