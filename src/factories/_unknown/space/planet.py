import random
from factories.generator_factories import DataFactory, ListFactory, FactoryTemplate
from models.generator_models.space.planet import PlanetType, Planet1, StarSystemType, StarSystem, LifeType, Planet
from sample_data.generator_fixtures.space.fixtures import atmospheres, environments, maps, non_earthPlanets, allPlanets, planet_names, planet_sizes, planet_name_origins
from utils.loaders import load_lines


class StarSystemTemplate(FactoryTemplate):
    @classmethod
    def generate_system_type(cls, system_types):
        return random.choice(system_types)

    @classmethod
    def generate_planets(cls, system_type):
        return random.randint(system_type.min_planets, system_type.max_planets)


class PlanetTemplate(FactoryTemplate):
    @classmethod
    def generate2(cls, names):
        return "Планета %s примерно в %s раз больше Земли, а ее гравитация примерно в %s раз выше, чем у Земли." % (
            names[0],
            round(names[1], 1),
            round(names[2], 2),
        )

    @classmethod
    def generate3(cls, names):
        return "Один день длится %s часов, а год длится %s дней. Планета состоит из %s континентов, которые состовляют %s%% территории суши." % (
            names[0],
            names[1],
            names[2],
            names[3],
        )

    @classmethod
    def generate4(cls, names):
        return "Вокруг планеты вращается %s лун, а планета %s вращается вокруг %s солнца по %s." % (
            names[0],
            names[1],
            names[2],
            names[3],
        )

    @classmethod
    def generate5(cls, names):
        return "Растительные организмы на этой планете - это %s\n%s\n%s\n%s" % (
            names[0],
            names[1],
            names[2],
            names[3],
        )


class StarSystemFactory(DataFactory):
    generated_class = StarSystem
    star_colors = load_lines("data/planet/star-color.txt")
    system_types = [StarSystemType(i, s) for i, s in enumerate(load_lines("data/planet/solar-system.txt"))]

    @classmethod
    def generate_text(cls):
        return random.choice(cls.star_colors)

    @classmethod
    def generate(cls, **kwargs):
        generated = cls.generated_class()
        generated.color = cls.generate_text()
        generated.system_type = StarSystemTemplate.generate_system_type(cls.system_types)
        generated.planets_count = StarSystemTemplate.generate_planets(generated.system_type)
        return generated


class PlanetFactory1(DataFactory):
    generated_class = Planet1
    life_types = [
        LifeType(
            description="Безжизненная",
            has_plants=False,
        ),
        LifeType(
            description="Слабо развитая",
            plant_types=[2, 4],
            life_list=load_lines("data/planet/life1.txt"),
        ),
        LifeType(
            description="Жизненная",
            plant_types=[1, 3],
            life_list=load_lines("data/planet/life2.txt"),
        ),
        LifeType(
            description="Жизненная",
            plant_types=[1, 3],
            life_list=load_lines("data/planet/life3.txt"),
        ),
    ]
    planet_sizes = planet_sizes

    @classmethod
    def generate_text(cls, living=None):
        planet_types = [
            PlanetType(
                0,
                names=load_lines("data/planet/planet-type0.txt"),
                has_continents=True,
                title="Continented",
            ),
            PlanetType(
                1,
                life_type=cls.life_types[0],
                names=load_lines("data/planet/planet-type1.txt"),
                orbit_types=load_lines("data/planet/orbit-type2.txt"),
                title="Uninhabited1 strange orbit",
            ),
            PlanetType(
                2,
                life_type=cls.life_types[0],
                names=load_lines("data/planet/planet-type2.txt"),
                title="Uninhabited2",
            ),
        ]

        star_system = StarSystemFactory.generate()
        size = random.choice(cls.planet_sizes)

        if living:
            planet_type = planet_types[0]
            allowed_life_types = cls.life_types[1:]
        else:
            planet_type = random.choice(planet_types)
            allowed_life_types = cls.life_types

        intelligent = random.random()
        basic_life = random.random()

        names_origin = load_lines("data/planet/planet-name-origin.txt")
        if intelligent > 0.5:
            names_origin += load_lines("data/planet/planet-name-origin2.txt")
            planet_type = planet_types[0]
            allowed_life_types = cls.life_types[1:]

        if planet_type.life_type is None:
            planet_type.life_type = random.choice(allowed_life_types)

        planet_name = random.choice(load_lines("data/planet/planet-name.txt"))
        planet_name_origin = random.choice(names_origin)
        planet_subtype = random.choice(planet_type.subtypes)
        planet_type_text = planet_subtype.title
        planet_size = size.random_size()
        planet_gravity = size.random_grav()
        planet_day = size.random_day()
        planet_year = size.random_year()
        planet_continents = size.random_continents()
        planet_landmass = size.random_landmass()
        planet_moons = size.random_moons()
        planet_orbit = random.choice(planet_type.orbit_types)

        names21 = load_lines("data/planet/plant.txt")

        if not planet_subtype.has_continents:
            planet_continents = 0
            planet_landmass = 0

        if planet_subtype.is_empty:
            life_list = load_lines("data/planet/life5.txt")
        else:
            life_list = load_lines("data/planet/life4.txt")

        if planet_type.life_type.life_list is None:
            planet_type.life_type.life_list = life_list

        generated = star_system.in_system([
            planet_name,
            planet_name_origin,
            planet_type_text,
        ]) + "\n" + PlanetTemplate.generate2([
            planet_name,
            planet_size,
            planet_gravity,
        ]) + "\n" + PlanetTemplate.generate3([
            planet_day,
            planet_year,
            planet_continents,
            planet_landmass,
        ]) + "\n" + PlanetTemplate.generate4([
            planet_moons,
            planet_name,
            star_system.color,
            planet_orbit,
        ])
        if planet_type.life_type.has_plants:
            generated += "\n" + PlanetTemplate.generate5([
                random.choice(planet_type.life_type.plant_list(-1)),
                random.choice(planet_type.life_type.plant_list(0)),
                random.choice(planet_type.life_type.plant_list(1)),
                random.choice(planet_type.life_type.life_list),
            ])
        # generated += "\n"
        # generated += str(planet_type.type_id) + planet_type.title + "\n"
        # generated += str(planet_subtype.subtype_id) + planet_subtype.title + "\n"
        # generated.name = planet_name
        # generated.name_origin = planet_name_origin
        # generated.system = star_system
        # generated
        return generated


class PlanetFactory(ListFactory):
    generated_class = Planet

    margin = 5.4

    atmospheres = atmospheres
    environments = environments
    maps = maps
    noEarthPlanets = non_earthPlanets
    combPlanets = allPlanets
    planet_names = planet_names
    planet_name_origins = planet_name_origins
    planet_sizes = planet_sizes

    @classmethod
    def __next__(cls, data=()):
        return random.choice(data)

    @classmethod
    def generate(cls, near=False, earth=False):
        if near:
            if not earth:
                planet_type = cls.__next__(cls.combPlanets)
                # combPlanets.splice(ranPlanet, 1);
            else:
                planet_type = cls.__next__(cls.noEarthPlanets)
                # combPlanets.splice(ranPlanet, 1);
        else:
            planet_type = cls.__next__(cls.noEarthPlanets)

        generated = cls.generated()
        generated.planet_type = planet_type
        return cls.fill_generated(generated)

    @classmethod
    def fill_generated(cls, generated):
        if generated.planet_type.earth:
            day_type = 1
            orbit_type = 1
            atmospheres = cls.atmospheres[1:]
        else:
            day_type = random.randrange(2)
            orbit_type = random.randrange(2)
            atmospheres = cls.atmospheres

        if day_type == 1:
            generated.hours = random.randrange(8, 51)
        else:
            generated.hours = random.randrange(2000, 6001)

        if orbit_type == 1:
            generated.days = ((random.random() * 2.8) + 0.2)
        else:
            generated.days = ((random.random() * 191) + 10)

        generated.name = cls.__next__(cls.planet_names)
        generated.size = cls.__next__(cls.planet_sizes)
        generated.environment = cls.__next__(cls.environments)
        generated.surface_map = cls.__next__(cls.maps)
        generated.atmosphere = cls.__next__(atmospheres)
        generated.moons = random.randint(1, generated.planet_type.max_moons)
        generated.tilt = random.randrange(18000) * 0.01

        return generated
