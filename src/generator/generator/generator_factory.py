import random
from fixtures.names import names_data


class Name:
    def __init__(self, *items):
        self.items = items

    def __str__(self):
        return "".join(self.items).title()

    def __repr__(self):
        return str(self)


class AlienNameGenerator:
    races = ('race1', 'race2', 'race3')
    block_id = 'aliens'

    def __init__(self, data=None):
        self._data = data or names_data

    def _race(self, race_id=None):
        if race_id is None:
            race_id = random.choice(self.races)
        return self._data[self.block_id].get(race_id)

    def _parts(self, race_id=None):
        return (random.choice(part) for part in self._race(race_id))

    def generate(self, race_id=None):
        return Name(*self._parts(race_id))


class NameGenerators:
    def __init__(self, data=None):
        self._data = data or names_data
        self.alien_name_generator = AlienNameGenerator(self._data)


class BaseGenerator1:
    name = "Item"

    def __init__(self):
        print(self.name)


class BaseGenerator2:
    name = "SubItem"

    def __init__(self, item):
        print(item, self.name)


class Generator1_1(BaseGenerator1):
    name = "Item1"


class Generator1_2(BaseGenerator1):
    name = "Item2"


class Generator2_1(BaseGenerator2):
    name = "SubItem1"


class Generator2_2(BaseGenerator2):
    name = "SubItem2"


class GeneratorFactory:
    def __init__(self):
        self.max_items = 5

    @property
    def items(self):
        for _ in range(self.max_items):
            item = self.generate_item()
            yield item, self.generate_sub(item)

    @classmethod
    def generate_item(cls):
        return BaseGenerator1()

    @classmethod
    def generate_sub(cls, item):
        return BaseGenerator2(item)


class GeneratorFactory1(GeneratorFactory):
    @classmethod
    def generate_item(cls):
        return Generator1_1()

    @classmethod
    def generate_sub(cls, item):
        return Generator2_1(item)


class GeneratorFactory2(GeneratorFactory):
    @classmethod
    def generate_item(cls):
        return Generator1_2()

    @classmethod
    def generate_sub(cls, item):
        return Generator2_2(item)
