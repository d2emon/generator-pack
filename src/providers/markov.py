from .provider import DataProvider


class MarkovChain(DataProvider):
    def __next__(self):
        return self.generate()

    def generate(self, length=32, *args, **kwargs):
        raise NotImplementedError()


class MarkovDataProvider:
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
        return {key: block for key, block in chain}
