from .generated_model import GeneratedModel
from .preparable_model import PreparableModel


class ComplexModel(GeneratedModel, PreparableModel):
    serialize_field_names = []
    children = {}

    @property
    def serialize_fields(self):
        return self.serialize_field_names + list(self.children.keys())

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
