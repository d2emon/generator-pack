from genesys.generator._unknown.character import race
import random


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
    marks = [Scar(i) for i in range(6)] + \
        [Birthmark(i) for i in range(6, 9)] + \
        [Moles(9), Frecles(10), SmoothSkin(11), ] + \
        [SoftSkin(12 + i) for i in range(10)]

    names20 = []
    races = [race.Human(i) for i in range(3)] + \
            [race.Elf(i) for i in range(3, 9)] + \
            [race.Gnome(10), ] + \
            [race.Troll(11), race.Orc(12), race.Goblin(13)] + \
            [race.Dwarf(14), race.Giant(15)] + \
            [race.Race(15 + i) for i in range(10)]

    names22 = []
    names23 = []

    names24 = []
    names25 = []
    names26 = []
    names27 = []
    names28 = []

    srace = random.choice(races)

    mark = random.choice(marks)
    mark_from = random.choice(mark.places_form)
    mark_through = random.choice(mark.places_through)
    mark_to = random.choice(mark.places_to)
    memory_type = random.choice(mark.memory_types)
    memory_of = random.choice(mark.memory_ofs)
    first_name = random.choice(srace.first_name)
    last_name = random.choice(srace.last_name)
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

    head = "%s a %s. %s over %s" % (
        srace.hair,
        srace.face,
        srace.eyes,
        srace.promise,
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
        srace,

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
        head,
        name2,
        name3,
        name4,
    ])
