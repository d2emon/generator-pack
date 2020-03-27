import random
from orm.model import Model
from sample_data.storm.worlds import sizes


class WorldSize(Model):
    database = sizes
    fields = [
        'name',
        'size_class',
        'size',
        'min_size',
        'max_size',
    ]

    def __init__(self, **fields):
        self.name = None
        self.size_class = None
        self.size = None
        self.min_size = None
        self.max_size = None
        super().__init__(**fields)
        self.min_size = int(self.min_size) if self.min_size else 0
        self.max_size = int(self.max_size) if self.max_size else None

    @property
    def text(self):
        return "\n".join([
            "Класс размера:\t{size_class.size_class}",
            "Описание:\t\t{size_class.name}",
            "Размер:\t\t\t{size_class.size}",
        ]).format(size_class=self)

    def generate_size(self):
        if self.min_size is None:
            return random.randrange(self.max_size)
        if self.max_size is None:
            return self.min_size
        if self.min_size == self.max_size:
            return self.min_size
        return random.randrange(self.min_size, self.max_size)
