from orm.models import DbModel
from genesys.storm.data.storm import shapes


class WorldShape(DbModel):
    database = shapes
    fields = [
        'name',
        'description',
    ]

    def __init__(self, **fields):
        self.name = None
        self.description = None
        super().__init__(**fields)
