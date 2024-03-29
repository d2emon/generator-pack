from factories.list_model_factory import ListModelFactory
from data.redlands.templates import TEMPLATES
from models.redlands.template import Template


class TemplateFactory(ListModelFactory):
    model = Template

    def __init__(self, data=None):
        super().__init__(data or TEMPLATES)
