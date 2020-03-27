from sample_data.fixtures import streets
from .generator_models import MarkovChain


class StreetChain(MarkovChain):
    def __init__(self, data=None, length=3):
        super().__init__(data or streets, length=length)
