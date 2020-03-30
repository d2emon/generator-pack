class Name:
    glue = ""

    def __init__(self, *items, generator=None):
        self._items = items
        self.generator = generator

    @property
    def value(self):
        return self.get_name(self._items)

    @value.setter
    def value(self, value):
        self._items = value,

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    @classmethod
    def get_name(cls, items):
        return cls.glue.join(items).title()
