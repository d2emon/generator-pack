class Model:
    def __iter__(self, data):
        self.__data = data

    @property
    def data(self):
        return {}


class MarkovChain(Model):
    class DataProvider:
        prepend = ' '
        append = '\n'

        @classmethod
        def __parse_item(cls, value, offset, item_length):
            first_char_id = offset - item_length
            last_char_id = offset + item_length

            prepend = ''
            if first_char_id < 0:
                prepend = cls.prepend * (0 - first_char_id)
                first_char_id = 0

            append = ''
            if last_char_id >= len(value):
                append = value[offset:] + cls.append * (last_char_id - len(value))
                last_char_id = len(value)

            initial_string = prepend + value[first_char_id:offset]
            final_string = value[offset:last_char_id] + append
            return initial_string, final_string

        @classmethod
        def parse_string(cls, value, item_length):
            # value = (self.start_char * length) + value + (self.break_char * length)
            chain = [cls.__parse_item(value, offset, item_length) for offset in range(len(value))]
            return {key: block  for key, block in chain}

    def __init__(self, data=(), length=2):
        super().__init__({})
        self.length = length
        for values in data:
            self.parse(values, length)

    def parse(self, value='', length=None):
        length = length or self.length
        # value = (self.start_char * length) + value + (self.break_char * length)
        chain = self.DataProvider.parse_string(value, length)
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
            return self.DataProvider.prepend * self.length
        if prev[-1] == self.DataProvider.append:
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
