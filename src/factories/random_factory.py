import random
from models.data_item import DataItem
from .factory import SimpleFactory


class RandomFactory(SimpleFactory):
    def __init__(self, data=()):
        super().__init__(data)

    def __next__(self):
        if not len(self.data):
            return None
        # random.shuffle(self.__data)
        return random.choice(self.data)


class DiceFactory(SimpleFactory):
    def __init__(self, dices):
        super().__init__(dices)

    def __next__(self):
        return sum(self.data.roll())


class DataItemFactory(RandomFactory):
    def __init__(self, group_id):
        self.group_id = group_id
        super().__init__(DataItem.get_values_by_group(self.group_id))
