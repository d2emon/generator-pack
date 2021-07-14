from v3.factories import ListModelFactory
from ..data.templates import TEMPLATES
from ..models.template import Template


class TemplateFactory(ListModelFactory):
    model = Template

    def __init__(self, data=None):
        super().__init__(data or TEMPLATES)
