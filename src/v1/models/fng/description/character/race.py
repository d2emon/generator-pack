from v1.fixtures.fng.description import character


class Race:
    def __init__(self, race_id, name):
        self.race_id = race_id
        self.name = name

    @property
    def male(self):
        raise NotImplementedError()

    @property
    def female(self):
        raise NotImplementedError()


class Human(Race):
    @property
    def male(self):
        return {
            1: character.male_names1,
            2: character.male_names2,
            4: character.male_names4,
            7: character.male_names7,
            10: character.male_names10,
            18: character.male_names18,
            19: character.male_names19,
        }

    @property
    def female(self):
        return {
            1: character.female_names1,
            2: character.female_names2,
            4: character.female_names4,
            7: character.female_names7,
            10: character.female_names10,
            18: character.female_names18,
            19: character.female_names19,
        }


class Elf(Race):
    @property
    def male(self):
        return {
            1: character.elf_male_names1,
            2: character.elf_male_names2,
            4: character.elf_male_names4,
            7: character.elf_male_names7,
            10: character.elf_male_names10,
            18: character.elf_male_names18,
            19: character.elf_male_names19,
        }

    @property
    def female(self):
        return {
            1: character.elf_female_names1,
            2: character.elf_female_names2,
            4: character.elf_female_names4,
            7: character.elf_female_names7,
            10: character.elf_female_names10,
            18: character.elf_female_names18,
            19: character.elf_female_names19,
        }


class Gnome(Race):
    @property
    def male(self):
        return {
            1: character.gnome_male_names1,
            2: character.gnome_male_names2,
            4: character.gnome_male_names4,
            7: character.male_names7,
            10: character.male_names10,
            18: character.gnome_male_names18,
            19: character.gnome_male_names19,
        }

    @property
    def female(self):
        return {
            1: character.gnome_female_names1,
            2: character.gnome_female_names2,
            4: character.gnome_female_names4,
            7: character.female_names7,
            10: character.female_names10,
            18: character.gnome_female_names18,
            19: character.gnome_female_names19,
        }


class Goblin(Race):
    @property
    def male(self):
        return {
            1: character.male_names1,
            2: character.goblin_male_names2,
            4: character.goblin_male_names4,
            7: character.male_names7,
            10: character.goblin_male_names10,
            18: character.goblin_male_names18,
            19: character.goblin_male_names19,
        }

    @property
    def female(self):
        return {
            1: character.female_names1,
            2: character.goblin_female_names2,
            4: character.goblin_female_names4,
            7: character.female_names7,
            10: character.goblin_female_names10,
            18: character.goblin_female_names18,
            19: character.goblin_female_names19,
        }


class Troll(Goblin):
    @property
    def male(self):
        return {
            1: character.male_names1,
            2: character.goblin_male_names2,
            4: character.goblin_male_names4,
            7: character.male_names7,
            10: character.goblin_male_names10,
            18: character.troll_male_names18,
            19: character.troll_male_names19,
        }

    @property
    def female(self):
        return {
            1: character.female_names1,
            2: character.goblin_female_names2,
            4: character.goblin_female_names4,
            7: character.female_names7,
            10: character.goblin_female_names10,
            18: character.troll_female_names18,
            19: character.troll_female_names19,
        }


class Orc(Goblin):
    @property
    def male(self):
        return {
            1: character.male_names1,
            2: character.goblin_male_names2,
            4: character.goblin_male_names4,
            7: character.male_names7,
            10: character.goblin_male_names10,
            18: character.orc_male_names18,
            19: character.orc_male_names19,
        }

    @property
    def female(self):
        return {
            1: character.female_names1,
            2: character.goblin_female_names2,
            4: character.goblin_female_names4,
            7: character.female_names7,
            10: character.goblin_female_names10,
            18: character.orc_female_names18,
            19: character.orc_female_names19,
        }


class Giant(Race):
    @property
    def male(self):
        return {
            1: character.male_names1,
            2: character.giant_male_names2,
            4: character.giant_male_names4,
            7: character.male_names7,
            10: character.male_names10,
            18: character.male_names18,
            19: character.male_names19,
        }

    @property
    def female(self):
        return {
            1: character.female_names1,
            2: character.giant_female_names2,
            4: character.giant_female_names4,
            7: character.female_names7,
            10: character.female_names10,
            18: character.female_names18,
            19: character.female_names19,
        }


class Dwarf(Giant):
    @property
    def male(self):
        return {
            1: character.male_names1,
            2: character.giant_male_names2,
            4: character.giant_male_names4,
            7: character.male_names7,
            10: character.male_names10,
            18: character.dwarf_male_names18,
            19: character.dwarf_male_names19,
        }

    @property
    def female(self):
        return {
            1: character.female_names1,
            2: character.giant_female_names2,
            4: character.giant_female_names4,
            7: character.female_names7,
            10: character.female_names10,
            18: character.dwarf_female_names18,
            19: character.dwarf_female_names19,
        }


def get_race(data):
    item_id = data.item_id

    if 3 < item_id < 9:
        race = Elf
    elif item_id == 10:
        race = Gnome
    elif item_id == 11:
        race = Troll
    elif item_id == 12:
        race = Orc
    elif item_id == 13:
        race = Goblin
    elif item_id == 14:
        race = Dwarf
    elif 15 <= item_id <= 16:
        race = Giant
    else:
        race = Human

    return race(item_id, data.value)
