from models.afactory import Item, Item1, Item2, SubItem, SubItem1, SubItem2


class Factory:
    def __init__(self, items_count=5):
        self.items_count = items_count

    @property
    def items(self):
        for _ in range(self.items_count):
            item = self.item()
            yield item, self.sub_item(item)

    @classmethod
    def item(cls):
        return Item()

    @classmethod
    def sub_item(cls, item):
        return SubItem(item)


class Factory1(Factory):
    @classmethod
    def item(cls):
        return Item1()

    @classmethod
    def sub_item(cls, item):
        return SubItem1(item)


class Factory2(Factory):
    @classmethod
    def item(cls):
        return Item2()

    @classmethod
    def sub_item(cls, item):
        return SubItem2(item)
