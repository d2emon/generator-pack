class Item:
    name = "Item"

    def __init__(self):
        print(self.name)


class Item1(Item):
    name = "Item1"


class Item2(Item):
    name = "Item2"


class SubItem:
    name = "SubItem"

    def __init__(self, item):
        print(item, self.name)


class SubItem1(SubItem):
    name = "SubItem1"


class SubItem2(SubItem):
    name = "SubItem2"


class Factory:
    def __init__(self):
        self.max_items = 5

    @property
    def items(self):
        for _ in range(self.max_items):
            item = self.generate_item()
            yield item, self.generate_sub(item)

    @classmethod
    def generate_item(cls):
        return Item()

    @classmethod
    def generate_sub(cls, item):
        return SubItem(item)


class Factory1(Factory):
    @classmethod
    def generate_item(cls):
        return Item1()

    @classmethod
    def generate_sub(cls, item):
        return SubItem1(item)


class Factory2(Factory):
    @classmethod
    def generate_item(cls):
        return Item2()

    @classmethod
    def generate_sub(cls, item):
        return SubItem2(item)
