import os
from config import DB_CONFIG
from database.csv_database import CSVDatabase
from database.json_database import JSONDatabase


CONFIG = DB_CONFIG.get('storm', {})
BASE_DIR = CONFIG.get('DATABASE_ROOT', '')


TYPES_DATABASE_FILENAME = os.path.join(BASE_DIR, 'worlds', 'types.json')
SHAPES_DATABASE_FILENAME = os.path.join(BASE_DIR, 'worlds', 'shapes.json')
SIZES_DATABASE_FILENAME = os.path.join(BASE_DIR, 'worlds', 'sizes.csv')
WORLDS_DATABASE_FILENAME = os.path.join(BASE_DIR, 'worlds', 'worlds.json')


types = JSONDatabase(filename=TYPES_DATABASE_FILENAME)
shapes = JSONDatabase(filename=SHAPES_DATABASE_FILENAME)
sizes = CSVDatabase(
    filename=SIZES_DATABASE_FILENAME,
    fields=[
      'size_class',
      'name',
      'size',
      'min_size',
      'max_size',
    ],
)
worlds = JSONDatabase(filename=WORLDS_DATABASE_FILENAME)
