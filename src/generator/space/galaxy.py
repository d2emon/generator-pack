import random
from .. import Generated, DataGenerator, GeneratorTemplate
from .fixtures import galaxy_names


class Galaxy(Generated):
    @property
    def title(self):
        return self.generated_value

    @title.setter
    def title(self, title):
        self.generated_value = title
            
    def __repr__(self):
        return "Galaxy: \"%s\"" % (self.generated_value)


class GalaxyGenerator1(DataGenerator):
    generated_class = Galaxy
    galaxy_names = galaxy_names[:2]

    @classmethod
    def generate_value(cls):
        choices = [random.choice(l) for l in cls.galaxy_names]
        return "%s %s" % (
            choices[0],
            choices[1],
        )


class GalaxyGenerator2(GalaxyGenerator1):
    galaxy_names = [
        galaxy_names[1],
        galaxy_names[3],
    ]


class GalaxyGenerator3(GalaxyGenerator1):
    galaxy_names = [
        galaxy_names[2],
        galaxy_names[3],
    ]


class GalaxyGenerator4(GalaxyGenerator1):
    template = "{c}{c}-{n}{n}"

    @classmethod
    def generate_value(cls):
        return GeneratorTemplate.pregenerate(cls.template)

    
class GalaxyGenerator5(GalaxyGenerator4):
    template = "{c}{c}{c} {n}{n}{c}"


class GalaxyGenerator(DataGenerator):
    generated_class = Galaxy
    subgenerators = {
        30: GalaxyGenerator1,
        50: GalaxyGenerator2,
        80: GalaxyGenerator3,
        90: GalaxyGenerator4,
        100: GalaxyGenerator5,
    }
    
    @classmethod
    def generator_by_chance(cls, chance=0):
        for c in sorted(cls.subgenerators):
            if c >= chance:
                return cls.subgenerators[c]

    @classmethod
    def generate_value(cls):
        chance = random.randint(0, 100)
        g = cls.generator_by_chance(chance)
        return g.generate_value()