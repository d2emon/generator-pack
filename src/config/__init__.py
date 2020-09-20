import os


BASE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CURRENT_PATH = os.path.abspath(os.path.join(os.path.curdir))


DB_CONFIG = {
    'storm': {
        'DATABASE_ROOT': os.path.join(BASE_ROOT, 'data'),
        'roll_on_double': True,
    },
}
