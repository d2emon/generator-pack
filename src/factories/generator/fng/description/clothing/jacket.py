from models.models import Model
from factories.factories.list_factory import ListFactory
from .sleeves import SleevesGenerator
from .material import Material
from .models.jacket import Tie, Jacket


class TieFactory(ListFactory):
    model_class = Tie
    descriptions = [
        "tightly tied with string",
        "loosely tied with string",
        "buttoned up completely",
        "almost completely buttoned up",
        "half buttoned up",
        "barely tied with string",
        "barely buttoned up",
        "bound",
    ]
    positions = [
        "at the center",
        "at the left side",
        "at the right side",
        "at the top left side",
        "at the top right side",
        "at the bottom left side",
        "at the bottom right side",
        "slightly off-center",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.description = cls.generate_value(cls.descriptions)
        generated.position = cls.generate_value(cls.positions)
        return generated


class JacketFactory(ListFactory):
    generated_class = Jacket

    def __init__(self, provider):
        self.provider = provider
        self.materials = map(Material, provider.materials)
        self.covers = provider.materials
        self.necklines = provider.necklines

    def fill_model(self, model):
        model.sleeves = SleevesGenerator.generate()
        model.material = next(self.materials)
        model.cover = next(self.jacket_covers)
        model.tie = next(TieFactory())
        model.neckline = next(self.necklines)
        return model
