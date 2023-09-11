from factories.list_model_factory import ListModelFactory
from data.redlands.origins import ORIGINS
from models.redlands.origin import Origin


class OriginFactory(ListModelFactory):
    default_data = ORIGINS
    model = Origin
