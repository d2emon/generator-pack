import random


class PlanetAtmosphere():
    def __init__(self, title, exist=True):
        self.title = title
        self.exist = exist

    def __repr__(self):
        return self.title


class PlanetType():
    earth = False
    max_moons = 60

    def __init__(self, image_id=1):
        self.image = image_id

    def __repr__(self):
        return self.image


class EarthPlanet(PlanetType):
    earth = True
    max_moons = 5

    def __repr__(self):
        if self.image < 10:
            image = "0" + str(self.image)
        else:
            image = str(self.image)
        return "earthPlanet%s" % (image)


class LayerPlanet(PlanetType):
    def __repr__(self):
        return "layerPlanet%s" % (self.image)


class TerPlanet(PlanetType):
    def __repr__(self):
        return "terplanet%s" % (self.image)


class MoonPlanet(PlanetType):
    def __repr__(self):
        return "moonPlanet%s" % (self.image)


class GasPlanet(PlanetType):
    def __repr__(self):
        return "gasPlanet%s" % (self.image)


class PlanetSize():
    min_size = 0.2
    max_size = 11.0
    min_grav = 0.2
    max_grav = 5.0
    min_day = 10
    max_day = 40
    min_year = 100
    max_year = 500
    min_continents = 1
    max_continents = 16
    min_landmass = 10
    max_landmass = 90
    min_moons = 1
    max_moons = 6
    min_orbit = 40
    max_orbit = 400

    def __init__(self, min_size=0, max_size=0, min_grav=0, max_grav=0):
        self.min_size = min_size
        self.max_size = max_size
        self.min_grav = min_grav
        self.max_grav = max_grav

    def random_size(self):
        return random.randrange(self.min_size * 10, self.max_size * 10) * 0.1 * 12742

    def random_grav(self):
        return random.randrange(self.min_grav * 100, self.max_grav * 100) * 0.01

    def random_day(self):
        return random.randrange(self.min_day * 100, self.max_day * 100) * 0.01

    def random_year(self):
        return random.randrange(self.min_year, self.max_year)

    def random_continents(self):
        return random.randrange(self.min_continents, self.max_continents)

    def random_landmass(self):
        return random.randrange(self.min_landmass, self.max_landmass)

    def random_moons(self):
        return random.randrange(self.min_moons, self.max_moons)

    def random_orbit(self):
        # generated.margin_left = (random.random() * cls.margin - 0.9 + 1) + 0.9
        return random.randrange(self.min_orbit * 10, self.max_orbit * 10) * 0.1
