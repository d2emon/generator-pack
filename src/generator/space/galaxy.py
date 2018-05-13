from ..generator import ListGenerator, PercentedGenerator, TemplatedGenerator
from ..generator.generated import Generated
#from ..generator.template import GeneratorTemplate
from ..generator.generator_data import ListData

from . import fixtures

import random


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
    galaxy_names = [
        galaxy_names[0],
        galaxy_names[1],
    ]

    @classmethod
    def __next__(cls):
        choices = [ListData(n) for n in cls.galaxy_names]
        return "%s %s" % (
            choices[0].__next__(),
            choices[1].__next__(),
        )


class GalaxyGenerator(PercentedGenerator):
    generated_class = Galaxy

    class GalaxyGenerator1(BaseGalaxyGenerator):
        galaxy_names = [
            galaxy_names[0],
            galaxy_names[1],
        ]


    class GalaxyGenerator2(BaseGalaxyGenerator):
        galaxy_names = [
            galaxy_names[1],
            galaxy_names[3],
        ]


    class GalaxyGenerator3(BaseGalaxyGenerator):
        galaxy_names = [
            galaxy_names[2],
            galaxy_names[3],
        ]


    class GalaxyGenerator4(TemplatedGenerator, BaseGalaxyGenerator):
        template = "{c}{c}-{n}{n}"


    class GalaxyGenerator5(TemplatedGenerator, BaseGalaxyGenerator):
        template = "{c}{c}{c} {n}{n}{c}"


    subgenerators = {
        30: GalaxyGenerator1,
        50: GalaxyGenerator2,
        80: GalaxyGenerator3,
        90: GalaxyGenerator4,
        100: GalaxyGenerator5,
    }
