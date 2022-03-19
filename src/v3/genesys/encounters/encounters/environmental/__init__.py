from .cave import encounters as __cave_encounters
from .city import encounters as __city_encounters
from .desert import encounters as __desert_encounters
from .forest import encounters as __forest_encounters
from .jungle import encounters as __jungle_encounters
from .mountains import encounters as __mountain_encounters
from .plains import encounters as __plain_encounters
from .thundra import encounters as __thundra_encounters

encounters = {
    'cave': __cave_encounters,
    'city': __city_encounters,
    'desert': __desert_encounters,
    'forest': __forest_encounters,
    'jungle': __jungle_encounters,
    'mountains': __mountain_encounters,
    'plain': __plain_encounters,
    'thundra': __thundra_encounters,
}
