from ...unknown import Insect, Worm
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from .cells import PlantCell
from ...chemistry import Dew


class GrassThought(Model):
    class Factory(ThingBuilder):
        class DataProvider:
            grass_thought = [':D', ':O', 'D:', ':|', ':]', '>:0']

        class BaseFactory(ThingBuilder.BaseFactory):
            data = property(lambda self: self.provider.grass_thought)

        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield None


class GrassThoughts(Model):
    default_name = 'thoughts'

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from GrassThought.multiple(1)


class GrassBlade(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield GrassThoughts.probable(2)
                yield Dew.probable(6)
                yield Worm.probable(3)
                yield Insect.probable(6)
                yield PlantCell


class Grass(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from GrassBlade.multiple(50, 100)
