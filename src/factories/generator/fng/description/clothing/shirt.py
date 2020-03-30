from models.models import Model
from factories.factory import DictFactory
from .sleeves import SleevesGenerator


class ShirtGenerator(ListGenerator):
    generated_class = Shirt
    styles = [
        "rough",
        "elegant",
        "fancy",
        "graceful",
        "luxurious",
        "relatively simple",
        "majestic",
        "modest",
        "noble",
        "ornate",
        "rather simple",
        "refined",
        "stylish",
        "traditional",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.style = cls.generate_value(cls.styles)
        generated.sleeves = SleevesGenerator.generate()
        return generated
