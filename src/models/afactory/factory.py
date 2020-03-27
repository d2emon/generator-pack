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
