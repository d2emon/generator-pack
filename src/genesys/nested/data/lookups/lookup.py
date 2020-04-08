from genesys.nested.factories.thing_builder import ListFactory


class Lookup:
    def __init__(self, *values):
        self.values = values

    def lookup(self):
        values = self.values

        class LookupFactory(ListFactory):
            def __init__(self):
                super().__init__(values)

        return LookupFactory
