import os


BASE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CURRENT_PATH = os.path.abspath(os.path.join(os.path.curdir))
DATA_PATH = os.path.join(BASE_ROOT, 'data')


DB_CONFIG = {
    'storm': {
        'DATABASE_ROOT': os.path.join(DATA_PATH, 'storm'),
        'roll_on_double': True,
    },
}
