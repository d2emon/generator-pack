from generated import life
from ...factory import Factory
from ...mind import PsycheFactory


class AnimalBodyFactory(Factory):
    default_model = life.AnimalBody

    @classmethod
    def eyes(cls):
        yield None

    @classmethod
    def mouth(cls):
        yield None

    @classmethod
    def skin(cls):
        yield None

    @classmethod
    def flesh(cls):
        yield None

    def children(self):
        yield from self.eyes()
        yield from self.mouth()
        yield from self.skin()
        yield from self.flesh()


class AnimalFactory(Factory):
    default_model = life.Animal
    names = []

    def generate_name(self):
        return self.select_item(*self.names)

    @property
    def body_factory(self):
        return AnimalBodyFactory()

    @property
    def psyche_factory(self):
        return PsycheFactory()

    def children(self):
        yield self.body_factory
        yield self.psyche_factory
