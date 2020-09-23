class Model:
    children = {}
    fields = []

    def __init__(self, **fields):
        self.uuid = None
        self.__values = {field: fields.get(field) for field in self.fields}
        # for field, value in fields.items():
        #    self.__setattr__(field, value)

    def __getitem__(self, item):
        return self.__values.get(item)

    def __setitem__(self, key, value):
        self.__values[key] = value

    def with_children(self):
        """
        Fill model with random children

        :return:
        """
        for k, v in self.children.items():
            if self.__values.get(k) is None:
                self.__values[k] = v.random()

        return self

    @classmethod
    def random(cls):
        return cls().with_children()
