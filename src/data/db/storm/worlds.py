import os
from database import CSVDatabase, JSONDatabase
from config import DB_CONFIG


CONFIG = DB_CONFIG.get('storm', {})
BASE_DIR = os.path.join(CONFIG.get('DATABASE_ROOT', ''), 'worlds')


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
