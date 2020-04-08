from genesys.nested.models import Model
from ..chemistry import Water, Silica
from ..biology import Worm, Insect


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


class Sand(Soil):
    class ChildrenFactory(Soil.ChildrenFactory):
        def children_classes(self):
            yield Silica
