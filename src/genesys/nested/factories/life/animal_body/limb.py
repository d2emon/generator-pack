from generated import life
from ...factory import Factory


class WingFactory(Factory):
    default_model = life.Wing

    @classmethod
    def feathers(cls):
        # Feathers
        yield None

    def children(self):
        yield from self.feathers()
        yield from super().children()
