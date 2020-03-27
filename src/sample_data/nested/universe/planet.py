from models.thing import Thing
from . import dummy
from .. import land, future


class PlanetCore(Thing):
    default_children_data = [
        dummy.SpaceMonster.probable_factory(0.5),
        dummy.Iron,
        dummy.Rock,
        dummy.Diamond.probable_factory(2),
        dummy.Magma,
    ]
    default_name = "core"


class PlanetBody(Thing):
    continent_class = None
    ocean_class = None
    sky_class = None

    @classmethod
    def continents_factory(cls):
        if cls.continent_class is None:
            return
        yield cls.continent_class.multiple_factory(2, 7)

    @classmethod
    def oceans_factory(cls):
        if cls.ocean_class is None:
            return
        yield cls.ocean_class.multiple_factory(1, 7)

    @classmethod
    def sky_factory(cls):
        if cls.sky_class is None:
            return
        yield cls.sky_class

    @classmethod
    def moon_factory(cls):
        yield from []

    @classmethod
    def children_data(cls):
        yield PlanetCore
        yield from cls.continents_factory()
        yield from cls.oceans_factory()
        yield from cls.sky_factory()
        yield from cls.moon_factory()
        yield from cls.default_children_data

    @property
    def core(self):
        return self.find_one(PlanetCore)

    @property
    def continents(self):
        return self.find(land.Continent)

    @property
    def oceans(self):
        return self.find(dummy.Ocean)

    @property
    def sky(self):
        return self.find_one(dummy.Sky)

    @property
    def moons(self):
        return self.find(PlanetBody)


class Moon(PlanetBody):
    default_children_data = [
        dummy.Ghost.probable_factory(0.1),
        dummy.Rock,
    ]
    moon_types = Thing.list_factory([
        "young", "old", "large", "small", "pale", "white", "dark", "black", "old",
    ])
    default_name = "{} moon"

    @classmethod
    def generate_name(cls):
        return cls.default_name.format(cls.moon_types.generate())


class TerraformedMoon(Moon):
    continent_class = land.ModernContinent
    ocean_class = dummy.Ocean
    sky_class = dummy.Sky
    moon_types = Thing.list_factory([
        "young", "old", "large", "small", "pale", "white", "dark", "black", "old",
        "green", "lush", "blue", "city", "colonized", "life"
    ])

    @classmethod
    def continents_factory(cls):
        yield cls.continent_class.multiple_factory(1, 4)

    @classmethod
    def oceans_factory(cls):
        yield cls.ocean_class.multiple_factory(1, 4)


class FutureMoon(Moon):
    pass


class Planet(PlanetBody):
    default_name = "planet"
    moon_class = None

    @classmethod
    def moon_factory(cls):
        yield Moon.probable_factory(40)
        yield Moon.probable_factory(20)
        yield Moon.probable_factory(10)
        if cls.moon_class is None:
            return
        yield cls.moon_class.probable_factory(30)


class TelluricPlanet(Planet):
    default_name = "telluric planet"


class BarrenPlanet(TelluricPlanet):
    galactic_life_probability = 10

    @classmethod
    def children_data(cls):
        yield from cls.default_children_data
        yield dummy.GalacticLife.probable_factory(cls.galactic_life_probability)
        yield dummy.Rock
        yield dummy.Ice.probable_factory(50)
        yield from TelluricPlanet.children_data()


class VisitorPlanet(BarrenPlanet):
    galactic_life_probability = 100
    default_children_data = [
        dummy.VisitorCity.multiple_factory(1, 8),
        dummy.VisitorInstallation.multiple_factory(2, 6),
    ]


class EarthLike(TelluricPlanet):
    continent_class = land.ModernContinent
    ocean_class = dummy.Ocean
    sky_class = dummy.Sky


class FuturePlanet(EarthLike):
    continent_class = future.FutureContinent
    sky_class = dummy.FutureSky
    moon_class = FutureMoon


class TerraformedPlanet(EarthLike):
    continent_class = land.ModernContinent
    sky_class = dummy.TerraformedSky
    moon_class = TerraformedMoon


class MedievalPlanet(EarthLike):
    continent_class = land.MedievalContinent

    @classmethod
    def continents_factory(cls):
        yield land.MedievalContinent.multiple_factory(2, 4)
        yield land.AncientContinent.multiple_factory(0, 3)


class AncientPlanet(EarthLike):
    continent_class = land.AncientContinent
