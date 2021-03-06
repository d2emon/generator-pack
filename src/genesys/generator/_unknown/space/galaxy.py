from genesys.generator import ListGenerator, PercentGenerator, TemplateGenerator
from genesys.generator import Generated
#from ..generator.template import GeneratorTemplate
from genesys.generator import ListData

from . import fixtures


class Galaxy(Generated):
    @property
    def title(self):
        return self.value

    @title.setter
    def title(self, title):
        self.value = title

    def __repr__(self):
        return "Galaxy: \"%s\"" % (self.value)


galaxy_names = fixtures.galaxy_names


class BaseGalaxyGenerator(ListGenerator):
    generated_class = Galaxy
    template = "{part1} {part2}"
    data = {
        'part1': ListData(galaxy_names[0]),
        'part2': ListData(galaxy_names[1]),
    }

    @classmethod
    def __next__1(cls):
        choices = [ListData(n) for n in cls.galaxy_names]
        return "%s %s" % (
            choices[0].__next__(),
            choices[1].__next__(),
        )


class GalaxyGenerator(PercentGenerator):
    generated_class = Galaxy

    class GalaxyGenerator1(BaseGalaxyGenerator):
        data = {
            'part1': ListData(galaxy_names[0]),
            'part2': ListData(galaxy_names[1]),
        }


    class GalaxyGenerator2(BaseGalaxyGenerator):
        data = {
            'part1': ListData(galaxy_names[1]),
            'part2': ListData(galaxy_names[3]),
        }


    class GalaxyGenerator3(BaseGalaxyGenerator):
        data = {
            'part1': ListData(galaxy_names[2]),
            'part2': ListData(galaxy_names[3]),
        }


    class GalaxyGenerator4(TemplateGenerator, BaseGalaxyGenerator):
        template_str = "{c}{c}-{n}{n}"


    class GalaxyGenerator5(TemplateGenerator, BaseGalaxyGenerator):
        template_str = "{c}{c}{c} {n}{n}{c}"


    subgenerators = {
        30: GalaxyGenerator1,
        50: GalaxyGenerator2,
        80: GalaxyGenerator3,
        90: GalaxyGenerator4,
        100: GalaxyGenerator5,
    }
