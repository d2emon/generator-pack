from genesys.nested.factories.v2.thing_builder import ListFactory


class Lookup(ListFactory):
    def __init__(self, *values):
        super().__init__(values)
