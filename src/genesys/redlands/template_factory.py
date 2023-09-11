from factories.list_model_factory import ListModelFactory
from data.redlands.templates import TEMPLATES
from models.redlands.template import Template


class TemplateFactory(ListModelFactory):
    default_data = TEMPLATES
    model = Template
