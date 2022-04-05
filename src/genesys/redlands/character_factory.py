from factories.model_factory import ModelFactory
from data.redlands.templates import TEMPLATES
from data.redlands.origins import ORIGINS
from data.redlands.movements import MOVEMENTS
from models.redlands.character import Character
from .template_factory import TemplateFactory
from .origin_factory import OriginFactory
from .movement_factory import MovementFactory


class CharacterFactory(ModelFactory):
    class FactoryData:
        def __init__(self):
            self.templates = TEMPLATES
            self.origins = ORIGINS
            self.movements = MOVEMENTS

    model = Character

    def __init__(self, data=None):
        super().__init__()

        self.data = data or self.FactoryData()

        self.template_factory = TemplateFactory(self.data.templates)
        self.origin_factory = OriginFactory(self.data.origins)
        self.movement_factory = MovementFactory(self.data.movements)

    def generate(self, *args, **kwargs):
        """
        Generate value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        template = self.template_factory(*args, **kwargs)
        origin = self.origin_factory(*args, **kwargs)
        movement = self.movement_factory(*args, **kwargs)
        return {
            'name': f'{origin.title}/{template.title}/{movement.title}',
            'template': template,
            'origin': origin,
            'movement': movement,
        }
