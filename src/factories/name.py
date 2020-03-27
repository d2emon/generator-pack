import random
from sample_data import genders
from sample_data.fixtures import generator_data


def random_generator(selector, generator_id=None, max_value=10):
    return selector(generator_id or random.randrange(max_value))


class Name:
    glue = ""

    def __init__(self, *items, generator=None):
        self._items = items
        self.generator = generator

    @property
    def value(self):
        return self.get_name(self._items)

    @value.setter
    def value(self, value):
        self._items = value,

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    @classmethod
    def get_name(cls, items):
        return cls.glue.join(items).title()


class TextFactory:
    class NamesProvider:
        block_id = ''
        default = generator_data
        groups = ()

        def __init__(self, data=None):
            self.__data = data

        @property
        def data(self):
            if self.__data is None:
                self.__data = self.default
            return self.__data

        @data.setter
        def data(self, value):
            self.__data = value

        @property
        def block(self):
            return self.data[self.block_id]

        def generate_data(self, group_id=None):
            return self.block.get(group_id or random.choice(self.groups)) if len(self.groups) > 0 else self.block

        def get_parts(self, group_id=None, **params):
            yield random.choice(self.generate_data(group_id))

    def __init__(self, data=None):
        self.provider = self.NamesProvider(data)

    def __iter__(self):
        return self

    def __next__(self):
        return self.get_text()

    def get_text(self, group_id=None, item_id=None, *args, **params):
        return Name(*self.provider.get_parts(group_id=group_id, **params), generator=self)


class NameFactory(TextFactory):
    class NamesProvider(TextFactory.NamesProvider):
        block_id = 'names'
        name_group_id = 'aliens'

        @property
        def block(self):
            return self.data[self.block_id][self.name_group_id]

        def get_parts(self, race_id=None, **params):
            return (random.choice(part) for part in self.generate_data(race_id))

    gender = genders.NEUTRAL

    def get_text(self, race_id=None, item_id=None, *args, **params):
        return Name(*self.provider.get_parts(race_id=race_id, **params), generator=self)


class ListNameFactory(NameFactory):
    class NamesProvider(NameFactory.NamesProvider):
        default = []

        def query(self, **params):
            return self.data

        def get_parts(self, gender=genders.NEUTRAL, **params):
            yield random.choice(self.query(gender=gender, **params))

    def get_text(self, gender=genders.NEUTRAL, item_id=None, *args, **params):
        return Name(*self.provider.get_parts(gender=gender, **params), generator=self)


class GenderListNameFactory(ListNameFactory):
    class NamesProvider(ListNameFactory.NamesProvider):
        default = {}

        def query(self, **params):
            return self.data[params.get('gender', genders.NEUTRAL)]
