import os


CONFIG = {
    'storm': {
        'DATABASE_ROOT': os.path.join(os.path.dirname(__file__), '..', 'data'),
        'roll_on_double': True,
    },
}
