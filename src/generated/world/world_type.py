import random
from orm.models import DbModel
from sample_data.storm.worlds import types
from .size import WorldSize


class WorldType(DbModel):
    database = types
    fields = [
        'world_type',
        'description',
        'encounters',
        'sizes',
    ]

    def __init__(self, **fields):
        self.world_type = None
        self.description = None
        self.encounters = None
        self.sizes = None
        super().__init__(**fields)

    def generate_size(self):
        if not self.sizes:
            return None
        size_class = random.choice(self.sizes)
        return WorldSize.first(lambda item: item.get('size_class') == size_class)
