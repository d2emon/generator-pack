from factories.name import NameFactory


class AlienNameGenerator(NameFactory):
    groups = ('race1', 'race2', 'race3')
    block_id = 'aliens'


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
