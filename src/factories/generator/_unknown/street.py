from factories.generator import MarkovGenerator, MarkovChain

from sample_data.fixtures import streets


class StreetChain(MarkovChain):
    def __init__(self, data=None, length=3):
        super().__init__(data or streets, length=length)


class Street(MarkovGenerator):
    chain_class = StreetChain

    def __repr__(self):
        return "ул. {}".format(self.name)
