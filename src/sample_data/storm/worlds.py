import os
from orm.database import CSVDatabase, JSONDatabase


BASE_DIR = 'worlds'


types = JSONDatabase(filename=os.path.join(BASE_DIR, 'types.json'))
shapes = JSONDatabase(filename=os.path.join(BASE_DIR, 'shapes.json'))
sizes = CSVDatabase(
    filename=os.path.join(BASE_DIR, "sizes.csv"),
    fields=[
      'size_class',
      'name',
      'size',
      'min_size',
      'max_size',
    ],
)
worlds = JSONDatabase(filename=os.path.join(BASE_DIR, 'worlds.json'))
