from .model import Model


class DescriptiveModel(Model):
    def __init__(self, value=None, **kwargs):
        super().__init__(**kwargs)

        self.value = value

    @property
    def description(self):
        return str(self.value)

    @description.setter
    def description(self, value):
        self.value = value

    def __str__(self):
        return self.description


class ListDescriptiveModel(DescriptiveModel):
    @property
    def description(self):
        return " ".join(self.value)
