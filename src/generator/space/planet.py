import random
from .. import Generated, DataGenerator, ParamGenerator, GeneratorTemplate, load_lines


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


class PlanetType():
    def __init__(
        self,
        type_id,
        life_type=None,
        names=[],
        orbit_types=[],
        has_continents=False,
    ):
        self.type_id = type_id
        self.life_type = life_type
        self.names = names
        self.orbit_types = load_lines("data/planet/orbit-type.txt") + orbit_types
        self.has_continents = has_continents


class PlanetSize():
    def __init__(self, min_size=0, max_size=0, min_grav=0, max_grav=0):
        self.min_size = min_size
        self.max_size = max_size
        self.min_grav = min_grav
        self.max_grav = max_grav

    def random_size(self):
        return random.random() * (self.max_size - self.min_size) + self.min_size

    def random_grav(self):
        return random.random() * (self.max_grav - self.min_grav) + self.min_grav

    def random_day(self):
        return round(random.random() * 40 + 10, 2)

    def random_year(self):
        return random.randrange(100, 500)

    def random_continents(self):
        return random.randrange(1, 16)

    def random_landmass(self):
        return random.randrange(10, 90)

    def random_moons(self):
        return random.randrange(1, 6)


class Planet(Generated):
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

    def __init__(self, has_plants=True, plant_types=[], life_list=None):
        self.has_plants = has_plants
        self.plant_types = plant_types
        self.life_list = life_list

    def plant_list(self, id):
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


class PlanetGenerator(ParamGenerator):
    generated_class = Planet
    life_types = [
        LifeType(
            has_plants=False,
        ),
        LifeType(
            plant_types=[2, 4],
            life_list=load_lines("data/planet/life1.txt"),
        ),
        LifeType(
            plant_types=[1, 3],
            life_list=load_lines("data/planet/life2.txt"),
        ),
        LifeType(
            plant_types=[1, 3],
            life_list=load_lines("data/planet/life3.txt"),
        ),
    ]
    planet_sizes = [
        PlanetSize(
            min_size=0.2,
            max_size=3,
            min_grav=0.2,
            max_grav=3,
        ),
        PlanetSize(
            min_size=3,
            max_size=8,
            min_grav=1,
            max_grav=5,
        ),
        PlanetSize(
            min_size=8,
            max_size=20,
            min_grav=3,
            max_grav=8,
        ),
        PlanetSize(
            min_size=20,
            max_size=40,
            min_grav=5,
            max_grav=15,
        ),
    ]

    @classmethod
    def generate_text(cls, living=None):
        planet_types = [
            PlanetType(
                0,
                names=load_lines("data/planet/planet-type0.txt"),
                has_continents=True,
            ),
            PlanetType(
                1,
                life_type=cls.life_types[0],
                names=load_lines("data/planet/planet-type1.txt"),
                orbit_types=load_lines("data/planet/orbit-type2.txt"),
            ),
            PlanetType(
                2,
                life_type=cls.life_types[0],
                names=load_lines("data/planet/planet-type2.txt"),
            ),
        ]

        star_system = StarSystemGenerator.generate()
        size = random.choice(cls.planet_sizes)

        life_type_id = random.randrange(4)
        planet_type_id = random.randrange(3)

        if living:
            planet_type = planet_types[0]
            if life_type_id < 1:
                life_type_id = 1
        else:
            planet_type = planet_types[planet_type_id]

        if planet_type.life_type is None:
            planet_type.life_type = cls.life_types[life_type_id]

        intelligent = random.random()
        basic_life = random.random()

        names_origin = load_lines("data/planet/planet-name-origin.txt")
        if intelligent > 0.5:
            names_origin += load_lines("data/planet/planet-name-origin2.txt")

        rnd3 = random.randrange(len(planet_type.names))

        planet_name = random.choice(load_lines("data/planet/planet-name.txt"))
        planet_name_origin = random.choice(names_origin)
        planet_type_text = planet_type.names[rnd3]
        planet_size = size.random_size()
        planet_gravity = size.random_grav()
        planet_day = size.random_day()
        planet_year = size.random_year()
        planet_continents = size.random_continents()
        planet_landmass = size.random_landmass()
        planet_moons = size.random_moons()
        planet_orbit = random.choice(planet_type.orbit_types)

        names21 = load_lines("data/planet/plant.txt")

        if rnd3 < 3:
            life_list = load_lines("data/planet/life5.txt")
            if not planet_type.has_continents:
                names10 = 0
                names11 = 0
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
        # generated.name = planet_name
        # generated.name_origin = planet_name_origin
        # generated.system = star_system
        # generated
        return generated
