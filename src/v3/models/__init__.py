from .model import Model
from .name import TextModel


class ComplexModel(Model):
    field_names = []
    children = {}

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__fields = {}
        self.fill(*args, **kwargs)

    def fill(self, *args, **kwargs):
        super().fill(*args, **kwargs)
        self.__fields = {name: kwargs.get(name) for name in self.field_names}

    def with_children(self):
        """
        Fill model with random children

        :return:
        """
        for k, v in self.children.items():
            if self.data.get(k) is None:
                self.data[k] = v.random()

        return self

    @classmethod
    def random(cls):
        return cls().with_children()
