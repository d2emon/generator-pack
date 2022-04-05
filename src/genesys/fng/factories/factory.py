from models.model import Model
from factories.factory import Factory as __Factory


class Factory(__Factory):
    @property
    def model(self):
        return Model
