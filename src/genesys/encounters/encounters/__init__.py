from .environmental import encounters
from .forest import encounters as __forest_encounters

encounters['forest'] = [
    *encounters.get('forest', []),
    *__forest_encounters,
]
