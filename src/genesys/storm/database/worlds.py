import os
from .database import JSONDatabase, CSVDatabase


types = JSONDatabase(filename=os.path.join("worlds", "types.json"))
shapes = JSONDatabase(filename=os.path.join("worlds", "shapes.json"))
sizes = CSVDatabase(
    filename=os.path.join("worlds", "sizes.csv"),
    fields=[
      'size_class',
      'name',
      'size',
      'min_size',
      'max_size',
    ],
)
worlds = JSONDatabase(filename=os.path.join("worlds", "worlds.json"))
