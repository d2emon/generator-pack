class Item:
    name = "Item"

    def __init__(self):
        print(self.name)


class Item1:
    name = "Item1"


class Item2:
    name = "Item2"


class Creator:
    def __init__(self):
        self.max_items = 5

    @property
    def items(self):
        for _ in range(self.max_items):
            yield self.generate()

    @classmethod
    def generate(cls):
        return Item()


class Item1Creator(Creator):
    @classmethod
    def generate(cls):
        return Item1()


class Item2Creator(Creator):
    @classmethod
    def generate(cls):
        return Item2()
