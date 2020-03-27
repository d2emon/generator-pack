from nestedg.mixins import EncounteredMixin, TerraformedMixin
from nestedg.model import Model
from nestedg.data import unknown, lookups, materials
from nestedg.data.materials import elements


class Atmosphere(Model, EncounteredMixin):
    contents = Model.children_property(
        elements.Helium,
        elements.Hydrogen,
        materials.Water,
        materials.Ammonia,
        materials.Methane,
    )

    class NameGenerator(Model.NameGenerator):
        default = 'atmosphere'


class GasGiantAtmosphere(Atmosphere):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            # Encounters
            yield unknown.GalacticLife.probable(10)
            # Contents
            yield elements.Helium
            yield elements.Hydrogen
            yield materials.Water.probable(50)
            yield materials.Ammonia.probable(50)
            yield materials.Methane.probable(50)


class PlanetCore(Model, EncounteredMixin):
    contents = Model.children_property(
        elements.Iron,
        materials.Rock,
        materials.Diamond,
        materials.Magma,
    )

    class NameGenerator(Model.NameGenerator):
        default = 'core'

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            # Encounters
            yield unknown.SpaceMonster.probable(0.5)
            # Contents
            yield elements.Iron
            yield materials.Rock
            yield materials.Diamond.probable(2)
            yield materials.Magma


class Orbit(Model, EncounteredMixin):
    pass


class PlanetLike(Orbit):
    atmosphere = Model.child_property(Atmosphere)
    core = Model.child_property(PlanetCore)
    land = Model.children_property(materials.Rock, unknown.Continent)
    water = Model.children_property(materials.Ice, unknown.Ocean)
    visited = Model.children_property(unknown.VisitorCity, unknown.VisitorInstallation)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield PlanetCore


# Moons


class Moon(PlanetLike):
    class BaseGenerator(Model.BaseGenerator):
        default = lookups.moons

    class ChildrenGenerator(PlanetLike.ChildrenGenerator):
        def children_classes(self):
            yield unknown.Ghost.probable(0.1)
            yield materials.Rock
            yield from PlanetLike.ChildrenGenerator.children_classes(self)


class TerraformedMoon(Moon, TerraformedMixin):
    class BaseGenerator(Model.BaseGenerator):
        default = lookups.terraformed_moons

    class ChildrenGenerator(Moon.ChildrenGenerator):
        def children_classes(self):
            yield from unknown.Continent.multiple(1, 4)
            yield from unknown.Ocean.multiple(1, 4)
            yield unknown.Sky
            yield from PlanetLike.ChildrenGenerator.children_classes(self)


####
FutureMoon = TerraformedMoon


# Planets


class Planet(PlanetLike):
    moons = Model.children_property(Moon)

    class ChildrenGenerator(PlanetLike.ChildrenGenerator):
        def children_classes(self):
            yield from PlanetLike.ChildrenGenerator.children_classes(self)
            yield Moon.probable(40)
            yield Moon.probable(20)
            yield Moon.probable(10)


class BarrenPlanet(Planet):
    class NameGenerator(Model.NameGenerator):
        default = 'telluric planet'

    class ChildrenGenerator(Planet.ChildrenGenerator):
        life_probability = 10

        def children_classes(self):
            yield unknown.GalacticLife.probable(self.life_probability)
            yield materials.Rock
            yield materials.Ice
            yield Planet.ChildrenGenerator.children_classes(self)


class VisitorPlanet(BarrenPlanet):
    class ChildrenGenerator(BarrenPlanet.ChildrenGenerator):
        life_probability = 100

        def children_classes(self):
            yield from unknown.VisitorCity.multiple(1, 8)
            yield from unknown.VisitorInstallation.multiple(2, 6)
            yield BarrenPlanet.ChildrenGenerator.children_classes(self)


class TelluricPlanet(Planet, TerraformedMixin):
    class ChildrenGenerator(Planet.ChildrenGenerator):
        @classmethod
        def _continents(cls):
            yield from unknown.Continent.multiple(2, 7)

        @classmethod
        def _oceans(cls):
            yield from unknown.Ocean.multiple(1, 7)

        @classmethod
        def _sky(cls):
            yield unknown.Sky

        @classmethod
        def _moons(cls):
            yield None

        def children_classes(self):
            yield from self._continents()
            yield from self._oceans()
            yield from self._sky()
            yield from self._moons()
            yield Planet.ChildrenGenerator.children_classes(self)


class FuturePlanet(TelluricPlanet):
    class ChildrenGenerator(TelluricPlanet.ChildrenGenerator):
        @classmethod
        def _continents(cls):
            yield from unknown.FutureContinent.multiple(2, 7)

        @classmethod
        def _sky(cls):
            yield unknown.FutureSky

        @classmethod
        def _moons(cls):
            yield FutureMoon.probable(30)


class TerraformedPlanet(TelluricPlanet):
    class ChildrenGenerator(TelluricPlanet.ChildrenGenerator):
        @classmethod
        def _sky(cls):
            yield unknown.TerraformedSky

        @classmethod
        def _moons(cls):
            yield TerraformedMoon.probable(30)


class MedievalPlanet(TelluricPlanet):
    class ChildrenGenerator(TelluricPlanet.ChildrenGenerator):
        @classmethod
        def _continents(cls):
            yield from unknown.MedievalContinent.multiple(2, 4)
            yield from unknown.AncientContinent.multiple(0, 3)


class AncientPlanet(TelluricPlanet):
    class ChildrenGenerator(TelluricPlanet.ChildrenGenerator):
        @classmethod
        def _continents(cls):
            yield from unknown.AncientContinent.multiple(2, 7)


class GasGiant(Planet):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield GasGiantAtmosphere
            yield PlanetCore.probable(50)
            yield from Moon.multiple(0, 3)
            yield TerraformedMoon.probable(20)
            yield TerraformedMoon.probable(10)


# Asteroids


class Asteroid(PlanetLike):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield unknown.SpaceAnimal.probable(0.5)
            yield materials.Rock
            yield materials.Ice.probable(30)


class AsteroidBelt(Orbit, EncounteredMixin):
    asteroids = Model.children_property(Asteroid)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield unknown.GalacticLife.probable(20)
            yield from Asteroid.multiple(10, 30)


class Earth(AsteroidBelt):
    class NameGenerator(Model.NameGenerator):
        default = 'Earth'
