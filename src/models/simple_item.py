from factories import Factory, ListFactory


class SimpleItem:
    class NameFactory(Factory):
        default = 'Unnamed'

    class DataFactory(ListFactory):
        default = []

    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        if self.__name is None:
            self.__name = next(self.NameFactory())
        return self.__name

    def __str__(self):
        return self.name

    @classmethod
    def next(cls):
        data = next(cls.DataFactory())
        return cls(data) if data is not None else None
