class Item:
    type_id = 0

    def __init__(self):
        self.name = None
        self.value = 0

    def show(self):
        print(self.name, self.value, self.type_id)


class Item1(Item):
    type_id = 1


class Item2(Item):
    type_id = 2
