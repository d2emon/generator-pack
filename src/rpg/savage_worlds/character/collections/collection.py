class Collection:
    def __init__(self, items):
        self.items = items

    def search(self, item_class):
        return (item for item in self.items if isinstance(item, item_class))

    def __getitem__(self, item):
        return next(self.search(item), None)

    @property
    def cost(self):
        return sum(item.cost for item in self.items)

    def set_values(self, items):
        for item_class, value in items.items():
            self[item_class].value = value
