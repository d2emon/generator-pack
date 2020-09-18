import random
from factories import MarkovFactory
from orm.models import Model
from providers.markov import MarkovDataProvider
# from providers.markov import MarkovChain
from sample_data.fixtures.streets import streets


class Street(Model):
    def __init__(self, name, **fields):
        super().__init__(**fields)
        self.name = name

    def __repr__(self):
        return "ул. {}".format(self.name)


class MarkovChain(Model):
    def __init__(self, data=(), length=2, **fields):
        super().__init__(**fields)
        self.__data = {}
        self.length = length
        for values in data:
            self.parse(values, length)

    @classmethod
    def data_provider(cls):
        return MarkovDataProvider

    @property
    def data(self):
        return self.__data

    def parse(self, value='', length=None):
        length = length or self.length
        # value = (self.start_char * length) + value + (self.break_char * length)
        chain = self.data_provider().parse_string(value, length)
        for key, block in chain.items():
            self[key] = block

    def __setitem__(self, key, value):
        if self.data.get(key) is None:
            self.data[key] = [value]
        else:
            self.data[key].append(value)

    def __getitem__(self, item):
        return self.data.get(item)

    def get_unit(self, prev=''):
        if len(prev) < self.length:
            return self.data_provider().prepend * self.length
        if prev[-1] == self.data_provider().append:
            return None
        next_unit = self[prev]
        if next_unit is None:
            return None
        else:
            return random.choice(next_unit)

    def get_chain(self, length=16):
        result = ''
        while len(result) < length:
            unit = self.get_unit(result[-self.length:])
            if unit is None:
                break
            result += unit
        return result.strip()

    def generate(self):
        return self.get_chain()


class StreetChain(MarkovChain):
    def __init__(self, data=None, length=3):
        super().__init__(data or streets, length)

    # def generate(self, length=32, *args, **kwargs):
    #     # raise NotImplementedError()


class StreetFactory(MarkovFactory):
    def __init__(self, provider=None):
        super().__init__(provider or StreetChain())

    def model_class(self):
        return Street

    def model(self, *args, **kwargs):
        """
        Get street from markov chain

        :param args: Chain args
        :param kwargs: Chain kwargs
        :return: Street
        """
        # return self.model_class(super().model(*args, **kwargs))
        return super().model(*args, **kwargs)
