import random
from factories import DictFactory
from genesys.generator_models.space import Star
from sample_data.generator_fixtures.space.fixtures import suns
from .planet import PlanetFactory


class StarFactory(DictFactory):
    generated_class = Star
    sun_list = suns[:30]
    blue_sun_list = suns[30:]

    @classmethod
    def __next__(cls, data=()):
        return random.choice(data)

    @classmethod
    def generate(cls, planets=0, blue_sun=False, only_blue=False, sun=None):
        generated = cls.generated()
        return cls.fill_generated(generated, planets=planets, blue_sun=blue_sun, only_blue=only_blue, sun=sun)

    @classmethod
    def fill_generated(cls, generated, planets=0, blue_sun=False, only_blue=False, sun=None):
        import random
        sun_list = cls.sun_list
        if blue_sun:
            sun_list += cls.blue_sun_list
        if only_blue:
            sun_list = cls.blue_sun_list

        if not sun:
            sun = cls.__next__(sun_list)
        generated.title = str(sun)
        generated.image = sun.image
        generated.blue = sun.blue
        generated.star_type = sun

        if not planets:
            planets = random.randrange(7) + 4

        earth = False
        for i in range(planets):
            planet = PlanetFactory.generate(i < 6, earth)
            # curPlanet = planet.slice(0, -2)
            if planet.planet_type.earth:
                earth = True
            generated.planets.append(planet)
        return generated
