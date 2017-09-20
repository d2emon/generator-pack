from .. import Generated, PercentedGenerator, ListGenerator, TemplatedGenerator
from . import fixtures


class Galaxy(Generated):
    @property
    def title(self):
        return self.generated_value

    @title.setter
    def title(self, title):
        self.generated_value = title
            
    def __repr__(self):
        return "Galaxy: \"%s\"" % (self.generated_value)


galaxy_names = fixtures.galaxy_names
    
class BaseGalaxyGenerator(ListGenerator):
    generated_class = Galaxy
    galaxy_names = [
        galaxy_names[0],
        galaxy_names[1],
    ]
    
    @classmethod
    def generate_value(cls):
        choices = [ListGenerator.generate_value(l) for l in cls.galaxy_names]
        return "%s %s" % (
            choices[0],
            choices[1],
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