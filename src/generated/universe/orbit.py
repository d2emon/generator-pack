from genesys.model.model import Model
from .planet.body import PlanetLike
# from generated.universe.space.life import Habitat


class Orbit(Model):
    # Habitat
    planets = Model.children_property(PlanetLike)


class PlanetOrbit(Orbit):
    planet = Model.child_property(PlanetLike)


class AsteroidBelt(Orbit):
    pass
