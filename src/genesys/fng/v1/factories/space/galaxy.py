from factories import DictFactory, ListFactory, PercentFactory, TemplateFactory
# from factories.template import FactoryTemplate
from models.generator_models.space.galaxy import Galaxy

from sample_data.generator_fixtures.space import fixtures


class BaseGalaxyGenerator(DictFactory):
    galaxy_names = fixtures.galaxy_names
    generated_class = Galaxy
    template =
    data = {
        'part1': ListFactory(galaxy_names[0]),
        'part2': ListFactory(galaxy_names[1]),
    }

    @property
    def text(self):
        """
        Generate text from factory data
        :return: str
        """
        return f"{self.data['part1']} {self.data['part2']}"

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
