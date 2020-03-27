from factories.providers.data_provider import BaseDataProvider


class DataManager:
    class DataProvider(BaseDataProvider):
        pass

    __instance = None

    def __init__(self):
        self.__provider = None
        self.__instance = self

    @property
    def provider(self):
        return self.__provider or self.DataProvider()

    @provider.setter
    def provider(self, value):
        self.__provider = value

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    @classmethod
    def get_provider(cls):
        return cls.instance().provider
