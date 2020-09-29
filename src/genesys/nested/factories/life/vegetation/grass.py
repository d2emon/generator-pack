from generated import life
from ...factory import Factory
from ...materials import DewFactory
from ...mind import ThoughtFactory, ThoughtsFactory
from .twig import TwigFactory


class GrassThoughtFactory(ThoughtFactory):
    names = [":D", ":O", "D:", ":|", ":]", ">:0"]

    def generate_name(self):
        return self.select_item(*self.names)


class GrassThoughtsFactory(ThoughtsFactory):
    def children(self):
        yield from GrassThoughtFactory().multiple(1)


class GrassBladeFactory(TwigFactory):
    default_model = life.GrassBlade

    def children(self):
        yield GrassThoughtsFactory().probable(2)
        yield DewFactory().probable(6)
        # "worm,3%"
        # "insect,6%"
        yield from super().children()


class GrassFactory(Factory):
    default_model = life.Grass

    def children(self):
        yield from GrassBladeFactory().multiple(50, 100)
