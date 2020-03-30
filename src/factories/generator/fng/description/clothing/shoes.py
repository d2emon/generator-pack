from models.models import Model
from factories.factory import DictFactory
from .material import MaterialGenerator


class ShoesGenerator(ListGenerator):
    generated_class = Shoes
    shoetypes = [
        "boots",
        "shoes",
    ]
    designs = [
        "quite simple",
        "a simple design",
        "an ordinary design",
        "a common design",
        "a common type",
        "not that special",
        "a design found commonly",
        "not any different from others",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.material = MaterialGenerator.generate()
        generated.name = cls.generate_value(cls.shoetypes)
        generated.design = cls.generate_value(cls.designs)
        return generated
