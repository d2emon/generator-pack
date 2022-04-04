from models.scales import Sized as Scalable, ScalableSize as Size

from .sotu import SOTU
from .starships import STARSHIPS
from .worlds import WORLDS
from .structures import SKYSCRAPERS
from .structures import STRUCTURES
from .military import MILITARY
from .animals import ANIMALS
from .solar import SOLAR
from .vehicles import VEHICLES
from .countries import COUNTRIES
from .stars import STARS

ITEMS = SOTU\
    + STARSHIPS\
    + WORLDS\
    + SKYSCRAPERS\
    + STRUCTURES\
    + MILITARY\
    + VEHICLES\
    + ANIMALS\
    + SOLAR\
    + STARS\
    + COUNTRIES\
    + [
        Scalable("Кеплер 22b", Size(30, 6)),
        Scalable("UY Щита", Size(2.5, 12)),
        Scalable("Сверхмассивнаяя черная дыра NGC 1277", Size(60, 12)),
        Scalable("TON 618", Size(400, 12)),

        Scalable("IC 1101", Size(60, 24)),
        Scalable("Войд Волопаса", Size(2.5, 27)),

        Scalable("Кеплер 10c", Size(31, 6)),

        Scalable("Ланиакея", Size(5, 27)),
    ]
