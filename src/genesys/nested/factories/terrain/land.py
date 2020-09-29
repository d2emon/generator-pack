from generated import terrain
from ..factory import Factory
from ..materials import FireFactory, SnowFactory, RockFactory, IronFactory
from ..life import GrassFactory, TreesFactory, JungleTreesFactory, HumusFactory
from .water import RiverFactory, LakeFactory
from .soil import SoilFactory


class LandscapeFactory(Factory):
    fire_probability = 0.3
    snow_probability = 5

    @classmethod
    def life(cls):
        yield None

    @classmethod
    def water(cls):
        yield from RiverFactory().multiple(0, 3)
        yield from LakeFactory().multiple(0, 1)

    @classmethod
    def vegetation(cls):
        yield GrassFactory()

    @classmethod
    def soil(cls):
        yield SoilFactory()

    def children(self):
        yield FireFactory().probable(self.fire_probability)
        yield from self.life()
        yield from self.water()
        yield from self.vegetation()
        yield from self.soil()
        yield SnowFactory().probable(self.snow_probability)


class PlainFactory(LandscapeFactory):
    default_model = terrain.Plain

    names = [
        'plain', 'steppe', 'valley', 'canyon', 'flatland', 'moor', 'grassland', 'prairie', 'desert', 'savannah',
        'tundra', 'wasteland',
    ]

    def generate_name(self):
        return self.select_item(*self.names)

    @classmethod
    def life(cls):
        # yield LandLife
        yield None


class ForestFactory(LandscapeFactory):
    default_model = terrain.Forest

    names = ['forest', 'woods', 'copse']

    def generate_name(self):
        return self.select_item(*self.names)

    @classmethod
    def life(cls):
        # yield ForestLife
        yield None

    @classmethod
    def water(cls):
        yield from RiverFactory().multiple(0, 2)

    @classmethod
    def vegetation(cls):
        yield TreesFactory()
        yield GrassFactory()

    @classmethod
    def soil(cls):
        yield HumusFactory()
        yield SoilFactory()


class JungleFactory(ForestFactory):
    default_model = terrain.Jungle
    snow_probability = 0

    names = ['jungle', 'rainforest']

    def generate_name(self):
        return self.select_item(*self.names)

    @classmethod
    def life(cls):
        # yield JungleLife
        yield None

    @classmethod
    def vegetation(cls):
        yield JungleTreesFactory()
        yield GrassFactory()


class CaveFactory(LandscapeFactory):
    default_model = terrain.Cave
    fire_probability = 0
    snow_probability = 0

    names = ['cave', 'cavern', 'grotto']

    def generate_name(self):
        return self.select_item(*self.names)

    @classmethod
    def life(cls):
        # yield CaveLife
        # yield DragonLair.probable(1)
        yield None

    @classmethod
    def water(cls):
        yield RiverFactory().probable(20)
        yield LakeFactory().probable(10)

    @classmethod
    def vegetation(cls):
        yield None

    @classmethod
    def soil(cls):
        yield RockFactory()
        yield IronFactory().probable(2)


class MountainFactory(LandscapeFactory):
    default_model = terrain.Mountain
    fire_probability = 0
    snow_probability = 40

    names = [
        'mountain', 'peak', 'hill', 'volcano', 'bluff', 'cliff', 'mesa', 'plateau',
    ]

    def generate_name(self):
        return self.select_item(*self.names)

    @classmethod
    def life(cls):
        # yield MountainLife
        yield None

    @classmethod
    def vegetation(cls):
        yield TreesFactory()

    @classmethod
    def soil(cls):
        yield SoilFactory()
        yield RockFactory()

    @classmethod
    def cave(cls):
        yield CaveFactory().probable(30)
        yield CaveFactory().probable(30)
        yield CaveFactory().probable(20)

    def children(self):
        yield from self.cave()
        yield from super().children()
