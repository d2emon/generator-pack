from genesys.nested.models.models.unknown import Bear
from genesys.nested.models import Model
from .soil import Sand, Soil, Mud
from ..chemistry import Water, Salt, Ice, WaterState
from ..biology import SeaLife, AbyssLife, BeachLife, RiverLife, LakeLife


class Abyss(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield AbyssLife
            yield Sand


class Beach(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield BeachLife
            yield Sand


class Iceberg(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Bear.probable(30)
            yield Bear.probable(10)
            yield Ice


class SeaWater(WaterState):
    class ChildrenFactory(WaterState.ChildrenFactory):
        def children_classes(self):
            yield Water
            yield Salt


class Sea(Model):
    class BaseFactory(Model.BaseFactory):
        default = map(
            lambda color: '{} sea'.format(color),
            [
                'great', 'wide', 'big', 'old', 'young', 'large', 'small', 'dead', 'shallow', 'deep', 'red', 'yellow',
                'green', 'blue', 'orange', 'brown', 'grey', 'black', 'white', 'purple', 'shady', 'bright', 'silver',
            ],
        )

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield SeaWater
            yield SeaLife
            yield from Beach.multiple(2, 6)


class Ocean(Sea):
    class ChildrenFactory(Sea.ChildrenFactory):
        def children_classes(self):
            yield SeaWater
            yield SeaLife
            yield from Beach.multiple(10, 20)
            yield from Model.BaseFactory([
                Iceberg.multiple(2, 6),
                None,
                None,
                None,
                None,
            ]).next()
            yield Abyss


class River(Model):
    class BaseFactory(Model.BaseFactory):
        default = ['river', 'stream', 'brook', 'creek']

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield RiverLife
            yield Water
            yield Soil
            yield Mud


class Lake(Model):
    class BaseFactory(Model.BaseFactory):
        default = ['lake', 'lagoon', 'pond', 'marsh', 'creek', 'cove']

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield LakeLife
            yield Water
            yield Soil
            yield Mud
