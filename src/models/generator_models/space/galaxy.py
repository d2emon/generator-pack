from ..generator_models import Model


class Galaxy(Model):
    @property
    def title(self):
        return self.value

    @title.setter
    def title(self, value):
        self.value = value

    def __repr__(self):
        return 'Galaxy: "{}"'.format(self.value)
