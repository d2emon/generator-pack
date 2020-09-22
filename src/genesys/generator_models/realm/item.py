import random


class Item:
    data = []

    def __init__(self, item_id, text):
        self.item_id = item_id
        self.text = text

    def __str__(self):
        return self.text

    @classmethod
    def choice(cls, data=None, **kwargs):
        if data is None:
            data = cls.data
        return random.choice(data)

    @classmethod
    def choice_unique(cls, count, data=None):
        if data is None:
            data = cls.data
        shuffled = list(data)
        random.shuffle(shuffled)
        return shuffled[:count]
