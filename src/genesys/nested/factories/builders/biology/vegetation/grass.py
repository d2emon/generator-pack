from .cells import PlantCell
from genesys.nested.models import models
from genesys.nested.factories.thing_builder import ThingBuilder


class GrassThought(ThingBuilder):
    model = models.GrassThought

    class DataProvider:
        grass_thought = [':D', ':O', 'D:', ':|', ':]', '>:0']

    class BaseFactory(ThingBuilder.BaseFactory):
        data = property(lambda self: self.provider.grass_thought)

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            yield None


class GrassThoughts(ThingBuilder):
    model = models.GrassThoughts

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            yield from GrassThought.multiple(1)


class GrassBlade(ThingBuilder):
    model = models.GrassBlade

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            yield GrassThoughts.probable(2)
            yield Dew.probable(6)
            yield Worm.probable(3)
            yield Insect.probable(6)
            yield PlantCell


class Grass(ThingBuilder):
    model = models.Grass

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            yield from GrassBlade.multiple(50, 100)
