from factories.generator.generator.generated import ListGenerated
from factories.generator.generator.generator_data import ListData

from sample_data.fixtures.space import universe


class Universe(ListGenerated):
    data = {'value': ListData(universe)}

    def __init__(self, value, position=(0, 0, 0)):
        super().__init__(value)
        self.position = position

    @classmethod
    def generate(cls):
        u = super().generate()
        u.position = [
            1,
            2,
            3,
        ]
        return u
