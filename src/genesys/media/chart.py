class Chart:
    def __init__(self, items=()):
        self._items = []
        for item in items:
            self.append(item)
        self.sort()

    def append(self, item):
        self._items.append(item)

    def __getitem__(self, item):
        return self._items[item]

    def sort(self):
        self._items.sort(key=lambda x: x.next, reverse=True)
