# from factories._unknown.character import race
from genesys.fng.list_item import ListItemProvider
# from ..marks import Scar, Birthmark, Moles, Frecles, SmoothSkin, SoftSkin
from genesys.fng.models.description.character import Scar, Birthmark, Moles, Freckles, SmoothSkin, SoftSkin
from v1.factories.fng.description.character.models import race


class DataProvider:
    @property
    def names(self):
        return [ListItemProvider([]) for _ in range(30)]

    @property
    def names1(self):
        return self.names[1]

    @property
    def names2(self):
        return self.names[2]

    @property
    def names3(self):
        return self.names[3]

    @property
    def names4(self):
        return self.names[4]

    @property
    def names5(self):
        return self.names[5]

    @property
    def names6(self):
        return self.names[6]

    @property
    def names7(self):
        return self.names[7]

    @property
    def names8(self):
        return self.names[8]

    @property
    def names9(self):
        return self.names[9]

    @property
    def names10(self):
        return self.names[10]

    @property
    def names11(self):
        return self.names[11]

    @property
    def names12(self):
        return self.names[12]

    @property
    def names13(self):
        return self.names[13]

    @property
    def names14(self):
        return self.names[14]

    @property
    def names15(self):
        return self.names[15]

    @property
    def names16(self):
        return self.names[16]

    @property
    def names17(self):
        return self.names[17]

    @property
    def names18(self):
        return self.names[18]

    @property
    def names19(self):
        return self.names[19]

    @property
    def names20(self):
        return self.names[20]

    @property
    def names21(self):
        return self.names[21]

    @property
    def names22(self):
        return self.names[22]

    @property
    def names23(self):
        return self.names[23]

    @property
    def names24(self):
        return self.names[24]

    @property
    def names25(self):
        return self.names[25]

    @property
    def names26(self):
        return self.names[26]

    @property
    def names27(self):
        return self.names[27]

    @property
    def names28(self):
        return self.names[28]

    @property
    def names29(self):
        return self.names[29]

    @property
    def names30(self):
        return self.names[30]

    @property
    def marks(self):
        return ListItemProvider(
            [Scar(i) for i in range(6)] + \
            [Birthmark(i) for i in range(6, 9)] + \
            [Moles(9), Freckles(10), SmoothSkin(11), ] + \
            [SoftSkin(12 + i) for i in range(10)]
        )

    @property
    def races(self):
        return ListItemProvider(
            [race.Human(i) for i in range(3)] + \
            [race.Elf(i) for i in range(3, 9)] + \
            [race.Gnome(10), ] + \
            [race.Troll(11), race.Orc(12), race.Goblin(13)] + \
            [race.Dwarf(14), race.Giant(15)] + \
            [race.Race(15 + i) for i in range(10)]
        )
