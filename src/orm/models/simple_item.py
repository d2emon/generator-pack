from factories import Factory, ListFactory
from .model import Model


class SimpleItem(Model):
    class NameFactory(Factory):
        default = 'Unnamed'

    class DataFactory(ListFactory):
        default = []

    __name_factory = None
    __data_factory = None

    def __init__(self, name=None, **fields):
        super().__init__(**fields)
        self.__name = name

    @classmethod
    def name_factory(cls):
        """
        Name factory getter
        :return: Name factory
        """
        if cls.__name_factory is None:
            cls.__name_factory = cls.NameFactory()
        return cls.__name_factory

    @classmethod
    def data_factory(cls):
        """
        Data factory getter
        :return: Data factory
        """
        if cls.__data_factory is None:
            cls.__data_factory = cls.DataFactory()
        return cls.__data_factory

    @property
    def name(self):
        if self.__name is None:
            self.__name = next(self.name_factory())
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return str(self.name)

    @classmethod
    def next(cls):
        data = next(cls.data_factory())
        return cls(data) if data is not None else None
