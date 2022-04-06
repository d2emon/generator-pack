from factories.list_factory import ListFactory


class Lookup(ListFactory):
    def __init__(self, *values):
        super().__init__(values)
