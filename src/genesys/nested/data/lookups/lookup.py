from genesys.nested.factories.thing_builder import ListFactory


class Lookup(ListFactory):
    def __init__(self, *values):
        super().__init__(values)
