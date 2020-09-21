from factories import ModelFactory
from ..models import Doll


class DollFactory(ModelFactory):
    @property
    def data(self):
        return None

    @property
    def model_class(self):
        return Doll
