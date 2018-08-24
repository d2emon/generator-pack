import random

from .generator_data import GeneratorData


class MarkovChain(GeneratorData):
    start_char = " "
    break_char = "\n"

    def __init__(self, data=(), length=2):
        super().__init__(dict())

        self.length = length
        for string in data:
            self.parse(string)

    def _string_unit(self, string, i, length):
        first = i - length
        last = i + length

        key = ""
        if first < 0:
            key = self.start_char * (-first)
            first = 0
        key += string[first:i]

        if last < len(string):
            value = string[i:last]
        else:
            value = string[i:]
            value += self.break_char * (last - len(string))

        return key, value

    def parse(self, string="", length=None):
        length = length or self.length
        # string = (self.start_char * length) + string + (self.break_char * length)

        chain = [self._string_unit(string, i, length) for i in range(len(string))]

        for key, unit in chain:
            self[key] = unit

    def select(self, prev=""):
        if len(prev) < self.length:
            return self.start_char * self.length
        if prev[-1] == self.break_char:
            return None

        block = prev[-self.length:]
        next_blocks = self.data.get(block)
        if next_blocks is None:
            return None
        return random.choice(next_blocks)

    def __setitem__(self, key, value):
        if self.data.get(key) is None:
            self.data[key] = [value]
        else:
            self.data[key].append(value)

    def __getitem__(self, item):
        return self.data.get(item)

    def generate(self, length=16):
        result = ""
        while len(result) < length:
            unit = self.select(result)
            if unit is None:
                break
            result += unit
        return result.strip()


class MarkovGenerator:
    chain_class = MarkovChain
    _chain = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def chain(cls):
        if cls._chain is None:
            cls._chain = cls.chain_class()
        return cls._chain

    @classmethod
    def generate(cls, length=32):
        name = cls.chain().generate(length)
        return cls(name)
