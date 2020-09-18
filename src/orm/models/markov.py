import random
from orm.models import Model
from providers.markov import MarkovDataProvider


class MarkovChain(Model):
    def __init__(self, data=(), length=2):
        super().__init__()
        self.__provider = MarkovDataProvider(length)
        self.__data = {}
        for value in data:
            self.parse(value, self.__provider.unit_length)

    def __getitem__(self, key):
        return self.__data.get(key)

    def __setitem__(self, key, value):
        if self.__data.get(key) is None:
            self.__data[key] = [value]
        else:
            self.__data[key].append(value)

    @property
    def data(self):
        return self.__data

    def parse(self, value='', length=None):
        # value = (self.start_char * length) + value + (self.break_char * length)
        chain = self.__provider.parse_string(value)
        for key, unit in chain.items():
            self[key] = unit

    def next_unit(self, prev=''):
        if len(prev) < self.__provider.unit_length:
            return self.__provider.starter

        if prev[-1] == self.__provider.append:
            return None

        next_unit = self[prev]
        return random.choice(next_unit) if next_unit is not None else None

    def get_chain(self, length=16):
        result = ''
        while len(result) < length:
            unit = self.next_unit(result[-self.__provider.unit_length:])
            if unit is None:
                break
            result += unit
        return result.strip()

    def generate(self):
        return self.get_chain()
