from .. import Generated, PercentedGenerator, ListGenerator, TemplatedGenerator
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


class GalaxyGenerator1(ListGenerator):
    generated_class = Galaxy
    galaxy_names = galaxy_names[:2]

    @classmethod
    def generate_value(cls):
        choices = [cls.generate_value(l) for l in cls.galaxy_names]
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


class GalaxyGenerator4(TemplatedGenerator):
    template = "{c}{c}-{n}{n}"

    
class GalaxyGenerator5(GalaxyGenerator4):
    template = "{c}{c}{c} {n}{n}{c}"


class GalaxyGenerator(PercentedGenerator):
    generated_class = Galaxy
    subgenerators = {
        30: GalaxyGenerator1,
        50: GalaxyGenerator2,
        80: GalaxyGenerator3,
        90: GalaxyGenerator4,
        100: GalaxyGenerator5,
    }