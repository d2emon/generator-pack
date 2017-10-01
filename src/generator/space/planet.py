import random
from .. import Generated, DataGenerator, ParamGenerator, ListGenerator, GeneratorTemplate, load_lines


class StarSystemType():
    def __init__(self, type_id=0, description=""):
        self.type_id = type_id
        self.description = description

    @property
    def min_planets(self):
        if self.type_id < 3:
            return 6
        else:
            return 13

    @property
    def max_planets(self):
        if self.type_id < 3:
            return 11
        elif self.type_id == 3:
            return 21
        else:
            return 29


class PlanetSubtype():
    def __init__(self, subtype_id, title="", planet_type=None):
        self.subtype_id = subtype_id
        self.title = title
        self.planet_type = planet_type

    @property
    def is_empty(self):
        return self.subtype_id < 3

    @property
    def has_continents(self):
        if not self.is_empty:
            return True
        return self.planet_type.has_continents


class PlanetType():
    def __init__(
        self,
        type_id,
        life_type=None,
        names=[],
        orbit_types=[],
        has_continents=False,
        title=""
    ):
        self.type_id = type_id
        self.life_type = life_type
        self.orbit_types = load_lines("data/planet/orbit-type.txt") + orbit_types
        self.has_continents = has_continents
        self.subtypes = [PlanetSubtype(i, t, self) for i, t in enumerate(names)]
        self.title = title


class Planet1(Generated):
    def __init__(self):
        Generated.__init__(self)
        self.name = "Unnamed"
        self.name_origin = ""
        self.type_text = ""
        self.system = None

    def __repr__(self):
        if self.system is not None:
            system_text = self.system.in_system([
                self.name,
                self.name_origin,
                self.type_text,
            ])
        else:
            system_text = "Планета %s, %s, это %s планета." % (
                self.name,
                self.name_origin,
                self.type_text,
            )
        return "Planet: \"%s\n%s\"" % (
            system_text,
            self.generated_text
        )


class StarSystem(Generated):
    planets_count_text = {
        6: "пятью",
        7: "шестью",
        8: "семью",
        9: "восемью",
        10: "девятью",
        11: "десятью",

        13: "двенадцатью",
        14: "тринадцатью",
        15: "четырнадцатью",
        16: "пятнадцатью",
        17: "шестнадцатью",
        18: "семнадцатью",
        19: "восемнадцатью",
        20: "девятнадцатью",
        21: "двадцатью",
        22: "двадцатью одной",
        23: "двадцатью двумя",
        24: "двадцатью тремя",
        25: "двадцатью четырмя",
        26: "двадцатью пятью",
        27: "двадцатью шестью",
        28: "двадцатью семью",
        29: "двадцатью восемью",
    }

    def __init__(self):
        Generated.__init__(self)
        self.system_type = None
        self.planets_count = 0
        self.color = ""
        self.planets = []

    @property
    def planets_text(self):
        return self.planets_count_text[self.planets_count]

    def in_system(self, planet):
        return "Планета %s, %s, является %s планетой в %s %s другими планетами." % (
            planet[0],
            planet[1],
            planet[2],
            self.system_type.description,
            self.planets_text,
        )


class StarSystemTemplate(GeneratorTemplate):
    @classmethod
    def generate_system_type(cls, system_types):
        return random.choice(system_types)

    @classmethod
    def generate_planets(cls, system_type):
        return random.randint(system_type.min_planets, system_type.max_planets)


class PlanetTemplate(GeneratorTemplate):
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


class LifeType():
    plant_lists = [
        load_lines("data/planet/plant.txt"),
        load_lines("data/planet/plant1.txt"),
        load_lines("data/planet/plant2.txt"),
        load_lines("data/planet/plant3.txt"),
        load_lines("data/planet/plant4.txt"),
    ]

    def __init__(self, description="", has_plants=True, plant_types=[], life_list=None):
        self.description = description
        self.has_plants = has_plants
        self.plant_types = plant_types
        self.life_list = life_list

    def plant_list(self, id):
        if not self.has_plants:
            return []
        print(id, self.plant_list)
        if id < 0:
            return self.plant_lists[0]
        else:
            return self.plant_lists[self.plant_types[id]]


class StarSystemGenerator(DataGenerator):
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


from .fixtures import atmospheres, environments, maps, non_earthPlanets, allPlanets, planet_names, planet_sizes


class PlanetGenerator1(ParamGenerator):
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

        star_system = StarSystemGenerator.generate()
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


class Planet(Generated):
    """
    <div class=\"planClose\" style=\"background-image: url('../images/planets/" + planet + ".png');\"></div>\
    <div class=\"planDetails\">\
        <textarea class=\"env\">Environment: " + environment[rnEnv] + "</textarea>\
        <textarea class=\"atmos\">Atmosphere: " + atmospheres[rnAtmos] + "</textarea>\
        <textarea class=\"map\">Surface map available: " + map[rnMap] + "</textarea>\
        <textarea class=\"day\">Day duration: " + rnDay + " hours</textarea>\
        <textarea class=\"grav\">Gravity: " + rnGrav + " (compared to Earth)</textarea>\
        <textarea class=\"orbit\">Orbit duration: " + rnOrbit + " Earth years</textarea>\
        <textarea class=\"moons\">Number of moons: " + rnMoons + "</textarea>\
        <textarea class=\"tilt\">Axial tilt: " + rnTilt + "&#176;</textarea>\
    </div>");
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.planet_type = kwargs.get('planet_type')
        self.environment = kwargs.get('environment')
        self.atmosphere = kwargs.get('atmosphere')
        self.surface_map = kwargs.get('surface_map')
        self.hours = kwargs.get('hours')
        self.days = kwargs.get('days')
        self.moons = kwargs.get('moons')
        self.tilt = kwargs.get('tilt')

        self.__orbit = kwargs.get('margin_left')
        self.__width = kwargs.get('width')
        self.__gravity = kwargs.get('gravity')
        self.size = planet_sizes[0]

    @property
    def width(self):
        if not self.__width:
            self.__width = self.size.random_size()
        return self.__width

    @property
    def gravity(self):
        if not self.__gravity:
            self.__gravity = self.size.random_grav()
        return self.__gravity

    @property
    def margin_left(self):
        if not self.__orbit:
            self.__orbit = self.size.random_orbit()
        return self.__orbit


class PlanetGenerator(ListGenerator):
    generated_class = Planet

    margin = 5.4

    atmospheres = atmospheres
    environments = environments
    maps = maps
    noEarthPlanets = non_earthPlanets
    combPlanets = allPlanets
    planet_names = planet_names
    planet_sizes = planet_sizes

    @classmethod
    def generate(cls, near=False, earth=False):
        if near:
            if not earth:
                planet_type = cls.generate_value(cls.combPlanets)
                # combPlanets.splice(ranPlanet, 1);
            else:
                planet_type = cls.generate_value(cls.noEarthPlanets)
                # combPlanets.splice(ranPlanet, 1);
        else:
            planet_type = cls.generate_value(cls.noEarthPlanets)

        generated = cls.generated()
        generated.planet_type = planet_type
        return cls.fill_generated(generated)

    @classmethod
    def fill_generated(cls, generated):
        if generated.planet_type.earth:
            dayType = 1
            orbitType = 1
            atmospheres = cls.atmospheres[1:]
        else:
            dayType = random.randrange(2)
            orbitType = random.randrange(2)
            atmospheres = cls.atmospheres

        if dayType == 1:
            generated.hours = random.randrange(8, 51)
        else:
            generated.hours = random.randrange(2000, 6001)

        if orbitType == 1:
            generated.days = ((random.random() * 2.8) + 0.2)
        else:
            generated.days = ((random.random() * 191) + 10)

        generated.name = cls.generate_value(cls.planet_names)
        generated.size = cls.generate_value(cls.planet_sizes)
        generated.environment = cls.generate_value(cls.environments)
        generated.surface_map = cls.generate_value(cls.maps)
        generated.atmosphere = cls.generate_value(atmospheres)
        generated.moons = random.randint(1, generated.planet_type.max_moons)
        generated.tilt = random.randrange(18000) * 0.01

        return generated
