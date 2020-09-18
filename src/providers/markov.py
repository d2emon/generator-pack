from .provider import DataProvider


class MarkovChain(DataProvider):
    def __next__(self):
        return self.generate()

    def generate(self, length=32, *args, **kwargs):
        raise NotImplementedError()


class MarkovUnit:
    def __init__(self, prev, value):
        self.prev = prev
        self.value = value


class MarkovDataProvider:
    prepend = ' '
    append = '\n'

    def __init__(self, unit_length=2):
        self.unit_length = unit_length

    @property
    def starter(self):
        return self.prepend * self.unit_length

    def __parse_unit(self, text, character_id):
        first_id = character_id - self.unit_length
        if first_id < 0:
            prepend = self.prepend * (0 - first_id)
            first_id = 0
        else:
            prepend = ''

        last_id = character_id + self.unit_length
        if last_id > len(text):
            append = text[character_id:last_id] + self.append * (last_id - len(text))
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
