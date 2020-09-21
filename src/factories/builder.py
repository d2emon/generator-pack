class Builder:
    def __init__(self):
        self.__ready = False
        self.__item = None
        self.reset()

    @property
    def is_ready(self):
        return self.__ready

    @property
    def item(self):
        return self.__item

    def new_item(self):
        raise NotImplementedError()

    def reset(self):
        self.__ready = False
        self.__item = self.new_item()

    def ready(self):
        self.__ready = True

    @property
    def result(self):
        return self.__item if self.is_ready else None
