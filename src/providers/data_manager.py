class DataManager:
    __instance = None

    def __init__(self, provider=None):
        self.provider = provider
        self.__instance = self

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    @classmethod
    def get_provider(cls):
        return cls.instance().provider
