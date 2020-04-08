from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from .cells import PlantCell
from ..insect import Insect
from ..mind import Thoughts, Thought
from ..worm import Worm
from ...chemistry import Dew


class GrassThought(Thought):
    class Factory(Thought.Factory):
        class DataProvider:
            grass_thought = [':D', ':O', 'D:', ':|', ':]', '>:0']

        class BaseFactory(Thought.Factory.BaseFactory):
            data = property(lambda self: self.provider.grass_thought)

        class ChildrenFactory(Thought.Factory.ChildrenFactory):
            def builders(self):
                yield None


class GrassThoughts(Thoughts):
    default_name = 'thoughts'

    class Factory(Thoughts.Factory):
        class ChildrenFactory(Thoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from GrassThought.multiple(1)


class GrassBlade(Model):
    cells = Model.child_property(PlantCell)
    thoughts = Model.child_property(GrassThoughts)
    dew = Model.child_property(Dew)
    worms = Model.children_property(Worm)
    insects = Model.children_property(Insect)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield GrassThoughts.probable(2)
                yield Dew.probable(6)
                yield Worm.probable(3)
                yield Insect.probable(6)
                yield PlantCell


class Grass(Model):
    grass_blades = Model.children_property(GrassBlade)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from GrassBlade.multiple(50, 100)
