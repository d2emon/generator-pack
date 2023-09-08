from models.v5 import terrain
from factories.thing.nested_factory import NestedFactory as Factory
from ..materials import SilicaFactory, WaterFactory


class SoilFactory(Factory):
    default_model = terrain.Soil

    @classmethod
    def life(cls):
        yield from cls.select_item(
            # Worm.multiple(0, 2),
            [],
            [],
        )
        yield from cls.select_item(
            # Insect.multiple(0, 2),
            [],
            [],
        )

    def children(self):
        yield from self.life()
        yield SilicaFactory()


class MudFactory(SoilFactory):
    default_model = terrain.Soil

    def children(self):
        yield from super().children()
        yield WaterFactory()


class SandFactory(SoilFactory):
    default_model = terrain.Sand

    @classmethod
    def life(cls):
        yield None
