from sample_data.generator_fixtures.space.fixtures import planet_sizes
from utils.loaders import load_lines
from ..generator_models import Model


class StarSystemType:
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


class PlanetSubtype:
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


class PlanetType:
    def __init__(
        self,
        type_id,
        life_type=None,
        names=(),
        orbit_types=(),
        has_continents=False,
        title=""
    ):
        self.type_id = type_id
        self.life_type = life_type
        self.orbit_types = load_lines("data/planet/orbit-type.txt") + orbit_types
        self.has_continents = has_continents
        self.subtypes = [PlanetSubtype(i, t, self) for i, t in enumerate(names)]
        self.title = title


class Planet1(Model):
    def __init__(self):
        super().__init__()
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


class StarSystem(Model):
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
        super().__init__()
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


class LifeType:
    plant_lists = [
        load_lines("data/planet/plant.txt"),
        load_lines("data/planet/plant1.txt"),
        load_lines("data/planet/plant2.txt"),
        load_lines("data/planet/plant3.txt"),
        load_lines("data/planet/plant4.txt"),
    ]

    def __init__(self, description="", has_plants=True, plant_types=(), life_list=None):
        self.description = description
        self.has_plants = has_plants
        self.plant_types = plant_types
        self.life_list = life_list

    def plant_list(self, item_id):
        if not self.has_plants:
            return []
        print(item_id, self.plant_list)
        if item_id < 0:
            return self.plant_lists[0]
        else:
            return self.plant_lists[self.plant_types[item_id]]


class Planet(Model):
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
        super().__init__()
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
    def value(self):
        return self.name

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
