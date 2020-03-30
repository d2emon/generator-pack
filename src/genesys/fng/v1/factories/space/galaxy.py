from factories.factory import ListFactory
from factories.generator_factories import ListFactory, PercentFactory, TemplateFactory
# from factories.template import FactoryTemplate
from models.generator_models.space.galaxy import Galaxy

from sample_data.generator_fixtures.space import fixtures


class BaseGalaxyGenerator(ListFactory):
    galaxy_names = fixtures.galaxy_names
    generated_class = Galaxy
    template = "{part1} {part2}"
    data = {
        'part1': ListFactory(galaxy_names[0]),
        'part2': ListFactory(galaxy_names[1]),
    }

    @classmethod
    def __next__1(cls):
        choices = [ListFactory(n) for n in cls.galaxy_names]
        return "%s %s" % (
            choices[0].__next__(),
            choices[1].__next__(),
        )


class GalaxyGenerator(PercentFactory):
    generated_class = Galaxy

    class GalaxyGenerator1(BaseGalaxyGenerator):
        data = {
            'part1': ListFactory(BaseGalaxyGenerator.galaxy_names[0]),
            'part2': ListFactory(BaseGalaxyGenerator.galaxy_names[1]),
        }

    class GalaxyGenerator2(BaseGalaxyGenerator):
        data = {
            'part1': ListFactory(BaseGalaxyGenerator.galaxy_names[1]),
            'part2': ListFactory(BaseGalaxyGenerator.galaxy_names[3]),
        }

    class GalaxyGenerator3(BaseGalaxyGenerator):
        data = {
            'part1': ListFactory(BaseGalaxyGenerator.galaxy_names[2]),
            'part2': ListFactory(BaseGalaxyGenerator.galaxy_names[3]),
        }

    class GalaxyGenerator4(TemplateFactory, BaseGalaxyGenerator):
        template_str = "{c}{c}-{n}{n}"

    class GalaxyGenerator5(TemplateFactory, BaseGalaxyGenerator):
        template_str = "{c}{c}{c} {n}{n}{c}"

    subgenerators = {
        30: GalaxyGenerator1,
        50: GalaxyGenerator2,
        80: GalaxyGenerator3,
        90: GalaxyGenerator4,
        100: GalaxyGenerator5,
    }