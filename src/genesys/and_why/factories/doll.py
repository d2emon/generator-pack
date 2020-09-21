from factories import Factory
from ..models import Doll


class DollFactory(Factory):
    @property
    def model_class(self):
        return Doll

    def model(self, *args, **kwargs):
        return self.model_class(*args, **kwargs)
