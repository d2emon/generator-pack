from .generated_model import GeneratedModel


class ComplexModel(GeneratedModel):
    field_names = []
    children = {}

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__fields = {}
        self.fill(*args, **kwargs)

    def fill(self, *args, **kwargs):
        super().fill(*args, **kwargs)
        self.__fields = {name: kwargs.get(name) for name in self.field_names}

    def serialize(self):
        """
        Serialize model fields

        :return: Dict with model data
        """
        result = {}
        for field in (self.field_names + list(self.children.keys())):
            value = self.__getattribute__(field)
            result[field] = value if not isinstance(value, self.__class__) else value.uuid
        return result

    @classmethod
    def deserialize(cls, data=None):
        """
        Deserialize model from dict

        :param data: Dict with model data
        :return: Deserialized model
        """
        return cls(**data) if data is not None else None

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
