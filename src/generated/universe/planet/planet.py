from genesys.model.model import Model
from genesys.model.mixins import TerraformedMixin
from .moon import Moon


class Planet(Model):
    # PlanetLike
    default_name = 'telluric planet'

    moons = Model.children_property(Moon)


class BarrenPlanet(Planet):
    pass


class VisitorPlanet(BarrenPlanet):
    pass


class TelluricPlanet(Planet, TerraformedMixin):
    pass


class FuturePlanet(TelluricPlanet):
    pass


class TerraformedPlanet(TelluricPlanet):
    pass


class MedievalPlanet(TelluricPlanet):
    pass


class AncientPlanet(TelluricPlanet):
    pass
