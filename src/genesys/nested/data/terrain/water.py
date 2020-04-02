from ..unknown import Bear, SeaLife, AbyssLife, BeachLife, Worm, Insect
from genesys.nested.models import Model
from ..chemistry import Water, Salt, Ice, WaterState, Silica


class Soil(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        class NameFactory(Model.NameFactory):
            default = 'dirt'

        def children_classes(self):
            yield from Model.BaseFactory([
                Worm.multiple(0, 2),
                None,
                None,
            ]).next()
            yield from Model.BaseFactory([
                Insect.multiple(0, 2),
                None,
                None,
            ]).next()
            yield Silica


class Mud(Soil):
    class ChildrenFactory(Soil.ChildrenFactory):
        def children_classes(self):
            yield from super().children_classes()
            yield Water


class Sand(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Silica


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
    class ChildrenFactory(Model.ChildrenFactory):
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
