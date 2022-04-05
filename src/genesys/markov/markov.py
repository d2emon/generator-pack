import random
from factories.factory import Factory
from models.v4.keyed.markov import MarkovUnit


class MarkovProvider(Factory):
    def __init__(
        self,
        data=(),
        first_char=' ',
        last_char='\n',
        unit_length=2,
    ):
        self.__data = {}
        self.first_char = first_char
        self.last_char = last_char
        self.unit_length = unit_length
        for value in data:
            self.parse(value)

    def __getitem__(self, key):
        if len(key) < self.unit_length:
            return self.starter

        if key[-1] == self.last_char:
            return None

        units = self.__data.get(key)
        return random.choice(units) if units is not None else None

    def __setitem__(self, key, value):
        if self.__data.get(key) is None:
            self.__data[key] = [value]
        else:
            self.__data[key].append(value)

    @property
    def starter(self):
        return MarkovUnit(None, self.first_char * self.unit_length)

    @property
    def data(self):
        return self.__data

    def append(self, unit):
        self[unit.prev] = unit

    def __parse_unit(self, text, character_id):
        first_id = character_id - self.unit_length
        if first_id < 0:
            prepend = self.first_char * (0 - first_id)
            first_id = 0
        else:
            prepend = ''

        last_id = character_id + self.unit_length
        if last_id > len(text):
            append = self.last_char * (last_id - len(text))
            last_id = len(text)
        else:
            append = ''

        return MarkovUnit(
            prepend + text[first_id:character_id],
            text[character_id:last_id] + append,
        )

    def parse_string(self, text):
        for item_id in range(len(text)):
            yield self.__parse_unit(text, item_id)

    def parse(self, value=''):
        # value = (self.start_char * self.length) + value + (self.break_char * self.length)
        for unit in self.parse_string(value):
            self.append(unit)
