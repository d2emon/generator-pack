from factories.markov import MarkovFactory
from .models import StreetChain
from .providers import StreetUnitProvider


class StreetFactory(MarkovFactory):
    def __init__(self, provider=None, max_length=32):
        super().__init__(provider or StreetUnitProvider(), max_length)

    @property
    def model_class(self):
        return StreetChain
