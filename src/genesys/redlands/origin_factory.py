from factories.list_model_factory import ListModelFactory
from data.redlands.origins import ORIGINS
from models.redlands.origin import Origin


class OriginFactory(ListModelFactory):
    model = Origin

    def __init__(self, data=None):
        super().__init__(data or ORIGINS)
