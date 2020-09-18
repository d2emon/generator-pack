from providers.markov import MarkovDataProvider


class Model:
    def __iter__(self, data):
        self.__data = data

    @property
    def data(self):
        return {}


class MarkovChain(Model):
    def __init__(self, data=(), length=2):
        super().__init__({})
        self.length = length
        for values in data:
            self.parse(values, length)

    @classmethod
    def data_provider(cls):
        return MarkovDataProvider

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

    def __next__(self):
        return self.get_chain()
