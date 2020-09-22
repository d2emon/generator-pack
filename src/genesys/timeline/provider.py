from . import era


class DataProvider:
    def __init__(self):
        # self.__desert_encounters = DataItemFactory(groups.DESERT_ENCOUNTERS)
        self.__prehistory = era.Prehistory()
        self.__ancient = era.Ancient()
        self.__past = era.Past()
        self.__modern = era.Modern()

    @property
    def prehistory(self):
        return self.__prehistory

    @property
    def ancient(self):
        return self.__ancient

    @property
    def past(self):
        return self.__past

    @property
    def modern(self):
        return self.__modern

    @property
    def timeline(self):
        yield from self.prehistory.events()
        yield from self.ancient.events()
        yield from self.past.events()
        yield from self.modern.events()
