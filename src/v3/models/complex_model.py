from .generated_model import GeneratedModel
from .preparable_model import PreparableModel
from .serializable_model import SerializableModel


class ComplexModel(GeneratedModel, PreparableModel, SerializableModel):
    children = {}

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__fields = {}

        self.fill(*args, **kwargs)

    def fill(self, *args, **kwargs):
        super().fill(*args, **kwargs)

        self.__fields = {name: kwargs.get(name) for name in self.field_names}

    @property
    def serialize_fields(self):
        return self.field_names + list(self.children.keys())

    def with_children(self):
        """
        Fill model with random children

        :return:
        """
        for k, v in self.children.items():
            if self.data.get(k) is None:
                self.data[k] = v.random() if isinstance(v, ComplexModel) else v

        return self

    @classmethod
    def random(cls):
        return cls().with_children()
