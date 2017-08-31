from generator.character.hair import *
import random


class Sware():
    adjectives = []  # 9
    towns = []  # 10
    objects = []  # 11


class Eyes():
    styles = []  # 6
    colors = []  # 7
    depths = []  # 8


class ElvishEyes(Eyes):
    colors = []  # 7


class ElvishSware(Sware):
    towns = []


class GoblinishSware(Sware):
    towns = []


class Race():
    hair_generator = hair.HairGenerator
    eyes_class = Eyes
    sware_class = Sware
    faces = []
    faces2 = []
    # 5
    # 8
    # 9

    first_names = []
    last_names = []

    def __init__(self, race_id):
        self.race_id = race_id
        self.hair = self.hair_generator.generate()
        self.eyes = self.eyes_class()
        self.sware = self.sware_class()


class Human(Race):
    pass


class Elf(Race):
    hair_generator = hair.ElfHairGenerator
    eyes_class = ElvishEyes
    sware_class = ElvishSware
    faces = []
    # 5
    # 6
    names7 = []
    # 8
    # 9

    first_names = []
    last_names = []


class Gnome(Race):
    hair_generator = hair.GnomeHairGenerator
    faces = []
    first_names = []
    last_names = []


class Goblinoid(Race):
    hair_generator = hair.GoblinHairGenerator
    sware_class = GoblinishSware
    faces = []


class Troll(Goblinoid):
    first_names = []
    last_names = []


class Orc(Goblinoid):
    first_names = []
    last_names = []


class Goblin(Goblinoid):
    first_names = []
    last_names = []


class Giant(Race):
    hair_generator = hair.GiantHairGenerator
    faces = []


class Dwarf(Giant):
    first_names = []
    last_names = []


class Mark():
    types = []  # 12
    places_from = []  # 13
    places_through = []  # 14
    places_to = []  # 15
    memory_types = []  # 16
    memory_ofs = []  # 17

    def __init__(self, name_id):
        self.name_id = name_id


class Scar(Mark):
    pass


class Birthmark(Mark):
    places_from = []  # 13
    places_through = []  # 14
    places_to = []  # 15


class Moles(Mark):
    places_from = []  # 13
    places_through = []  # 14
    places_to = []  # 15


class Frecles(Mark):
    places_from = []  # 13
    places_through = []  # 14
    places_to = []  # 15
    memory_types = []  # 16
    memory_ofs = []  # 17


class SmoothSkin(Mark):
    places_from = []  # 13
    places_through = []  # 14
    places_to = []  # 15
    memory_types = []  # 16
    memory_ofs = []  # 17


class SoftSkin(Mark):
    places_from = []  # 13
    places_through = []  # 14
    places_to = []  # 15
    memory_types = []  # 16
    memory_ofs = []  # 17


def charGen():
    names6 = []
    names8 = []
    names9 = []
    names11 = []

    marks = [Scar(i) for i in range(6)] + \
        [Birthmark(i) for i in range(6, 9)] + \
        [Moles(9), Frecles(10), SmoothSkin(11), ] + \
        [SoftSkin(12 + i) for i in range(10)]

    names20 = []
    races = [Human(i) for i in range(3)] + \
        [Elf(i) for i in range(3, 9)] + \
        [Gnome(10), ] + \
        [Troll(11), Orc(12), Goblin(13)] + \
        [Dwarf(14), Giant(15)] + \
        [Race(15 + i) for i in range(10)]

    names22 = []
    names23 = []

    names24 = []
    names25 = []
    names26 = []
    names27 = []
    names28 = []

    race = random.choice(races)

    face1 = random.choice(race.faces)
    face2 = random.choice(race.faces2)
    eyes_style = random.choice(race.eye.styles)
    eyes_color = random.choice(race.eye.colors)
    eyes_depth = random.choice(race.eye.depths)
    random9 = random.choice(names9)
    sware_adjective = random.choice(race.sware.adjectives)
    sware_town = random.choice(race.sware.towns)

    sware_object = random.choice(race.sware.objects)
    mark = random.choice(marks)
    mark_from = random.choice(mark.places_form)
    mark_through = random.choice(mark.places_through)
    mark_to = random.choice(mark.places_to)
    memory_type = random.choice(mark.memory_types)
    memory_of = random.choice(mark.memory_ofs)
    first_name = random.choice(race.first_name)
    last_name = random.choice(race.last_name)
    random20 = random.choice(names20)
    random22 = random.choice(names22)
    random23 = random.choice(names23)
    random24 = random.choice(names24)
    random25 = random.choice(names25)
    random26 = random.choice(names26)
    while random26 == random25:
        random26 = random.choice(names26)
    random27 = random.choice(names27)
    random28 = random.choice(names28)

    name1 = "%s a %s, %s face. %s %s eyes, set %s within their sockets, watch %s over the %s they've %s for so long." % (
        race.hair,
        face1,
        face2,

        eyes_style,
        eyes_color,
        eyes_depth,
        sware_adjective,
        sware_town,
        sware_object,
    )
    name2 = "%s %s %s %s leaves %s of %s." % (
        mark,
        mark_from,
        mark_through,
        mark_to,
        memory_type,
        memory_of,
    )
    name3 = "This is the face of %s %s, a true %s among %s. He stands %s others, despite his %s frame." % (
        first_name,
        last_name,
        random20,
        race,

        random22,
        random23,
    )
    name4 = "There's something %s about him, perhaps it's %s or perhaps it's simply %s. But nonetheless, people tend to %s, while %s." % (
        random24,
        random25,
        random26,

        random27,
        random28,
    )

    return "\n".join([
        name1,
        name2,
        name3,
        name4,
    ])
