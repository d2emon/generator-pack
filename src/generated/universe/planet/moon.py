from genesys.model.mixins import TerraformedMixin
from .body import PlanetLike


class Moon(PlanetLike):
    pass


class TerraformedMoon(Moon, TerraformedMixin):
    pass
