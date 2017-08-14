import random
from .. import Generated, ParamGenerator, GeneratorTemplate, load_lines


class Planet(Generated):
    def __repr__(self):
        return "Planet: \"%s\"" % (self.generated_text)


class PlanetTemplate(GeneratorTemplate):
    @classmethod
    def generate1(cls, names):
        return "The planet %s%s is a %s planet in %s %s other planets." % (
            names[0],
            names[1],
            names[2],
            names[3],
            names[4],
        )

    @classmethod
    def generate2(cls, names):
        return "%s is about %s times bigger than Earth and its gravity is about %s times that of Earth." % (
            names[0],
            names[1],
            names[2],
        )

    @classmethod
    def generate3(cls, names):
        return "A single day lasts %s hours and a year lasts %s days. The planet is made up of %s continents, which make up %s%% of the planet's landmass." % (
            names[0],
            names[1],
            names[2],
            names[3],
        )

    @classmethod
    def generate4(cls, names):
        return "%s moon(s) orbit the planet and %s itself orbits a %s sun in a %s." % (
            names[0],
            names[1],
            names[2],
            names[3],
        )

    @classmethod
    def generate5(cls, names):
        return "The plant-like organisms on this planet are %s\n%s\n%s\n%s" % (
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


class PlanetGenerator(ParamGenerator):
    generated_class = Planet

    @classmethod
    def generate_text(cls, living=None):
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
        planet_types = [
            PlanetType(
                0,
                names=load_lines("data/planet/planet-type0.txt"),
                has_continents=True,
            ),
            PlanetType(
                1,
                life_type=life_types[0],
                names=load_lines("data/planet/planet-type1.txt"),
                orbit_types=load_lines("data/planet/orbit-type2.txt"),
            ),
            PlanetType(
                2,
                life_type=life_types[0],
                names=load_lines("data/planet/planet-type2.txt"),
            ),
        ]

        life_type_id = random.randrange(4)
        planet_type_id = random.randrange(3)

        if living:
            planet_type = planet_types[0]
            if life_type_id < 1:
                life_type_id = 1
        else:
            planet_type = planet_types[planet_type_id]

        if planet_type.life_type is None:
            planet_type.life_type = life_types[life_type_id]

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

        size = random.choice(planet_sizes)

        intelligent = random.random()
        basic_life = random.random()

        names1 = load_lines("data/planet/planet-name.txt")

        names2 = load_lines("data/planet/planet-name-origin.txt")
        if intelligent > 0.5:
            names2 += load_lines("data/planet/planet-name-origin2.txt")

        names3 = planet_type.names
        rnd3 = random.randrange(len(names3))

        names4 = load_lines("data/planet/solar-system.txt")
        rnd4 = random.randrange(len(names4))

        names5 = load_lines("data/planet/solar-system-planets.txt")

        names6 = round(size.random_size(), 1)
        names7 = round(size.random_grav(), 2)

        names8 = round(random.random() * 40 + 10, 2)
        names9 = round(random.random() * 400 + 100)

        names10 = round(random.random() * 15 + 1)
        names11 = round(random.random() * 80 + 10)

        names12 = round(random.random() * 5 + 1)
        names13 = load_lines("data/planet/star-color.txt")

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

        if rnd4 > 3:
            names5 = load_lines("data/planet/solar-system-planets2.txt")
        elif rnd4 == 3:
            names5 = load_lines("data/planet/solar-system-planets3.txt")

        planet_name = random.choice(names1)
        generated = PlanetTemplate.generate1([
            planet_name,
            random.choice(names2),
            names3[rnd3],
            names4[rnd4],
            random.choice(names5),
        ]) + "\n" + PlanetTemplate.generate2([
            planet_name,
            names6,
            names7,
        ]) + "\n" + PlanetTemplate.generate3([
            names8,
            names9,
            names10,
            names11,
        ]) + "\n" + PlanetTemplate.generate4([
            names12,
            planet_name,
            random.choice(names13),
            random.choice(planet_type.orbit_types),
        ])
        if planet_type.life_type.has_plants:
            generated += "\n" + PlanetTemplate.generate5([
                random.choice(planet_type.life_type.plant_list(-1)),
                random.choice(planet_type.life_type.plant_list(0)),
                random.choice(planet_type.life_type.plant_list(1)),
                random.choice(planet_type.life_type.life_list),
            ])
        return generated
