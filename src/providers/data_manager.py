class DataManager:
    __instance = None

    def __init__(self, provider=None):
        self.provider = provider
        self.__instance = self

    @classmethod
    def instance(cls):
        return cls.__instance or cls().instance()

    @classmethod
    def get_provider(cls):
        return cls.instance().provider
