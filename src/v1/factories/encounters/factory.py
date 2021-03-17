import random
from v1.models.encounters import Encounter


class EncounterFactory:
    default_data = []
    model_class = Encounter

    def __init__(self, data=None):
        self.__data = data or self.default_data

    def items(self, **kwargs):
        return filter(lambda item: all(item[k] == v for k, v in kwargs.items()), self.__data)

    def model(self, **kwargs):
        return self.model_class(**kwargs)

    def __call__(self, *args, item_id=None, **kwargs):
        items = list(self.items(**kwargs))

        if len(items) == 0:
            return self.model()

        values = random.choice(items)
        return self.model(**values)
