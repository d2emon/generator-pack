class Name:
    def __init__(self, items):
        self.items = items

    @property
    def value(self):
        return ''

    @classmethod
    def test_swear(cls, name):
        return name

    def __str__(self):
        return self.test_swear(self.value)
