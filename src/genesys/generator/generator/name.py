import random
from sample_data.fixtures import generator_data


GENDER_NEUTRAL = 0
GENDER_MALE = 1
GENDER_FEMALE = 2


def random_generator(selector, generator_id=None, max_value=10):
    if generator_id is None:
        generator_id = random.randrange(max_value)
    return selector(generator_id)


class Name:
    glue = ""

    def __init__(self, *items, generator=None):
        self._items = items
        self.generator = generator

    @classmethod
    def build_name(cls, items):
        return cls.glue.join(items).title()

    @property
    def value(self):
        return self.build_name(self._items)

    @value.setter
    def __set_name__(self, value):
        self._items = value,

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)


class TextGenerator:
    block_id = ''
    groups = ()
    data = []

    def __init__(self, data=None):
        data = data or generator_data
        self.data = data[self.block_id]

    def generate_data(self, group_id=None):
        if len(self.groups) < 1:
            return self.data

        if group_id is None:
            group_id = random.choice(self.groups)
        return self.data.get(group_id)

    def generate(self, group_id=None, item_id=None, *args, **kwargs):
        return Name(random.choice(self.generate_data(group_id)), generator=self)

    def __iter__(self):
        return self

    def __next__(self):
        return self.generate()


class NameGenerator(TextGenerator):
    block_id = 'names'
    name_group_id = 'aliens'
    gender = GENDER_NEUTRAL

    def __init__(self, data=None):
        super().__init__(data)
        self.data = self.data[self.name_group_id]

    def generate(self, race_id=None, item_id=None, *args, **kwargs):
        parts = (random.choice(part) for part in self.generate_data(race_id))
        return Name(*parts, generator=self)


class ListNameGenerator(NameGenerator):
    names = []

    @classmethod
    def select_names(cls, *args, **kwargs):
        return cls.names

    @classmethod
    def generate(cls, gender=GENDER_NEUTRAL, *args, **kwargs):
        return Name(random.choice(cls.select_names(gender=gender, *args, **kwargs)), cls)


class GenderListNameGenerator(ListNameGenerator):
    names = dict()

    @classmethod
    def select_names(cls, gender=GENDER_NEUTRAL, *args, **kwargs):
        return cls.names[gender]
