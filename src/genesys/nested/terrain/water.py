from models.v5 import terrain
from factories.thing.nested_factory import NestedFactory as Factory
from ..materials import WaterFactory, SaltFactory, IceFactory
from ..life import AbyssLifeFactory, BeachLifeFactory, SeaLifeFactory, RiverLifeFactory, LakeLifeFactory
from .soil import SandFactory, SoilFactory, MudFactory


class AbyssFactory(Factory):
    default_model = terrain.Abyss

    def children(self):
        yield SandFactory()
        yield AbyssLifeFactory()


class BeachFactory(Factory):
    default_model = terrain.Beach

    def children(self):
        yield SandFactory()
        yield BeachLifeFactory()


class IcebergFactory(Factory):
    default_model = terrain.Iceberg

    def children(self):
        yield IceFactory()
        # yield Bear.probable(30)
        # yield Bear.probable(10)


class SeaWaterFactory(Factory):
    default_model = terrain.SeaWater

    def children(self):
        yield WaterFactory()
        yield SaltFactory()


class SeaFactory(Factory):
    default_model = terrain.Sea
    names = [
        'great', 'wide', 'big', 'old', 'young', 'large', 'small', 'dead', 'shallow', 'deep', 'red', 'yellow', 'green',
        'blue', 'orange', 'brown', 'grey', 'black', 'white', 'purple', 'shady', 'bright', 'silver',
    ]

    def generate_name(self):
        return f'{self.select_item(*self.names)} sea'

    @classmethod
    def water(cls):
        yield SeaWaterFactory()

    @classmethod
    def life(cls):
        yield SeaLifeFactory()
        yield None

    @classmethod
    def beaches(cls):
        yield from BeachFactory().multiple(2, 6)

    def children(self):
        yield from self.water()
        yield from self.life()
        yield from self.beaches()


class OceanFactory(SeaFactory):
    default_name = 'ocean'
    default_model = terrain.Ocean

    def generate_name(self):
        return self.default_name

    @classmethod
    def beaches(cls):
        yield from BeachFactory().multiple(10, 20)

    @classmethod
    def icebergs(cls):
        yield from cls.select_item(
            IcebergFactory().multiple(2, 6),
            [],
            [],
            [],
            [],
        )

    @classmethod
    def abyss(cls):
        yield AbyssFactory()

    def children(self):
        yield from super().children()
        yield from self.icebergs()
        yield from self.abyss()


class RiverFactory(Factory):
    default_model = terrain.River
    names = ['river', 'stream', 'brook', 'creek']

    def generate_name(self):
        return self.select_item(*self.names)

    def children(self):
        yield RiverLifeFactory()
        yield WaterFactory()
        yield SoilFactory()
        yield MudFactory()


class LakeFactory(Factory):
    default_model = terrain.Lake
    names = ['lake', 'lagoon', 'pond', 'marsh', 'creek', 'cove']

    def generate_name(self):
        return self.select_item(*self.names)

    def children(self):
        yield LakeLifeFactory()
        yield WaterFactory()
        yield SoilFactory()
        yield MudFactory()
