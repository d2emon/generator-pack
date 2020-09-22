from generated.nested_v2.models import DragonLair
from genesys.nested.models import Model
from .soil import Soil
from .water import River, Lake
from generated.chemistry import Fire, Snow, Rock, elements
from ..biology import LandLife, ForestLife, JungleLife, MountainLife, CaveLife, Trees, JungleTrees, Humus, Grass


class Plain(Model):
    class BaseFactory(Model.BaseFactory):
        default = [
            'plain', 'steppe', 'valley', 'canyon', 'flatland', 'moor', 'grassland', 'prairie', 'desert', 'savannah',
            'tundra', 'wasteland',
        ]

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Fire.probable(0.3)
            yield LandLife
            yield from River.multiple(0, 3)
            yield from Lake.multiple(0, 1)
            yield Grass
            yield Soil
            yield Snow.probable(5)


class Forest(Model):
    class BaseFactory(Model.BaseFactory):
        default = ['forest', 'woods', 'copse']

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Fire.probable(0.3)
            yield ForestLife
            yield from River.multiple(0, 2)
            yield Trees
            yield Grass
            yield Humus
            yield Soil
            yield Snow.probable(5)


class Jungle(Forest):
    class BaseFactory(Model.BaseFactory):
        default = ['jungle', 'rainforest']

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Fire.probable(0.3)
            yield JungleLife
            yield from River.multiple(0, 2)
            yield JungleTrees
            yield Grass
            yield Humus
            yield Soil


class Cave(Model):
    class BaseFactory(Model.BaseFactory):
        default = ['cave', 'cavern', 'grotto']

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield CaveLife
            yield DragonLair.probable(1)
            yield River.probable(20)
            yield Lake.probable(10)
            yield Rock
            yield elements['Fe'].probable(2)


class Mountain(Model):
    class BaseFactory(Model.BaseFactory):
        default = [
            'mountain', 'peak', 'hill', 'volcano', 'bluff', 'cliff', 'mesa', 'plateau',
        ]

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield MountainLife
            yield from River.multiple(0, 3)
            yield from Lake.multiple(0, 1)
            yield Cave.probable(30)
            yield Cave.probable(30)
            yield Cave.probable(20)
            yield Trees
            yield Soil
            yield Rock
            yield Snow.probable(40)
