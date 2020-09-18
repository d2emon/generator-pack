class Model:
    children = {}

    def __init__(self, **fields):
        self.uuid = None
        for field, value in fields.items():
            self.__setattr__(field, value)

    def with_children(self):
        """
        Fill model with random children

        :return:
        """
        for k, v in self.children.items():
            if self.__getattribute__(k) is None:
                self.__setattr__(k, v.random())

        return self

    @classmethod
    def random(cls):
        return cls().with_children()
