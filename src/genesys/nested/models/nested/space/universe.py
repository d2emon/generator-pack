from factories.factory import ListFactory
from models.models import ListModel
from sample_data.fixtures.space import universe


class Universe(ListModel):
    data = {'value': ListFactory(None, universe)}

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
