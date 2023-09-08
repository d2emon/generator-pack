from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from ...materials import DewFactory
from ...mind import PsycheFactory, ThoughtsFactory, ThoughtFactory
from .twig import TwigFactory


class GrassThoughtFactory(ThoughtFactory):
    thoughts = [":D", ":O", "D:", ":|", ":]", ">:0"]


class GrassThoughtsFactory(ThoughtsFactory):
    black_hole_probability = 0

    @classmethod
    def thoughts(cls):
        yield from GrassThoughtFactory().multiple(1)


class GrassPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        yield GrassThoughtsFactory().probable(2)

    @property
    def memories_factory(self):
        return None


class GrassBladeFactory(TwigFactory):
    default_model = life.GrassBlade

    def children(self):
        yield GrassPsycheFactory()
        yield DewFactory().probable(6)
        # "worm,3%"
        # "insect,6%"
        yield from super().children()


class GrassFactory(Factory):
    default_model = life.Grass

    def children(self):
        yield from GrassBladeFactory().multiple(50, 100)
