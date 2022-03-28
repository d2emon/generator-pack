from generated import life
from factories.nested_factory import NestedFactory as Factory
from .body_parts import SkinlessSoftBodyPartFactory, BodyPartFactory


class WingFactory(Factory):
    default_model = life.Wing

    @classmethod
    def feathers(cls):
        # Feathers
        yield None

    def children(self):
        yield from self.feathers()
        yield from super().children()


class TentacleFactory(SkinlessSoftBodyPartFactory):
    default_model = life.Tentacle


class TailFactory(BodyPartFactory):
    default_model = life.Tail
